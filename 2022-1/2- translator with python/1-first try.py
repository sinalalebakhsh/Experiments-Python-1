from ctypes.wintypes import SIZE
import os
os.system('cls')
import tkinter as tk
from deep_translator import GoogleTranslator

window_translator = tk.Tk()
window_translator.title('Sina Lalebakhsh')

help_text = tk.Label(
    master=window_translator,
    text='Write your text - متن خودتو بنویس',
    width=30,
    height=3,
    font=('Arial', '30'),
)
help_text.grid(row=0, column=0, columnspan=3)



window_translator.mainloop()

