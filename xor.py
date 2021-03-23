import  sys
class Crypt:
    def __init__(self,key):
        self.key= key
    
    def encrypt(self,msg):
        keyList = list(self.key)
        msgList = list(msg)
        keyLen = len(keyList)
        msgLen = len(msgList)
        cipherTxst = [''] * msgLen
        for i in range(msgLen):
            cipherTxst[i] = chr(ord(msgList[i]) ^ ord(keyList[i%keyLen]))
        return ''.join(cipherTxst)
        
    def decrypt(self,msg):
        keyList = list(self.key)
        msgList = list(msg)
        keyLen = len(keyList)
        msgLen = len(msgList)
        cipherTxst = [''] * msgLen
        for i in range(msgLen):
            cipherTxst[i] = chr ( ord( msgList[i]) ^ ord( keyList[ i % keyLen]))
        return ''.join(cipherTxst)

if __name__ == '__main__':
    if len(sys.argv)>2:
        if sys.argv[1]=='-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3])) 
        elif sys.argv[1]=='-d':
            c = Crypt(sys.argv[2])
            print(c.decrypt(sys.argv[3]))