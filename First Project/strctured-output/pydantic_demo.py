from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'John Doe'
    age: Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5.0)

new_student={'age':'32', 'email': 'abc@gmail.com'}
student=Student(**new_student)


print(student.model_dump_json())
