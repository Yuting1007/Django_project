### Django Project Setting
we need to activate the virtual environment first under the directory of django
```
source django/bin/activate
cd myproject
```
For creating a project or an applicaion
```
django-admin startproject project_name;
django-admin startapp app_name;
```
### Mysql Database Setting
Start a new terminal for database first.
When you install MySQL and try to access it on the local machine with the [root user](https://phoenixnap.com/kb/how-to-reset-mysql-root-password-windows-linux), the command you use is:
```
mysql -u root -p
```
[reference](https://phoenixnap.com/kb/access-denied-for-user-root-localhost)
The database I created for this project is called yutingsite `create database yutingsite;`.
```
use mysite;
show tables;
```
running the coomands above is going to show all the tables created by migration.

For now, the mysql database is settled. We need to connect it with our project. In the `settings.py` file, follow the [instruction](https://docs.djangoproject.com/en/2.2/ref/settings/#databases) to change the database setting.

Then, back to the terminal, run command,
```
python manage.py migrate
```
It will help to initiate some tables.

### Database Design
In this step, I create a new app called blog `django-admin startapp app_name` . And defined all tables in models.py. Then add this app in the project `settings.py`.
After this, in the terminal, async this app and create tables in mysql databases
```
python manage.py makemigrations blog
python manage.py migrate
```
in mysql, check the results by `show tables; desc blog_post;`

### Django Admin
The path for admin site is `.../admin`. We can see a page for login.
To create a admin account, we can use the command like `python manage.py createsuper user` and login with that account.
To async the blog app in the admin page we just create, we could change the `admin.py` file in blog app and give settings to its display.

Also, for customizing your `admin.py` we could follow this [document](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/).
