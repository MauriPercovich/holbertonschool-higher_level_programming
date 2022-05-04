#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        cont = 0
        for j in i:
            cont += 1
            if len(i) != cont:
                print(f"{(j):d}", end=" ")
            else:
                print(f"{(j):d}", end="")
                print()
