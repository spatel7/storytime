import os
from django.utils import timezone

def populate():
	u1 = add_user("spatel7", "spatel7@berkeley.edu", "123", "Sahil", "Patel", "I like food.")

	s1 = add_story(u1, "Berkeley Beginnings")

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

	s2 = add_story(u1, "Haircut Problems")

	add_photo(story=s2,
		position=0,
		caption="Here's the before. Here goes nothing.")

	add_photo(story=s2,
		position=1,
		caption="The after! Not bad!")

	for s in Story.objects.all():
		for p in Photo.objects.filter(story=s):
			print "- {0} - {1}".format(str(s), str(p))

def add_user(username, email, password, first_name, last_name, bio):
	u = User.objects.get_or_create(username=username, email=email, first_name=first_name, last_name=last_name)[0]
	u.set_password(password)
	u.save()
	p = Profile.objects.get_or_create(user=u, bio=bio)[0]
	return u

def add_story(user, title):
	s = Story.objects.get_or_create(user=user, title=title, pub_date=timezone.now())[0]
	return s

def add_photo(story, position, caption):
	p = Photo.objects.get_or_create(story=story, position=position, caption=caption, pub_date=timezone.now())[0]
	return p

if __name__ == '__main__':
	print "Starting Stories population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stories.settings')
	from storiesapp.models import Story, Photo, Profile
	from django.contrib.auth.models import User
	populate()