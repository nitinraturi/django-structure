# django-structure
Pre configured django project for making development easy

## Usage
- git clone https://github.com/nitinraturi/django-structure.git
- pip install -r requirements.txt
- create a file .env where manage.py is located and set your environment variables. Have a look same file: .env-sample
- Generate SECRET_KEY using: ``` python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))' ```
- Now replace the SECRET_KEY value with the value generated above in your .env file.
- That's all, start developing...

## Features
- Django version 2.2.8 (LTS).
- Manage multiple environments
