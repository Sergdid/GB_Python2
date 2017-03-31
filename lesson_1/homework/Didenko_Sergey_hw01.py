import csv
import hashlib

line = []

def hash_all(i, code_all):
    '''
    >>> print (line[0]['line3'])
    9233eac58259dd3a13d6c9c59f8001823b6b1fee
    '''
    
    h = i['line1'].encode('utf-8')
    if code_all == 'sha1':
        hsh = hashlib.sha1(h).digest()
    elif code_all == 'md5':
        hsh = hashlib.md5(h).digest()
    elif code_all == 'sha512':
        hsh = hashlib.sha512(h).digest()

    return hsh.hex()


with open('need_hashes.csv', 'r+', encoding='utf-8') as f:
    row = csv.DictReader(f, delimiter=';', fieldnames=['line1', 'line2', 'line3'])
    for i in row:
        i['line3'] = (hash_all(i, i['line2']))
        line.append(i)

    rw = csv.DictWriter(f, delimiter=';', fieldnames=['line1', 'line2', 'line3'])
    for i in line:
        rw.writerow(i)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()       

        
 
