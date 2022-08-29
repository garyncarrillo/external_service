# add django tutorial
https://docs.djangoproject.com/en/3.2/intro/tutorial01/

# url course
https://platzi.com/clases/2694-django/45263-nuestro-primer-proyecto-premios-platzi-app/
# create app
django-admin startproject mysite

# add git control code change
git init

# add gitignorefile
touch .gitignore   

# runserver with python on DJango
python manage.py runserver

# create app into the main project
python manange.py startapp name_app (poll)

# create migration into del microservices o micro app
python manage.py makemigrations polls

# run migration
python manage.py migrate

# python console
python manage.py shell

# import models of microservices or microapp
from polls.models import Question, Choice

# data_time fields
from django.utils import timezone
# get all elements a models
Question.objects.all()

q =  Question(question_text='Cual es el mejor curso de platzi', pub_date= timezone.now())
q.save()


pip install django-enviro