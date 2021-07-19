"""Подсчет кратеров на поверхности Луны."""
from scipy.ndimage import label
import numpy as np
import csv


def read_craters(filename: str, delimiter: str) -> list:
    """Считывает файл и возвращает матрицу на его основе."""
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)
        data = []
        for row in reader:
            data += [
                [row],
            ]
        return data


def calculate(matr: list) -> int:
    """Функция для подсчета кратеров на поверхности Луны.

    Принимает:
      matr - список из 0 и 1
    Возвращает
      число найденных кратеров
    """
    matrxix = np.array(matr)
    larr, num = label(matrxix)
    return num

def calculate_selfmade(matr: list) -> int:
    """Функция для подсчета кратеров на поверхности Луны.

    Принимает:
      matr - список из 0 и 1
    Возвращает
      число найденных кратеров
    """
    labeled_matr = np.zeros( (len(matr), len(matr[0])))
    print(labeled_matr)
    conflicts = set()
    for i in range(len(matr)):
      label = 1
      for j in range(len(matr[0])):
        print(i)
        if matr[i][j]:
          if j > 0 and not matr[i][j - 1]:
            label += 1
          labeled_matr[i][j] = label

          if i > 0 and labeled_matr[i - 1][j]:
            above = labeled_matr[i - 1][j]
            conflicts.add((max(above, label), min(above, label)))         
        print(labeled_matr)
    
    return 5

matr_test = [
            [1, 1, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]

calculate_selfmade(matr_test)
