import tkinter as tk
from tkinter import messagebox

class NameAnalyzer:
    def __init__(self, name):
        self.name = name.lower()

    def count_letters(self):
        return len([char for char in self.name if char.isalpha()])

    def count_vowels(self):
        vowels = "aeiou"
        return len([char for char in self.name if char in vowels])

    def is_isogram(self):
        return len(set(self.name)) == len(self.name)

    def is_palindrome(self):
        return self.name == self.name[::-1]


class NameAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title =('Name Analyzer App')

        self.label = tk.Label(master, text = "Enter a name:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.analyze_button = tk.Button(master, text = "Analyze", command = self.analyze_name)
        self.analyze_button.pack()

    def analyze_name(self):
        user_name = self.entry.get()
        analyzer = NameAnalyzer(user_name)


        result_message = (f"Number of letters: {analyzer.count_letters()}\n"
                          f"Number of vowels: {analyzer.count_vowels()}\n"
                          f"The name is {'an' if analyzer.is_isogram() else 'not an'} isogram.\n"
                          f"The name is {'a' if analyzer.is_palindrome() else 'not a'} palindrome.\n"

                          )

        messagebox.showinfo("Name Analysis Result", result_message)



if __name__ == "__main__":
    root = tk.Tk()
    app = NameAnalyzerApp(root)
    root.mainloop()
