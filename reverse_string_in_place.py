arr = ['a','b','c','d','e','f','g','h']
def reverse_list():
    global arr
    box = ''
    for i in range(0, int(len(arr)/2)):
        box = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = box
    return arr

reverse_list()