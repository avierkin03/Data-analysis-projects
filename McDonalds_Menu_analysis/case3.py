import pandas as pd
import matplotlib.pyplot as plt
import math

# Завантажуємо дані з CSV файлу
df = pd.read_csv('case3_menu.csv')
print(df.info())
print(df.head())


#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми вітаміну А?
df.groupby(by="Category")["Vitamin A (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='pie')
plt.show()
df.groupby(by="Category")["Vitamin A (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='barh', figsize=(10,5))
plt.show()

#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми вітаміну С?
df.groupby(by="Category")["Vitamin C (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='pie')
plt.show()
df.groupby(by="Category")["Vitamin C (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='barh', figsize=(10,5))
plt.show()

#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми Кальцію?
df.groupby(by="Category")["Calcium (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='pie')
plt.show()
df.groupby(by="Category")["Calcium (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='barh', figsize=(10,5))
plt.show()

#------------------------------------0-------------------------------------
#В якій категорії меню найбільший відсотковий вміст відосно денної норми Заліза?
df.groupby(by="Category")["Iron (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='pie')
plt.show()
df.groupby(by="Category")["Iron (% Daily Value)"].mean().sort_values(ascending=False).head(5).plot(kind='barh', figsize=(10,5))
plt.show()




#------------------------------------0-------------------------------------
#В якій категорії меню найбільше калорій
df[['Category', 'Calories']].groupby('Category').mean().head(10).plot(kind='barh', figsize=(10,5))
plt.show()



#------------------------------------1-------------------------------------
#У скільки разів більше у меню McDonalds Вітаміну А ніж Вітаміну C
avaverage_vitama = df['Vitamin A (% Daily Value)'].mean()
avaverage_vitamc = df['Vitamin C (% Daily Value)'].mean()

# Обчислюємо наскільки більше в середньому міститься вітаміну А ніж вітаміну С
result = avaverage_vitama / avaverage_vitamc

# Округлюємо результат до двох знаків після коми
rounded_result = round(result, 2)

print('У:', rounded_result)



# def check_infinity(result):
#     if math.isinf(result):
#         return 0
#     else:
#         return result
    
# df['AvgResults'] = df['Vitamin A (% Daily Value)'] / df['Vitamin C (% Daily Value)'] 
# #При діленні на 0 в стовпчику 'AvgResults' було багато значень inf (нескінченність), через що дуже псувався отриманий результат
# #тому я додав функцію, яка перевіряє чи є в стовпчику нескінченності і замінює їх на нулі
# df['AvgResults'] = df['AvgResults'].apply(check_infinity)
# print(df["AvgResults"].head(100))


# df['AvgResults'].value_counts().plot(kind = 'pie')
# plt.show()

# #те саме, але стовпчикова діарама
# df['AvgResults'].plot(kind = 'hist',  figsize=(7,5), grid=True)
# plt.show()


#----------------------------------2-----------------------------------------
#Яка частка калорій отриманих з жиру серед усіх калорій в їжі Макдональдсу
avaverage_calories = df['Calories'].mean()
avaverage_fat = df['Calories from Fat'].mean()

result1 = (avaverage_calories / avaverage_fat) * 100

rounded1_result = round(result1, 2)

print('Склад жиру:', rounded1_result)



#------------------------------------3-------------------------------------
# Якої продукції в меню Макдональдс найбільше?
df["Category"].value_counts().plot(kind="barh", ylabel="Категорія", xlabel="К-ть найменувань", figsize=(12, 6))
plt.show()




#------------------------------------4-------------------------------------
# В якій їжі Макдональдсу найбільше протеїну?
df.groupby(by = "Category")["Protein"].mean().plot(kind = 'barh', figsize = (15, 7), grid = True)
plt.show()


#------------------------------------5-------------------------------------
#Чи існує взаємозв'язок між загальною к-тю калорій та к-тю калорій отриманих з жиру?
df.plot(x = 'Calories', y = 'Calories from Fat', kind = 'scatter', figsize=(10, 4), xlabel="Calories", ylabel="Calories from Fat")
plt.show()

#Бачимо, що зв'язок дуже сильний. Це може вказувати на те, що більшість калорій, які люди отримують з їжі Макдональдса отримуються саме з жирної їжі:(