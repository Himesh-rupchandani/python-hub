def vowels_count(n):
    vowels = 0
    for i in n:
        if i.lower() in "aeiou":
            vowels = vowels + 1
    return vowels

n = input("Enter anything: ")
print(vowels_count(n))