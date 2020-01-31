# 17. Letter Combinations of a phone number
dict1 = {
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
}
def comb(num_str,num_dict):
    if len(num_str) == 0:
        return num_dict[num_str]
    else:
        list1 = []
        i1,i2 = num_str[0], num_str[1]
        for x in num_dict[i1]:
            for y in num_dict[i2]:
                list1.append(x+y)
        return list1+(comb(num_str[1:],num_dict))
        