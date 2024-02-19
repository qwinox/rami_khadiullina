import streamlit as st

from math import pi
import pandas as pd
import matplotlib.pyplot as plt

st.title("Нужно придумать название сюда")

with st.expander('Основные показатели'):
    beam_length = st.text_input("Введите длину балки в м:", 0.2).replace(',', '.')
    beam_width = st.text_input("Введите ширину балки в м:", 0.55).replace(',', '.')
    
    as0 = str(st.text_input("Введите первый тип арматуры:", "2D18"))
    as1 = str(st.text_input("Введите второй тип арматуры:", "2D14"))
    n = st.text_input("Количество итераций:", 10)

with st.expander('Класс материалов'):
    options1 = ['B3,5', 'B5', 'B7,5', 'B10', 'B12,5', 'B15', 'B20', 'B25', 'B30', 'B35', 'B40', 'B45', 'B50', 'B55', 'B60', 'B70', 'B80', 'B90', 'B100']
    concrete_class = st.selectbox("Введите класс бетона:", options1)
    reinforcement_class = st.text_input("Введите класс арматуры:", "A400").replace(',', '.')

as0 = ((int(as0[2:]) / 2 / 1000) ** 2 * pi) * 2
as1 = ((int(as1[2:]) / 2 / 1000) ** 2 * pi) * 2

Rb_list = [2100, 2800, 4500, 6000, 7500, 8500, 11500, 14500, 17000, 19500, 22000, 25000, 27500, 30000, 33000, 37000, 41000, 44000, 47500]
Rbn_list = [2700, 3500, 5500, 7500, 9500, 11000, 15000, 18500, 22000, 25500, 29000, 32000, 36000, 39500, 43000, 50000, 57000, 64000, 71000]
Rbt_list = [260, 370, 480, 560, 660, 750, 900, 1050, 1150, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2100, 2150, 2200]
Eb_list = [9500000, 13000000, 16000000, 19000000, 21500000, 24000000, 27500000, 30000000, 32500000, 34500000, 36000000, 37000000, 38000000, 39000000, 39500000, 41000000, 42000000, 42500000, 43000000]

Rb = Rb_list[options1.index(concrete_class)]
Rbn = Rbn_list[options1.index(concrete_class)]
Eb = Eb_list[options1.index(concrete_class)]

Rbt = 750

Rbtn = 1100

Rs = 355000
Rsn = 400000
Rsc = 355000


Es = 200000000

as_ = 0.03
asc = 0.03
# h0 = beam_width - 0.03

with st.expander('Нагрузка'):
    q = st.text_input("Введите распределённую нагрузку в  т/м:").replace(',', '.')
    l = st.text_input("Введите длину момента в  м:").replace(',', '.')
    # m = q * l ** 2 / 8
    # m_ = m * 9.8

# _______________________________________________________________
# Трехлинейная диаграмма деформирования бетона на сжатие
data_0 = [
    (0, 0),
    (Rb * 0.6, Rb * 0.6 / Eb),
    (Rbn, 0.002),
    (Rbn, 0.0035)]

# Создание DataFrame
df_0 = pd.DataFrame(data_0, columns=['σ', 'ε'])

# Разделение данных на оси x и y
y = [item[0] for item in data_0]
x = [item[1] for item in data_0]

# Построение графика
plt_0.plot(x, y, marker='o')
plt_0.title('Трехлинейная диаграмма деформирования бетона на сжатие')
plt_0.grid(True)


with st.expander('Расчёты'):
    on1 = st.toggle('Отобразить деформирования бетона на сжатие')

    if on1:
        col1, col2 = st.columns([1,3])
        
        with col1:
            # Вывод таблицы
            st.write("Таблица деформирования бетона на сжатие:")
            st.write(df_0)
        with col2:
            # Отображение графика
            st.pyplot(plt_0)

    on2 = st.toggle('Отобразить деформирования бетона на сжатие')

    if on2:
        col1, col2 = st.columns([1,3])
        
        with col1:
            # Вывод таблицы
            st.write("Таблица деформирования бетона на сжатие:")
            st.write(df_0)
        with col2:
            # Отображение графика
            st.pyplot(plt)
