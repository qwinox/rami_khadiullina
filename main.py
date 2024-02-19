import streamlit as st

from math import pi
import pandas as pd
import matplotlib.pyplot as plt

st.title("Нужно придумать название сюда")

with st.expander('Основные показатели'):
    beam_length = st.text_input("Введите длину балки в м:", 0.2).replace(',', '.')
    beam_width = st.text_input("Введите ширину балки в м:", 0.55).replace(',', '.')
    concrete_class = st.text_input("Введите класс бетона:", "В15").replace('.', ',')
    reinforcement_class = st.text_input("Введите класс арматуры:", "A400").replace(',', '.')
    as0 = str(st.text_input("Введите первый тип арматуры:", "2D18"))
    as1 = str(st.text_input("Введите второй тип арматуры:", "2D14"))
    n = st.text_input("Количество итераций:", 10)

as0 = ((int(as0[2:]) / 2 / 1000) ** 2 * pi) * 2
as1 = ((int(as1[2:]) / 2 / 1000) ** 2 * pi) * 2

Rb = 8500
Rbt = 750
Rbn = 11000
Rbtn = 1100

Rs = 355000
Rsn = 400000
Rsc = 355000

Eb = 24000000
Es = 200000000

as_ = 0.03
asc = 0.03
h0 = beam_width - 0.03

q = float(input("Введите распределённую нагрузку в  т/м:").replace(',', '.'))
l = float(input("Введите длину момента в  м:").replace(',', '.'))
m = q * l ** 2 / 8
m_ = m * 9.8

# _______________________________________________________________
# Трехлинейная диаграмма деформирования бетона на сжатие
data_0 = [
    (0, 0),
    (Rbn * 0.6, Rbn * 0.6 / Eb),
    (11000, 0.002),
    (11000, 0.0035)
]

# Создание DataFrame
df_0 = pd.DataFrame(data_0, columns=['σ', 'ε'])

# Вывод таблицы
print("Деформирования бетона на сжатие")
print(df_0)
print()

# Разделение данных на оси x и y
y = [item[0] for item in data_0]
x = [item[1] for item in data_0]

# Построение графика
plt.plot(x, y, marker='o')
plt.title('Трехлинейная диаграмма деформирования бетона на сжатие')
plt.grid(True)

# Отображение графика
plt.show()

# _______________________________________________________________
# Трехлинейная диаграмма деформирования бетона на растяжение
data_1 = [
    (0, 0),
    (Rbtn * 0.6, Rbtn * 0.6 / Eb),
    (11000, 0.0001),
    (11000, 0.00015)
]

# Создание DataFrame
df_1 = pd.DataFrame(data_1, columns=['σ', 'ε'])

# Вывод таблицы
st.write("Деформирования бетона на растяжение")
st.write(df_1)

# Разделение данных на оси x и y
y = [item[0] for item in data_1]
x = [item[1] for item in data_1]

# Построение графика
plt.plot(x, y, marker='o')
plt.title('Трехлинейная диаграмма деформирования бетона на растяжение')
plt.grid(True)

# Отображение графика
st.write(plt)

# _______________________________________________________________
# Двухлинейная диаграмма деформирования арматуры на сжатие
data_2 = [
    (0, 0),
    (Rsn, Rs / Es),
    (Rsn, 0.025)
]

# Создание DataFrame
df_2 = pd.DataFrame(data_2, columns=['σ', 'ε'])

# Вывод таблицы
print("Деформирования арматуры на сжатие")
print(df_2)
print()

# Разделение данных на оси x и y
y = [item[0] for item in data_0]
x = [item[1] for item in data_0]

# Построение графика
plt.plot(x, y, marker='o')  # Маркер 'o' добавляет точки на графике
plt.title('Двухлинейная диаграмма деформирования арматуры на сжатие')
plt.grid(True)

# Отображение графика
plt.show()

# _______________________________________________________________
# Двухлинейная диаграмма деформирования арматуры на растяжение
data_3 = [
    (0, 0),
    (Rsn, Rsc / Es),
    (Rsn, 0.025)
]

# Создание DataFrame
df_3 = pd.DataFrame(data_3, columns=['σ', 'ε'])

# Вывод таблицы
print("Деформирования арматуры на растяжение")
print(df_3)
print()


# Разделение данных на оси x и y
y = [item[0] for item in data_3]
x = [item[1] for item in data_3]

# Построение графика
plt.plot(x, y, marker='o')  # Маркер 'o' добавляет точки на графике
plt.title('Двухлинейная диаграмма деформирования арматуры на растяжение')
plt.grid(True)

# Отображение графика
plt.show()