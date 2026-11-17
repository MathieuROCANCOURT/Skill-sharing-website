# Skill-sharing-website

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