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

	path('upload/', views.upload, name='upload'), # import Bankbook

]
