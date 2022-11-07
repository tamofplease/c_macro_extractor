import uuid
from os import environ,  path, makedirs
from typing import List
from shutil import rmtree
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import git
from src.client.csv import CsvClient


class NotFound(Exception):
    pass


class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    url: str
    commit_hash: str

    @classmethod
    def list(cls) -> List["Project"]:
        load_dotenv()
        db_path = environ['DB_ROOT_PATH']
        client = CsvClient(db_path=db_path)
        projects = [cls(**record)
                    for record in client.list_all(table_name='project')]
        return projects

    def save(self) -> "Project":
        load_dotenv()
        db_path = environ['DB_ROOT_PATH']
        client = CsvClient(db_path=db_path)
        client.insert(table_name='project', data=(
            self.id, self.name, self.url, self.commit_hash))
        return self

    @classmethod
    def get_by_id(cls, project_id: str) -> "Project":
        load_dotenv()
        db_path = environ['DB_ROOT_PATH']
        client = CsvClient(db_path=db_path)
        data = client.find_by(table_name='project',
                              prop='id', value=project_id)
        if len(data) == 0:
            raise Exception('data did not found', project_id)
        return [cls(**record) for record in data][0]

    @classmethod
    def clone(cls, url: str) -> "Project":
        output_folder = environ['PROJECT_ROOT_PATH']
        name = url.rsplit('/', maxsplit=1)[-1].split('.')[0]
        output_path = output_folder + '/' + name
        if path.exists(output_path):
            rmtree(output_path)
        repo = git.Repo.clone_from(url, output_path)
        new_commit = repo.head.commit
        return Project(
            name=name,
            url=url,
            commit_hash=new_commit.hexsha
        )

    @classmethod
    def create_table(cls):
        load_dotenv()
        db_path = environ['DB_ROOT_PATH']
        if not path.exists(db_path):
            makedirs(db_path)
        client = CsvClient(db_path=db_path)
        client.create_table(table_name='project', columns=[
                            'id', 'name', 'url', 'commit_hash'])
