from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from schemas.index import User, Validate, ConsultationForm
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.db import conn
import re

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Signup
@app.get("/signup/")
async def read_signup(request: Request):
    return templates.TemplateResponse("login_signup.html", {"request": request})


@app.post("/signup/")
async def signup(request: Request):
    try:
        form = await request.form()
        user = dict(form)
        print(user)
        cursor = conn.cursor()
        if user['password'] != user['confirm_password']:
            return {"message": "Password and Confirm Password don't match"}

        query = "SELECT * FROM user_info WHERE email =%s"
        cursor.execute(query, (user['email'],))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            return {"message": "Email already exists!"}

        query = "INSERT INTO user_info (user_name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (user['user_name'],
                       user['email'], user['password']))
        conn.commit()
        cursor.close()
        response_message = {"message": "Signup Successful!"}
        return response_message

    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal server error')


# Login
@app.get("/login/")
async def read_login(request: Request):
    return templates.TemplateResponse("login_signup.html", {"request": request})


@app.post("/login/")
async def login(request: Request):
    try:
        form = await request.form()
        user = dict(form)
        print(user)
        cursor = conn.cursor()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user['email']):
            cursor.close()
            return {"message": "Incorrect email or password"}

        query = "SELECT * FROM user_info WHERE email = %s AND password = %s"
        cursor.execute(query, (user['email'], user['password']))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return {"message": "Login successful!"}
        else:
            return {"message": "Email or Password are incorrect!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal server error')


# Consultation Form
@app.get("/consultation/")
async def read_root(request: Request):
    return templates.TemplateResponse("connect.html", {"request": request})


@app.post("/consultation/")
async def submit_consultation_form(request: Request):
    try:
        form = await request.form()
        form_dict = dict(form)
        print(form_dict)
        cursor = conn.cursor()
        if form_dict['query'] == 'other':
            form_dict['query'] = form_dict['other_query']

        query_ = "Insert INTO consultation_form (first_name,last_name,company_name,job_title,email_id,phone_number,country,domain_name,share_details,query,hear_about) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query_, (form_dict['first_name'], form_dict['last_name'], form_dict['company_name'], form_dict['job_title'],
                                form_dict['email_id'], form_dict['phone_number'], form_dict['country'], form_dict['domain_name'], form_dict['share_details'], form_dict['query'], form_dict['hear_about']))

        conn.commit()
        cursor.close()
        response_message = {"message": "Form submitted successfully!"}
        return response_message

    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal server error')


# Home
@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# About
@app.get("/about/")
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


# Service
@app.get("/service/")
async def read_service(request: Request):
    return templates.TemplateResponse("service.html", {"request": request})


# After Login Page
@app.get("/after_login/")
async def read_index(request: Request):
    return templates.TemplateResponse("AfterLogin.html", {"request": request})
