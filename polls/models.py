#/polls/models
from datetime import datetime
from pyexpat import model
from secrets import choice
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published") # "field's description"
    
    def __str__(self):
        return self.question_text
    
    def was_publised_resently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def find_by(id):
     return Question.objects.get(pk=id)

    def all():
        return Question.objects.all()

    def choices(id):
        return Question.objects.get(pk=id).choice_set.all()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
