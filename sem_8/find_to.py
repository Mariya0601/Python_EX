def find_to ():
    searchable = input('введите имя или номер для поиска: ')
    with open('sem_8/phonebook.txt', 'r', encoding='utf-8') as data:
        for i in data:
            if searchable in i:
                print(i)
                action = input('\n Нажмите 1 - для удаления контакта  \n Нажмите 2 - для изменения контакта\n нажмите 0 - закрыть контакт\n' )
                if action == '1':
                   return delete(i)
                elif action =='2':
                    return replace(i)
                elif action =='3':
                    return 
        print ('No found')

def delete(el):
    with open('sem_8/phonebook.txt', 'r', encoding='utf-8') as rdata:
        lines = rdata.readlines()
        with open('phonebook.txt', 'w', encoding='utf-8') as wdata:
            for line in lines:
                if el not in line:
                    wdata.write(line)
    print('deleted')

def replace(el):
    with open('sem_8/phonebook.txt', 'r', encoding='utf-8') as rdata:
        lines = rdata.readlines()
        with open('sem_8/phonebook.txt', 'w', encoding='utf-8') as wdata:
            for line in lines:
                if el in line:
                    line = line.split()
                    for part in line:
                        new_note = part.replace(part,input(f'Введите изменяемую информацию {part}'))
                        wdata.writelines(new_note + '')
                        print('Done')
                else:
                    wdata.write(str(line))
            
