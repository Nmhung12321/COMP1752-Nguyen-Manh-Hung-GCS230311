import tkinter as tk # Importing the tkinter module as tk
 
import font_manager as fonts # Importing the font_manager module as fonts
from check_video import CheckVideos # Importing the CheckVideos class from the check_video module
from create_video_list import CreateVideoList # Importing the CreateVideoList class from the create_video_list module
from update_videos import UpdateVideos # Importing the UpdateVideos class from the update_videos module
 
# Defining the check_video function that creates a new window for the CheckVideos class and updates the status label
def check_video():
    CheckVideos(tk.Toplevel(main_window))
    status_label.config(text="Check Video button was clicked successfully!")
 
# Defining the create_video_list function that creates a new window for the CreateVideoList class and updates the status label
def create_video_list():
    CreateVideoList(tk.Toplevel(main_window))
    status_label.config(text="Create Video List button was clicked successfully!")
 
# Defining the update_videos function that creates a new window for the UpdateVideos class and updates the status label
def update_videos():
    UpdateVideos(tk.Toplevel(main_window))
    status_label.config(text="Update Video button was clicked successfully!")

main_window = tk.Tk() # Creating the main window
main_window.geometry("520x150") # Setting the size of the main window
main_window.title("Video Player") # Setting the title of the main window
 
fonts.configure() # Configuring the fonts
 
header_label = tk.Label(main_window, text="Select an option by clicking one of the buttons below") # Creating a label for the header
header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Placing the header label in the grid
 
check_video_button = tk.Button(main_window, text="Check Video", command=check_video) # Creating a button for the check_video function
check_video_button.grid(row=1, column=0, padx=10, pady=10) # Placing the check_video button in the grid
 
create_video_list_button = tk.Button(main_window, text="Create Video List", command=create_video_list) # Creating a button for the create_video_list function
create_video_list_button.grid(row=1, column=1, padx=10, pady=10) # Placing the create_video_list button in the grid
 
update_video_button = tk.Button(main_window, text="Update Videos", command=update_videos) # Creating a button for the update_videos function
update_video_button.grid(row=1, column=2, padx=10, pady=10) # Placing the update_videos button in the grid
 
status_label = tk.Label(main_window, text="", font=("Helvetica", 10)) # Creating a label for the status
status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10) # Placing the status label in the grid
 
main_window.mainloop() # Starting the main loop for the main window
