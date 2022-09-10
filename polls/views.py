from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<strong>Esta es la pagina principal de premios platzi</strong>")

def details(request, question_id):
    return HttpResponse(f"Esta viendo la pregunta no {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta no {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta no {question_id}")
