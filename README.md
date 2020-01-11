# django-structure
Pre configured django project for making development fast, by cutting the initial setup time.

## Features
- Django version 2.2.8 (LTS)
- Ideal directory structure
- Manage multiple environments
- Logging configured
- Extended User model i.e., apps.users.User
- Compressor and Minifier Implemented.
- Pages app for static pages
- Sitemap implemented **[OPTIONAL]** i.e., conf/sitemaps.py and conf/urls.py #code commented

## Dependencies
- Install memcached for caching
```
sudo apt-get install memcached
```

## Usage
- git clone https://github.com/nitinraturi/django-structure.git
- First, remove **.git** file and set your own repository later
```
rm -rf .git
```
- Create and activate your virtual environment
```
virtualenv -p python3 venv
source venv/bin/activate
```
- Now install **requirements.txt**
```
pip install -r requirements.txt
```
- Create a file **.env** where **manage.py** is located and set your environment variables. Have a look sample file: **.env-sample**
- Generate **SECRET_KEY** using the command
```
python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'
```
- Now replace the **SECRET_KEY** value inside your **.env** file with the value *generated in your terminal*.
- Let's create required directories now, run
```
mkdir -p static/{css,js,img} static_cdn/{static_root,media_root} templates/{snippets,layouts} apps logs locale
```
- Compressing and minifying will run when DEBUG=FALSE by default. [Read usage](https://raturi.in/blog/compress-and-minify-files-django/)


> That's all, start developing. Don't forget to contribute if you have any improvements or bug fixes.
