from config.celery import app
from .utils import send_activation_code
from .utils_2 import send_recovery_code
from .utils_emp import send_employer_activation_code


@app.task()
def send_activation_code_celery(email, activation_code):
    send_activation_code(email, activation_code)


@app.task()
def send_recovery_code_celery(email, recovery_code):
    send_recovery_code(email, recovery_code)


@app.task()
def send_employer_activation_code_celery(email, employer_activation_code):
    send_employer_activation_code(email, employer_activation_code)

