''' 
Christopher Anciano 3/22/24
Youtube Video Downloader
'''
from pytube import YouTube  # Import the YouTube class from the pytube library
import tkinter as tk  # Import the tkinter library as tk for creating GUI
from tkinter import filedialog  # Import the filedialog module from tkinter for opening file dialogs

def download_video(url, save_path):
    """Function to download a YouTube video given its URL and save path."""
    try:
        # Create a YouTube object using the provided URL
        yt = YouTube(url)
        # Filter available streams to get the highest resolution stream
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_streams = streams.get_highest_resolution()
        # Download the video to the specified save path
        highest_res_streams.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
    """Function to open a file dialog for selecting a folder to save the video."""
    folder = filedialog.askdirectory()  # Open a file dialog to select a folder
    if folder:
        print(f"Selected folder: {folder}")
        return folder

if __name__ == "__main__":
    root = tk.Tk()  # Create a tkinter root window
    root.withdraw()  # Hide the root window

    video_url = input("Enter the YouTube video URL: ")  # Prompt the user to enter a YouTube video URL
    save_dir = open_file_dialog()  # Call the open_file_dialog function to select a folder

    if save_dir:
        print("Please select a folder...")
    else:
        download_video(video_url, save_dir)  # Download the video to the selected folder
