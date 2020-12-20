import tkinter as tk
import random


# Fungsi untuk swap dua bars yang akan dianimasikan
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21 - bar11, 0)
    canvas.move(pos_1, bar12 - bar22, 0)

worker = None

# Bubble Sort
def _bubble_sort():
    global barList
    global lengthList

    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if (lengthList[j] > lengthList[j + 1]):
                lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
                swap(barList[j + 1], barList[j])
                yield

# Comb Sort
def _comb_sort():
    global barList
    global lengthList

    gap = n = len(lengthList)
    swapped = True

    while gap > 1 or swapped:
        swapped = False
        gap = int(gap * 10 / 13)

        if gap < 1:
            swapped = False
            gap = 1

        for i in range(n - gap):
            if lengthList[i] > lengthList[i + gap]:
                lengthList[i], lengthList[i + gap] = lengthList[i + gap], lengthList[i]
                barList[i], barList[i + gap] = barList[i + gap], barList[i]
                swap(barList[i + gap], barList[i])
                swapped = True
                yield

# Fungsi untuk men-trigger animasi
def comb_sort():
    global worker
    worker = _comb_sort()
    animate()

def bubble_sort():
    global worker
    worker = _bubble_sort()
    animate()

# Fungsi Animasi
def animate():
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(20, animate)
        except StopIteration:
            worker = None
        finally:
            window.after_cancel(animate)
            
# Fungsi untuk memuat data
def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = []

    # Membuat bar
    for bar in range(1, 60):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(barstart, randomY, barend, 365, fill='yellow')
        barList.append(bar)
        barstart += 10
        barend += 10

    # Memberikan panjang bar dan memasukkan kedalam length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    # Maximum diwarnai merah
    # Minimum diwarnai hitam
    for i in range(len(lengthList) - 1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='red')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='black')

# Membuat window menggunakan Tk widget
window = tk.Tk()
window.title('Tubes AKA')
window.geometry('600x450')

# Membuat Canvas didalam window untuk menampilkan konten
canvas = tk.Canvas(window, width='600', height='400')
canvas.grid(column=0, row=0, columnspan=50)

# Buttons
comb = tk.Button(window, text='Comb Sort', command=comb_sort)
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
shuf = tk.Button(window, text='Shuffle', command=generate)
comb.grid(column=2, row=1)
bubble.grid(column=3, row=1)
shuf.grid(column=0, row=1)

generate()
window.mainloop()
