
from datetime import datetime
# чтение файла в список
f_in = open('zno.csv', 'r')
i = 0
base = []
for line in f_in:
    base.append(line)
    i = i + 1
f_in.close()
print('Строк = ' + str(i))

fio_mn = set()
for line in base:
    line_sp = line.split(';')
    fio_mn.add(line_sp[5])

print('ФИО = ' + str(len(fio_mn)))
fio_mn_sort  =sorted(fio_mn)
f_out = open('zno+analize.csv', 'w')
for fio in fio_mn_sort:
    j = 0
    zno = []
    for line in base:
        line_sp = line.split(';')
        if line_sp[5] == fio:
            j = j + 1
            zno.append(line)
    print(fio + ' = ' + str(j))
    city = ''
    zno_c = ''
    close = ''
    x = 0
    y = 0
    zno_skip = ''
    for line in zno:
        line_sp = line.split(';')
        text = line_sp[5] + ';' + line_sp[2]+';'+line_sp[3]+';'+line_sp[4]+';'+line_sp[7]
        if city =='':
            city = line_sp[7]
            zno_c = line_sp[2]
            close = line_sp[4]
#            print(city+' '+zno_c+' '+close)
        else:
            if city == line_sp[7] or int(line_sp[9]) == 0:
                text=text+';нет перемещения'
                city = line_sp[7]
                zno_c = line_sp[2]
                close = line_sp[4]
#                print(city + ' ' + zno_c + ' ' + close)
            else:
#                print('есть перемещение')
                text = text + ';есть перемещение'
                y = 0
                for line_2 in zno:
                    line_2_sp = line_2.split(';')
                    zno_skip = ''
                    if ( (datetime.strptime(line_2_sp[3], '%d.%m.%Y %H:%M') <  datetime.strptime(close, '%d.%m.%Y %H:%M')) and (datetime.strptime(line_2_sp[4], '%d.%m.%Y %H:%M') > datetime.strptime(close, '%d.%m.%Y %H:%M')) and city==line_2_sp[7]):
#                        print(line_2_sp[2])
                        y = y + 1
                        zno_skip = zno_skip + line_2_sp[2]
                if y > 0:
                    x = x +1
                city = line_sp[7]
                zno_c = line_sp[2]
                close = line_sp[4]
#                print(city+' '+zno_c+' '+close)
        f_out.write(text+';'+str(x)+';'+str(y)+';'+zno_skip+'\n')
#    print(fio + ' = ' + str(j) + ' ' + str(x))
f_out.close()
print('Остановка')