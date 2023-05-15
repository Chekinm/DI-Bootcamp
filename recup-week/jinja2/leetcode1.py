def divide( dvd, dvs):
    int_max = 2147483648
    minus = (dvd >= 0) ^ (dvs >= 0)
    a_dvd = abs(dvd)
    a_dvs = abs(dvs)
    power_2_dvs = [(a_dvs,1)]
    power_2 = 1
    if a_dvd >= a_dvs:
        while True:
            a_dvs += a_dvs
            power_2 += power_2
            if a_dvs > a_dvd:
                break
            power_2_dvs.append((a_dvs,power_2))
        ratio = 0
        for num, pow2 in reversed(power_2_dvs):
            if a_dvd - num >= 0:
                ratio += pow2
                a_dvd -= num
            else:
                continue    
    else:
        return 0 

    if ratio > int_max and minus:
        ratio = int_max
    if ratio > int_max - 1 and not minus:
        ratio = int_max - 1

    return -ratio if minus else ratio

print(divide(1000,10))