from pydantic import BaseModel


class PersonModel(BaseModel):
    name: str
    age: str


class PersonResponse(PersonModel):
    id: int


class AgeModel(BaseModel):
    age: str

class DeleteResponse(BaseModel):
    status: str
