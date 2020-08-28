from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('year', views.year, name='year'),
    path('yearly', views.yearly, name='yearly'),
    path('month', views.month, name='month'),
    path('monthly', views.monthly, name='monthly'),
    path('budget', views.budget, name='budget'),

    path('bankbook', views.importBankbook, name='bankbook'),
    path('incomes', views.importIncomes, name='incomes'),
    path('expenses/<int:year>/<int:month>/', views.importExpenses, name='expenses'),

	path('upload/', views.upload, name='upload'), # import Bankbook

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
