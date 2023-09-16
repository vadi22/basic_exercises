from collections import *
# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print()


# Вывести количество букв "а" в слове
word = 'Архангельск'
# print((dict(Counter(word).most_common()))['а'])

# list_word = list(word)
print(word.count('а'))
print()


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for i in word.lower():
    if i in 'ауоыиэяюёе':
        count +=1
print(count)
print()


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print()


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])
print()

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
list_sentense = [len(i) for i in sentence.split()]
print(int((sum(list_sentense)/len(sentence.split()))))
