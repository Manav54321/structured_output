from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Don Toliver" # Default value
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, le=10)  

new_student = {"age": 31, 
               "email": "don.toliver@noidea.com",
               "cgpa": 9.20
}

student = Student(**new_student)

new_student_dict = dict(student)
new_student_json = student.model_dump_json()

print(new_student_dict)
print(new_student_json)

print(type(new_student_dict))
print(type(new_student_json))

print(student)
print(type(student))