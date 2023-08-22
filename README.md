# Django app starter template

Use this as a template to start your Django app from.

## Included/installed Features:
- "Switch user" admin feature
- Basic flexible page template
- Custom sign in/out pages
- Custom error pages
- Custom error handling, with logging and slack room notifications
- Debugging toolbar
- Django extensions
- Template helpers for preset design components; buttons, icons, header, tabs, etc
- UI framework using Bloodline, Tachyons, select2, tooltip and overlays


## Install Requirements

Python 3.9 ish +

Postgres 14 ish +


## 📖 Installation
```
$ git clone https://github.com/ecumike/django-app-starter.git
$ cd django-app-starter
```

Setup some localhost variables:
```
  export DJANGO_DEBUG=True
```

Now setup local environment and install:

```
$ python3 -m venv .env
$ source .env/bin/activate

(.env) $ pip install -r requirements.txt
(.env) $ ./manage.py migrate
(.env) $ ./manage.py createsuperuser
(.env) $ ./manage.py runserver

# Load the site at http://127.0.0.1:8000
```


## ✍ Customizing for your project:

Search and replace default names with your project/app names (CASE SENSATIVE):
```
Search for: `myproject` replace with `your_project_name`

Search for: `Myproject` replace with `Your_project_name`

Search for: `myapp` replace with `your_app_name`

Search for: `Myapp` replace with `Your_app_name`
```

Change directory names:
```
`myproject` to `your_project_name`

`myapp` to `your_app_name`

`templates/myapp` to `templates/your_app_name`
```



## Coding style guidelines
 
We follow the basic Django and Python coding principles and styles:  
https://docs.djangoproject.com/en/4.0/misc/design-philosophies/  
https://docs.djangoproject.com/en/4.0/internals/contributing/writing-code/coding-style/  

 
## ⭐️ Support
Give a ⭐️  if this project helped you!

## License
[Apache 2 license - Free to use and modify](LICENSE)

