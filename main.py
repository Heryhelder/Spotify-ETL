import datetime
import time
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml

def main():
    # Import spotify's app keys from config file
    with open('config.yml', 'r') as config_file:
        keys = yaml.safe_load(config_file)

    CLIENT_ID = keys['spotify_keys']['CLIENT_ID']
    CLIENT_SECRET = keys['spotify_keys']['CLIENT_SECRET']

    # Get current date at midnight in brazillian timezone (BRT)
    current_day = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-3), name='BRT')).replace(hour=0, minute=0, second=0, microsecond=0)

    unix_timestamp_in_milliseconds = int(time.mktime(current_day.timetuple()))

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:8080', scope='user-read-recently-played'))

    results_data = sp.current_user_recently_played(limit=1, after=unix_timestamp_in_milliseconds)
    
    # Save the JSON response in a file if it not exists
    # Using the file pattern of spotify_data_<current date>.json
    base_folder = 'data'
    file_name = 'spotify_data_' + current_day.strftime('%Y-%m-%d') + '.json'
    
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    if not os.path.exists(os.path.join(base_folder, file_name)):
        with open(os.path.join(base_folder, file_name), 'w') as json_file:
            json_file.write(json.dumps(results_data))

if __name__ == '__main__':
    main()