import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('case_7_investments_VC.csv')
df = df.dropna()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.to_csv('case7.csv', index=False)
print(df.info())


#---------------------------------------1.В якому місті найбільша к-ть стартапів?----------------------
#Вираховуємо кількість стартапів у кожному місті
startup_count_by_city = df['city'].value_counts()
# Вибираємо перший елемент, який буде містом з найбільшою кількістю стартапів
most_common_city = startup_count_by_city.index[0]
print("Місто з найбільшою кількістю стартапів:", most_common_city)

#Покажемо на діаграмі топ-5 міст з найбільшою кількістю стартапів (стовпчаста діаграма та кругова)
df['city'].value_counts().head(5).plot(kind="barh", grid=True)
plt.show()
df['city'].value_counts().head(5).plot(kind="pie", grid=True)
plt.show()



#---------------------------------------2. Скільки стартапів отримало грант?----------------------
# Рахуємо кількість стартапів, які отримали грант
granted_startups = df[df['grant'] != 0]
granted_count = len(granted_startups)
print("Кількість стартапів, які отримали грант:", granted_count)

startups_without_grant = len(df['grant']) - granted_count

#Покажемо на діаграмі к-ть стартапів з грантами та к-ть стартапів без грантів. Яких більше?
# Назви стовпчиків
categories = ['Отримали грант', 'Не отримали грант']
values = [granted_count, startups_without_grant]
# Створення діаграми
fig, ax = plt.subplots()
ax.bar(categories, values, color=['green', 'red'])
# Додавання підписів
ax.set_xlabel('Категорії')
ax.set_ylabel('Кількість стартапів')
ax.set_title('Кількість стартапів, що отримали та не отримали грант')
# Показ діаграми
plt.show()



#---------------------------------------3. В якому кварталі було найбільше стартапів?----------------------
# Групуємо дані за кварталами та рахуємо кількість стартапів у кожному кварталі
quarterly_startup_count = df['founded_quarter'].value_counts()

# Знаходимо квартал з найбільшою кількістю стартапів
most_successful_quarter = quarterly_startup_count.idxmax()
print("Найуспішніший квартал:", most_successful_quarter)



#---------------------------------------4. В якому році було найбільше стартапів?----------------------
# Рахуємо кількість стартапів у кожному році
yearly_startup_count = df['founded_year'].value_counts()

#Графічно показуємо топ-5 років по к-ті стартапів (стовпчаста діаграма та кругова)
yearly_startup_count.head(5).plot(kind="barh", grid=True)
plt.show()
yearly_startup_count.head(5).plot(kind="pie")
plt.show()

# Знаходимо рік з найбільшою кількістю стартапів
most_successful_year = yearly_startup_count.idxmax()
print("Рік з найбільшою кількістю стартапів:", most_successful_year)



#---------------------------------------5. В яких категоріях було найбільше стартапів?----------------------
# Підраховуємо кількість стартапів у кожній категорії
category_count = df['category_list'].value_counts()
# Знаходимо категорію з найбільшою кількістю стартапів
most_popular_category = category_count.index[0]
print("Найпопулярніша категорія стартапів:", most_popular_category)

# Графічно показуємо топ-5 найпопулярніших категорій по к-ті стартапів (стовпчаста діаграма та кругова)
category_count.head(5).plot(kind="barh", grid=True)
plt.show()
category_count.head(5).plot(kind="pie", grid=True)
plt.show()