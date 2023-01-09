def kinematic(d = 'n', t = 'n', vi = 'n', vf = 'n', a = 'n'):

    #避免'a'为0不能作为余数的情况
    def time(d, t, vi, vf, a):
        t = (vf - vi) / a if a != 0 else d / vi
        return t

    #避免'a'等于0缺少条件的情况
    def displacement(d, t, vi, vf, a):
        if vi == vf and a == 0:
            print('Missing Input')
        else:
            d = (vf ** 2 - vi ** 2) / (2 * a)
        return d

    #'d'为0时会有两种可能，但默认't'不能为0，所以'vi'和'vf'互为相反数        
    def velocity_final(d, t, vi, vf, a):
        if d == 0:
            vf = -vi
            print("Default: when 'd' is 0, vf = -vi")
        else:
            vf = (vi ** 2 + 2 * a * d) ** (1/2)
        return vf

    #'d'为0时会有两种可能，但默认't'不能为0，所以'vi'和'vf'互为相反数
    def velocity_initial(d, t, vi, vf, a):
        if d == 0:
            vi = -vf
            print("Default: when 'd' is 0, vi = -vf")
        else:
            vi = (vf ** 2 - 2 * a * d) ** (1/2)
        return vi

    #检测输入数据是否合法可计算
    varifyList = [d, t, vi, vf, a]
    #必须要两个未知数，且't'不能为0
    start = True if varifyList.count('n') == 2 and t != 0 else False

    if start == True:

        if a == 'n' and t == 'n':
            a = (vf ** 2 - vi ** 2) / (2 * d)
            t = time(d = d, t = t, vi = vi, vf = vf, a = a)

        elif a == 'n' and vi == 'n':
            vi = (2 * d - vf * t) / t
            a = (vf - vi) / t

        elif vi == 'n' and t == 'n':
            vi = velocity_initial(d = d, t = t, vi = vi, vf = vf, a = a)
            t = time(d = d, t = t, vi = vi, vf = vf, a = a)

        elif a == 'n' and vf == 'n':
            a = (2 * (d - vi * t)) / t ** 2
            vf = a * t + vi         

        elif vf == 'n' and t == 'n':
            vf = velocity_final(d = d, t = t, vi = vi, vf = vf, a = a)
            t = time(d = d, t = t, vi = vi, vf = vf, a = a)            

        elif vi == 'n' and vf == 'n':
            vi = (d - a * t ** 2 / 2) / t
            vf = a * t + vi   

        elif vf == 'n' and d == 'n':
            d = vi * t + a * t ** 2 / 2
            vf = a * t + vi              

        elif a == 'n' and d == 'n':
            a = (vf - vi) / t
            d = vi * t + a * t ** 2 / 2

        elif t == 'n' and d == 'n':
            d = displacement(d = d, t = t, vi = vi, vf = vf, a = a)
            if d != 'n': t = time(d = d, t = t, vi = vi, vf = vf, a = a)

        elif vi == 'n' and d == 'n':
            vi = vf - a * t
            d = vi * t + a * t ** 2 / 2

        #返还全部数值
        return 'd:', d, 't:', t, 'vi:', vi, 'vf:', vf, 'a:', a
    
    else:
        #报错
        print('Input Error')

print(kinematic(vi = 16, a = -9.8, d = -64))
