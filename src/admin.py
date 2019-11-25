from src.databases.DropsDAO import DropsDAO
from src.Utils import Utils
import json

class Admin:

    def __init__(self, config):
        self.drops_dao = DropsDAO(config)
        self.config = config
        self.utils = Utils()
    
    

    def add_role_to_role(self, email, role):
        user_id = self.drops_dao.select_user_id_by_email(email)
        if user_id is None:
            return None
        current_roles = self.drops_dao.select_user_role_by_id(user_id[0])
        if current_roles is None:
            return None
        roles = str(current_roles[0]).split(",")
        if role in roles:
            print("user " + email +"actually have the role " + role + "\n")
            return None
        new_roles = str(current_roles[0]) + "," + role
        update = self.drops_dao.update_user_role_by_id(user_id[0], new_roles)
        
    def add_list_of_roles(self, jsonfile):
        for entry in jsonfile['entities']:
            self.add_role_to_role(entry['email'], 'employee')
            self.add_role_to_role(entry['email'], entry['entity'])



    def add_oauth_client(self, client_id, client_secret, redirect_uri):
        result = self.drops_dao.add_oauth_client(client_id, client_secret, redirect_uri)
        print(result)

    def parser(self, subparsers):
        parser = subparsers.add_parser('admin', help='setup docker ')
        parser.add_argument(
            '-r', '--role',
            nargs=2,
            metavar=('email, role'),
            help="add role to user"
                )
        parser.add_argument(
            '-l', '--list',
            nargs=1,
            metavar=('list'),
            help="add list of email role tuple"
                )
        parser.set_defaults(which="admin")
        return parser

    def execute(self, args, parser):
        if args.role is not None:
            output = self.add_role(args.role[0], args.role[1])
            print(output)
        elif args.list is not None:
            json_file = self.utils.load_json_from_file(args.list[0])
            self.add_list_of_roles(json_file)
        else:
            parser.print_help()
