def longestCommonPrefix(strs):
    # Eğer liste boşsa boş dön
    if not strs:
        return ""
    
    # Kelimeleri alfabetik olarak sırala
    strs.sort()
    
    # En baştaki (en küçük) ve en sondaki (en büyük) kelimeleri al
    first = strs[0]
    last = strs[-1]
    
    i = 0
    # İki kelimenin karakterlerini karşılaştır
    # Hem index aşılmamalı hem de karakterler aynı olmalı
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    # Ortak olan kısmı kesip döndür
    return first[:i]

# Test
print(longestCommonPrefix(["flower", "flow", "flight"])) # Çıktı: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))   # Çıktı: ""