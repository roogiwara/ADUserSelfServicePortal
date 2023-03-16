from flask import Flask, render_template, request, redirect, url_for, session
import tel_cadastro
from itsdangerous import URLSafeTimedSerializer
from tel_ad_ldap_auth import ldap_authentication

app = Flask(__name__)
app.secret_key = 'g8zt9mkwdDFad##23145r1dasfcastemwvq95dasiudPyglZfscvxge!'

serializer = URLSafeTimedSerializer(app.secret_key)

@app.route('/')
def inicio():
    return redirect('/login')

@app.route('/login', methods=('GET', 'POST'))
def index():
    if request.method in ('POST') :
        login_id = request.form['user_name_pid']
        login_password = request.form['user_pid_Password']
        encrypted_data = serializer.dumps({'username': login_id})
        login_msg = ldap_authentication(login_id, login_password)
 
        if login_msg == "Success":
            session['login_info'] = encrypted_data
            return redirect(url_for('cadastro'))
        else:
            error_message = f"*** Authentication Failed - Usuário ou senha inválidos - {login_msg}"
            return render_template("error.html", error_message=str(error_message))
 
    return render_template('login.html')
 
@app.route('/cadastro', methods=('GET', 'POST'))
def cadastro():
    encrypted_data = session.get('login_info')
    if encrypted_data:
        login_info = serializer.loads(encrypted_data)
        username = login_info['username']
    else:
        return redirect(url_for("index"))    

    if request.method == 'POST':
        phone = request.form['telefone1']

        retorno = tel_cadastro.update_phone(phone, username)

        if retorno == "success":
            return render_template('resultado.html', user=username)

    return render_template('index.html', user=username)
 
if __name__ == '__main__':
    app.run(debug=True)