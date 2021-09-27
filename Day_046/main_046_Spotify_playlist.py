import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CURRENT_USER = str()
SEARCHED_DATE = str()
BILLBOARD_SITE = "https://www.billboard.com/charts/hot-100/"


def make_playlist():
    global CURRENT_USER
    # authenticate on spotify and set scope for adding and modifying private playlists
    scope = "playlist-modify-private"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    # return current user ID and save it as constant
    user = spotify.current_user()
    CURRENT_USER = user["display_name"]
    # set a new playlist name, concatenating title with searched date
    new_playlist_name = f"Billboard Top 100 for {SEARCHED_DATE}"
    # return a list of user playlists to check if playlist for current day already exist
    playlists = spotify.current_user_playlists()
    # make a list out of existing playlist names, and check it with new playlist name
    existing_playlists_list = list()
    new_playlist_id = str()
    for existing_playlist in playlists["items"]:
        existing_playlists_list.append(existing_playlist["name"])
    # if playlist with such name exist start script from the beginning
    if new_playlist_name in existing_playlists_list:
        print("Playlist for given day, already exist.")
        main()
    # if there is no playlist for given day, create one and return it's ID
    else:
        new_playlist = spotify.user_playlist_create(
            user=CURRENT_USER,
            name=new_playlist_name,
            public=False
            )
        new_playlist_id = new_playlist["id"]
    return new_playlist_id


def add_songs(song_list, playlist_id):
    global SEARCHED_DATE, CURRENT_USER
    # authenticate on spotify and set scope
    scope = "playlist-modify-private"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    # set counter because there's problem with string name of songs "1", "2" it's not treated like dict only like string
    counter = 1
    # create list of URI of songs to add to the playlist
    songs_uri_list = list()
    # go through all songs from Top 100 and search for each one of them and add to URI list
    while counter <= len(song_list):
        # assign variables from Top 100 songs dictionary
        song_title = song_list[str(counter)]['title']
        artist = song_list[str(counter)]['artist']
        # search for given songs on Spotify
        results = spotify.search(q=f"track:{song_title} AND artist:{artist}")
        song = results['tracks']['items']
        # try to add only first occurrence out of whole search into the list
        try:
            songs_uri_list.append(song[0]["uri"])
        # if no song is fund go on with the function
        except IndexError:
            pass

        counter += 1
    spotify.user_playlist_add_tracks(user=CURRENT_USER, playlist_id=playlist_id, tracks=songs_uri_list)


def scrape_website():
    global SEARCHED_DATE
    # set url to get top songs
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{SEARCHED_DATE}")
    billboard = response.text
    # extract info from website response
    soup = bs4.BeautifulSoup(billboard, "html.parser")
    song_list = soup.find(name="ol")
    artists = song_list.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    songs_titles = song_list.find_all(name="span",
                                      class_="chart-element__information__artist text--truncate color--secondary")
    ranks = song_list.find_all(name="span", class_="chart-element__rank__number")
    # create a dictionary out of top songs
    final_list = {rank.getText(): {
        "title": song_title.getText(),
        "artist": title.getText()} for (song_title, title, rank) in zip(artists, songs_titles, ranks)}
    # return dictionary of top songs to use in "add_songs" function
    return final_list

def ask_user_for_a_date():
    global SEARCHED_DATE

    year = input("What year you wanna look in?:\n")
    month = input("What month you wanna look in?:\n")
    day = input("What day you wanna look in?:\n")
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    SEARCHED_DATE = year + "-" + month + "-" + day


def main():
    print("Making Spotify playlist out of Billboard Top 100 list for given day.")
    # ask user to set date for song search
    ask_user_for_a_date()
    # prepare a dictionary out of songs scraped from website
    song_list = scrape_website()
    # create new playlist, if playlist for given day exists, program will restart
    playlist_id = make_playlist()
    # if playlist doesn't exist add songs to newly created playlist
    add_songs(song_list, playlist_id)


if __name__ == "__main__":
    main()
