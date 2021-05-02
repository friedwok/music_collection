from django import forms
from . import models

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class AddSongInCollectionForm(forms.Form):
	song_name = forms.CharField(max_length=100, help_text="Enter a name of the song you want to verify your action")

	def clean_song_name(self):
		# data means songs added in collection
		data = self.cleaned_data['song_name']
		print(data)

		song_titles = [ song.title for song in models.Song.objects.all() ]
		if data not in song_titles:
			raise ValidationError(_('Song name is not valid'))

		return data
