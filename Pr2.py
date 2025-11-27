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

text = (
    "Калькулятор использует метрические единицы объёма:\n"
    "● м3 — кубический метр\n"
    "● дм3 — кубический дециметр\n"
    "● см3 — кубический сантиметр\n"
    "● мм3 — кубический миллиметр"
)
label_hint = tk.Label(root, text=text, font=("Arial", 12), fg="gray", bg="#f2f2f2", justify="left")
label_hint.pack(pady=10)

label_res = tk.Label(root, text="", font=("Arial", 18, "bold"), fg="blue", bg="#f2f2f2")
label_res.pack(pady=30)

conversion = {
    "м3": 1,
    "дм3": 0.001,
    "см3": 0.000001,
    "мм3": 0.000000001
}

def convert():
     try:
              value = float(entry_value.get())
     except  ValueError:
              label_res.configure(text="Ошибка: введите число!", fg="red")
              return
              
              from_unit = entry_from.get().strip()
              to_unit = entry_to.get().strip()

              if from_unit not in conversion or to_unit not in conversion:
                     label_res.configure(text="Ошибка: используйте только м3, дм3, см3 или мм3!",fg="red")
                     return

              value_in_m3 = value * conversion[from_unit]
              result = value_in_m3 / conversion[to_unit]

              label_res.configure(text=f"Результат: {result:.6f} {to_unit}", fg="green")
