from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.shortcuts import render, redirect
from . import forms
# 
import datetime
import csv
from io import TextIOWrapper, StringIO
from django.db.models import Sum
# 
from .models import BankPayee
from .models import BankPaysource
from .models import Bank
from .models import BankShop
from .models import Bankbook
from .models import BankbookIn
from .models import BankbookOut
from .models import IncomeKind
from .models import Income
from .models import ExpenseKind
from .models import PayMethod
from .models import Expense

def top(request):
	return redirect('index')

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

def budget(request):
	return render(request, 'budget.html')

#def importBankbook(request):
#	banks = Bank.objects.all()
#	context = {'banks' : banks, 'Bankbooks' : []}
#	return render(request, 'import/Bankbook.html', context)
def importBankbook(request):
	if request.method == 'POST':
		if 'csv' in request.FILES:
			form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
			csv_file = csv.reader(form_data)
			header = next(csv_file)  # skip header

			for line in csv_file:
				BankbookIn = BankbookIn()
				#TODO
				BankbookIn.bank_book = Bankbook.objects.get(id=1)
				#TODO
				BankbookIn.bank_payee = BankPayee.objects.get(id=1)
				BankbookIn.amount = line[1]
				BankbookIn.date = datetime.datetime.now()
				BankbookIn.note = request.POST['select'] #str(line[4])
				BankbookIn.save()

		return redirect('monthly')
	else:
		form = forms.SampleChoiceForm()
		context = {
			'form': form,
		}
		return render(request, 'import/Bankbook.html', context)

def importIncomes(request):
	form = forms.SampleCalenderForm(initial = {'input' : '2020-05'})
	context = {
		'form': form,
	}
	return render(request, 'import/incomes.html', context)

def importExpensesThisMonth(request):
	dt_now = datetime.datetime.now()
	return redirect('expenses', year=dt_now.year, month=dt_now.month)

class ExpenseDetail():
	def __init__(self):
		self.id = ''
		self.type = ''
		self.bankbook_out = 0
		self.date = ''
		self.amount = 0
		self.expense_kind = ''
		self.note = ''


def importExpenses(request, year, month):
	expenses = Expense.objects.filter(date__year=year, date__month=month)
	bankbookOuts = BankbookOut.objects.filter(date__year=year, date__month=month)
	expenseKinds = ExpenseKind.objects.all()
	#sum = BankbookOut.objects.filter(date__year=year, date__month=month).aggregate(Sum('amount'))
	#'total' : sum['amount__sum'],

	list = []
	for bankbookOut in bankbookOuts:
		expenseSum = 0
		for expense in expenses:
			if expense.bankbook_out == bankbookOut:
				item = ExpenseDetail()
				item.id = expense.id
				item.type = 'expense'
				item.bankbook_out = expense.bankbook_out
				item.date = expense.date
				item.amount = expense.amount
				item.expense_kind = expense.expense_kind
				item.note = expense.note
				list.append(item)
				expenseSum += expense.amount
		# rest
		if expenseSum < bankbookOut.amount:
			item = ExpenseDetail()
			item.id = 0
			item.type = 'bankbook'
			item.bankbook_out = bankbookOut
			item.date = bankbookOut.date
			item.amount = bankbookOut.amount - expenseSum
			item.expense_kind = 'others'
			item.note = bankbookOut.note
			list.append(item)

	context = {
		'year' : year,
		'month' : str(month).zfill(2),
		'expenseKinds' : expenseKinds,
		'expenses' : list,
	}
	return render(request, 'import/expenses.html', context)

def importExpensesModify(request, year, month, expense_id):
	expense = Expense.objects.get(id=expense_id)
	expense.amount = request.POST['amount']
	expense.expense_kind = ExpenseKind.objects.get(name=request.POST['expense_kind'])
	expense.save()
	return redirect('expenses', year=year, month=month)

def importExpensesDelete(request, year, month, expense_id):
	expense = Expense.objects.get(id=expense_id)
	expense.delete()
	return redirect('expenses', year=year, month=month)

def importExpensesAdd(request, year, month, bankbook_out):
	expense = Expense()
	expense.bankbook_out = BankbookOut.objects.get(id=bankbook_out)
	expense.expense_kind = ExpenseKind.objects.get(name=request.POST['expense_kind'])
	# pay_method
	expense.amount = request.POST['amount']
	expense.date = BankbookOut.objects.get(id=bankbook_out).date
	expense.save()
	return redirect('expenses', year=year, month=month)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

def creditCard(request):
	return HttpResponse("credit")


#TODO rename import/bankbook 
def upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		header = next(csv_file)  # skip header

		for line in csv_file:
			BankbookIn = BankbookIn()
			#TODO
			BankbookIn.bank_book = Bankbook.objects.get(id=1)
			#TODO
			BankbookIn.bank_payee = BankPayee.objects.get(id=1)
			BankbookIn.amount = line[1]
			BankbookIn.date = datetime.datetime.now()
			BankbookIn.note = request.POST['bank'] #str(line[4])
			BankbookIn.save()

		return importBankbook(request)

	else:
		return importBankbook(request)



#class SampleChoiceView(View):
#	def get(self, request):
#		form = forms.SampleChoiceForm()
#		context = {
#			'form': form
#		}
#		return render(request, 'choice_sample.html', context)

#sample_choice_view = SampleChoiceView.as_view()
