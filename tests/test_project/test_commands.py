from os import environ, path, listdir
from shutil import rmtree
import pytest
from dotenv import load_dotenv
from src.project.command import add_project, add_projects

load_dotenv()
db_path = environ['DB_ROOT_PATH']
project_root_path = environ['PROJECT_ROOT_PATH']


def test_add_project():
    url = "https://github.com/octalmage/robotjs.git"
    add_project(url)

    assert path.exists(db_path + '/project.csv')
    assert path.exists(project_root_path + '/robotjs')


def test_add_projects():
    file_path = './test_project_list'
    add_projects(file_path, True)

    assert path.exists(project_root_path)
    files = listdir(project_root_path)
    assert len(files) == 3
    assert path.exists(project_root_path)
    file_path = db_path + '/project.csv'
    with open(file_path, mode='r', errors='ignore', encoding='utf-8') as f_object:
        assert len(f_object.readlines()) == 4


@pytest.fixture(scope='function', autouse=True)
def scope_function():
    yield
    rmtree(db_path)
    rmtree(project_root_path)
