from fact_rect import fact_rect
from fact_cikl import factorial_cikl

from simple_benchmark import benchmark
import matplotlib.pyplot as plt

func = [fact_rect, factorial_cikl]
arguments = {}
for i in range(100):
    arguments['i'+str(i)] = i
print(arguments)
arguments_name = 'natural numbers'
aliases = {fact_rect: "рекурсия", factorial_cikl: 'циклическая'}
b = benchmark(func, arguments, arguments_name,function_aliases=aliases )
b.plot()
plt.show(b)