import hashlib
import os
import glob
import codecs


parts = []
dict_file = {}

with open('file2\\parts.md5', 'r') as md:
    for i in md:
        parts.append(i)                     
       
print (parts)


with open('file_new.pdf', 'wb') as new_f:
    for i in parts:
        for infile in glob.glob('file2/*'):
            with open(infile, 'rb') as f:
                
                if infile != 'file2\parts.md5':
                    in_f = f.read()
                    hsh = hashlib.md5(in_f).hexdigest()
                                               
                    if hsh == i.strip():
                        print (hsh)
                        #in_f += in_f
                        print (in_f)
                        new_f.write(in_f)




            

    
        
