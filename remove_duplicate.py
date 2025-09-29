def duplicate(text):
    result = ""

    for i in text:
        if i not in result:
            result += i
    return result
word = "programming"
print(f"without duplicates : {duplicate(word)}")