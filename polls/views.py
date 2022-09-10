from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    lastes_question_list = Question.objects.filter()
    # render(request=, "template", "context")
    
    return render(request, "polls/index.html", {
        "lastes_question_list": lastes_question_list
    })

def details(request, question_id):
    return HttpResponse(f"Esta viendo la pregunta no {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta no {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta no {question_id}")
