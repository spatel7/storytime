import os
from django.utils import timezone

def populate():
	s1 = add_story("spatel7", "Berkeley Beginnings")

	add_photo(story=s1,
		position=0,
		caption="It was not difficult to decide on Berkeley.")

	add_photo(story=s1,
		position=1,
		caption="It was extremeley difficult to find the right words.")

	add_photo(story=s1,
		position=2,
		caption="Waiting was even worse.")

	add_photo(story=s1,
		position=3,
		caption="But boy was the award sweet.")

	s2 = add_story("spatel7", "Haircut Problems")

	add_photo(story=s2,
		position=0,
		caption="Here's the before. Here goes nothing.")

	add_photo(story=s2,
		position=1,
		caption="The after! Not bad!")

	for s in Story.objects.all():
		for p in Photo.objects.filter(story=s):
			print "- {0} - {1}".format(str(s), str(p))

def add_story(author, title):
	s = Story.objects.get_or_create(author=author, title=title, pub_date=timezone.now())[0]
	return s

def add_photo(story, position, caption):
	p = Photo.objects.get_or_create(story=story, position=position, caption=caption, pub_date=timezone.now())[0]
	return p

if __name__ == '__main__':
	print "Starting Stories population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stories.settings')
	from storiesapp.models import Story, Photo
	populate()