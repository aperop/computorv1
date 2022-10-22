import tkinter as tk
from tkinter import ttk


def absolute(x: float) -> float:
    return x if x >= 0 else (-1) * x


def sqrt(n: float, eps: float = 1e-5) -> float:
    x = n
    while True:
        root = 0.5 * (x + (n / x))
        if absolute(root - x) < eps:
            break
        x = root
    return root


def discriminant(a: float = 0, b: float = 0, c: float = 0):
    return (b * b) - (4 * a * c)


def solve(a: float = 0, b: float = 0, c: float = 0):
    if not a:
        return None if not b else c / b

    x_1 = ((-1 * b) + sqrt(discriminant(a, b, c))) / (2 * a)
    x_2 = ((-1 * b) - sqrt(discriminant(a, b, c))) / (2 * a)
    return x_1, x_2


def parser():
    poly_str = ''.join(input().upper().split())
    poly_lst = poly_str.split('=')
    if poly_lst[-1] != 0:
        poly_lst[0] += '-'
        poly_lst[0] += poly_lst[-1]
        poly_lst[0] = poly_lst[0].replace('--', '-')
    poly_str = poly_lst[0]
    print(poly_str)
    degree = {'X^0': 0, 'X^1': 0, 'X^2': 0}

    lst = poly_str.split('*')

    print(lst)


def gui():

    def calc():
        value = solve(x2.get(), x1.get(), x0.get())
        if isinstance(value, tuple):
            value_1.set(f'{int(value[0])}' if value[0] == int(value[0]) else f'{value[0]:.4}')
            value_2.set(f'{int(value[1])}' if value[1] == int(value[1]) else f'{value[1]:.4}')
        elif value is None:
            value_1.set('Not calc')

        else:
            value_1.set(f'{int(value)}' if value == int(value) else f'{value:.4}')

    window = tk.Tk()
    window.title('Solving Quadratic Equations')
    window.geometry('750x250+1000+500')
    window.resizable(False, False)
    icon = tk.PhotoImage(file='favicon.png')
    window.iconphoto(True, icon)

    x2 = tk.DoubleVar()
    entry_x2 = ttk.Entry(justify='center', width=11, font=("Math", 20), textvariable=x2)
    label_x2 = ttk.Label(text='×  X²  +', font=("Math", 20))
    entry_x2.grid(row=0, column=0, padx=10, pady=10)
    label_x2.grid(row=0, column=1)

    x1 = tk.DoubleVar()
    entry_x1 = ttk.Entry(justify='center', width=11, font=("Math", 20), textvariable=x1)
    label_x1 = ttk.Label(text='×  X  +', font=("Math", 20))
    entry_x1.grid(row=0, column=2, padx=10, pady=10)
    label_x1.grid(row=0, column=3)

    x0 = tk.DoubleVar()
    entry_x0 = ttk.Entry(justify='center', width=11, font=("Math", 20), textvariable=x0)
    entry_x0.grid(row=0, column=4, padx=10, pady=10)

    label_0 = ttk.Label(text='=  0', font=("Math", 20))
    label_0.grid(row=0, column=5)

    btn_calc = ttk.Button(text='Calculate', command=calc)
    btn_calc.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

    x_1 = ttk.Label(text='X₁ = ', font=("Math", 20), justify='right')
    x_2 = ttk.Label(text='X₂ = ', font=("Math", 20), justify='right')
    x_1.grid(row=3, column=0)
    x_2.grid(row=4, column=0)

    value_1 = tk.StringVar()
    value_2 = tk.StringVar()
    x_1_value = ttk.Label(text='___', font=("Math", 20), textvariable=value_1)
    x_2_value = ttk.Label(text='___', font=("Math", 20), textvariable=value_2)
    x_1_value.grid(row=3, column=1)
    x_2_value.grid(row=4, column=1)

    window.mainloop()


if __name__ == '__main__':
    gui()
    pass
