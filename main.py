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
    labeled_matr = [[],] * len(matr)
    conflicts = []
    for i in range(len(matr)):
      label = 0
      for j in range(len(matr[0])):
        if matr[i][j]:
          if j > 0 and not matr[i][j - 1]:
            label += 1
          labeled_matr[i][j] = label
          if i > 0 and labeled_matr[i - 1][j]:
            above = labeled_matr[i - 1][j]
            conflicts.add((max(above, label), min(above, label)))
        else:
          labeled_matr[i][j] = 0
    print(labeled_matr)
   # return num
