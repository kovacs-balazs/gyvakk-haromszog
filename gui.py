import tkinter as tk
import triangle

# A text inputbox default szövegének kivétele
def on_entry_click(event, text):
    if event.widget.get() == text:
        event.widget.delete(0, "end")
        event.widget.insert(0, '')
        event.widget.config(fg = 'black')

# A text inputbox default szövegének visszatétele
def on_focusout(event):
    if entry_a.get() == '' and (event.widget != entry_a): # Ha üres és nem a felső sinputboxba kattint
        entry_a.insert(0, text_a)
        entry_a.config(fg = 'grey')
        event.widget.focus()
    elif entry_b.get() == '' and (event.widget != entry_b): # Ha üres és nem az alsó inputboxba kattint
        entry_b.insert(0, text_b)
        entry_b.config(fg = 'grey')
        event.widget.focus()


def calculate() -> float:
    try:
        a: float = float(entry_a.get().strip())
        b: float = float(entry_b.get().strip())
    except ValueError:
        print("A beadott érték csak szám lehet!")
        return 0
    
    if a <= 0 or b <= 0:
        print("A beadott érték nullánál nagyobb kell legyen!")
        return 0

    triangle_: triangle.Triangle = triangle.Triangle(a, b)
    print(f"a: {a}\nb: {b}\nKerület: {triangle_.get_kerulet_rounded()}")

    triangle.add(triangle_)
    reset_input_boxes()
    return triangle_.get_kerulet_rounded()

# Felvétel utáni default szöveg visszarakása
def reset_input_boxes():
    entry_a.delete(0, "end")
    entry_a.insert(0, text_a)
    entry_a.config(fg = 'grey')

    entry_b.delete(0, "end")
    entry_b.insert(0, text_b)
    entry_b.config(fg = 'grey')
    window.focus()

# GUI megnyitása
def gui_open():
    window.mainloop()

# Kerulet dictionary kiírása value alapján csökkenőbe rendezve
def print_keruletek():
    print(triangle.get_keruletek_sorted())

window = tk.Tk()

window.geometry("300x110") # Az ablak mérete
window.resizable(width=0, height=0) # Az ablakot ne lehessen átméretezni
window.title("Háromszög kalkulátor") # Az ablak címének megadása

window.eval('tk::PlaceWindow . center') # Az ablak középre tétele

# A felső (a befogó) inputbox
text_a = 'a befogó'
entry_a = tk.Entry(window) # az ablakhoz csatolása
entry_a.insert(0, text_a) # default szöveg megadása
entry_a.bind('<FocusIn>', lambda event: on_entry_click(event, text_a)) # Event meghívása a megadott szöveggel
entry_a.bind('<FocusOut>', on_focusout) # Event meghívása
entry_a.config(fg = 'grey') # Szöveg színezése
entry_a.pack(side=tk.TOP, padx=10, pady=10) # Az inuputbox elhelyezése és csomagolása

# Az alsó (b befogó) inputbox
text_b = 'b befogó'
entry_b = tk.Entry(window) # az ablakhoz csatolása
entry_b.insert(0, text_b) # default szöveg megadása
entry_b.bind('<FocusIn>', lambda event: on_entry_click(event, text_b)) # Event meghívása a megadott szöveggel
entry_b.bind('<FocusOut>', on_focusout) # Event meghívása
entry_b.config(fg = 'grey') # Szöveg színezése
entry_b.pack(side=tk.TOP, padx=10, pady=0) # Az inuputbox elhelyezése és csomagolása

# Felvétel gomb
button_add = tk.Button(window, text="Felvétel", command=calculate)
button_add.pack(padx=0, pady=10)

# Listázó gomb
button_list = tk.Button(window, text="Listázás", command=print_keruletek)
button_list.place(x=232, y=68)

window.bind("<Button-1>", on_focusout)
window.bind('<FocusOut>', on_focusout)