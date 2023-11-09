# To-do-list
This project is done using HTML, CSS, Javascript. The framework used is django.
### Start
Create a folder and then open that with any code editor, I used VS code in my case. Make a login and registration form.
### Django application
Install django usinf `pip install django`
Open the terminal and run `django-admin makeproject <your project name>`<br>
After that a folder will be created containing all the required dependencies and later requirements, there we'll be having a manage.py so open the terminal and run `python manage.py startapp <your app's name`.<br>
This will create a project for you and you will be having a default sqlite database in it which I have used to store my data in it.<br>
Now when the login registration and the todo list files are ready then we have to create a folder named `template` inside our app. Where we need to store the files to be used.
And then the form of login and registration is completed which in my case is in the same file in the same file and I used the wrapper property so that tha login page slides up the registration page.
Now we have to register our app inside the django where the app name is written in the `settings.py` file. And then we have to register our template folder in the dirs list of `settings.py`.
Write ~python manage.py makemigrations~  and run python manage.py migrate for making and pushing the registered user's data into the database.
