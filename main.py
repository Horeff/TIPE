from Optical_flow import lucas_kanade_method
from matplotlib import pyplot as plt
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from Calculs import trouver_angle

def add_video():
    filename = filedialog.askopenfilename()

    if filename == '':
        try:
            l = lucas_kanade_method("/Users/simonlefranc/Desktop/TIPE/vid.mp4")
        except:
            raise("Impossible d'ouvrir le fichier")
    else:
        l = lucas_kanade_method(filename)
    for i in range(len(l[0])):
        plt.scatter(l[0][i], l[1][i])
    trouver_angle(l)
    plt.show()


root = tk.Tk()
root.title("TIPE : Résultats")

main = ttk.Frame(root)

res = ttk.Frame(main)
lab1 = ttk.Label(res, text="Test Label 1")
lab1.pack()
lab2 = ttk.Label(res, text="Test Label 2")
lab2.pack()
res.pack(fill=tk.BOTH, expand=1)

but = ttk.Button(main, text="Add Video", command=lambda: add_video())
but.pack()

main.pack(fill=tk.BOTH, expand=1)

root.mainloop()









