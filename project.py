# from googletrans import Translator

# Create a Translator object
# translator = Translator()


# Function to translate text
# def translate_text(text, src_lang='auto', dest_lang='fr'):
#     translation = translator.translate(text, src=src_lang, dest=dest_lang)
#     return translation.text
#
#
# # Example usage
# text_to_translate = "Hola, ¿cómo estás?"
# translated_text = translate_text(text_to_translate, src_lang='es', dest_lang='fr')
# print(f"Original text: {text_to_translate}")
# print(f"Translated text: {translated_text}")

import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
from gtts import gTTS
import os
import betterplaysound
import re  # For input validation

class TranslatorApp:
    LANG_CODES = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'German': 'de',
        'Hausa': 'ha',
        'Yoruba': 'yo',
        'Igbo': 'ig',
        'Chinese (Simplified)': 'zh',
        'Arabic': 'ar',
        'Japanese': 'ja'
    }

    def __init__(self, root):
        self.root = root
        self.root.title("E-Translate (Language Translator)")
        self.root.geometry("600x600")
        self.root.configure(bg="#f5f5dc")  # Cream background color

        # Title Label
        self.title_label = ttk.Label(self.root, text="E-Translate", font=("Helvetica", 16, "bold"), background="#f5f5dc", foreground="#4d4d4d")
        self.title_label.pack(pady=10)

        # Translator object
        self.translator = Translator()

        # Input Frame
        self.input_frame = ttk.Frame(self.root, padding="10", style="TFrame")
        self.input_frame.pack(pady=10)

        # Label and Text Box for input
        self.input_label = ttk.Label(self.input_frame, text="Original Text:", background="#f5f5dc", foreground="#4d4d4d")
        self.input_label.grid(row=0, column=0, sticky="w")
        self.input_text = tk.Text(self.input_frame, height=5, width=50, bg="#f5f5f5", fg="#4d4d4d")
        self.input_text.grid(row=1, column=0, columnspan=2, pady=5)

        # Language Selection Frame
        self.lang_frame = ttk.Frame(self.root, padding="10")
        self.lang_frame.pack(pady=10)

        # From and To Language Selectors
        self.from_lang_label = ttk.Label(self.lang_frame, text="From Language:", background="#f5f5dc", foreground="#4d4d4d")
        self.from_lang_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.from_lang = ttk.Combobox(self.lang_frame, values=list(self.LANG_CODES.keys()), width=15)
        self.from_lang.grid(row=1, column=0, padx=5, pady=5)
        self.from_lang.set("English")

        self.to_lang_label = ttk.Label(self.lang_frame, text="To Language:", background="#f5f5dc", foreground="#4d4d4d")
        self.to_lang_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.to_lang = ttk.Combobox(self.lang_frame, values=list(self.LANG_CODES.keys()), width=15)
        self.to_lang.grid(row=1, column=1, padx=5, pady=5)
        self.to_lang.set("French")

        # Button Frame
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Translate, Clear, and Pronounce buttons
        self.translate_button = ttk.Button(self.button_frame, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=0, column=0, padx=5, pady=10)

        self.clear_button = ttk.Button(self.button_frame, text="Clear", command=self.clear_text)
        self.clear_button.grid(row=0, column=1, padx=5, pady=10)

        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=2, padx=5, pady=10)

        self.pronounce_button = ttk.Button(self.button_frame, text="Pronounce", command=self.pronounce_text)
        self.pronounce_button.grid(row=1, column=1, pady=5)

        # Output Frame
        self.output_frame = ttk.Frame(self.root, padding="10", style="TFrame")
        self.output_frame.pack(pady=10)

        # Label and Text Box for output
        self.output_label = ttk.Label(self.output_frame, text="Translated Text:", background="#f5f5dc", foreground="#4d4d4d")
        self.output_label.grid(row=0, column=0, sticky="w")
        self.output_text = tk.Text(self.output_frame, height=5, width=50, bg="#f5f5f5", fg="#4d4d4d")
        self.output_text.grid(row=1, column=0, columnspan=2, pady=5)

    def translate_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        from_lang = self.from_lang.get()
        to_lang = self.to_lang.get()

        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        if re.search(r'[^a-zA-Z\s]', input_text):
            messagebox.showerror("Invalid Input", "Please enter valid text (no numbers or special symbols).")
            return

        try:
            translated = self.translator.translate(input_text, src=self.LANG_CODES.get(from_lang), dest=self.LANG_CODES.get(to_lang))
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated.text)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def pronounce_text(self):
        translated_text = self.output_text.get("1.0", tk.END).strip()
        to_lang = self.LANG_CODES.get(self.to_lang.get())

        if not translated_text:
            messagebox.showwarning("Pronunciation Error", "No translated text available to pronounce.")
            return

        if not to_lang:
            messagebox.showerror("Language Error", "Selected language is not supported for pronunciation.")
            return

        try:
            tts = gTTS(text=translated_text, lang=to_lang)
            audio_file = "pronunciation.mp3"
            tts.save(audio_file)
            betterplaysound.playsound(audio_file)
            os.remove(audio_file)
        except Exception as e:
            messagebox.showerror("Pronunciation Error", str(e))

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()


