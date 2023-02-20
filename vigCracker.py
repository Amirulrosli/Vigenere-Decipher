

def decrypt_function(cipherText, keyWords,f):
    global num
    count = 0
    arrValue = []
    for i in cipherText:
        
        keyValue = num.get(keyWords[count])
        cipherValue = num.get(i)
        plainValue = cipherValue - keyValue
        if (plainValue<0) :
            plainValue = 26 + plainValue
            plainValue = abs(plainValue)
    
        plaintext = [k for k, v in num.items() if v == plainValue]
        arrValue.append(plaintext[0])
        
        count = count+1
        if (count==len(keyWords)):
            count = 0

    f.write("\n")
    print("==================PLAIN TEXT========================")
    f.write("===================================================")
    for i in arrValue:
        f.write(i)
        print(i, end='')
        
cipherText = input("Enter ciphertext:" ).upper()
keyText = input("Enter Keywords (if no keywords leave blank and Enter):" ).upper()


    
print("")    
print("Automatic Solving the key - - -")

num = ({
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':10,
    'L':11,
    'M':12,
    'N':13,
    'O':14,
    'P':15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25,
})
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'




f = open("data.text",'a')

if keyText=='':
    # lengthText = int(input("Enter Key Length: "))
    
    # lengthNo = 1
    # for i in range(lengthText):
    #     lengthNo = lengthNo * 26
    # count = 0
    
    my_list = []
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                for c4 in chars:
                    my_list.append(c1+c2+c3+c4)
    
    for i in my_list:
        print("")
        print("Key:"+i)
        f.write("\n")
        f.write("Key: "+i)
        f.write("\n")
        f.write("===========================")
        decrypt_function(cipherText,i,f)
else:
    print("Key:"+keyText)
    f.write("\n")
    f.write("Key: "+keyText)
    f.write("\n")
    f.write("===========================")
    decrypt_function(cipherText,keyText,f)
    
f.close()
    
    


