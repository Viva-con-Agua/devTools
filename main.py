import os
import argparse
from src.admin import Admin
from src.Utils import Utils

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    utils = Utils()
    settings = utils.load_settings()
    ##
    # add tools
    ##
    admin = Admin(settings['admin'])
    parser = argparse.ArgumentParser(prog='pool-cli')
    subparsers = parser.add_subparsers()
    ##
    # add subparser for tools
    ##
    admin_parser = admin.parser(subparsers)
    args = parser.parse_args()
    ##
    # execute tools
    ##
    if 'which' in args:
        if args.which == 'admin':
            admin.execute(args, admin_parser)
        else:
            parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
