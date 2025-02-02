day=int(input('عددي را وارد کنيد:  '))
if day<0 :
    print('عدد وارد شده نا معتبر است')
t=day % 7
if t==1:
    print('اولين روز هفته')
elif t==2:
    print('دومين روز هفته')
elif t==3:
    print('سومين روز هفته')
elif t==4:
    print('چهارمين روز هفته')
elif t==5:
    print('پنجمين روز هفته')
elif t==6:
    print('ششمين روز هفته')
elif t==0:
    print('هفتمين روز هفته')
    
