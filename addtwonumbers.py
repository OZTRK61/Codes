# Bağlı liste düğümü tanımı
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Sonuç listesini tutmak için boş bir başlangıç düğümü (dummy)
    dummy = ListNode(0)
    current = dummy
    carry = 0 # Elde var kısmı
    
    # İki liste bitene veya elde kalan sayı sıfırlanana kadar devam et
    while l1 or l2 or carry:
        # Değerleri al, eğer liste bittiyse 0 kabul et
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Toplamı hesapla
        total = val1 + val2 + carry
        carry = total // 10  # Yeni elde var (Örn: 13 ise elde 1)
        new_val = total % 10 # Yazılacak rakam (Örn: 13 ise 3 yazılır)
        
        # Yeni düğümü ekle
        current.next = ListNode(new_val)
        
        # İşaretçileri kaydır
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return dummy.next