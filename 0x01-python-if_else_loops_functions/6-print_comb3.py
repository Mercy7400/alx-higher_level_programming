#!/usr/bin/python3
print("01", end=", ")
for i in range(1, 9):
    for j in range(i + 1, 10):
        pint("{:d}{:d}".format(i, j), end=", ")
print("\n")
