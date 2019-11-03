from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ClueSearchForm(forms.Form):
	
	VALUES = [
		('any', 'any'),
		('100', 100.0),
		('200', 200.0),
		('300', 300.0),
		('400', 400.0),
		('500', 500.0),
		('600', 600.0),
		('700', 700.0),
		('800', 800.0),
		('900', 900.0),
		('1000', 1000.0),
	]

	SORT_OPTIONS = [
	('airdate', 'airdate'),
	('category', 'category'),
	('value', 'value'),
	]

	keyword = forms.CharField(label='Search', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter keyword here'}),required=False)
	category = forms.CharField(label='Category', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter specific category'}), required=False)
	start_date = forms.CharField(label='Start Date', max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'mm/dd/yyyy'}))
	end_date = forms.CharField(label='End Date', max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'mm/dd/yyyy'}))
	value = forms.ChoiceField(label='Difficulty (cost)',choices=VALUES)
	sort = forms.ChoiceField(label='Sort by',choices=SORT_OPTIONS, required=False)
	# 2014-02-11T22:47:18.878Z

	

class BasicSearchForm(forms.Form):
	keyword = forms.CharField(label='keyword', max_length=100)



