from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QuestionForm
from .models import QandA

# Create your views here.


def home_page(request):
    question_answer = {
        "What color is the sky": "The sky is blue you dumb ass !!",
        "What do you know about Python": "Python is the best language"
    }
    if request.method == 'POST':
        question = request.POST.get('question', '')
        answer = question_answer.get(question, 'Sorry i dont know this question...')
    else:
        question = ''
        answer = ''


    return render(request, 'index.html', {
        'question': question,
        'answer': answer
    })