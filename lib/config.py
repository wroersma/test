"""Project secrets config parser"""
import yaml


class ConfigParser:
    project_secrets = {}

    def __init__(self) -> None:
        """init to load project information and license info"""
        with open("config.yml", 'rb') as project_secrets_file:
            project_secrets_strings = project_secrets_file.read()
        self.project_secrets = yaml.load(project_secrets_strings)

    def get(self) -> dict:
        return self.project_secrets
