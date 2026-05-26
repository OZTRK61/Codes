def convert(s:str,numRows:int)->str:
    if numRows==1 or numRows>=len(s):
        return s
    # Her satır için boş bir liste oluşturuyoruz
    rows=["" for _ in range(numRows)]
    current_row=0
    step=1 # 1 aşağı 1 yukarı gitmeyi temsil eder
    for char in s:
        rows[current_row]+=char
        # En üst satıra geldiysek aşağı (1), 
        # En alt satıra geldiysek yukarı (-1) dön
        if current_row==0:
            step=1
        elif current_row==numRows-1:
            step=-1
            current_row+=step
            # Satırları birleştirip döndür
    return "".join(rows)
print(convert("PAYPALISHIRING", 3))



