from django import forms

class SampleChoiceForm(forms.Form):
	choice1 = forms.fields.ChoiceField(
		choices = (
			('ja', '日本'),
			('us', 'アメリカ'),
			('uk', 'イギリス'),
			('ch', '中国'),
			('kr', '韓国')
		),
		required=True,
		widget=forms.widgets.Select
	)

