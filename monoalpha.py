import random
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''.join(random.sample(alpha,len(alpha)))

def encrypt(encrypt_msg):
        final_ans = ""
        for char in encrypt_msg:
                num = alpha.find(char)
                final_ans = final_ans + key[num]
        print(final_ans)
def decrypt(decrypt_msg):
        final_ans = ""
        for char in decrypt_msg:
                num = key.find(char)
                final_ans = final_ans + alpha[num]
        print(final_ans)


while True:
        n = int(input("Enter value:: \n1) To Encrypt Text:: \n2) To Decrypt Text:: \n3) See Key:: \n4) To Exit \n"))
        if (n == 1):
             encrypt_msg = str(input("Enter Text:: "))
             encrypt(encrypt_msg.upper())
        elif (n == 2):
             decrypt_msg = str(input("Enter Crypt Text:: "))
             decrypt(decrypt_msg.upper())
        elif (n==3):
                print(key)
        elif (n==4):
                break
        else:
                print("Invalid Input; Enter  Again!!")
        
