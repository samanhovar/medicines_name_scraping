# import numpy as np
# import pandas as pd

word_list = []

# alphabet = np.array([chr(i) for i in range(97, 123)])
# for i in alphabet:
#     word_list.append(alphabet + i)


alphabet = [chr(i) for i in range(97, 123)]

for i in alphabet:
    for j in alphabet:
        word_list.append(i + j)


# print(word_list)
