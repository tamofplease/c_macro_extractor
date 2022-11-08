from os import path, listdir
from shutil import rmtree
import pytest
from src.project.command import add_project, add_projects
from src.config import DB_ROOT_PATH, PROJECT_ROOT_PATH


def test_add_project():
    url = "https://github.com/octalmage/robotjs.git"
    add_project(url)

    assert path.exists(DB_ROOT_PATH + '/project.csv')
    assert path.exists(PROJECT_ROOT_PATH + '/robotjs')


def test_add_projects():
    file_path = './test_project_list'
    add_projects(file_path, True)

    assert path.exists(PROJECT_ROOT_PATH)
    files = listdir(PROJECT_ROOT_PATH)
    assert len(files) == 3
    assert path.exists(PROJECT_ROOT_PATH)
    file_path = DB_ROOT_PATH + '/project.csv'
    with open(file_path, mode='r', errors='ignore', encoding='utf-8') as f_object:
        assert len(f_object.readlines()) == 4


@pytest.fixture(scope='function', autouse=True)
def scope_function():
    yield
    rmtree(DB_ROOT_PATH, ignore_errors=True)
    rmtree(PROJECT_ROOT_PATH, ignore_errors=True)
