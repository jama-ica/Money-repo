from django import forms
#
from .models import Bank

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

