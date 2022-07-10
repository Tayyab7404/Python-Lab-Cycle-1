digits = 0
upper = 0
lower = 0

s = input("Enter a sentence: ").strip() + '.'
#to define the end of the sentence
a = [i for i in s.split()]
for i in s:
    if i.isdigit():
        digits += 1
    elif i.islower():
        lower += 1
    elif i.isupper():
        upper += 1

print('Number of words: ', len(a))
print('Number of digits: ', digits)
print('Number of lowercase letters: ', lower)
print('Number of uppercase letters: ', upper)
