import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these with your Spotify API credentials
client_id = '03c8d7b0f3434fbf9797ca2d12662e7f'
client_secret = 'ae914ba0769d4bb2bfddd3a8f84ed51b'

# Authentication with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Playlist URL
playlist_url = 'https://open.spotify.com/playlist/23oQu0IlHdX7pk5mWl2uT6'  # Replace with your playlist URL

# Extract Playlist ID from URL
playlist_id = playlist_url.split('/')[-1].split('?')[0]

# Fetch playlist details
playlist = sp.playlist(playlist_id)

# Create a list of dictionaries to hold song info
songs = []

# Fetch and print track details
print("Songs in the playlist:")
for idx, item in enumerate(playlist['tracks']['items'], 1):
    track = item['track']
    song_info = {
        'order': idx,
        'song': track['name'],
        'artist': track['artists'][0]['name']
    }
    songs.append(song_info)
    print(f"{idx}. {track['name']} by {track['artists'][0]['name']}")

# Function to remove songs by their order number
def remove_songs(songs_list, to_remove):
    return [song for song in songs_list if song['order'] not in to_remove]

# Example: Ask the user which songs to remove
def get_songs_to_remove():
    to_remove = input("Enter the order numbers of songs to remove (comma separated): ").split(',')
    to_remove = [int(x.strip()) for x in to_remove if x.strip().isdigit()]
    return to_remove

# Keep asking the user if they want to filter until they say "n"
while True:
    choice = input("Do you want to remove any songs from the list? (y/n): ").lower()

    if choice == 'y':
        to_remove = get_songs_to_remove()
        songs = remove_songs(songs, to_remove)

        # Print the filtered list
        print("\nFiltered playlist:")
        for song in songs:
            print(f"{song['order']}. {song['song']} by {song['artist']}")

    elif choice == 'n':
        print("\nNo more changes made to the playlist.")
        break  # Exit the loop if the user enters 'n'

    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

# Print final playlist after all changes
print("\nFinal playlist:")
with open("WebScraping Audio/output.txt", "w") as file:
    for song in songs:
        output_line = f"{song['order']}. {song['song']} by {song['artist']}\n"
        print(output_line.strip())  # Print to the console
        file.write(output_line)     # Write to the file

print("\nPlaylist saved to 'output.txt'.")
