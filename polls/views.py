from django.shortcuts import render, get_object_or_404
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
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, "polls/details.html", {
        "question": question
    })

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta no {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta no {question_id}")
