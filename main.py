from fastapi import FastAPI, HTTPException
from database import *
from api_models import *

app = FastAPI(
    title="Stage Two Task: A simple REST API capable of CRUD operations on a 'person' resource.",
    version="1.0.0",
    on_shutdown=[conn.close],
)


# create
@app.post("/api/")
async def create_person(person: PersonModel) -> PersonResponse:
    if db_read_person(person.name):
        raise HTTPException(
            status_code=409,
            detail=f"Person with '{person.name}' already exists",
        )

    person = db_create_person(person.name, person.age)
    return person_map(person)


# read
@app.get("/api/{name}")
async def read_person(name: str) -> PersonResponse:
    person = db_read_person(name)
    if person:
        return person_map(person)

    raise HTTPException(status_code=404, detail=f"Person with '{name}' not found")


# update
@app.put("/api/{name}")
async def update_person(name: str, age_model: AgeModel) -> PersonResponse:
    if db_read_person(name):
        db_update_person_age(name, age_model.age)
        return person_map(db_read_person(name))

    raise HTTPException(status_code=404, detail=f"Person with '{name}' not found")


# delete
@app.delete("/api/{name}")
async def delete_person(name: str) -> DeleteResponse:
    if db_read_person(name):
        db_delete_person(name)
        return dict(status=f"Person with '{name}' deleted")

    raise HTTPException(status_code=404, detail=f"Person with '{name}' not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        use_colors=True,
        host="127.0.0.1",
        port=8000,
        reload=0,
    )
