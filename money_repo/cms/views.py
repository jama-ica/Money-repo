from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question



def index(request):
    return render(request, 'index.html')

def year(request):
    return render(request, 'year.html')

def yearly(request):
    return render(request, 'yearly.html')

def month(request):
    return render(request, 'month.html')

def monthly(request):
    return render(request, 'monthly.html')

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)