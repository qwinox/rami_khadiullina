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
    q = st.text_input("Введите распределённую нагрузку в  т/м:", 3).replace(',', '.')
    l = st.text_input("Введите длину момента в  м:", 6).replace(',', '.')
    # m = q * l ** 2 / 8
    # m_ = m * 9.8

with st.expander('Класс материалов'):
    options1 = ['B3,5', 'B5', 'B7,5', 'B10', 'B12,5', 'B15', 'B20', 'B25', 'B30', 'B35', 'B40', 'B45', 'B50', 'B55', 'B60', 'B70', 'B80', 'B90', 'B100']
    concrete_class = st.selectbox("Введите класс бетона:", options1)
    options2 = ['A240', 'A400', 'A500', 'A600', 'A800', 'A1000', 'B500', 'Bp500', 'Bp1200', 'Bp1300', 'Bp1400', 'Bp1500', 'Bp1600', 'K1400', 'K1450', 'K1500', 'K1550', 'K1650', 'K1750', 'K1850', 'K1900']
    reinforcement_class = st.selectbox("Введите класс арматуры:", options2)


as0 = ((int(as0[2:]) / 2 / 1000) ** 2 * pi) * 2
as1 = ((int(as1[2:]) / 2 / 1000) ** 2 * pi) * 2

as_ = 0.03
asc = 0.03
# h0 = beam_width - 0.03

Rb_list = [2100, 2800, 4500, 6000, 7500, 8500, 11500, 14500, 17000, 19500, 22000, 25000, 27500, 30000, 33000, 37000, 41000, 44000, 47500]
Rbn_list = [2700, 3500, 5500, 7500, 9500, 11000, 15000, 18500, 22000, 25500, 29000, 32000, 36000, 39500, 43000, 50000, 57000, 64000, 71000]

Rbt_list = [260, 370, 480, 560, 660, 750, 900, 1050, 1150, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2100, 2150, 2200]
Rbtn_list = [390, 550, 700, 850, 1000, 1100, 1350, 1550, 1750, 1950, 2100, 2250, 2450, 2600, 2750, 3000, 3300, 3600, 3800]

Eb_list = [9500000, 13000000, 16000000, 19000000, 21500000, 24000000, 27500000, 30000000, 32500000, 34500000, 36000000, 37000000, 38000000, 39000000, 39500000, 41000000, 42000000, 42500000, 43000000]

Rb = Rb_list[options1.index(concrete_class)]
Rbn = Rbn_list[options1.index(concrete_class)]

Rbt = Rbt_list[options1.index(concrete_class)]
Rbtn = Rbtn_list[options1.index(concrete_class)]

Eb = Eb_list[options1.index(concrete_class)]

Rs_list = [210000, 340000, 435000, 520000, 695000, 870000, 415000, 415000, 1000000, 1100000, 1170000, 1250000, 1340000, 1170000, 1200000, 1250000, 1350000, 1435000, 1515000, 1600000, 1670000]
Rsc_list = [210000, 340000, 435000, 470000, 500000, 500000, 415000, 390000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000]
Rsn_list = [240000, 390000, 500000, 600000, 800000, 1000000, 500000, 500000, 1200000, 1300000, 1400000, 1500000, 1600000, 1400000, 1450000, 1500000, 1550000, 1650000, 1740000, 1840000, 1920000]

Rs = Rs_list[options2.index(reinforcement_class)]
Rsc = Rsc_list[options2.index(reinforcement_class)]
Rsn = Rsn_list[options2.index(reinforcement_class)]

Es = 195000 if reinforcement_class[0] == "K" else 200000

# _______________________________________________________________
# Трехлинейная диаграмма деформирования бетона на сжатие
data_0 = [
    (0, 0),
    (Rb * 0.6, Rb * 0.6 / Eb),
    (Rbn, 0.002),
    (Rbn, 0.0035)]

# Создание DataFrame
df_0 = pd.DataFrame(data_0, columns=['σ', 'ε'])
df_0 = df_0.round(6)

# _______________________________________________________________
# Трехлинейная диаграмма деформирования бетона на растяжение

temp_1 = Rbt * 0.6 / Eb
if temp_1 < 0.0001:
    temp_1 = str(temp_1)
    temp_1 = temp_1[:3] + temp_1[-4:] 
data_1 = [
    (0, 0),
    (Rbt * 0.6, temp_1),
    (Rbtn, 0.0001),
    (Rbtn, 0.00015)
]

# Создание DataFrame
df_1 = pd.DataFrame(data_1, columns=['σ', 'ε'])

# _______________________________________________________________
# Двухлинейная диаграмма деформирования арматуры на сжатие
data_2 = [
    (0, 0),
    (Rsn, Rs / 1000 / Es),
    (Rsn, 0.025)
]

# Создание DataFrame
df_2 = pd.DataFrame(data_2, columns=['σ', 'ε'])

# _______________________________________________________________
# Двухлинейная диаграмма деформирования арматуры на растяжение
data_3 = [
    (0, 0),
    (Rsn, Rsc / 1000 / Es),
    (Rsn, 0.025)
]

# Создание DataFrame
df_3 = pd.DataFrame(data_3, columns=['σ', 'ε'])

# _______________________________________________________________
with st.expander('Расчёты'):
    on1 = st.toggle('Отобразить деформирование бетона на сжатие')
    
    if on1:
        plt.clf()
        col1, col2 = st.columns([1,2])
        
        with col1:
            st.write("Таблица деформирования бетона на сжатие:")
            st.write(df_0)
        with col2:
            # Разделение данных на оси x и y
            y = [item[0] for item in data_0]
            x = [item[1] for item in data_0]
            
            # Построение графика
            plt.plot(x, y, marker='o')
            st.write('Трехлинейная диаграмма деформирования бетона на сжатие')
            plt.grid(True)
            st.pyplot(plt)

    on2 = st.toggle('Отобразить деформирование бетона на растяжение')
    
    if on2:
        plt.clf()
        col1, col2 = st.columns([1,2])
        
        with col1:
            # Вывод таблицы
            st.write("Таблица деформирования бетона на растяжение:")
            st.dataframe(df_1)
        with col2:
            # Разделение данных на оси x и y
            y = [item[0] for item in data_1]
            x = [item[1] for item in data_1]
            
            # Построение графика
            plt.plot(x, y, marker='o')
            st.write('Трехлинейная диаграмма деформирования бетона на растяжение')
            plt.grid(True)
            st.pyplot(plt)

    on3 = st.toggle('Отобразить деформирования арматуры на сжатие')
    
    if on3:
        plt.clf()
        col1, col2 = st.columns([1,2])
        
        with col1:
            st.write("Таблица деформирования арматуры на сжатие:")
            st.write(df_2)
        with col2:
            # Разделение данных на оси x и y
            y = [item[0] for item in data_2]
            x = [item[1] for item in data_2]
            
            # Построение графика
            plt.plot(x, y, marker='o')
            st.write('Трехлинейная диаграмма деформирования бетона на сжатие')
            plt.grid(True)
            st.pyplot(plt)

    on4 = st.toggle('Отобразить деформирования арматуры на растяжение')
    
    if on4:
        plt.clf()
        col1, col2 = st.columns([1,2])
        
        with col1:
            st.write("Таблица деформирования арматуры на сжатие:")
            st.write(df_3)
        with col2:
            # Разделение данных на оси x и y
            y = [item[0] for item in data_3]
            x = [item[1] for item in data_3]
            
            # Построение графика
            plt.plot(x, y, marker='o')
            st.write('Трехлинейная диаграмма деформирования бетона на сжатие')
            plt.grid(True)
            st.pyplot(plt)
