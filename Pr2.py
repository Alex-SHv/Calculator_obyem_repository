import tkinter as tk

root = tk.Tk()
root.title("Конвертер объёмов (метрическая система)")
root.geometry("800x800")
root.configure(bg="#f2f2f2")

label_title = tk.Label(root, text="Конвертер объёмов", font=("Arial", 15, "bold"), bg="#f2f2f2")
label_title.pack(pady=(50, 10))

label_value = tk.Label(root, text="Введите значение:", font=("Arial", 14), bg="#f2f2f2")
label_value.pack(pady=(10, 10))
entry_value = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
entry_value.pack(pady=10)

frame_units = tk.Frame(root, bg="#f2f2f2")
frame_units.pack(pady=20)

label_from = tk.Label(frame_units, text="Из единицы:", font=("Arial", 12), bg="#f2f2f2")
label_from.pack(pady=10)
entry_from = tk.Entry(frame_units, font=("Arial", 12), width=10, justify="center")
entry_from.pack(pady=10)

label_to = tk.Label(frame_units, text="В единицу:", font=("Arial", 12), bg="#f2f2f2")
label_to.pack(pady=10)
entry_to = tk.Entry(frame_units, font=("Arial", 12), width=10, justify="center")
entry_to.pack(pady=10)