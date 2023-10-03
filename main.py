import tkinter as tk


class TypingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disappearing Text Typing App")

        # Creating a text widget to display the user's input
        self.text_box = tk.Text(self.root, width=60, height=10)
        self.text_box.pack()

        # Creating a label to display the time remaining
        self.time_remaining_label = tk.Label(self.root, text="Time remaining: 5 seconds")
        self.time_remaining_label.pack()

        # Initializing the timer
        self.timer = 5  # Set the initial timer value to 5 seconds
        self.timer_running = False  # Flag to track if the timer is running

        # Binding the key press event to the on_key_press() method
        self.text_box.bind("<KeyPress>", self.on_key_press)

        # Starting the mainloop
        self.root.mainloop()

    def update(self):
        # Getting the time remaining
        time_remaining = self.timer

        # If the time remaining is 0, clear the text box and reset the timer
        if time_remaining == 0:
            self.text_box.delete("1.0", "end")
            self.timer = 5  # Reset the timer to 5 seconds
            self.timer_running = False
            self.time_remaining_label.config(
                text="Time over! Your text has been deleted. Please type to restart the timer.")

        # Otherwise, update the time remaining label and decrement the timer
        else:
            self.time_remaining_label.config(text="Time remaining: {} seconds".format(time_remaining))
            self.timer -= 1

            # Schedule the next timer tick
            self.root.after(1000, self.update)

    def on_key_press(self, event):
        # Reset the timer when a key is pressed
        self.timer = 5

        # If the timer is not already running, start it
        if not self.timer_running:
            self.timer_running = True
            self.update()


if __name__ == "__main__":
    app = TypingApp()
