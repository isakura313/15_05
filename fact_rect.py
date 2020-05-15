def fact_rect(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact_rect(number-1)
print(fact_rect(256))