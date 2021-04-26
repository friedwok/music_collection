from django.shortcuts import render
from .models import Song, SongInstance, Author, Genre, Album
from django.views import generic
from .additions import lyrics_html
from django.contrib.auth.mixins import LoginRequiredMixin

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


#class SongsCollectedByUserListView(LoginRequiredMixin, generic.ListView):
	#model = SongInstance
	#template_name = 'catalog/songinstance_list_collected_user.html'
	#paginate_by = 10

	#def get_queryset(self):
	#	return SongInstance.objects.filter(collector=self.request.user).order_by('song')

