


import socket
import datetime


summ = 1000000 #сумма перевода
id_company = 9999 #id организации для перевода средств



def tranz_plat(summ, id_company):
    """
     Создается транзакция с суммой и id
    """
    data = (summ << 64) | (id_company << 32)
    return data
               

def data_cod():
    year = (datetime.datetime.now().year - 2000)
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    data_t = ((year << 9) | ( month << 5) | (day & 31))
    return data_t



HOST, PORT = 'localhost', 8000

print('Клиент запущен')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))



packet = data_cod() + tranz_plat(summ, id_company) # создаем пакет

sock.sendall(bytes(str(packet), 'utf-8'))

# Как со стороны сервира мне из пакета достать все обратно?


recvd = str(sock.recv(1024), 'utf-8')

print(recvd)


sock.close()


