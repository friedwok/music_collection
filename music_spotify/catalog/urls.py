from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.index, name='index'),
	path('songs/', views.SongListView.as_view(), name='songs'),
	path('song/<int:pk>/', views.SongPageView.as_view(), name='song-page'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>/', views.AuthorPageView.as_view(), name='author-detail'),
	path('albums/', views.AlbumListView.as_view(), name='albums'),
	path('album/<int:pk>/', views.AlbumPageView.as_view(), name='album-detail'),
]

urlpatterns += [
	path('mysongs/', views.SongsCollectedByUserListView.as_view(), name='my-collected'),
]

urlpatterns += [
	path('song/<int:pk>/add/', views.add_song, name='add-new-song'),
]

urlpatterns += [
	path('author/info/<int:pk>/', views.AuthorProfileView.as_view(), name='my-profile'),
]

# REST API
#urlpatterns += [
#	path('genres/', GenreView.as_view()),
#]
