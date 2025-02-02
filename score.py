score=int(input('نمره خود را وارد کنيد:  '))
if score<0 or score>100:
    print('نمره وارد شده نا معتبر است')
elif score>=0 and score<50:
    print('مردود')
elif score>=50 and score<70:
    print('قابل قبول')
elif score>=70 and score<90:
    print('خوب')
elif score>=90 and score<=100:
    print('عالي')
