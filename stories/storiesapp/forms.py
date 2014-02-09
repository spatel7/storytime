from django import forms
from storiesapp.models import Story, Photo, Profile
from django.contrib.auth.models import User

class StoryForm(forms.ModelForm):
	title = forms.CharField(max_length=200, help_text="What is your story called?")

	class Meta:
		model = Story
		fields = ('title',)

class PhotoForm(forms.ModelForm):
	caption = forms.CharField(max_length=200, help_text="Caption your moment.")

	class Meta:
		model = Photo
		fields = ('picture', 'caption',)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio',)