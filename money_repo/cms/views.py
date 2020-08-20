from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.shortcuts import render
from . import forms
# 
import datetime
import csv
from io import TextIOWrapper, StringIO
# 
from .models import BankPayee
from .models import BankPaysource
from .models import Bank
from .models import BankShop
from .models import BankBook
from .models import BankBookIn
from .models import BankBookOut
from .models import IncomeKind
from .models import Income
from .models import ExpenseKind
from .models import PayMethod
from .models import Expense


def index(request):
	return render(request, 'index.html')

def year(request):
	context = {'year' : 2020}
	return render(request, 'year.html', context)

def yearly(request):
	years = [2010, 2011, 2012, 2020]
	context = {'years' : years}
	return render(request, 'yearly.html', context)

def month(request):
	return render(request, 'month.html')

def monthly(request):
	return render(request, 'monthly.html')

#def importBankbook(request):
#	banks = Bank.objects.all()
#	context = {'banks' : banks, 'bankBooks' : []}
#	return render(request, 'import/bankbook.html', context)
def importBankbook(request):
	form = forms.SampleChoiceForm()
	banks = Bank.objects.all()
	context = {
		'form': form,
		'banks' : banks,
		'bankBooks' : [],
	}
	return render(request, 'import/bankbook.html', context)

def importDetail(request):
	return render(request, 'import/detail.html')

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



def upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		header = next(csv_file)  # skip header

		for line in csv_file:
			bankBookIn = BankBookIn()
			#TODO
			bankBookIn.bank_book = BankBook.objects.get(id=1)
			#TODO
			bankBookIn.bank_payee = BankPayee.objects.get(id=1)
			bankBookIn.amount = line[1]
			bankBookIn.date = datetime.datetime.now()
			bankBookIn.note = request.POST['bank'] #str(line[4])
			bankBookIn.save()

		return importBankbook(request)

	else:
		return importBankbook(request)



class SampleChoiceView(View):
	def get(self, request):
		form = forms.SampleChoiceForm()
		context = {
			'form': form
		}
		return render(request, 'choice_sample.html', context)

sample_choice_view = SampleChoiceView.as_view()
