def is_palindrome(s):
    
    cleaned_s = ''.join(e for e in s if e.isalnum()).lower()
    
    
    return cleaned_s == cleaned_s[::-1]


word_or_phrase = input("Enter a word or phrase: ")
if is_palindrome(word_or_phrase):
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")
