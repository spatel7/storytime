from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from storiesapp.models import Story, Photo
from storiesapp.forms import StoryForm, PhotoForm, UserForm, ProfileForm
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

def index(request):
	context = RequestContext(request)
	return render_to_response('storiesapp/index.html', {}, context)

@login_required
def add_story(request):
	context = RequestContext(request)
	PhotoFormSet = formset_factory(PhotoForm, max_num=6, formset=BaseFormSet)
	if request.method == 'POST':
		story_form = StoryForm(request.POST)
		photo_formset = PhotoFormSet(request.POST, request.FILES)
		if story_form.is_valid() and photo_formset.is_valid():
			u = User.objects.get(username=request.user)
			story = story_form.save(commit=False)
			story.user = u
			story.pub_date = timezone.now()
			story.save()
			position = 0
			for form in photo_formset.forms:
				photo = form.save(commit=False)
				photo.story = story
				photo.position = position
				photo.pub_date = timezone.now()
				if 'picture' in request.FILES:
					photo.picture = request.FILES['picture']
				photo.save()
				position += 1
			return HttpResponseRedirect("/storiesapp/home/")
		else:
			print story_form.errors
			print photo_formset.errors
	else:
		story_form = StoryForm()
		photo_formset = PhotoFormSet()
	return render_to_response('storiesapp/add_story.html', {'story_form': story_form, 'photo_formset': photo_formset}, context)

def user_login(request):
	context = RequestContext(request)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/storiesapp/home/')
			else:
				return HttpResponse("Your Stories account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('storiesapp/login.html', {}, context)

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = ProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True
			return HttpResponseRedirect('/storiesapp/login/')
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = ProfileForm()
	return render_to_response('storiesapp/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

@login_required
def home(request):
	context = RequestContext(request)
	story_list = Story.objects.filter(user=request.user)
	photos_list = Photo.objects.filter(story__in=story_list)
	context_dict = {'stories': story_list, 'photos': photos_list}
	return render_to_response("storiesapp/home.html", context_dict, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/storiesapp/')

