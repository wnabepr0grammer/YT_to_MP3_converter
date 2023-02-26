from pytube import YouTube
import os

# Ask the user to input the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object and get the highest available resolution stream
yt = YouTube(url)

# Check if an audio stream is available
audio_streams = yt.streams.filter(only_audio=True)
if not audio_streams:
    print("No audio stream is available for this video.")
    exit()

# Get the highest available audio stream
stream = audio_streams.order_by('abr').desc().first()

# Download the audio and save it to a file
audio_filename = f'{yt.title}.mp3'
output_dir = os.path.expanduser('E:\PY_Music_Converter')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Processing video...")
stream.download(output_path=output_dir, filename=audio_filename)
print("Done!")

# Rename the file to match the video title
os.rename(os.path.join(output_dir, audio_filename), os.path.join(output_dir, f'{yt.title}.mp3'))

# Get the size of the downloaded file
file_size = os.path.getsize(os.path.join(output_dir, f'{yt.title}.mp3'))

# Get the bitrate of the downloaded stream
bitrate = int(stream.abr.replace('kbps', ''))

# Print the details of the downloaded file
print(f"File saved in {output_dir}")
print(f"File size: {file_size / (1024*1024):.2f} MB")
print(f"Bitrate: {bitrate} kbps")
