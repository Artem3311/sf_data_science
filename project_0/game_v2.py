"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from tkinter import N
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number_1 = np.random.randint(1, 18)  # предполагаемое число
        predict_number_2 = np.random.randint(17, 34)
        predict_number_3 = np.random.randint(33, 49)
        predict_number_4 = np.random.randint(48, 66)
        predict_number_5 = np.random.randint(65, 82)
        predict_number_6 = np.random.randint(81, 101)

        if number == predict_number_1 or number == predict_number_2 or number == predict_number_3 or number == predict_number_4 or number == predict_number_5 or number == predict_number_6:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
