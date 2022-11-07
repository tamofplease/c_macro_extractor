from os import environ, path, makedirs
from shutil import rmtree
from typing import List
from dotenv import load_dotenv
import pytest
from src.project.model import Project


load_dotenv()
db_path = environ['DB_ROOT_PATH']


@pytest.fixture(name='project_zstd')
def fixture_project_zstd():
    return Project(
        name='zstd',
        url='https://github.com/facebook/zstd.git',
        commit_hash='commit_hash_example'
    )


@pytest.fixture(name='project_micropython')
def fixture_project_micropython():
    return Project(
        name='',
        url='https://github.com/micropython/micropython.git',
        commit_hash='7c54b6428058a236b8a48c93c255948ece7e718b',
    )


# @pytest.mark.skip(reason="Because it take times.")
def test_clone(project_zstd):
    url = project_zstd.url
    name = project_zstd.name
    cloned_project = Project.clone(url)
    output_path = environ['PROJECT_ROOT_PATH'] + '/' + name

    assert cloned_project.url == url
    assert cloned_project.name == name
    assert path.exists(output_path)

    rmtree(output_path)


def test_create_table():
    if not path.exists(db_path):
        makedirs(db_path)
    Project.create_table()

    assert path.exists(db_path + '/project.csv')


def test_save(project_zstd):
    project = project_zstd
    saved_project = project.save()

    assert project.name == saved_project.name
    assert project.url == saved_project.url
    assert project.commit_hash == saved_project.commit_hash


def test_get_by_id(project_micropython):
    project = project_micropython
    saved_project = project.save()
    fetched_project = Project.get_by_id(project_id=saved_project.id)

    assert saved_project.id == fetched_project.id
    assert saved_project.name == fetched_project.name
    assert saved_project.url == fetched_project.url
    assert saved_project.commit_hash == fetched_project.commit_hash


def test_list(project_zstd, project_micropython):
    fetched_projects: List["Project"] = Project.list()

    assert len(fetched_projects) == 2
    assert fetched_projects[0].name == project_zstd.name
    assert fetched_projects[0].url == project_zstd.url
    assert fetched_projects[0].commit_hash == project_zstd.commit_hash
    assert fetched_projects[1].name == project_micropython.name
    assert fetched_projects[1].url == project_micropython.url
    assert fetched_projects[1].commit_hash == project_micropython.commit_hash

    rmtree(db_path)


# @pytest.fixture(scope='function', autouse=True)
# def scope_function():
#     print("            setup before function")
#     yield
#     print("            teardown after function")
