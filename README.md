# ADUserSelfServicePortal

This is a simple Python App that serves a form to update Active Directory User's telephone number attribute.

# Usage

Clone the repository and create a requirements.txt file with the following content:
```
Flask==2.2.3
gunicorn==20.1.0
```
And a Dockerfile file with the following content:
```
FROM python:3.8.10
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install ldap3
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "wsgi:app"]
```
Build the image `docker build -t aduserselfserviceportal .`

Run the Docker image by passing the required parameters as env variables:
```
NETBIOS
ADFQDN
USER
PASSWORD
BASEDN
```
`docker run -e NETBIOS=contoso -e ADFQDN=AD2016.contoso.local -e USER=service.account -e PASSWORD=password -e BASEDN=DC=contoso,DC=local -d --name aduserselfserviceportal -p 5000:5000 aduserselfserviceportal`
