import math

#Is prime metho used to check p and q
def isPrime(num):
    if num < 2:
        print("number must be > 2")
        return False
        
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

#Get p and q from user and check if they are prime
p = int (input("Enter a P *Must be Prime*\n"))
while(isPrime(p)== False ):
    p = int(input("P is not prime try again: "))
q = int (input("Enter a Q *Must be Prime*\n"))
while(isPrime(q) == False):
    q = int(input("Q is not prime try again: "))
#message to be encrypted
x = int (input("Enter a message to be encrypted 'x': "))
#n later used for public key
n = p*q

#eulers function phi (n)
eulersFunction = (p-1)*(q-1)

#Allowing user to choose an e must fit criteria of:
#Must be > 1
#GCD (e,eulers function must = 1)
#if either one of these criteria aren't met user must pick another e

e = int(input("choose an e from {1,2,3..." + (str(eulersFunction - 1)) + "} " + "and gcd(e," + str(eulersFunction) + ") = 1: "))
while e < 1 or e > eulersFunction-1 or math.gcd(e,eulersFunction) != 1:
    if(e < 1 or e > eulersFunction-1):
        print("Invalid e, must be between " + "{1,2,3..." + (str(eulersFunction - 1)) + "}")
        e = int(input("Try again: "))
    elif(math.gcd(e,eulersFunction) != 1):
        print("GCD of " + "(" + str(e) + "," + str(eulersFunction) + ")" + " does not equal 1")
        e = int(input(" Try again: "))
#Public key used for encryption
keyPub = [n, e]
#Private key (d) user for decryption 
keyPriv = pow(e,-1,eulersFunction)

#encryption method
def encrypt(x, e, n):
    lowestMod = pow(x,e,n)
    return lowestMod

#decryption method
def decrypt(lowestMod, keyPriv, n):
    decryptMessage = pow(lowestMod, keyPriv, n)
    return decryptMessage

encrypted = encrypt(x,e,n)
decrypted = decrypt(encrypted, keyPriv, n)
print("\n")
print("Original (plaintext) message: " + str(x))
print("Encrypted (ciphertext) message: "+ str(encrypted))
print("Decrypted (back to plaintext) message: " + str(decrypted))

