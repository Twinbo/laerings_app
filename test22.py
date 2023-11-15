import tkinter as tk
from tkinter import messagebox
import random

class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")

        self.score = 0
        self.current_question = ""
        self.answer = 0

        self.label_question = tk.Label(root, text="", font=("Helvetica", 18))
        self.label_question.pack(pady=10)

        self.entry_answer = tk.Entry(root, font=("Helvetica", 16))
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.button_submit.pack(pady=10)

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])

        if operator == "+":
            self.answer = num1 + num2
        elif operator == "-":
            self.answer = num1 - num2
        elif operator == "*":
            self.answer = num1 * num2
        elif operator == "/":
            # Avoid division by zero
            while num2 == 0:
                num2 = random.randint(1, 10)
            self.answer = num1 / num2

        self.current_question = f"{num1} {operator} {num2}"
        self.label_question.config(text=self.current_question)
        self.entry_answer.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.entry_answer.get()

        try:
            user_answer = float(user_answer)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        if user_answer == self.answer:
            messagebox.showinfo("Correct", "Congratulations! Your answer is correct.")
            self.score += 1
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {self.answer}.")

        self.generate_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuiz(root)
    root.mainloop()

