def lengthOfLongestSubstring(s: str) -> int:
    # Karakterlerin en son hangi indexte görüldüğünü tutan sözlük
    char_index={}
     # Pencerenin başlangıcı (sol işaretçi)
    left=0
    # En uzun tekrarsız alt string uzunluğu
    max_length=0
     # Sağ işaretçi (right) ile string'de ilerliyoruz
    for right in range(len(s)):
        current_char=s[right]
         # Eğer karakter daha önce görüldüyse VE pencerenin içindeyse
        if current_char in char_index and char_index[current_char]>=left:
          # Karakterin son görüldüğü index'i güncelle
          char_index[current_char]=right
          # Mevcut pencere uzunluğunu hesapla (right - left + 1)
          current_length=right-left+1
          # Maksimum uzunluğu güncelle
        max_length = max(max_length, current_length)
        
    
    return max_length