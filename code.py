number = int(input ("ตัวเลขแม่สูตรคูณ : "))
print ("สูตรคูณแม่ ", number)
for count in range(1, 13, 1):
   print (number, 'x', count, '=', number * count)
