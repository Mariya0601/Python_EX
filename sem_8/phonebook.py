import os, sys
from find_to import find_to


def main_import_contacts(): 
    with open('sem_8/phonebook.txt', 'r', encoding='utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s[i].split()
        # print(phonebook)

def import_contacts(some_string):
    finded_contacts = list()
    for i in phonebook:
        if some_string in phonebook[i]:
            finded_contacts.append(phonebook[i])
    return finded_contacts
   

def export_contacts(new_contact):
    with open('sem_8/phonebook.txt', 'a+', encoding='utf-8') as data:
        data.writelines(' '.join(new_contact)+ '\n') 
        phonebook[len(phonebook)+1] = new_contact
    
       
def input_contact():
    new_contact = [input('Фамили: ')]
    new_contact.append(input('Имя: '))
    new_contact.append(input('Отчество: '))
    new_contact.append(input('номер телефона: '))
    export_contacts(new_contact)


def find_contact():
    s = import_contacts(input('Кого найти?: '))
    print(*s)

def user_interface():
    main_import_contacts()
    print('Phonebook \nЧто хотите сделать?\n1 - Добавить контакт\n2 - Найти контакт\n4- Удалить/Изменить контакт\n0 - Выход')
    user_input = input('Ваш выбор: ')
    while user_input in ('1','2','3','4'):
        if user_input == '1':
            input_contact()
        elif user_input == '2':  
            find_contact()
        elif user_input == '3':
            print()
            for i in phonebook:
                print(*phonebook[i])
        elif user_input == '4':
            find_to()
        user_input = input('Ваш выбор: ')
    print('bye')

phonebook = dict()
user_interface()

