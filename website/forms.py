from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Research

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = ('title', 'author', 'file', 'cover')

class GraphFrom(forms.Form):
	city = forms.CharField(max_length=100)
	year = forms.CharField(max_length=4)

class GraphByYearForm(forms.Form):
	city = forms.CharField(max_length=100)
	yearStart = forms.CharField(max_length=4)
	yearEnd = forms.CharField(max_length=4)