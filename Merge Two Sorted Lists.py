# Bağlı liste düğümü tanımı (Daha önceki sorularda kullandığımız yapı)
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def mergeTwoLists(list1:ListNode,list2:ListNode)->ListNode:
        # Başlangıçta boş bir "dummy" (sahte) düğüm oluşturuyoruz.
        # Bu, yeni listemizin temelini atacak.
     dummy=ListNode(0)
     current=dummy
     # İki liste de bitmediği sürece karşılaştırmaya devam et
     while list1 and list2:
        if list1.val<list2.val:
           current.next=list1 # list1'deki eleman küçükse onu ekle
           list1 = list1.next    # list1'de bir sonraki elemana geç
        else:
           current.next=list2
           list2 = list2.next    # list2'de bir sonraki elemana geç
           current=current.next  # Sonuç listesinde bir adım ilerle
           # Döngü bittiğinde listelerden birinde hala eleman kalmış olabilir.
           # Kalan elemanları (zaten sıralı oldukları için) direkt sona ekle.
     current.next = list1 if list1 else list2
     # dummy.next döndürüyoruz çünkü dummy'nin kendisi 0 değerinde boş bir başlangıçtı.
     return dummy.next
