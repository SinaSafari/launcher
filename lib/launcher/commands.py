import os


def run_update_requirements_txt_command():
    os.system("pip freeze > requirements.txt ")


def run_serve_app_command():
    os.system("uvicorn main:app --reload")


def run_tests_command():
    os.system("pytest")


def run_format_command():
    os.system("black .")
