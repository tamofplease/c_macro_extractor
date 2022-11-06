import io
from dotenv import load_dotenv
from os import environ, path
from src.project.command import add_project


def test_add_project(monkeypatch):
    load_dotenv()
    url = "https://github.com/radareorg/radare2.git"
    monkeypatch.setattr('sys.stdin', io.StringIO(url))
    add_project()
    db_path, project_root_path = environ['DB_ROOT_PATH'], environ['PROJECT_ROOT_PATH']

    assert path.exists(db_path)
    assert path.exists(project_root_path + 'radare2')
