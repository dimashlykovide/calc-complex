import tkinter as tk
from tkinter import messagebox
import cmath

class ComplexCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("калькулятор комплексных чисел")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Заголовок
        tk.Label(self.root, text="калькулятор комплексных чисел", 
                 font=("Arial", 16, "bold")).pack(pady=10)
        
        # Поля ввода
        tk.Label(self.root, text="Первое число (a+bj):").pack()
        self.entry_z1 = tk.Entry(self.root, width=40)
        self.entry_z1.pack(pady=5)
        
        tk.Label(self.root, text="Второе число (a+bj):").pack()
        self.entry_z2 = tk.Entry(self.root, width=40)
        self.entry_z2.pack(pady=5)
        
        # Кнопки операций
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="+", width=8, command=self.add).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="−", width=8, command=self.subtract).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="×", width=8, command=self.multiply).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="÷", width=8, command=self.divide).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="^", width=8, command=self.power).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="conj", width=8, command=self.conjugate).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="|z|", width=8, command=self.modulus).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(btn_frame, text="arg", width=8, command=self.argument).grid(row=1, column=3, padx=5, pady=5)
        
        # Поле вывода результата
        tk.Label(self.root, text="результат:").pack()
        self.result_text = tk.Text(self.root, height=6, width=50)
        self.result_text.pack(pady=10, padx=20)
        self.result_text.config(state="disabled")
    
    def parse_complex(self, entry_widget):
        try:
            value = entry_widget.get().strip()
            if not value:
                raise ValueError("поле не должно быть пустым")
            return complex(value)
        except ValueError as e:
            messagebox.showerror("ошибка", f"некорректное комплексное число: {e}")
            return None
    
    def show_result(self, text):
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state="disabled")
    
    def add(self):
        z1 = self.parse_complex(self.entry_z1)
        z2 = self.parse_complex(self.entry_z2)
        if z1 is not None and z2 is not None:
            result = z1 + z2
            self.show_result(f"{z1} + {z2} = {result}")
    
    def subtract(self):
        z1 = self.parse_complex(self.entry_z1)
        z2 = self.parse_complex(self.entry_z2)
        if z1 is not None and z2 is not None:
            result = z1 - z2
            self.show_result(f"{z1} − {z2} = {result}")
    
    def multiply(self):
        z1 = self.parse_complex(self.entry_z1)
        z2 = self.parse_complex(self.entry_z2)
        if z1 is not None and z2 is not None:
            result = z1 * z2
            self.show_result(f"{z1} × {z2} = {result}")
    
    def divide(self):
        z1 = self.parse_complex(self.entry_z1)
        z2 = self.parse_complex(self.entry_z2)
        if z1 is not None and z2 is not None:
            if z2 == 0:
                self.show_result("ошибка: деление на ноль!")
            else:
                result = z1 / z2
                self.show_result(f"{z1} ÷ {z2} = {result}")
    
    def power(self):
        z1 = self.parse_complex(self.entry_z1)
        z2 = self.parse_complex(self.entry_z2)
        if z1 is not None and z2 is not None:
            try:
                result = z1 ** z2
                self.show_result(f"({z1}) ^ ({z2}) = {result}")
            except OverflowError:
                self.show_result("ошибка: результат слишком большой!")
    
    def conjugate(self):
        z = self.parse_complex(self.entry_z1)
        if z is not None:
            result = z.conjugate()
            self.show_result(f"сопряжённое к {z}: {result}")
    
    def modulus(self):
        z = self.parse_complex(self.entry_z1)
        if z is not None:
            result = abs(z)
            self.show_result(f"|{z}| = {result:.4f}")
    
    def argument(self):
        z = self.parse_complex(self.entry_z1)
        if z is not None:
            if z == 0:
                self.show_result("аргумент нуля не определён.")
            else:
                rad = cmath.phase(z)
                deg = rad * 180 / cmath.pi
                self.show_result(f"arg({z}) = {rad:.4f} рад\n            = {deg:.4f}°")

if __name__ == "__main__":
    root = tk.Tk()
    app = ComplexCalculator(root)
    root.mainloop()
