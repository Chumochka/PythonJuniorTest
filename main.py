import json
import datetime

list_result:list = []
competitors:json

def compile_result():
    with open("results_RUN.txt",'r') as conn:
        start:list[str] = conn.readline().split()   #Получаем строку со значениями старта
        finish:list[str] = conn.readline().split()  #Получаем строку со значениями финиша
        try:
            while(finish!="" or start!=""):
                time_start:datetime = datetime.datetime.strptime(start[2], '%H:%M:%S,%f')   #Форматируем строки во время
                time_finish:datetime = datetime.datetime.strptime(finish[2], '%H:%M:%S,%f')
                number_of_person: str = finish[0]                                           #Получаем номер из строки
                time_span:datetime = time_finish-time_start                                 #Высчитываем время забега
                name, surname = get_name_of_person(number_of_person)                        #Получаем имя и фамилию из другого файла по номеру
                list_result.append([number_of_person,name,surname,time_span])               #Записываем значения в лист
                start = conn.readline().split()
                finish = conn.readline().split()
        except(IndexError):
            pass

def get_name_of_person(number):
    name:str = competitors[number]['Name']              #Получаем значения Name и Surname у элемента number
    surname:str = competitors[number]['Surname']
    return name, surname

def sort_result():
    for i in range(len(list_result)):
        for j in range(i, len(list_result)):
            if (list_result[i][3]>list_result[j][3]):   #Если время меньше, то меняем строки
                list_result[i], list_result[j] = list_result[j], list_result[i]

def print_result():
    print("| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |\n| --- | --- | --- | --- | --- |")
    for i in range(len(list_result)):
        print(f"| {i+1} | {list_result[i][0]} | {list_result[i][1]} | {list_result[i][2]} | {list_result[i][3]} |")

with open("competitors2.json", "r", encoding="utf-8-sig") as file:
    competitors = json.load(file)
compile_result()
sort_result()
print_result()