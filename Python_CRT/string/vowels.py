"""WAPP to read a string as input from the user 
print the count of uppercase vowels 
print the count of lowercase vowels
print the count of uppercase consonants 
print the count of lowercase consonants """
str=input("Enter the string:")
U_Vowels,U_Consonants,L_Vowels,L_Consonants=0,0,0,0
for char in str:
    if (char.isalpha() and char.isupper()):
        if char in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(char.isalpha() and char.islower()):
        if char in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Lower case Vowel count: {L_Vowels}")
print(f"Lower case Vowel count: {U_Vowels}")
print(f"Lower case Vowel count: {L_Consonants}")
print(f"Lower case Vowel count: {U_Consonants}")