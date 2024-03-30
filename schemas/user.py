from pydantic import BaseModel, EmailStr


class User(BaseModel):
    user_name: str
    email: str = None
    password: str


class Validate(BaseModel):
    email: EmailStr
    password: str


class ConsultationForm(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    job_title: str
    email_id: str
    phone_number: str
    country: str
    domain_name: str
    share_details: str
    query: str
    hear_about: str
