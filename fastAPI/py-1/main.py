from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Path, Query
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Todo(BaseModel):
    name: Annotated[str, Field(max_length=50, min_length=1, title="Name of task", description="Name of the task/ todo")]
    description: Annotated[str, Field(default=None, max_length=200, min_length=20, title="Description of the task")]
    priority: Annotated[int, Field(default=1, ge=1, title="Priority of the task", description="lesser number means greater priority")]
    completed: Annotated[bool, Field(default=False, title="If task is completed or not")]
    subTasks: Annotated[list["Todo"], Field(default=[], min_length=0, max_length=10, title="Subtasks of the task", description="List of subtasks")]

@app.get("/")
def hello():
    return { "message": "Hello World", "Success": True, "timestamp": datetime.now().isoformat() }
