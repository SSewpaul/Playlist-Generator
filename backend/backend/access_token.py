import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Access:

    def __init__(self) -> None:
        load_dotenv()

        ccm = SpotifyClientCredentials(client_id= os.getenv('CLIENT_ID'), client_secret= os.getenv('CLIENT_SECRET'))
        self.sp = spotipy.Spotify(client_credentials_manager= ccm)

    