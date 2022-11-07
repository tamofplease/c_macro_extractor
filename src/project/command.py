from os import environ, path
from shutil import rmtree
from typing import Optional
from dotenv import load_dotenv
import tqdm
from src.project.model import Project


def add_project(url: Optional[str]):
    load_dotenv()
    if not url:
        url = input('\033[96m' + 'Please input github url: ')
    cloned_project = Project.clone(url)
    db_path = environ['DB_ROOT_PATH']
    if not path.exists(db_path):
        Project.create_table()
    cloned_project.save()


def add_projects(url: Optional[str], force=False):
    if not url:
        url = './project_list'
    db_path, project_root_path = environ['DB_ROOT_PATH'], environ['PROJECT_ROOT_PATH']
    if path.exists(db_path) or path.exists(project_root_path):
        if not force:
            res = input(
                '\033[93m' + 'Output path are already exist. Are you sure to overwrite? [Y/N]')
            if res != "Y":
                return
        if path.exists(db_path):
            rmtree(db_path)
        if path.exists(project_root_path):
            rmtree(project_root_path)
    with open(url, mode='r', errors='ignore', encoding='utf-8') as f_object:
        for github_url in tqdm.tqdm(f_object):
            add_project(github_url.replace("\n", ''))
