from django.contrib import admin
from .models import Song, SongInstance, Author, Genre, Album

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('alias', 'first_name', 'last_name')
	fields = ['first_name', 'last_name', 'alias', 'info']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'released', 'author')

class SongInstanceInline(admin.TabularInline):
	model = SongInstance

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'album')
	inlines = [SongInstanceInline]

@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
	# add the collector later
	list_display = ('song', 'status', 'collector', 'number_of_listens', 'bought')
	list_filter = ('number_of_listens', 'bought')

	fieldsets = (
		(None, {
			'fields': ('song', 'collector', 'number_of_listens')
		}),
		('Availability', {
			'fields': ('status', 'bought')
		}),
	)

#admin.site.register(Song)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(SongInstance)
#admin.site.register(Album)
