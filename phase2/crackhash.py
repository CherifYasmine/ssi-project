import hashlib

def md5():
    msg = input("Entrer le mesaage a craquer md5 : \n")
    try:
            fp = open("C:/Users/Yasmine/Desktop/ssi-project/phase2/dictionnaire.txt")
            line = fp.readline().strip()
            while line:
                msgEncode = line.encode("utf-8")
                result = hashlib.md5(msgEncode).hexdigest()
                if result == msg:
                   print("Le message craqué : ", line)
                   break
                line = fp.readline().strip()
            print('done')
    finally:
            fp.close()

def sha1():
    msg = input("Entrer le mesaage a craquer sha1 : \n")
    try:
            fp = open("C:/Users/Yasmine/Desktop/ssi-project/phase2/dictionnaire.txt")
            line = fp.readline().strip()
            while line:
                msgEncode = line.encode("utf-8")
                result = hashlib.sha1(msgEncode).hexdigest()
                if result == msg:
                   print("Le message craqué : ", line)
                   break
                line = fp.readline().strip()
            print('done')
    finally:
            fp.close()

def sha256():
    msg = input("Entrer le mesaage a craquer sha256 : \n")
    try:
            fp = open("C:/Users/Yasmine/Desktop/ssi-project/phase2/dictionnaire.txt")
            line = fp.readline().strip()
            while line:
                msgEncode = line.encode("utf-8")
                result = hashlib.sha256(msgEncode).hexdigest()
                if result == msg:
                   print("Le message craqué : ", line)
                   break
                line = fp.readline().strip()
            print('done')
    finally:
            fp.close()

