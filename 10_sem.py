"""1. Провести дисперсионный анализ для определения того, есть ли
   различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. 
   Даны значения роста в трех группах случайно выбранных спортсменов:
    Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
    Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
    Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170."""

import numpy as np
from scipy import stats


# нулевая гипотеза :различия среднего роста среди взрослых футболистов, хоккеистов и штангистов нет
# альтернативная гипотеза : различия среднего роста среди взрослых футболистов, хоккеистов и штангистов есть

football=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifting=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

alpha=0.05 
print(stats.f_oneway(football, hockey, weightlifting))

# отвергаем нулевую гипотезу т.к. p-value = 0.01048