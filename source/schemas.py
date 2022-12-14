from typing import Optional

from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class User(UserLogin):
    key: str


class UserFileRelation(BaseModel):
    user_key: str
    file_key: str
    owner_key: str


class File(BaseModel):
    name: str
    size: int
    owner_key: str
    content_type: str
    last_modified: str
    deleted: bool = False


class BodyRename(BaseModel):
    name: str

class BodyChangeOwner(BaseModel):
    owner_key: str

class Record(BaseModel):
    name: str
    data: bytes
    type: str
