import tkinter as tk
import constants

class Checkers:
    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        self.root.title("Checkers Main menu")
        self.root.configure(bg="orange")

        # Create buttons for different game modes
        self.PlayervsPlayer_button = self.create_button("Player vs Player", self.PlayervsPlayer)
        self.PlayervsComp_button = self.create_button("Player vs Comp", self.PlayervsComp)

        # Pack the buttons
        self.PlayervsComp_button.pack()
        self.PlayervsPlayer_button.pack()

    def create_button(self, text, command):
        # Function to create a button with specified text and command
        return tk.Button(self.root, text=text, command=command, fg="red", bg="lightgreen")
    
    def PlayervsPlayer(self):
        # Function to set the game mode to Player vs Player
        constants.comp = False  # Set comp to False (Player vs Player mode)
        self.root.destroy()    # Close the main menu window

    def PlayervsComp(self):
        # Function to set the game mode to Player vs Comp and present options
        constants.comp = True   # Set comp to True (Player vs Comp mode)
        self.clear_main_page() # Clear the main menu page

        # Add a scale widget to choose bot depth
        self.w = tk.Scale(self.root, from_=1, to=constants.maxbot, orient=tk.HORIZONTAL, bg="lightblue", fg="red")
        self.w.pack()

        # Buttons for selecting player color
        self.play_white_button = self.create_button("Play as White", self.play_white)
        self.play_white_button.pack()
        self.play_black_button = self.create_button("Play as Black", self.play_black)
        self.play_black_button.pack()
        
    def play_white(self):
        # Function to set game parameters when playing as White
        constants.depth = self.w.get()  # Set the bot depth
        constants.botplayer = 0          # Set bot player to 0 (White)
        self.root.destroy()              # Close the main menu window

    def play_black(self):
        # Function to set game parameters when playing as Black
        constants.depth = self.w.get()  # Set the bot depth
        constants.botplayer = 1          # Set bot player to 1 (Black)
        self.root.destroy()              # Close the main menu window

    def clear_main_page(self):
        # Function to clear the main menu page
        for widget in self.root.winfo_children():
            widget.destroy() 

def main_menu():
    # Function to create the main menu window and start the GUI loop
    root = tk.Tk()
    Checkers(root)
    root.mainloop()

    