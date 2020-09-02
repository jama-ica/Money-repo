from django.urls import path

from . import views

urlpatterns = [
	# index
	path('', views.top, name='top'),
	path('index', views.index, name='index'),

	path('year', views.year, name='year'),
	path('yearly', views.yearly, name='yearly'),
	path('month', views.month, name='month'),
	path('monthly', views.monthly, name='monthly'),
	path('budget', views.budget, name='budget'),

	path('bankbook', views.importBankbook, name='bankbook'),
	path('incomes', views.importIncomes, name='incomes'),

	# expenses
	path('expenses-this-month/', views.importExpensesThisMonth, name='expenses-this-month'),
	path('expenses/<int:year>/<int:month>/', views.importExpenses, name='expenses'),
	path('expenses/<int:year>/<int:month>/delete/<int:expense_id>', views.importExpensesDelete, name='expenses-delete'),
	path('expenses/<int:year>/<int:month>/modify/<int:expense_id>', views.importExpensesModify, name='expenses-modify'),
	path('expenses/<int:year>/<int:month>/add/<int:bankbook_out>', views.importExpensesAdd, name='expenses-modify'),

	path('credit-card', views.creditCard, name='credit-card'),

	path('upload/', views.upload, name='upload'), # import Bankbook

]
