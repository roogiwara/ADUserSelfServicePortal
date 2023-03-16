import os
from ldap3 import Server, Connection, ALL, NTLM


def ldap_authentication(user_name, user_pwd):
    NETBIOS = os.getenv('NETBIOS')
    ADFQDN = os.getenv('ADFQDN')

    AD_Accnt = NETBIOS + "\\"
    DC_Root = ADFQDN

    ldap_user_name = AD_Accnt + user_name
    ldap_user_pwd = user_pwd

    ms_ad_server = Server(DC_Root, get_info=ALL)

    connection = Connection(ms_ad_server, user=ldap_user_name, password=ldap_user_pwd, authentication=NTLM)
    if not connection.bind():
        print(f" *** Cannot bind to ldap server: {connection.last_error} ")
        l_success_msg = f' ** Failed Authentication: {connection.last_error}'
    else:
        print(f" *** Successful bind to ldap server")
        l_success_msg = 'Success'
            
    return l_success_msg
