# Skill-sharing-website

## Command-line

### Check the system.

This command check if a url is link to a view and settings for example.

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
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
```

### Change database Django

This command permit to add, delete or modify the tables with models implementers in the models.

```bash
python manage.py shell
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