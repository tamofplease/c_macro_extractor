import uuid
from pydantic import BaseModel, Field
import git


class NotFound(Exception):
    pass


class Projects(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: str
    commit_hash: str

    @classmethod
    def clone(cla, url: str):
        repo = git.Repo.clone_from(url, "./", no_checkout=True)
