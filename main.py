# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random
import time


def float_didgit_summ():
    float_didgit = input("введите дробное число")
    i = 0
    didg_sum=0

    while i < (len(float_didgit)):
        if (float_didgit[i] == ".") or (float_didgit[i] =="-"):
            i+=1
        else:
            didg_sum += int(float_didgit[i])
            i += 1
    print(didg_sum)

def list_of_sums():
    n=int(input("введите число: "))
    def factorialiys(n):

        if n == 0:
            return 1
        return factorialiys(n-1)*n

    for i in range(1,n+1):
        print(factorialiys(i) ,end=", ")

def kakoije_zamechatelny_predel():

    total_sum = 0
    n = int(input("введите степень "))
    archive = [0]*(n+1)
    print(f"для n ={n}: ")
    for i in range(1 , n+1):
        archive[i] = (1+1/i)**i
        total_sum+=archive[i]
        print(f"{i}: {archive[i]}", end=", ")
        i += 1
    print("\n cумма всех элементов: ",total_sum)

def multiply_elems_po_index():
    N=int(input("N= "))
    indexed_elem_multiply = 1
    list_of_didgit=[]
    for i in range(-abs(N),abs(N+1)):
        list_of_didgit.append(i)
    print(list_of_didgit)
    interesing_indexes=list(map(int, input("аккуратненько введите 3 интересующих вас индекса через пробел\n"
                                           "после третьего пробел не надо\n"
                                           "как бы можете ввести и б0льше^^\n"
                                           "по условию нужно только 3 \n"
                                           ":  ").split()))
    print(interesing_indexes)
    for i in range(0, len(interesing_indexes)):
        indexed_elem_multiply *= int (list_of_didgit[ interesing_indexes[i] ] )
        if i == (len(interesing_indexes)-1):
            print( list_of_didgit[interesing_indexes[i]] )
        else:
            print(list_of_didgit[ interesing_indexes[i] ], "*")

    print(f'={indexed_elem_multiply}')

def list_random_sort():
    width=int(input(" какой длинны хотим видеть список? "))
    rand_list = []
    for i in range (0,width):
        rand_list.append(random.randint(-99,99))
    print(f"случайно сгенерированный список из {width} элементов: ")
    print(rand_list)

    random.shuffle(rand_list)
    print( 'можно было бы ограничиться и функцией random.shuffle : \n',
    rand_list,
           ' \nно видитися мне ,смысл в том , чтобы сделать это вручную)' )

    for i in range (0, math.ceil(width/2)):
        bufer = rand_list[i]
        j=random.randint( math.floor(width/2),width-1)
        rand_list[i]=rand_list[j]
        rand_list[j] =bufer

    print(rand_list)


def goEsho():
    input("введите ENTER для продолжения")
    main()


def main():
    shoKavo=int(input("какое задание хотим проверить?\n"
          "\n0-закрыть программу"
          "\n1-Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр."
          "\n2-Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."
          "\n3-Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму."
          "\n4-Задайте список из N элементов, заполненных числами из промежутка [-N, N]."
          "\nНайдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел."
          "\n5-Реализуйте алгоритм перемешивания списка.\n"
                  "-->"))
    if shoKavo == 0:
        print("надеюсь это была наша последняя встреча^^")
        time.sleep(3)
        exit()
    elif shoKavo == 1:
        float_didgit_summ()
    elif shoKavo == 2:
        list_of_sums()
    elif shoKavo == 3:
        kakoije_zamechatelny_predel()
    elif shoKavo == 4:
        multiply_elems_po_index()
    elif shoKavo == 5:
        list_random_sort()
    goEsho()


if __name__ == "__main__" :
    main()
