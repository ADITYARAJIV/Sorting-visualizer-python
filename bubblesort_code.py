import time

def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])