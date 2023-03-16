import os
from ldap3 import Server, Connection, SUBTREE, ALL_ATTRIBUTES, ALL, NTLM, MODIFY_REPLACE


OBJECT_CLASS = ['top', 'person', 'organizationalPerson', 'user']
LDAP_HOST = os.getenv('ADFQDN')
LDAP_USER = os.getenv('USER')
LDAP_DOMAIN = os.getenv('NETBIOS')
LDAP_PASSWORD = os.getenv('PASSWORD')
LDAP_BASE_DN = os.getenv('BASEDN')

search_filter = "(sAMAccountName={0}*)"

# AD Server
ms_ad_server = Server(LDAP_HOST, get_info=ALL)

def ldap_connection():
    return Connection(ms_ad_server, user='{}\\{}'.format(LDAP_DOMAIN, LDAP_USER), password=LDAP_PASSWORD, authentication=NTLM, auto_bind=True)

def update_phone(phone, username):
    with ldap_connection() as c:
        c.search(search_base=LDAP_BASE_DN,
                 search_filter=search_filter.format(username),
                 search_scope=SUBTREE,
                 attributes=ALL_ATTRIBUTES,
                 get_operational_attributes=True)
        if(c.entries):
            for x in c.entries:
                dn = x.distinguishedName
        else:
            result = "Could not get USER DN"

        dnstr = dn[0]
        c.modify(dnstr,{'telephoneNumber': [(MODIFY_REPLACE, [phone])]})
        result = "success"
        
        return result