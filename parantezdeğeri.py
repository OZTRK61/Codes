def isValid(s: str) -> bool:
    # Parantez eşleşmelerini bir sözlükte tutalım
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # Eğer karakter bir kapama paranteziyse
        if char in mapping:
            # Yığının en üstündeki elemanı al (yığın boşsa 'dummy' bir değer al)
            top_element = stack.pop() if stack else '#'
            
            # Eğer en üstteki eleman, bu kapama parantezinin eşi değilse geçersizdir
            if mapping[char] != top_element:
                return False
        else:
            # Eğer bir açma paranteziyse, yığına ekle
            stack.append(char)

    # Eğer yığın boşsa True, eleman kaldıysa (açık kalan parantez var demektir) False dön
    return not stack

# Testler
print(isValid("()"))       # True
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([)]"))     # False