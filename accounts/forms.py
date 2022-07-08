from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

# Forms

class NewUserForm(SignupForm):
	first_name = forms.CharField(label='First name (optional)', required=False, max_length=150, widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'First name'}))
	last_name = forms.CharField(label='First name (optional)', required=False, max_length=150, widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Last name'}))

	# class Meta:
	# 	model = User
	# 	fields = ("username", "email", "first_name", "last_name", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.first_name = self.cleaned_data['first_name']
	# 	user.last_name = self.cleaned_data['last_name']
	# 	if commit:
	# 		user.save()
	# 	return user

	def save(self, request):
		adapter = get_adapter(request)
		user = adapter.new_user(request)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		adapter.save_user(request, user, self)
		self.custom_signup(request, user)
		setup_user_email(request, user, [])
		return user