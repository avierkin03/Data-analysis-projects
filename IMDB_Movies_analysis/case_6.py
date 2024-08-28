import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("case_6_IMDB-Movie-Data.csv")

#видаляємо з датафрейма всі порожні значення
df.dropna(axis=0, inplace=True)

#функція, яка розділяє рядок з комами на список 
def split_genres(genres):
   return genres.split(',')

#переписуємо стовпичк 'Genre' - представляємо його елементи у вигляді списку
df['Genre'] = df['Genre'].apply(split_genres)
#створюємо новий стовпчик 'Number of genres' - тут показиватимуться к-ть жанрів для кожного фільма
df['Number of genres'] = df['Genre'].apply(len)



#----------------------------------------------------------1-------------------------------------------------------
#1. Фільмів з якою кількістю жанрів найбільше?
df["Number of genres"].value_counts().plot(kind ='pie')
plt.show()
#Висновок1: на діаграмі бачимо, що найбільша к-ть фільмів, які відносяться одночасно до 3-х жанрів


#----------------------------------------------------------2-------------------------------------------------------
#2. Чи залежить прибуток фільма від к-ті жанрів, до яких він відноситься?
#Показуємо середнє арифметичне прибутку для фільмів, які мають 1\2\3 жанри
df.groupby(by = "Number of genres")["Revenue (Millions)"].mean().plot(kind = "barh", grid = True)
plt.show()
#Висновок2: фільми, які мають більше жанрів приносять більше грошей




#----------------------------------------------------------3-------------------------------------------------------
#3. Чи залежить рейтинг фільма на сайті Metascore від к-ті жанрів, до яких він відноситься?
#Показуємо середнє арифметичне рейтингу на сайті Metascore для фільмів, які мають 1\2\3 жанри
df.groupby(by = "Number of genres")["Metascore"].mean().plot(kind = "barh", grid = True)
plt.show()
#Висновок3: незалежно від к-ті жанрів(1\2\3), в середньому фільми мають приблизно однакову середню оцінку на сайті Metascore



#----------------------------------------------------------4-------------------------------------------------------
#4. У якому році люди в середньому найбільше залишали оцінок фільмам?
#лінійний графік
df.groupby(by = "Year")["Votes"].mean().plot(kind="line", grid=True)
plt.show()

#ступінчаста діаграма
df.groupby(by = "Year")["Votes"].mean().plot(kind="barh", grid = True)
plt.show()
#Висновок4: по графікам бачимо, що найбільша к-ть відгуків була дана за 2012 рік (трохи менше 300 000 відгуків)



#----------------------------------------------------------5-------------------------------------------------------
#5. У якому році був найвищий середній дохід з одного фільма?
print("Середній дохід по фільмам, в залежності від року його виходу:")
print(df.groupby("Year")["Revenue (Millions)"].mean())

df.groupby(by = "Year")["Revenue (Millions)"].mean().plot(kind="barh", grid = True)
plt.show()
#Висновок5: по графіку бачимо, що найбільший середній дохід за 1 фільм був в 209 році (приблизно 115 000$)




#----------------------------------------------------------6-------------------------------------------------------
#6. Чи впливає рейтинг фільма на його прибуток?
df.plot(x = 'Rating', y = 'Revenue (Millions)', kind = 'scatter')
plt.show()
#Висновок6: на діаграмі розсіювання бачимо, що зв'язок не сильний, проте рисутній - фільми з кращим рейтингом мають трохи кращий прибуток




#----------------------------------------------------------7-------------------------------------------------------
#7. Як з роками змінювалася середня тривалість фільмів?
average_runtimes = df.groupby('Year')['Runtime (Minutes)'].mean()
print(average_runtimes)

df.groupby('Year')['Runtime (Minutes)'].mean().plot(kind="line", x='Year', y='Runtime (Minutes)', title='Зміна тривалості фільмів з роками', xlabel="Рік", ylabel="Середня тривалість фільмів (хв)", grid=True, figsize=(10, 6))
plt.show()
#Висновок7: (на графіку все видно)



#----------------------------------------------------------8-------------------------------------------------------
#8. Який середній рейтинг фільмів у кожного режисера?
print("Середній рейтинг фільмів у кожного режисера:")
print(df.groupby(by = "Director")["Rating"].mean())
