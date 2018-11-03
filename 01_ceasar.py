plaintext = input(' Input message :')
alphabet = "abcdefghijklmnopqrstuvwxyz"
k = 1
cipher = ''

for c in plaintext:
    if c in alphabet:
        cipher +=  alphabet[(alphabet.index(c)+k)% (len(alphabet))]

print('Your encrypted message is : '+ cipher)
