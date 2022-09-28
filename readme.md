# Steps to run  Project:

### Step-1:
Set up the virtual environment 

#
### Step-2: 
Install packages
 ```
 pip install -r requirements.txt
 ```
#

### Step-3: 
Setup mysql server
after that update settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME':<Database name>,  
        'USER':<Username>,  
        'PASSWORD':<Yourpassword>,  
        'HOST':'localhost',  
        'PORT':'3306'  
    }
}

```
### Step-4:
migrate your database
```
python manage.py migrate
```
### Step-5:
For admin login you need to create superuser
```
python manage.py createsuperuser
```
### Step-6:
Run Server
```
python manage.py runserver
```


