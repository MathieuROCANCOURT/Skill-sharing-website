# Skill-sharing-website

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Installation and run

### Python compatibility

Django 5.2 supports Python 3.10, 3.11, 3.12, 3.13, and 3.14 (as of 5.2.8). We highly recommend and only officially
support the latest release of each series.

### Windows

Open your terminal (Windows PowerShell) and enter these commands.

```bash
git clone https://github.com/MathieuROCANCOURT/Skill-sharing-website.git
cd ./Skill-sharing-website
python -m venv .venv
.\.venv\Script\activate
pip install -r requirements.txt
python manage.py runserver
```

### Ubuntu

Open your terminal and enter these commands.

```bash
git clone https://github.com/MathieuROCANCOURT/Skill-sharing-website.git
cd ./Skill-sharing-website
python -m venv .venv
source ./.venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```

## User in actual database

| Username | Password          |
|----------|-------------------|
| user     | fD86adVs0p\cM£s>j |
| pilou    | jop&59k-ferHjuy   |
| toupie   | fselhiµ594fer486y |

## UML Diagrams

### Use case diagram

![Use case diagram.png](doc/1-Use%20case/Use%20case%20diagram.png)

### Class diagram

![Class diagram.png](doc/2-Class/Class%20diagram.png)

### Sequence diagram

![User sequential diagram on display calendar with available.png](doc/3-Sequence/User%20sequential%20diagram%20on%20display%20calendar%20with%20available.png)

## Mockup website

![website mockup.png](doc/4-Mockup/website%20mockup.png)

## Command-line

### Check the system.

This command check if a url is link to a view and settings for example also before migrate in the database.

```bash
python migrate.py check
```

### Launch shell Django

This command open a shell python where we can make the operations on Django Database.

```bash
python migrate.py shell
```

### Change models and migrate in database to apply modification in the models

```bash
python manage.py makemigrations skill_sharing
python manage.py sqlmigrate skill_sharing 0001
```

### Change database Django

This command permit to add, delete or modify the tables with models implementers in the models.

```bash
python manage.py shell
```

#### Create a user in shell Django

**Vigilance:** L'argument doit être en simple quote pour que le mot de masse soit crypté par l'algorithme PBKDF2. En
double quotes, cela affiche le mot de passe en clair dans la base de données.

```py
from django.contrib.auth.models import User

user = User.objects.create_user(username="toupie", first_name="Toto", last_name="Vopa", email="tv@examp.com",
                                password='fselhiµ594fer486y')
user.save()
```

### Create an admin in database

```bash
python manage.py createsuperuser
```

### Launch Django development server

This command permit to launch the code and see the website on the localhost.

```bash
python manage.py runserver
```