print("Hello Git")
from fastapi import FastAPI

app = FastAPI()

students = {}


@app.get("/")
def home():
    return {"message": "Student API"}



# CREATE student
@app.post("/students")
def create_student(id: int,
                   name: str,
                   age: int):

    students[id] = {
        "name": name,
        "age": age
    }

    return {
        "message": "Student added",
        "data": students[id]
    }

# READ all students
@app.get("/students")
def get_students():

    return students

# UPDATE student
@app.put("/students/{id}")
def update_student(id: int,
                   name: str,
                   age: int):

    if id not in students:
        return {
            "message":"Student not found"
        }

    students[id] = {
        "name":name,
        "age":age
    }

    return {
        "message":"Student updated",
        "data":students[id]
    }
# DELETE student
@app.delete("/students/{id}")
def delete_student(id: int):

    if id not in students:
        return {
            "message":"Student not found"
        }

    deleted_student = students.pop(id)

    return {
        "message":"Student deleted",
        "data": deleted_student
    }