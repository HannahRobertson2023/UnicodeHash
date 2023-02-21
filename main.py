import random
import os

LENGTH = 55295
KEYCHAR = "0"

# the key to the example is Fulton School of Engineering

def getUNICODE():
    c = 0
    while True:
        strn = str(c) + ": " + chr(c) + "\n"
        f = open("unicode.txt", "a")
        f.write(strn)
        f.close()
        c = c + 1
        print(strn)


def encode(m):
    resolve = ""
    global KEYCHAR
    m = KEYCHAR + m
    rand = random.randint(1, LENGTH)
    for i in m:
        letter_position = ord(i)
        if letter_position >= 0:
            resolve = resolve + chr(letter_position + rand)
        else:
            resolve = resolve + i

    print(resolve)
    return resolve


def decode(m):
    global KEYCHAR
    shift = ord(m[0]) - ord(KEYCHAR)
    resolve = ""
    for i in m:
        letter_position = ord(i)
        if letter_position >= 0:
            resolve = resolve + chr(letter_position - shift)
        else:
            resolve = resolve + i

    print(resolve)
    return resolve[1:]


def keyencode(m, key):
    output = ""
    for i in range(len(m)):
        shift = random.randint(1, LENGTH)
        letter = m[i]
        kletter = key[i % len(key)]
        letter_position = ord(kletter)
        if letter_position >= 0:
            output = output + chr((letter_position + shift) % LENGTH)  # key letter
            output = output + chr((ord(letter) + shift) % LENGTH)  # message letter

        else:
            output = output + kletter
            output = output + letter

    print(output)
    return output


def keydecode(m, key):
    output = ""
    for i in range(len(m)):
        if i % 2 == 0:
            kletter = ord(key[int(i / 2) % len(key)])
            sletter = ord(m[i])
            shift = sletter - kletter
            diff = ord(m[i + 1]) - shift

            if diff >= 0:
                output = output + chr(diff % LENGTH)
            else:
                output = output + chr(diff + LENGTH)

    print(output)
    return output


def writeout(message):
    IMGPATH = "messages/"
    if not os.path.exists(IMGPATH):
        os.mkdir(IMGPATH)
    ask = input("what should the file name be: ")
    f = open(IMGPATH + ask + ".txt", "w", encoding="utf-8")
    f.write(message)
    f.close()


k = input("Input k to use a key, hit any other key for a plain caesar cypher. ")
f = input("Hit f to import from file, any other key to import from console. ")
m = ""
if f == "f":
    IMGPATH = "messages/"
    if not os.path.exists(IMGPATH):
        os.mkdir(IMGPATH)
    fn = input("What is the name of the file?")
    try:
        f = open(IMGPATH + fn + ".txt", "r", encoding="utf-8")
        m = f.read()
        f.close()
    except:
        input("No file found. what is the message: ")
else:
    m = input("what is the message: ")

plaineord = input("would you like to encode or decode(e for encode): ")
message = ""
if k == "k":
    kin = input("what is the key: ")
    if plaineord == "e":
        message = keyencode(m, kin)
    else:
        message = keydecode(m, kin)
else:
    if plaineord == "e":
        message = encode(m)
    else:
        message = decode(m)

text = input(" do you want to write it to a text file(y or n): ")
if text == "y":
    writeout(message)
else:
    print("")
