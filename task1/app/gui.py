import tkinter as tk
import time

from ..models.color import Color, RGB, complement

color_list = [
    Color("Air Force Blue", RGB(93, 138, 168)),
    Color("Amethyst", RGB(153, 102, 204)),
    Color("Banana yellow", RGB(255, 225, 53)),
    Color("Bright Pink", RGB(255, 0, 127)),
    Color("Caribbean green", RGB(0, 204, 153)),
    Color("Dark pastel green", RGB(3, 192, 60)),
    Color("Electric indigo", RGB(111, 0, 255)),
    Color("Ferrari red", RGB(255, 40, 0)),
    Color("Lime", RGB(191, 255, 0)),
    Color("Mulberry", RGB(197, 75, 140)),
    Color("Olive", RGB(128, 128, 0)),
    Color("Orange red", RGB(255, 69, 0)),

]


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
myapp = App()
myapp.master.title("Color app")
myapp.master.minsize(400, 300)

index = tk.IntVar()
index.set(0)
print(index.get(), "Index")
selected_color = color_list[int(index.get())]


color_frame = tk.Frame(width=100, height=100, bg=selected_color.hex)
color_frame.pack(fill=tk.X)
color_frame_name = tk.Label(color_frame, text=selected_color.name, fg=complement(selected_color).hex,
                            bg=selected_color.hex)
color_frame_hex = tk.Label(color_frame, text=selected_color.hex, fg=complement(selected_color).hex,
                           bg=selected_color.hex)
color_frame_name.pack()
color_frame_hex.pack()

comp_color_frame = tk.Frame(width=100, height=100, bg=complement(selected_color).hex)
comp_color_frame.pack(fill=tk.X)
comp_color_frame_name = tk.Label(comp_color_frame, text=complement(selected_color).name, fg=selected_color.hex,
                                 bg=complement(selected_color).hex)
comp_color_frame_hex = tk.Label(comp_color_frame, text=complement(selected_color).hex, fg=selected_color.hex,
                                bg=complement(selected_color).hex)
comp_color_frame_name.pack()
comp_color_frame_hex.pack()

counter = 0
def color_update():
    if index.get() <= len(color_list) - 2:
        global counter

        index.set(counter)
        print(index.get(), "index")

        global selected_color
        selected_color = color_list[int(index.get())]
        print(selected_color.name)

        color_frame.config(bg=selected_color.hex)
        color_frame_name.config(bg=selected_color.hex, fg=complement(selected_color).hex, text=selected_color.name)
        color_frame_hex.config(bg=selected_color.hex, fg=complement(selected_color).hex, text=selected_color.hex)

        comp_color_frame.config(bg=complement(selected_color).hex)
        comp_color_frame_name.config(bg=complement(selected_color).hex, fg=selected_color.hex, text=complement(selected_color).name)
        comp_color_frame_hex.config(bg=complement(selected_color).hex, fg=selected_color.hex, text=complement(selected_color).hex)

        counter += 1
        print(counter, "Counter")




def start_color_update():
    change_color_btn.config(state=tk.DISABLED)
    for c in color_list:
        color_update()
        myapp.update()
        time.sleep(1)
    index.set(0)
    global counter
    counter = 0
    change_color_btn.config(state=tk.NORMAL)



change_color_btn = tk.Button(text='Click to loop all colors', padx=20, pady=5, fg='white', bg='black', command=start_color_update)
change_color_btn.place(relx=0.25, rely=0.5)

# start the program
myapp.mainloop()
