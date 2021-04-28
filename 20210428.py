# from typing import Sequence


# hero_villain = [["Batman", "Joker"], ["Ironman", "Hammer"]]


# sentence = "Batman is a hero, but Joker is a villain."
# words = (
#     sentence.split()
# )  # ['Batman', 'is', 'a', 'hero,', 'but', 'Joker', 'is', 'a', 'villain.']
# print(words)
# swapped_sentence = []

# for word in words:
#     for [hero, villain] in hero_villain:
#         if word.find(hero) != -1:
#             word = word.replace(hero, villain)
#         elif word.find(villain) != -1:
#             word = word.replace(villain, hero)
#     swapped_sentence.append(word)
# print(" ".join(swapped_sentence))


# def no_return_twice_plus_two(num):
#     i = 2
#     print(num * 2 + i)


# def return_twice_plus_two(num):
#     i = 2
#     return num * 2 + i


# print(no_return_twice_plus_two(2))  # None
# print(return_twice_plus_two(2))


# def dog_fn():
#     print("woof")


# def cat_fn():
#     print("meow")


# dog_n = int(input("Enter number of dogs: "))
# cat_n = int(input("Enter number of dogs: "))
# for d in range(dog_n):
#     dog_fn()
# for d in range(cat_n):
#     cat_fn()


def gugu_odd(n):
    for i in range(1, 10, 2):
        print(f"{n} * {i} = {n * i}")


def gugu_even(n):
    for i in range(2, 9, 2):
        print(f"{n} * {i} = {n * i}")


num = int(input("Enter n: "))

gugu_odd(num)
gugu_even(num)
