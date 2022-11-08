import uuid
from pydantic import BaseModel, Field


class File(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    path: str
    project_id: str

    @classmethod
    def list(cls, project_id):
        pass
