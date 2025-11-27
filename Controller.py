# controller.py
import tkinter as tk
from View import ConverterView
from Model import convert

class ConverterController:
    def __init__(self, root):
        self.view = ConverterView(root)
        self.view.button.config(command=self.on_convert)

    def on_convert(self):
        value = self.view.entry_value.get()
        from_unit = self.view.entry_from.get().strip()
        to_unit = self.view.entry_to.get().strip()

        result, error = convert(value, from_unit, to_unit)

        if error:
            self.view.label_res.config(text=error, fg="red")
        else:
            self.view.label_res.config(text=f"Результат: {result:.6f} {to_unit}", fg="green")

# 🚀 Точка входа теперь здесь
def run():
    root = tk.Tk()
    controller = ConverterController(root)
    root.mainloop()

if __name__ == "__main__":
    run()