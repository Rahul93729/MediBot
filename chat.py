# import json
# import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# from tensorflow import keras
# from sklearn.preprocessing import LabelEncoder

# import colorama
# colorama.init()
# from colorama import Fore, Style, Back

# import random
# import pickle

# with open('intents.json') as file:
#     data = json.load(file)

# def chat():
#     #load trained model
#     model = keras.models.load_model('chat-model.h5')


#     #load tokenizer object
#     with open('tokenizer.pickle', 'rb') as handle:
#         tokenizer = pickle.load(handle)

#     #load label encoder object
#     with open('label_encoder.pickle', 'rb') as enc:
#         lbl_encoder = pickle.load(enc)

#     #parameters
#     max_len = 20

#     while True:
#         print(Fore.LIGHTBLUE_EX + 'User: ' + Style.RESET_ALL, end = "")
#         inp = input()
#         if inp.lower() == 'quit':
#             print(Fore.GREEN + 'MediBot:' + Style.RESET_ALL, "Take care. See you soon.")
#             break
    
#         result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating = 'post', maxlen = max_len))
#         tag = lbl_encoder.inverse_transform([np.argmax(result)])

#         for i in data['intents']:
#             if i['tag'] == tag:
#                 print(Fore.GREEN + 'MediBot:' + Style.RESET_ALL, np.random.choice(i['responses']))

    
# print(Fore.YELLOW + 'Start talking with MediBot, your Personal Therapeutic AI Assistant. (Type quit to stop talking)' + Style.RESET_ALL)
# chat()


# # {"tag": "",
# #  "patterns": [""],
# #  "responses": [""]
# # },





















# # Working code for the chabot with styling issues

# import tkinter as tk
# from tkinter import scrolledtext
# import json
# import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# from tensorflow import keras
# from sklearn.preprocessing import LabelEncoder
# import colorama
# colorama.init()
# from colorama import Fore, Style, Back
# import random
# import pickle

# with open('intents.json') as file:
#     data = json.load(file)

# BG_GRAY = "#ABB2B9"
# BG_COLOR = "#17202A"
# TEXT_COLOR = "#EAECEE"

# FONT = "Helvetica 14"
# FONT_BOLD = "Helvetica 13 bold"

# class ChatApplication(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("MediBot - Your Personal Therapeutic AI Assistant")
#         self.geometry("600x750")
#         self.resizable(False, False)
#         self.configure(bg=BG_COLOR)
#         self._setup_ui()

#     def _setup_ui(self):
#         # Head label
#         head_label = tk.Label(self, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
#         head_label.pack(fill=tk.X)

#         # Divider
#         divider = tk.Label(self, width=450, bg=BG_GRAY)
#         divider.pack(fill=tk.X, pady=(0, 10))

#         # Text widget
#         self.output_area = scrolledtext.ScrolledText(self, width=20, height=20, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
#         self.output_area.pack(fill=tk.BOTH, expand=True)
#         self.output_area.configure(cursor="arrow", state="disabled")

#         # Bottom label
#         bottom_label = tk.Label(self, bg=BG_GRAY, height=80)
#         bottom_label.pack(side=tk.BOTTOM, fill=tk.X)

#         # Message entry box
#         self.entry = tk.Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
#         self.entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
#         self.entry.focus()
#         self.entry.bind("<Return>", self.send)

#         # Send button
#         send_button = tk.Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, command=self.send)
#         send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

#         # Load model and tokenizer
#         self.model = keras.models.load_model('chat-model.h5')
#         with open('tokenizer.pickle', 'rb') as handle:
#             self.tokenizer = pickle.load(handle)
#         with open('label_encoder.pickle', 'rb') as enc:
#             self.lbl_encoder = pickle.load(enc)

#         self.max_len = 20

#         self.output_area.insert(tk.END, f"{Fore.YELLOW}Start talking with MediBot, your Personal Therapeutic AI Assistant. (Type quit to stop talking){Style.RESET_ALL}\n")

#     def send(self, event=None):
#         user_input = self.entry.get()
#         if user_input.lower() == 'quit':
#             self.output_area.insert(tk.END, f"{Fore.GREEN}MediBot:{Style.RESET_ALL} Take care. See you soon.\n")
#             self.output_area.yview(tk.END)
#         else:
#             result = self.model.predict(keras.preprocessing.sequence.pad_sequences(self.tokenizer.texts_to_sequences([user_input]), truncating='post', maxlen=self.max_len))
#             tag = self.lbl_encoder.inverse_transform([np.argmax(result)])
#             for i in data['intents']:
#                 if i['tag'] == tag:
#                     response = np.random.choice(i['responses'])
#                     self.output_area.configure(state="normal")
#                     self.output_area.insert(tk.END, f"{Fore.LIGHTBLUE_EX}User:{Style.RESET_ALL} {user_input}\n")
#                     self.output_area.insert(tk.END, f"{Fore.GREEN}MediBot:{Style.RESET_ALL} {response}\n")
#                     self.output_area.configure(state="disabled")
#                     self.output_area.yview(tk.END)
#         self.entry.delete(0, tk.END)

# if __name__ == "__main__":
#     app = ChatApplication()
#     app.mainloop()
































# import json
# import numpy as np
# import warnings
# warnings.filterwarnings("ignore")
# from tensorflow import keras
# from sklearn.preprocessing import LabelEncoder

# import colorama
# colorama.init()
# from colorama import Fore, Style, Back

# import random
# import pickle

# with open('intents.json') as file:
#     data = json.load(file)

# def chat():
#     #load trained model
#     model = keras.models.load_model('chat-model.h5')


#     #load tokenizer object
#     with open('tokenizer.pickle', 'rb') as handle:
#         tokenizer = pickle.load(handle)

#     #load label encoder object
#     with open('label_encoder.pickle', 'rb') as enc:
#         lbl_encoder = pickle.load(enc)

#     #parameters
#     max_len = 20

#     while True:
#         print(Fore.LIGHTBLUE_EX + 'User: ' + Style.RESET_ALL, end = "")
#         inp = input()
#         if inp.lower() == 'quit':
#             print(Fore.GREEN + 'MediBot:' + Style.RESET_ALL, "Take care. See you soon.")
#             break
    
#         result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating = 'post', maxlen = max_len))
#         tag = lbl_encoder.inverse_transform([np.argmax(result)])

#         for i in data['intents']:
#             if i['tag'] == tag:
#                 print(Fore.GREEN + 'MediBot:' + Style.RESET_ALL, np.random.choice(i['responses']))

    
# print(Fore.YELLOW + 'Start talking with MediBot, your Personal Therapeutic AI Assistant. (Type quit to stop talking)' + Style.RESET_ALL)
# chat()


# # {"tag": "",
# #  "patterns": [""],
# #  "responses": [""]
# # },











# All styling codes and with uodated features

import os
import tensorflow as tf
from tensorflow import keras
import tkinter as tk
from tkinter import scrolledtext
import json
import numpy as np
import warnings
from sklearn.preprocessing import LabelEncoder
import colorama
colorama.init()
from colorama import Fore, Style, Back
import random
import pickle

USER_COLOR = 'blue'
MEDIBOT_COLOR = 'green'
USER_ICON = '👤'
MEDIBOT_ICON = '🤖'

class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MediBot - Your Personal Therapeutic AI Assistant")
        self.geometry("600x750")
        self.resizable(False, False)

        # Background image
        self.background_image = tk.PhotoImage(file='background_image1.png')
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.configure(bg="#CCD3CA")  # Setting background color to CCD3CA
        self._setup_ui()

    def _setup_ui(self):
        # Head label
        head_label = tk.Label(self, bg="#CCD3CA", fg="black", text="MEDIBOT", font=("Helvetica", 20, "bold"), pady=20)
        head_label=tk.Label(self, text="Welcome to MediBot How may I help You?" , bg="#CCD3CA", fg=USER_COLOR, font=("Helvetica",10,"bold"),pady=20)
        head_label.pack(fill=tk.X)

        # Divider
        divider = tk.Label(self, width=450, bg="#B5C0D0")  # Changing divider color to B5C0D0
        divider.pack(fill=tk.X, pady=(0, 10))

        # Text widget
        self.output_area = scrolledtext.ScrolledText(self, width=20, height=20, bg="#B5C0D0", fg="black", font="Helvetica 14", padx=5, pady=5)
        self.output_area.pack(fill=tk.BOTH, expand=True)
        self.output_area.configure(cursor="arrow", state="disabled")

        # Bottom label
        bottom_label = tk.Label(self, bg="#EED3D9", height=80)  # Changing bottom label color to EED3D9
        bottom_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Message entry box
        self.entry = tk.Entry(bottom_label, bg="#CCD3CA", fg="white", font="Helvetica 14")  # Changing entry box color to black
        self.entry.place(relwidth=0.74, relheight=0.10, rely=0.012, relx=0.017)
        
        self.entry.focus()
        self.entry.bind("<Return>", self.send)

        # Send button
        send_button = tk.Button(bottom_label, text="Send", font="Helvetica 13 bold", width=23, bg="white", fg="black", command=self.send)  # Changing button color to white and text color to black
        send_button.place(relx=0.77, rely=0.008, relheight=0.10, relwidth=0.28)

        # Load model and tokenizer
        self.model = keras.models.load_model('chat-model.h5')
        with open('tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        with open('label_encoder.pickle', 'rb') as enc:
            self.lbl_encoder = pickle.load(enc)

        self.max_len = 20

        self.output_area.insert(tk.END, "Start talking with MediBot, your Personal Therapeutic AI Assistant. (Type quit to stop talking)\n")

    def send(self, event=None):
        try:
            user_input = self.entry.get()
            if user_input.lower() == 'quit':
                self.output_area.insert(tk.END, f"{MEDIBOT_ICON} MediBot: Take care. See you soon.\n", 'medibot_msg')
                self.output_area.yview(tk.END)
            else:
                result = self.model.predict(keras.preprocessing.sequence.pad_sequences(self.tokenizer.texts_to_sequences([user_input]), truncating='post', maxlen=self.max_len))
                tag = self.lbl_encoder.inverse_transform([np.argmax(result)])
                for i in data['intents']:
                    if i['tag'] == tag:
                        response = np.random.choice(i['responses'])
                        self.output_area.configure(state="normal")
                        # Insert user message and bot response with appropriate alignment and spacing
                        self.output_area.insert(tk.END, f"{USER_ICON} You: {user_input}\n", 'user_msg')
                        self.output_area.insert(tk.END, "\n\n", 'spacing')
                        self.output_area.insert(tk.END, f"{MEDIBOT_ICON} MediBot: {response}\n", 'medibot_msg')
                        self.output_area.insert(tk.END, "\n\n\n", 'spacing')
                        self.output_area.tag_config('user_msg', foreground=USER_COLOR, justify='left')  # Set user message color and align to the left
                        self.output_area.tag_config('medibot_msg', foreground=MEDIBOT_COLOR, justify='right')  # Set bot response color and align to the right
                        self.output_area.tag_config('spacing', spacing2=20)  # Add spacing between messages
                        self.output_area.configure(state="disabled")
                        self.output_area.yview(tk.END)
            self.entry.delete(0, tk.END)
        except KeyboardInterrupt:
            # Handle the KeyboardInterrupt gracefully
            pass

if __name__ == "__main__":
    # Set environment variable to turn off oneDNN optimizations
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    
    # Rebuild TensorFlow with appropriate compiler flags (if necessary)
    # You may need to rebuild TensorFlow separately outside of this script.

    # Train or evaluate the model to build the compiled metrics
    # (if you haven't already done so before saving the model)

    # Load intents
    with open('intents.json') as file:
        data = json.load(file)
    
    app = ChatApplication()
    app.mainloop()
