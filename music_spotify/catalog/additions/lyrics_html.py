import sys


def generate(lyrics):
	path = '/Users/pupsik/Desktop/coursepy/music_app_proj/' + \
			'music_spotify/catalog/templates/catalog/'

	text = ''
	with open(path + 'song_detail.html', 'r') as f:
		line = ''
		while not line.endswith('<hr>\n'):
			line = f.readline()
			text += line

		lines = lyrics.split('\n')
		text += '		<p>' + lines[0] + '<br>\n'
		for song_str in lines[1:-1:1]:
			text += '		' + song_str + '<br>\n'
		text += '		' + lines[-1] + '</p>\n'

		text += '	</div>\n'
		text += '{% endblock %}'

	with open(path + 'song_detail_2.html', 'w') as f:
		f.write(text)
