def vowels_count(text):
    words = "AEIOUaeiou"
    vowels_word = []
    total_vowels = []
    freq = {}
    for i in text:
        if i in words:
            vowels_word.append(i)
            f = i.lower()
            if f in freq:
                freq[f] = freq[f] + 1
            else:
                freq[f] = 1
    total_vowels = len(vowels_word)
    return vowels_word,f"Total no.of vowels:{total_vowels}",f"Frequency of the word:{freq}"




text = "Ronaldo is best footballer"
vowels_list,total,Frequency = vowels_count(text)

print(f"The vowels are:{vowels_list}")
print(f"The total = {total}")
print(f"The frequency is:{Frequency}")