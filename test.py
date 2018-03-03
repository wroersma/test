from lib.config import ConfigParser


run = ConfigParser()
project_secrets_config = run.get()
project_api_key = project_secrets_config["secrets"]["my_project_api_key"]
print(project_api_key)
