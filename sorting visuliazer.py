from tkinter import *
from tkinter import ttk
import random
from bubblesort_code import bubble_sort

root = Tk()
root.title('DSA PROJECT Sorting Algorithm Visualiser')
root.geometry("750x600")
root.config(bg='orange')

select_algorithm = StringVar()
arr = []

#GENERATING THE ARRAY 
def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())

    arr = []
    for i in range(size):
        arr.append(random.randrange(lowest, highest+1))

    drawrectangle(arr, ['red' for x in range(len(arr))]) 
    
    

#DRAWING THE ARRAY ELEMENTS AS RECTANGLES
def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [ i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        #top left coordinates
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        #bottom right coordinates
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))
    
    root.update_idletasks()


def sorting():
    global arr
    bubble_sort(arr, drawrectangle, sortingspeed.get())


#GUI CODING PART

options_frame = Frame(root, width= 700, height=300, bg='green')
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=350, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=5)


Label(options_frame, text="Algorithm Choice: ",).grid(row=0, column=0, padx=10, pady=10)

algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Bubble Sort'],width=10)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.1, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Sorting Speed ")
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

Button(options_frame, text="Start Sorting", command=sorting, bg='red',height=5).grid(row=0, column=3, padx=5, pady=5)

lowest_Entry = Scale(options_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

highest_Entry = Scale(options_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)

arrsize_Entry = Scale(options_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Array size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)

Button(options_frame, text="Current Array", command=Generate_array, bg='blue',height=5).grid(row=1, column=3, padx=10, pady=10)

root.mainloop()