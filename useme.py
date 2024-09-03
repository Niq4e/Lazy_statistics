
#Несколько полезных функций для проверки нулевой гипотезы и описания выборок.

################################

def check_ind(data1,data2, alt: str = "two-sided"):
    """Функция принимает 2 НЕзависимые выборки и параметр для one tailed test (greater или less), проводит тест Шапиро - Уилка(проверка нормального распределения), \
\n тест Левена (проверка равенства дисперсий), считает коэффицент корреляции Пирсона и определяет вероятность Н0\
\nс помощью т-критерия Стьюдента (при равных дисперсиях) или т-критерию Уэлча (при неравных дисперсиях).\
\nПри отсутствии нормального распределения применяется u-тест Манна-Уитни"""
    from scipy import stats
    set = [data1,data2]
    sides = f'Выбранный метод проверки - {alt if alt == "two-sided" else "one-sided"+'('+str(alt)+')'}.'   
    if stats.shapiro(data1)[1] >=0.05 and stats.shapiro(data2)[1] >=0.05:
        pierson = data1.corr(data2)
        if pierson != 0:
            print(f'Данные распределены нормально, коэффицент корреляции Пирсона: {round(pierson,2)} ({"Сильная" if abs(pierson) >= 0.7 else \
         ( "Средняя" if abs(pierson) >= 0.5 else "Слабая")} {"положительная" if pierson > 0 else "отрицательная"} корреляция)')
        else: print('Переменные линейно независимы друг от друга')
        try:    
            if stats.levene(data1,data2)[1] >=0.05:
                print(f'Дисперсии выборок равны.\
\nВероятность H0 по т-критерию Cтьюдента {"ниже" if stats.ttest_ind(data1, data2, alternative = alt)[1] < 0.05 else "выше"}\
 порога значимости ({stats.ttest_ind(data1, data2, alternative = alt)[1]}). \n{sides}\n-H0: равенство средних-') 
            else:
                print(f'Дисперсии выборок не равны.\
\nВероятность H0 по т-критерию Уэлча {"ниже" if stats.ttest_ind(data1, data2, equal_var=False, alternative = alt)[1] < 0.05 else "выше"}\
 порога значимости ({stats.ttest_ind(data1, data2, equal_var=False, alternative = alt)[1]}). \n{sides}\n-H0: равенство средних-') 
        except ValueError: print('Введен некорректный параметр для one tailed test, укажите "greater" или "less")')
    else:
        print(f'Отсутствует нормальное распределение.\
\nВероятность H0 по критерию Манна-Уитни {"ниже" if stats.mannwhitneyu(data1, data2, alternative = alt)[1] < 0.05 else "выше"}\
 порога значимости ({stats.mannwhitneyu(data1, data2, alternative = alt)[1]}). \n{sides}\n-H0: равенство распределений-')         



def check_rel(data1,data2, alt: str = "two-sided"):
    """Функция принимает 2 зависимые выборки, проводит тест Шапиро - Уилка (проверка нормального распределения), \
\nопределяет вероятность Н0 с помощью парного т-критерия.\
\nПри отсутствии нормального распределения применяется непараметрический ранговый тест Вилкоксона"""
    from scipy import stats
    set = [data1,data2]
    sides = f'Выбранный метод проверки - {alt if alt == "two-sided" else "one-sided"+'('+str(alt)+')'}.'
    if stats.shapiro(data1)[1] >=0.05 and stats.shapiro(data2)[1] >=0.05:
        pierson = data1.corr(data2)
        if pierson != 0:
            print(f'Данные распределены нормально, коэффицент корреляции Пирсона: {round(pierson,2)} ({"Сильная" if abs(pierson) >= 0.7 else \
        ( "Средняя" if abs(pierson) >= 0.5 else "Слабая")} {"положительная" if pierson > 0 else "отрицательная"} корреляция)')
        else: print('Переменные линейно независимы друг от друга')
        try:
            print(f'Вероятность H0 по парному т-критерию {"ниже" if stats.ttest_rel(data1, data2, alternative = alt)[1] < 0.05 else "выше"}\
 порога значимости ({stats.ttest_rel(data1, data2, alternative = alt)[1]}). \n{sides}\n-H0: равенство средних-') 
        except ValueError: print('Введен некорректный параметр для one tailed test, укажите "greater" или "less")')
    else:
        print(f'Отсутствует нормальное распределение.\
\nВероятность H0 по т-критерию Вилкоксона {"ниже" if stats.wilcoxon(data1, data2, alternative = alt)[1] < 0.05 else "выше"}\
 порога значимости ({stats.wilcoxon(data1, data2, alternative = alt)[1]}). \n{sides}\
\n-H0: 2 зависимые выборки происходят из одного распределения-')  
        
