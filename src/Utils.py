import yaml
import json


class Utils:
    def __init__(self):
        self.dummy = "dummy"

    def load_settings(self):
        with open("./conf/settings.yml", 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        return cfg

    def load_json_from_file(self, path):
        with open(path, 'r') as jsonfile:
            print(jsonfile)
            json_file = json.load(jsonfile)
            print(json_file)
        return json_file
