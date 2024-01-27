import numpy as np
# Матрица коэффициентов
A = np.array([[1.0, -1.0, 1.0],
              [2.0, 3.0, -1.0],
              [3.0, 1.0, 2.0]])
# Вектор правой части
B = np.array([5.0, 8.0, 2.0])
# Расширенная матрица системы
AB = np.column_stack((A, B))
# Применяем метод Гаусса
n = len(B)
for i in range(n):
    # Приводим текущий столбец к единичному значению
    AB[i] /= AB[i, i]
    # Обнуляем остальные элементы в текущем столбце
    for j in range(i + 1, n):
        AB[j] -= AB[j, i] * AB[i]
# Обратный ход метода Гаусса
for i in range(n - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        AB[j] -= AB[j, i] * AB[i]
# Извлекаем решение
solution = AB[:, -1]
print("Решение системы линейных уравнений:")
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])
