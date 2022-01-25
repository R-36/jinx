import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class MusicPlayer(object):
    scope = "user-library-read"

    def __init__(self):
        self.username = 'de7d8a9cdf7642eeb0469ff09be546bd'
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))

    def set_device(self):
        print(self.spotify)
        devices = self.spotify.devices()
        print(devices)
        device_id = ''
        for device in devices['devices']:
            if device['name'] == 'DESKTOP-IK69VG3':
                device_id = device['id']
        return device_id

    def play(self):
        trackResults = self.spotify.album_tracks('3ewRuYOSneUjBqbVQn45Jy?si=B7nfhigIQzmjSI3Lmcw_kg')
        print(json.dumps(trackResults, sort_keys=True, indent=4))
        print(trackResults['tracks']['items'])
        trackURIs = []
        for item in trackResults['tracks']['items']:
            trackURIs.append(item['uri'])
        self.spotify.start_playback(self.set_device(), None, trackURIs)
