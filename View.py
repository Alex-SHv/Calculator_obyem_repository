# view.py
import tkinter as tk

class ConverterView:
    def __init__(self, root):
        root.title("Конвертер объёмов (метрическая система)")
        root.geometry("800x800")
        root.configure(bg="#f2f2f2")

        self.label_title = tk.Label(root, text="Конвертер объёмов", font=("Arial", 15, "bold"), bg="#f2f2f2")
        self.label_title.pack(pady=(50, 10))

        self.label_value = tk.Label(root, text="Введите значение:", font=("Arial", 14), bg="#f2f2f2")
        self.label_value.pack(pady=(10, 10))
        self.entry_value = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
        self.entry_value.pack(pady=10)

        self.frame_units = tk.Frame(root, bg="#f2f2f2")
        self.frame_units.pack(pady=20)

        self.label_from = tk.Label(self.frame_units, text="Из единицы:", font=("Arial", 12), bg="#f2f2f2")
        self.label_from.pack(pady=10)
        self.entry_from = tk.Entry(self.frame_units, font=("Arial", 12), width=10, justify="center")
        self.entry_from.pack(pady=10)

        self.label_to = tk.Label(self.frame_units, text="В единицу:", font=("Arial", 12), bg="#f2f2f2")
        self.label_to.pack(pady=10)
        self.entry_to = tk.Entry(self.frame_units, font=("Arial", 12), width=10, justify="center")
        self.entry_to.pack(pady=10)

        text = (
            "Калькулятор использует метрические единицы объёма:\n"
            "● м3 — кубический метр\n"
            "● дм3 — кубический дециметр\n"
            "● см3 — кубический сантиметр\n"
            "● мм3 — кубический миллиметр"
        )
        self.label_hint = tk.Label(root, text=text, font=("Arial", 12), fg="gray", bg="#f2f2f2", justify="left")
        self.label_hint.pack(pady=10)

        self.label_res = tk.Label(root, text="", font=("Arial", 18, "bold"), fg="blue", bg="#f2f2f2")
        self.label_res.pack(pady=30)

        self.button = tk.Button(root, text="Конвертировать", font=("Arial", 14), fg="green")
        self.button.pack(pady=80)