letter=input('يک حرف را وارد کنيد:  ')
if letter=='a' or letter=='e'  or letter=='i' or letter=='o' or letter=='u' or letter=='A' or letter=='E' or letter=='I' or letter=='O'  or letter=='U':
    print('حرف صدا دار')
elif len( letter)>1:
    print('فقط يک حرف انتخاب کنيد')
else:
    print('حرف بيصدا')
    
