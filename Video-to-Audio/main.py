# imports
import os
import glob
import moviepy.editor

# UNCHANGED BY Code BUT by USER
INPUT_DIRECTORY = 'Input'
MOVIE_EXTENSIONS = ["*.mp4", "*.mkv"]
AUDIO_EXTENSIONS = [".mp3"] #  + [".wav", ".ogg"]

def video_to_audio_conversion(movie_extensions: list, audio_extensions: list):
    '''
    Arguments:
        List of all video extensions you want found in your folder of interest.
        List of all audio extensions that you want the videos to be converted to.

    Returns:
        Audio files converted and stored in subdirectory called 'output' folder, found in same directory
    '''

    # Folder_path found by os
    PATH_DIRECTORY = f"{os.path.dirname(os.path.abspath(__file__))}"

    # Define the input and output directories
    input_dir = os.path.join(PATH_DIRECTORY, INPUT_DIRECTORY)
    output_dir = os.path.join(PATH_DIRECTORY, 'Output')

    # Create the input and output directories if they don't exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Collect all movie files from both the main folder and the input subfolder
    movie_filenames_list = []
    # Loop every each movie extensions mentioned
    for movie_extension in movie_extensions:

        # Get a list of all the files with movie extension in pathdir folder.
        movie_filenames_list += glob.glob(os.path.join(PATH_DIRECTORY, movie_extension))
        movie_filenames_list += glob.glob(os.path.join(input_dir, movie_extension))


    if len(movie_filenames_list) != 0:
        for filename in movie_filenames_list:
            print(f"Processing {filename}...")

            video = moviepy.editor.VideoFileClip(filename)
            audio = video.audio

            if audio is not None:

                # Loop over each audio extension to create multiple audio files
                for audio_extension in audio_extensions:
                    audio_filename = os.path.join(
                        output_dir, 
                        os.path.splitext(os.path.basename(filename))[0] + audio_extension
                    )
                    print(f"Saving audio to {audio_filename}...")
                    
                    # audio_filename = filename.replace(movie_extensions, audio_extension)
                    audio.write_audiofile(audio_filename)
            else:
                print(f"No audio found in {filename}")

    print('Conversion Finished!')

video_to_audio_conversion(MOVIE_EXTENSIONS, AUDIO_EXTENSIONS)