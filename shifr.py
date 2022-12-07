import numpy as np

text_base = tuple("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,!? ")
login_base = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.,!?")
password_base = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.,!?")

def encrypt(message):
    ciph_alph = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'X'}
    key = "formula"
    temp = ""
    temp_list = []
    X = np.array([['y', 'o', 'l', 'r', 'z'],
                  ['w', 'b', 'd', 'u', 'f'],
                  ['x', 'n', 'v', 's', 't'],
                  ['c', 'm', 'q', 'e', 'a'],
                  ['k', 'i', 'h', 'p', 'g']])
    for i in range(len(message)):

        for j in range(5):

            if message[i] in X[j]:
                col = int(str(np.where(X[j] == message[i])).replace("(array([", '').replace("], dtype=int64),)", ''))

                temp += f"{ciph_alph[j]}{ciph_alph[col]}"

        #print(message[i])
    #print(temp)

    for i in range(len(key)):
        temp_list.append([temp[x] for x in range(len(temp)) if (x%len(key)+1) == (i+1)])
        #print(key[i], temp_list[i])
    temp_key = [x for x in key]
    for i in range(len(temp_key)):
        mn = [temp_key[i], i]
        for j in range(i, len(temp_key)):
            if(mn[0] > temp_key[j]):
                mn[0], mn[1] = key[j], j
        temp_key[i], temp_key[mn[1]] = temp_key[mn[1]], temp_key[i]
        temp_list[i], temp_list[mn[1]] = temp_list[mn[1]], temp_list[i]

    #print(*temp_key)
    #for i in range(len(temp_list)):
        #print(temp_key[i], temp_list[i])