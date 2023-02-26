# YT_to_MP3_converter
Python code that converts YouTube video URL to MP3 music format

# For code to work, you have to install pytube for Python
    https://pytube.io/en/latest/user/install.html

So, here is an explanation of how the code works:

  1.The user is prompted to enter a YouTube video URL.
  2.A YouTube object is created using the URL entered by the user.
  3.The code checks if there is an available audio stream for the video. If there is no audio stream, the program exits.
  4.If an audio stream is available, the program selects the highest available bitrate audio stream.
  5.The program creates a file name for the audio file based on the video title.
  6.The program creates an output directory for the audio file at *your file destination* if it does not already exist.
  7.The program downloads the audio stream using the download method of the selected audio stream object, and saves it to the output directory with the previously created file name.
  8.The program renames the audio file with the video title.
  9.The program gets the size of the downloaded file.
  10.The program prints out the location of the saved file, the file size, and the bitrate at which the audio was downloaded.

Overall, this program allows users to easily download the highest quality audio available for a given YouTube video and save it as an mp3 file in a *your designated folder* .
