from dotenv import load_dotenv
import discord, os, re, requests

#load .env properties
load_dotenv()
TOKEN = os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Ready to go', self.user)

    async def on_message(self, message):
        if re.search(r'^(?:spotify:|https|http://[a-z]+.spotify.com/(track/))(.*)$', str(message.content)):
            playlist_id = os.getenv("PLAYLIST_ID")
            match = re.search(r'\bhttps?:\/\/[^/]*\bspotify\.com\/track\/([^\s?]+)', str(message.content))
            track_id = str(match.group(1))
            api_url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks?uris=spotify:track:' + track_id
            headers = {"Accept": "Accept: application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer <TOKEN PLACEHOLDER>"}
            requests.post(api_url, headers=headers)
                

client = MyClient()
client.run(TOKEN)