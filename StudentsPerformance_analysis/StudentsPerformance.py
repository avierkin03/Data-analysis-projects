import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("StudentsPerformance.csv")
print(df)

#-----------------------------------------------------------1-------------------------------------------------------------
# Гіпотеза 1: відвідування підготовчих курсів підвищує результати іспитів у абітурієнтів із сімей, де обидва батьки не мають вищої освіти. 

#Створюємо новий стовпчик 'AvgResults' з середнім результатом тестувань кожного учня
df['AvgResults'] = (df['math score'] + df['reading score']  + df['writing score']) / 3
#print(df)


# групуємо дані по значенням в стовпчику "освітній рівень батьків"
# для кожного освітнього рівня батьків рахуємо середнє значення результатів тестування учнів
print("\nВсі учні (які навчалися та не навчалися на підготовчих курсах):")
print(df.groupby(by = 'parental level of education')['AvgResults'].mean())



# відфільтровуємо тільки учнів, які завершили підготовчі курси
# групуємо дані по значенням в стовпчику "освітній рівень батьків"
# для кожного освітнього рівня батьків рахуємо середнє значення результатів тестування учнів
print("\nТільки учні, які завершили підготовчі курси:")
df_after_courses = df[(df['test preparation course'] == 'completed')].groupby(by = 'parental level of education')['AvgResults'].mean()
print(df_after_courses)
# будуємо ступінчасту діаграму для візуалізації результатів
df[(df['test preparation course'] == 'completed')].groupby(by = 'parental level of education')['AvgResults'].mean().plot(kind = 'barh', figsize = (8, 5), grid = True)
#plt.show()




# відфільтровуємо тільки учнів, які не завершили підготовчі курси
# групуємо дані по значенням в стовпчику "освітній рівень батьків"
# для кожного освітнього рівня батьків рахуємо середнє значення результатів тестування учнів
print("\nТільки учні, які не навчалися на підготовчих курсах:")
df_without_courses = df[(df['test preparation course'] == 'none')].groupby(by = 'parental level of education')['AvgResults'].mean()
print(df_without_courses)

# знаходимо прогрес по балам учнів, які ходили на курси, та учнями які їх не відвідували
master_degree_progress = df_after_courses["master's degree"]-df_without_courses["master's degree"]
bach_degree_progress = df_after_courses["bachelor's degree"]-df_without_courses["bachelor's degree"]
assos_degree_progress = df_after_courses["associate's degree"]-df_without_courses["associate's degree"]
college_progress = df_after_courses["some college"]-df_without_courses["some college"]
high_school_progress = df_after_courses["high school"]-df_without_courses["high school"]

print("\nПрогрес по балам учнів, чиї батьки завершили магістартуру: ", round(master_degree_progress, 1))
print("Прогрес по балам учнів, чиї батьки завершили бакалавр: ", round(bach_degree_progress, 1))
print("Прогрес по балам учнів, чиї батьки мають ступінь молодшого спеціаліста: ", round(assos_degree_progress, 1))
print("Прогрес по балам учнів, чиї батьки завершили коледж: ", round(college_progress, 1))
print("Прогрес по балам учнів, чиї батьки завершили середню школу: ", round(high_school_progress, 1))

# Висновок: гіпотезу можна відкинути, бо дослідження показало протилежну картину - кращі результати мають учні,
# які займалися на підготовчих курсах і чиї батьки мають вищу освіту .


#------------------------------------------------------------------2-----------------------------------------------------------------------
# Гіпотеза 2: краще написали тести ті учні, які нормально поснідали перед ними.

print("\nРезультати учнів, в залежності від сніданків:")
print(df.groupby(by = 'lunch')['AvgResults'].mean())

# будуємо кругову діаграму для візуалізації результатів
df.groupby(by = 'lunch')['AvgResults'].mean().plot(kind = 'pie')
plt.show()

# будуємо ступінчасту діаграму для візуалізації результатів
df.groupby(by = 'lunch')['AvgResults'].mean().plot(kind = 'barh', figsize = (8, 5), grid = True)
plt.show()

# будуємо коробку з вусами 1 для візуалізації результатів
df[df['lunch'] == 'free/reduced']['AvgResults'].plot(kind = 'box')
plt.show()
# будуємо коробку з вусами 2 для візуалізації результатів
df[df['lunch'] == 'standard']['AvgResults'].plot(kind = 'box')
plt.show()


# Висновок: гіпотеза підтвердилася - учні, в яких був стандартний сніданок мають набагато кращий середній бал ніж ті,
# хто взагалі не снідав або просто легенько перекусив.