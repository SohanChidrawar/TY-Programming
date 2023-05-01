#It is a Hospital Enquiry desk chatbok 

import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections

# Define a dictionary of patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!"]),
    (r"what is your name?", ["My name is Hospital Enquiry Bot.", "I'm Hospital Enquiry Bot."]),
    (r"what services do you offer?", ["We offer a range of medical services. Please specify your enquiry."]),
    (r"(.*) (hours|open|close)", ["We are open 24/7. How can we assist you?"]),
    (r"(.*) (appointment|schedule|book)", ["To book an appointment, please call our reception desk at 123-456-7890."]),
    (r"(.*) (emergency|urgent)", ["For emergencies, please call 911 or go to the nearest emergency room."]),
    (r"(.*) (payment|insurance|cost)", ["Please contact our billing department at 555-555-5555 for any questions related to payments or insurance."]),
    (r"(.*)", ["Thank you for your enquiry. We will get back to you as soon as possible."])
]

# Create a chatbot object using the defined patterns and responses
chatbot = Chat(patterns, reflections)

# Define a function to handle button click events
def button_click():
    # Get user input from the text entry widget
    user_input = entry.get()
    # Clear the text entry widget
    entry.delete(0, tk.END)
    # Generate a response to the user's input using the chatbot object
    response = chatbot.respond(user_input)
    # Display the response in the chat history widget
    history.config(state=tk.NORMAL)
    history.insert(tk.END, "You: " + user_input + "\n")
    history.insert(tk.END, "Bot: " + response + "\n")
    history.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Hospital Enquiry Bot")

# Create the chat history widget
history = tk.Text(root, state=tk.DISABLED)
history.pack(fill=tk.BOTH, expand=True)

# Create the text entry widget
entry = tk.Entry(root)
entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the send button
button = tk.Button(root, text="Send", command=button_click)
button.pack(side=tk.RIGHT)

# Start the main event loop
root.mainloop()
