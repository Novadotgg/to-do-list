# To-do-list
This project is done using HTML, CSS, Javascript. The framework used is django.
## Start
Create a folder and then open that with any code editor, I used VS code in my case. Make a login and registration form.
## Django application
Install django usinf `pip install django`
Open the terminal and run `django-admin makeproject <your project name>`<br>
After that a folder will be created containing all the required dependencies and later requirements, there we'll be having a manage.py so open the terminal and run `python manage.py startapp <your app's name>`.<br>
This will create a project for you and you will be having a default sqlite database in it which I have used to store my data in it.<br>
Now when the login registration and the todo list files are ready then we have to create a folder named `template` inside our app. Where we need to store the files to be used.
And then the form of login and registration is completed which in my case is in the same file in the same file and I used the wrapper property so that tha login page slides up the registration page.
For running this project open the terminal and write 
~~~
python manage.py runserver
~~~
Now we have to register our app inside the django where the app name is written in the `settings.py` file. Like: (in my case it was app1)
~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
]
~~~

And then we have to register our template folder in the dirs list of `settings.py`:
~~~
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

~~~
Write 
~~~
python manage.py makemigrations
~~~
 and run 
 ~~~
 python manage.py  migrate
 ~~~

for making and pushing the registered user's data into the database.
### url.py django
This is the part where you need to specify the urls like when you click the login page os signup/registration page where should it redirect you, so you need to provide a path for the redirection, in my case I used separate for login, registration, home page:
~~~
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('log/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.Logout,name='logout'),
]
~~~

 ## To do list part
 Here the logic are made such that the todo list consists of the add task, add subtask, set due date, set priority.
 The create task part is contained in a container of a HTML file where the task can be added along with their respective due date and respective priority and this tasks consists of a checkbox, which when clicked marks the tasks as completed and then cuts off the whole task and then we can remove the task completely from the task list.
 ### Subtask
 The subtask button is connected along witht the task itself, so whenever any task is created we have the option to create a subtask too and we can even set the due date of the subtask itself and there exists a checkbox whch can be clicked when the subtask is completed.
 And after finishing the wholde task we can then completely cut off the main task and can remove it finally.
 And whenever the browser is refreshed the list will still be there as it's stored in the browser cache.
 ## Working
 When the user register and then logs in with the correctw credentials then he/she is redirected to the todolist site where the person can ass his/her todo list and can add subtasks too inside his/her todolist and can store them after that if they want to logout they can logout and will be redirected to the registration page.
