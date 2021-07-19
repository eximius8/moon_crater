"""Подсчет кратеров на поверхности Луны."""
from scipy.ndimage import label
import numpy as np
import csv
import itertools


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
    """Функция для подсчета кратеров на поверхности Луны реализована с использованием сторонней библиотеки.

    Принимает:
      matr - список из 0 и 1
    Возвращает
      число найденных кратеров
    """
    matrxix = np.array(matr)
    larr, num = label(matrxix)
    return num


def calculate_selfmade(matr: list) -> int:
    """Функция для подсчета кратеров на поверхности Луны. Функция использует метод Row-by-Row.

    Подробнее о методе:
    https://www.youtube.com/watch?v=hMIrQdX4BkE
    Принимает:
      matr - список из 0 и 1
    Возвращает
      число найденных кратеров
    """
    if len(matr) == 0 or len(matr[0]) == 0:
        return 0
    # создание наполненной нулями матрицы ярлыков того же размера что исходная
    labeled_matr = np.zeros((len(matr), len(matr[0])))
    # создание сета для записи конфликтов. Например {(2,1), (3,2)}
    conflicts = set()
    label = 0
    for i in range(len(matr)):
        # текущее значение ярлыка для внесения в матрицу ярлыков
        for j in range(len(matr[0])):
            # Если значение не равно 0 создать ярлык в матрице ярлыков
            if matr[i][j]:
                # Если значение слева ненулевое, ярлык = значение слева
                if j > 0 and matr[i][j - 1] != 0:
                    labeled_matr[i][j] = labeled_matr[i][j - 1]
                # Если значение сверху ненулевое, ярлык = значение сверху
                elif i > 0 and matr[i - 1][j] != 0:
                    labeled_matr[i][j] = labeled_matr[i - 1][j]
                else:
                    label += 1
                    labeled_matr[i][j] = label
                # Работа с конфликтами
                if i > 0:
                    # Значение текущего ярлыка
                    current_label = labeled_matr[i][j]
                    # Значение ярлыка над текущим
                    above_label = labeled_matr[i - 1][j]
                    # Если текущй ярлык не равен ярлыку над ним, то создаем конфликт.
                    if above_label and above_label != current_label:
                        conflicts.add((max(above_label, current_label), min(above_label, current_label)))

    for i in range(len(labeled_matr)):
        for j in range(len(labeled_matr[0])):
            for conflict in sorted(conflicts, reverse=True):
                if labeled_matr[i][j] == conflict[0]:
                    labeled_matr[i][j] = conflict[1]
    all_labels = set(itertools.chain.from_iterable(labeled_matr))
    if 0 in all_labels:
        return len(all_labels) - 1
    else:
        return len(all_labels)
