# 2. Write a python program using function to convert Celsius to Fahrenheit.

def cel_to_fe(celcious):
    return (celcious * (9/5)) + 32

def fe_to_ce(feranhite):
    return 5*(feranhite-32)/9

print(cel_to_fe(100))
print(round(fe_to_ce(100),2))