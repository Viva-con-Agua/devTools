##
# Drops Database Access via mysql
##
import mysql.connector
class DropsDAO:
    
    def __init__(self, config):
        if 'mysql-drops' not in config:
            print('can`t find key mysql in settings.yml')
            exit(1)
        mysql_config = config['mysql-drops']
        
        if 'host' not in mysql_config:
            print('can`t find key mysql.host in settings.yml')
            exit(1)
        elif 'user' not in mysql_config: 
            print('can`t find key mysql.user in settings.yml')
            exit(1)
        elif'passwd' not in mysql_config:
            print('can`t find key mysql.passwd in settings.yml')
            exit(1)
        elif 'database' not in mysql_config:
            print('can`t find key mysql.database in settings.yml')
        else:
            self.mydb = mysql.connector.connect(
                host=mysql_config['host'],
                user=mysql_config['user'],
                passwd=mysql_config['passwd'],
                database=mysql_config['database']
            )
            self.cursor = self.mydb.cursor()
            
        
    def select_user_id_by_email(self, email):
        self.cursor.execute("SELECT u.id FROM User u INNER JOIN Profile p ON (u.id = p.user_id)  WHERE p.email=%s", (email,))
        result = self.cursor.fetchone()
        if result is None:
            print("Can´t find user with given email \n")
        return result
    
    def select_user_role_by_id(self, user_id):
        self.cursor.execute("SELECT roles FROM User WHERE id=%s", (user_id,))
        result = self.cursor.fetchone()
        if result is None:
            print("Can`t find user with given id")
        return result

    def update_user_role_by_id(self, user_id, role):
        self.cursor.execute("UPDATE User set roles=%s WHERE id=%s", (role, user_id,))
        self.mydb.commit()
        return self.cursor.fetchone()
    
    def add_oauth_client(self, client_id, secret, redirect_Uri):
        self.cursor.exectue(
                'INSERT INTO OauthClient (id, secret, redirectUri, grantTypes) VALUE (%s, %s, %s, "authorization_code")', 
                (client_id, secret, redirectUri)
                )
        self.mydb.commit()
        return self.cursor
 
