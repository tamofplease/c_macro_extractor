from os import environ, path
from dotenv import load_dotenv
from src.project.model import Project


def add_project():
    load_dotenv()
    url = input('\033[96m' + 'Please input github url: ')
    cloned_project = Project.clone(url)
    print('\033[96m' + "clone project...")
    db_path, project_root_path = environ['DB_ROOT_PATH'], environ['PROJECT_ROOT_PATH']
    if not path.exists(db_path):
        Project.create_table()
    cloned_project.save()
    print('\033[96m' + "cloned project to: ", project_root_path)
    print('\033[96m' + "save info to: ", db_path)
