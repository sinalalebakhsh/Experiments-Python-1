from ctypes.wintypes import SIZE
import os
os.system('cls')
import tkinter as tk
from deep_translator import GoogleTranslator

window_translator = tk.Tk()
window_translator.title('Sina Lalebakhsh || سینا لاله بخش || Translator')

help_text = tk.Label(
    master=window_translator,
    text='Write your text - متن خودتو بنویس',
    width=30,
    height=2,
    font=('Arial', '30'),
)
help_text.grid(row=0, column=0, columnspan=3)

user_text = tk.Entry(
    master=window_translator,
    text='Write your text - متن خودتو بنویس',
    width=30,
    font=('Arial', '20'),
)
user_text.grid(row=1, column=0, columnspan=3)

button_to_translate = tk.Button(
    master=window_translator,
    text='Enter to translate',
    width=15,
    bg='#f4004f',
    height=2,
    font=('Arial', '15'),
)
button_to_translate.grid(row=2, column=0, columnspan=3)

window_translator.mainloop()

