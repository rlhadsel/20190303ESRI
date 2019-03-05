#!/usr/bin/env python
import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73],
     [11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90],
     [75, 37, 11, 62, 35, 76, 38, 4]]
)  # <1>

print('a =>', a, '\n')

i = a > 50  # <2>
print('i (a > 50) =>', i, '\n')

print('a[i] =>', a[i], '\n')  # <3>

print('a[a > 50] =>', a[a > 50], '\n')  # <4>

print('a[i].min(), a[i].max() =>', a[i].min(), a[i].max(), '\n')  # <5>

x = np.where(a > 50) # [[row indices], [col indices]]

print("x is", x)


a[i] = 0  # <6>
print('a =>', a, '\n')


print("a[a < 15] += 10")
a[a < 15] += 10  # <7>
print(a, '\n')

