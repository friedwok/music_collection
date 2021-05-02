from django.shortcuts import render
from .models import Song, SongInstance, Author, Genre, Album
from django.views import generic
from .additions import lyrics_html
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	num_songs = Song.objects.all().count()
	num_authors = Author.objects.all().count()
	num_albums = Album.objects.all().count()

	#Number of visits in main page (index)
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	return render(
		request,
		'index.html',
		context={'num_songs': num_songs,
			'num_authors': num_authors,
			'num_albums': num_albums,
			'num_visits': num_visits,
			},
	)


class SongListView(generic.ListView):
	model = Song
	paginate_by = 20


class SongPageView(generic.DetailView):
	model = Song
	template_name = 'catalog/song_detail_2.html'

	def get_context_data(self, **kwargs):
		current_song = Song.objects.filter(id=self.kwargs['pk'])[0]
		lyrics_html.generate(current_song.lyrics)
		context = super(SongPageView, self).get_context_data(**kwargs)
		return context

	#def song_page_view(request, pk):
	#	try:
	#		song_id = Song.objects.get(pk=pk)
	#	except Song.DoesNotExist:
	#		raise Http404("Song does not exist")

	#	return render(
	#		request,
	#		'catalog/song_page.html',
	#		context={'song': song_id,}
	#	)

class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10


class AuthorPageView(generic.DetailView):
	model = Author
	template_name = 'catalog/author_detail.html'


class AlbumListView(generic.ListView):
	model = Album
	paginate_by = 5


class AlbumPageView(generic.DetailView):
	model = Album
	template_name = 'catalog/album_detail.html'


class SongsCollectedByUserListView(generic.ListView):
	model = SongInstance
	template_name = 'catalog/songinstance_list_collected_user.html'
	paginate_by = 10

	permission_required = 'catalog.can_append_songs'

	def get_queryset(self):
		return SongInstance.objects.filter(collector=self.request.user).order_by('song')


class AuthorProfileView(generic.DetailView):
	model = Author
	template_name = 'catalog/author_profile.html'


from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddSongInCollectionForm
import datetime

@permission_required('catalog.can_append_songs')
def add_song(request, pk):
	song_object = get_object_or_404(Song, pk=pk)

	if request.method == 'POST':
		form = AddSongInCollectionForm(request.POST)
		print(form)
		# complete the ownership check later
		if form.is_valid():
			#s = SongInstance(song=models.Song.objects.all()[0],
			#		bought=datetime.date.today(),
			#		collector=models.User.objects.all()[1])
			s = SongInstance(song=song_object,
					bought=datetime.date.today(),
					collector=request.user)
			s.save()

			return HttpResponseRedirect(reverse('my-collected'))
	# for GET or any others methods (do later)
	else:
		#default_song_name = 'Kanye West - Monster'
		#song_name = song_inst.title
		#form = AddSongInCollectionForm(initial={'song_name': default_song_name,})
		form = AddSongInCollectionForm(initial={'song': song_object,})
	return render(request, 'catalog/add_song_collection.html', {'form': form, 'song': song_object})
