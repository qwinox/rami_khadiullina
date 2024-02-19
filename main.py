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
# h0 = beam_width - 0.03

q = st.text_input("Введите распределённую нагрузку в  т/м:").replace(',', '.')
l = st.text_input("Введите длину момента в  м:").replace(',', '.')
# m = q * l ** 2 / 8
# m_ = m * 9.8

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
st.write("Деформирования бетона на сжатие")
st.write(df_0)

# Разделение данных на оси x и y
y = [item[0] for item in data_0]
x = [item[1] for item in data_0]

# Построение графика
plt.plot(x, y, marker='o')
plt.title('Трехлинейная диаграмма деформирования бетона на сжатие')
plt.grid(True)

# Отображение графика
st.write(plt)
