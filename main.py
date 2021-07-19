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
