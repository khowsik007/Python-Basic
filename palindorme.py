def palindrome(text):
    cleaned_text = text.lower()
    if cleaned_text == cleaned_text[::-1]:
        return "Yes is a Palindrome"
    else:
        return "No it is not a palindrome"
    
word = input("Enter the word to check :")
print(f"The given word is={word}:{palindrome(word)}")