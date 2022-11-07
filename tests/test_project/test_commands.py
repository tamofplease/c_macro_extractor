from os import environ, path
from shutil import rmtree
from dotenv import load_dotenv
from src.project.command import add_project


def test_add_project():
    load_dotenv()
    url = "https://github.com/radareorg/radare2.git"
    add_project(url)
    db_path, project_root_path = environ['DB_ROOT_PATH'], environ['PROJECT_ROOT_PATH']

    assert path.exists(db_path + '/project.csv')
    assert path.exists(project_root_path + '/radare2')

    rmtree(db_path)
    rmtree(project_root_path)
