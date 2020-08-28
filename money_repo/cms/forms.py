from django import forms
#
from .models import Bank
import datetime

#class SampleChoiceForm(forms.Form):
#	select = forms.fields.ChoiceField(
#		choices = (
#			('ja', '日本'),
#			('us', 'アメリカ'),
#			('uk', 'イギリス'),
#			('ch', '中国'),
#			('kr', '韓国')
#		),
#		required=True,
#		widget=forms.widgets.Select
#	)

class SampleChoiceForm(forms.Form):
	select = forms.ModelChoiceField(Bank.objects)

class SampleCalenderForm(forms.Form):
	#input = forms.DateTimeField(
	#	#label='所有者',
	#	initial=datetime.date.today,
	#	#error_messages={'required': 'Please enter your name'},
	#	#help_text='A valid email address, please.',
	#	#widget=forms.DateTimeInput(attrs={"type":"date"})
	#	widget=forms.SelectDateWidget(attrs={'type': 'month'})
	#)
	input = forms.DateTimeField(
		initial='2019-05',
		widget=forms.DateInput(attrs={'type': 'month'})
	)
	