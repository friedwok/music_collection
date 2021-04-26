from django.db import models
import uuid
from django.urls import reverse
from .additions import lyrics_html
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Song(models.Model):

	title = models.CharField(max_length=100)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, default='unknown')
	lyrics = models.TextField(max_length=10000, help_text="Enter some lyrics.")
	genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, help_text="Enter genres of the song.")
	album = models.ForeignKey('Album', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

	def get_authors(self):
		return ', '.join([ auth.alias for auth in Author.objects.filter(alias=self.author.alias) ])
		#return ', '.join([ auth.alias for auth in authors_of_song.objects.all() ])
		#return ', '.join([ auth.alias for auth in Author.objects.all() ])

	def get_full_song_name(self):
		#return 'get_full_song_name'
		#song_authors = ', '.join([ auth.alias for auth in authors.objects.all() ])
		#return self.get_authors() + ' - ' + self.title
		return self.author.alias + ' - ' + self.title

	def get_absolute_url(self):
		return reverse('song-page', args=[str(self.id)])

	def display_genre(self):
		return ', '.join([ song.name for genre in self.genre.all()[:3]])
	display_genre.short_description = 'Genre'

	def get_listening_count(self):
		return SongInstance.objects.filter(song=self).count()


class SongInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4,
				help_text="Unique ID for this composition of art.")
	song = models.ForeignKey('Song', on_delete=models.CASCADE, null=True)
	number_of_listens = models.IntegerField(default=0)
	released = models.DateField(null=True, blank=True)
	#ceollector is a owner of a colletion of musicial arts
	collector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	LOAN_STATUS = (
		('s', 'Coming out soon'),
		('r', 'Removed from public access'),
		('a', 'Available'),
		('d', 'Disabled in this region'),
	)

	status = models.CharField(max_length=1,
				choices=LOAN_STATUS,
				blank=True,
				default='s',
				help_text='Status for the song'
				)

	class Meta:
		ordering = ["-number_of_listens"]

	def __str__(self):
		authors = ', '.join([ author.alias for author in Author.objects.all() ])
		return '%s - %s (%s)' % (authors, self.song, self.released)
		#return '%s (%s) %s' % (self.song, self.released, self.number_of_listens)
		#return '%s (%s)' % (self.id, self.song.title)


class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100, blank=True)

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	#def __str__(self):
	#	return '%s \'%s\' %s' % (self.first_name, self.alias, self.last_name)

	def __str__(self):
		return self.alias

	def get_songs_of_author(self):
		#return Song.objects.all()
		return Song.objects.filter(author=self)

	def get_full_name(self):
		return self.first_name + ' \'' + self.alias + '\' ' + self.last_name


class Genre(models.Model):

	name = models.CharField(max_length=200,
				help_text="Enter a song genre (e.g. hip-hop, rock, alternative, techno etc.)")

	def __str__(self):
		return self.name

	def display_genre(self):
		return ', '.join([ genre.name for genre in self.genre.all()])
	display_genre.short_description = 'Genre'


class Album(models.Model):

	name = models.CharField(max_length=200, help_text="Name of album")
	released = models.DateField(null=True, blank=True)

	def get_absolute_url(self):
		return reverse('album-detail', args=[str(self.id)])

	def get_songs_from_album(self):
		return Song.objects.filter(album=self)

	def __str__(self):
		return self.name


