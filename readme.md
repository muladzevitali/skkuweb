# Portfolio project

## Installation
* Change sender EMAIL_HOST_USER, EMAIL_HOST_PASSWORD and RECIPIENT_LIST parameters in setting.py
* Install the requirements with:
```bash
pip install -r requirements.txt
```
* Make migrations with
```bash
python manage.py makemigrations
python manage.py makemigrations web
python manage.py migrate
```
* Create super user with:
```bash
python manage.py createsuperuser
```

* Run the server with:
```bash
python manage.py runserver
```
---

**Notice 1**: _You should add landscape & portfolio photos in the folders **media/portfolio/landscapes** & **media/portfolio/portfolios** accordingly_  
**Notice 2**: _Admin url path: **/skuadmin**_