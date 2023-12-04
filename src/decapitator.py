import pandas as pd

def decapitator(file, rows=[2, 3]):
    print(rows)
    for i in range(len(rows)):
        rows[i] -= 1
    print(rows)
    file = file.drop(labels=rows, axis=0)
    return file
