# put your python code here
m, n = map(int, input('Введите номер месяца и день в одну строчку: ').split()) #вводятся два числа
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 < m <= 12:
    if m ==3 or m == 5 or m ==7 or m ==8 or m == 10 or m ==12:
        if n <= 31:
            kile = str(n-1)
            x = str(m) + '.' + kile.rjust(2, '0') 
            if kile == '0':
                if m==8:
                    kile = '31'
                    x = str(m-1) + '.' + kile.rjust(2, '0')
                    print(x.rjust(len(x)+ 1, '0'), end=' ')
                    s = str(n+1)
                    z = str(m) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
                elif m == 3:
                    kile = '28'
                    x = str(m-1) + '.' + kile.rjust(2, '0')
                    print(x.rjust(len(x)+ 1, '0'), end=' ')
                    s = str(n+1)
                    z = str(m) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
                else:
                    kile = '30'
                    x = str(m-1) + '.' + kile.rjust(2, '0')
                    print(x.rjust(len(x), '0'), end=' ')
                    s = str(n+1)
                    z = str(m) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
            else:  
                if len(x) == 5:                
                    print(x.rjust(len(x), '0'), end=' ') 
                else:
                    print(x.rjust(len(x)+1, '0'), end=' ') 
                s = str(n+1)
                z = str(m) + '.' + s.rjust(2, '0') 
                if n+1 > 31 and m <12:
                    s = '01'
                    z = str(m+1) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
                elif m+1 > 12:
                    s = '01'
                    m = 0
                    z = str(m+1) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
                else:
                    print(z.rjust(5, '0'))
    elif m == 2:
        kile = str(n-1)
        if kile == '0':
            kile = '31'
            x = str(m-1) + '.' + kile
            print(x.rjust(len(x)+1, '0'), end=' ')
            s = str(n+1)
            z = str(m) + '.' + s.rjust(2, '0')
            print(z.rjust(len(z)+1, '0'))
        else:  
            if 29 == n+1:
                x = str(m) + '.' + str(n-1)
                print(x.rjust(5, '0'), end=' ')
                s = '01'
                z = str(m+1) + '.' + s
                print(z.rjust(5, '0'))
            elif n < 28:
                k = str(n-1)
                x = str(m) + '.' + k.rjust(2, '0')
                print(x.rjust(len(x)+1, '0'), end=' ')
                s = str(n+1)
                z = str(m) + '.' + s 
                h = str(m+1) + '.' + s.rjust(2, '0')
                print(h.rjust(5, '0'))

    elif m == 1:
        if n <= 31:
            kile = str(n-1)
            x = str(m) + '.' + kile.rjust(2, '0')    
            if int(kile) == 0:
                print('12.31'+' 01.02', end=' ')
            else:
                if len(x) == 5:                
                    print(x.rjust(len(x), '0'), end=' ') 
                else:
                    print(x.rjust(len(x)+1, '0'), end=' ') 
                s = str(n+1)
                z = str(m) + '.' + s.rjust(2, '0') 
                if n+1 > 31 and m <12:
                    s = '01'
                    z = str(m+1) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
                elif m+1 > 12:
                    s = '01'
                    m = 0
                    z = str(m+1) + '.' + s.rjust(2, '0') 
                    print(z.rjust(5, '0'))
                else:
                    print(z.rjust(5, '0'))
        else:
            pass
            
    else:
        kile = str(n-1)
        
        if kile =='0':
            kile = '31'
            p = str(n-1)
            x = str(m-1) + '.' + kile
            print(x.rjust(len(x), '0'), end=' ')
            s = str(n+1)
            z = str(m) + '.' + s.rjust(2, '0')
            print(z.rjust(5, '0'))
        else:
            if n <=30:
                p = str(n-1)
                x = str(m) + '.' + p.rjust(2, '0')
                print(x.rjust(len(x), '0'), end=' ')
                s = str(n+1)
                z = str(m) + '.' + s.rjust(2, '0')
                if n+1 > 30 and m <12:
                    s = '01'
                    z = str(m+1) + '.' + s
                    print(z.rjust(5, '0'))
                elif m+1 > 12:
                    s = '01'
                    m = 0
                    z = str(m+1) + '.' + s
                    print(z.rjust(5, '0'))
                else:
                    print(z.rjust(5, '0'))
            else:
                pass
