import  sys
class Crypt:
    def __init__(self,key):
        self.key= key
    
    def encrypt(self,msg):
        key = self.key
        msgList = list(msg)
        msgLen = len(msgList)
        cipherTxst = [''] * msgLen
        n = [''] * msgLen
        for i in range(msgLen):
            cipherTxst[i] = ord(msgList[i]) + int(key)
            if ord(msgList[i])>=65 and ord(msgList[i])<=90:
                if cipherTxst[i] > ord('Z'):
                    cipherTxst[i] -= 26
                elif cipherTxst[i] < ord('A'):
                    cipherTxst[i] += 26
            elif ord(msgList[i])>=97 and ord(msgList[i])<=122:
                if cipherTxst[i] > ord('z'):
                    cipherTxst[i] -= 26
                elif cipherTxst[i] < ord('a'):
                    cipherTxst[i] += 26
            cipherTxst[i] = chr(cipherTxst[i])
        return ''.join(cipherTxst)

    def decrypt(self,msg):
        key = self.key
        msgList = list(msg)
        msgLen = len(msgList)
        cipherTxst = [''] * msgLen
        n = [''] * msgLen
        for i in range(msgLen):
            cipherTxst[i] = ord(msgList[i]) - int(key)
            if ord(msgList[i])>=65 and ord(msgList[i])<=90:
                if cipherTxst[i] > ord('Z'):
                    cipherTxst[i] -= 26
                elif cipherTxst[i] < ord('A'):
                    cipherTxst[i] += 26
            elif ord(msgList[i])>=97 and ord(msgList[i])<=122:
                if cipherTxst[i] > ord('z'):
                    cipherTxst[i] -= 26
                elif cipherTxst[i] < ord('a'):
                    cipherTxst[i] += 26
            cipherTxst[i] = chr(cipherTxst[i])
        return ''.join(cipherTxst)

if __name__ == '__main__':
    if len(sys.argv)>2:
        if sys.argv[1]=='-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3])) 
        elif sys.argv[1]=='-d':
            c = Crypt(sys.argv[2])
            print(c.decrypt(sys.argv[3]))