def reverse_sentence():
    
    sentence = input("Enter a sentence: ")
    
    
    words = sentence.split()
    
   
    reversed_sentence = ' '.join(reversed(words))
    
    return reversed_sentence


result = reverse_sentence()
print(f"Reversed sentence: {result}")
