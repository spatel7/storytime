from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from storiesapp.models import Story, Photo
from storiesapp.forms import StoryForm, PhotoForm
from django.forms.formsets import formset_factory, BaseFormSet
from django.utils import timezone

def index(request):
	context = RequestContext(request)
	story_list = Story.objects.all()
	photos_list = Photo.objects.filter(story__in=story_list)
	context_dict = {'stories': story_list, 'photos': photos_list}
	return render_to_response('storiesapp/index.html', context_dict, context)

def add_story(request):
	context = RequestContext(request)
	PhotoFormSet = formset_factory(PhotoForm, max_num=6, formset=BaseFormSet)
	if request.method == 'POST':
		story_form = StoryForm(request.POST)
		photo_formset = PhotoFormSet(request.POST, request.FILES)
		if story_form.is_valid() and photo_formset.is_valid():
			story = story_form.save()
			story.pub_date = timezone.now()
			story.save()
			position = 0
			for form in photo_formset.forms:
				photo = form.save(commit=False)
				photo.story = story
				photo.position = position
				photo.pub_date = timezone.now()
				photo.save()
				position += 1
			return index(request)
		else:
			print story_form.errors
			print photo_formset.errors
	else:
		story_form = StoryForm()
		photo_formset = PhotoFormSet()
	return render_to_response('storiesapp/add_story.html', {'story_form': story_form, 'photo_formset': photo_formset}, context)

def login(request):
	context = RequestContext(request)
	return render_to_response('storiesapp/login.html', {}, context)

def register(request):
	context = RequestContext(request)
	return render_to_response('storiesapp/register.html', {}, context)