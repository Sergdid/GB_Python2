import random
import string


def create_file(namef, dir_1, size):
    if size.isdigit() != True:
        if size.endswith('KB') == True:
            s1 = size.split('KB')
            size1 = int(s1[0])*1024
            token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(size1))
        if size.endswith('MB') == True:
            s1 = size.split('MB')
            size1 = int(s1[0]) * 1048567
            token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(size1))
        if size.endswith('GB') == True:
            s1 = size.split('GB')
            size1 = int(s1[0]) * 1073741824
            token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(size1))
                            
    else:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(int(size)))

    file = open(dir_1 + namef, "w")
    file.write(token)


create_file("/test1.txt","D:",'10KB')
create_file("/test2.txt","D:",'1024')
create_file("/test11.txt","D:",'2MB')
create_file("/test21.txt","D:",'1')
