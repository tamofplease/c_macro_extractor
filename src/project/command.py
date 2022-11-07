from os import environ, path
from typing import Optional
from dotenv import load_dotenv
from src.project.model import Project


def add_project(url: Optional[str]):
    load_dotenv()
    if not url:
        url = input('\033[96m' + 'Please input github url: ')
    print('\033[96m' + "clone project...")
    cloned_project = Project.clone(url)
    db_path, project_root_path = environ['DB_ROOT_PATH'], environ['PROJECT_ROOT_PATH']
    if not path.exists(db_path):
        Project.create_table()
    cloned_project.save()
    print('\033[96m' + "complete cloned project to:",
          project_root_path + '/' + cloned_project.name)
    print('\033[96m' + "save info to:", db_path)
