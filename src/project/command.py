from os import path
from shutil import rmtree
from typing import Optional
import tqdm
from src.project.model import Project
from src.config import DB_ROOT_PATH, PROJECT_ROOT_PATH


def add_project(url: Optional[str] = None):
    if not url:
        url = input('\033[96m' + 'Please input github url: ')
    cloned_project = Project.clone(url)
    if not path.exists(DB_ROOT_PATH):
        Project.create_table()
    cloned_project.save()


def add_projects(url: Optional[str] = None, force=False):
    if not url:
        url = './project_list'
    if path.exists(DB_ROOT_PATH) or path.exists(PROJECT_ROOT_PATH):
        if not force:
            res = input(
                '\033[93m' + 'Output path are already exist. Are you sure to overwrite? [Y/N]')
            if res != "Y":
                return
        if path.exists(DB_ROOT_PATH):
            rmtree(DB_ROOT_PATH)
        if path.exists(PROJECT_ROOT_PATH):
            rmtree(PROJECT_ROOT_PATH)
    with open(url, mode='r', errors='ignore', encoding='utf-8') as f_object:
        for github_url in tqdm.tqdm(f_object):
            add_project(github_url.replace("\n", ''))
