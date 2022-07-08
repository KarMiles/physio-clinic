from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Forms

class NewUserForm(UserCreationForm):
	fname = forms.CharField(required=False, max_length=150)
	sname = forms.CharField(required=False, max_length=150)

	class Meta:
		model = User
		fields = ("username", "email", "fname", "sname", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.fname = self.cleaned_data['fname']
		user.sname = self.cleaned_data['sname']
		if commit:
			user.save()
		return user