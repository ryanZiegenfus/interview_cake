message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

def reverse_message():
    global message
    storage = []
    counter = 0
    if len(message) != 0:
        storage.append('')
    for i in message:
        if i == ' ':
            storage.append('')
    for i in message:
        if i != ' ':
            storage[counter] += i
        else:
            counter += 1
    counter = 0
    for i in range(0, len(storage)):
        for j in storage[-(1 + i)]:
            message[counter] = j
            counter += 1
        if counter < len(message):
            message[counter] = ' '
            counter += 1


reverse_message()
print(''.join(message))