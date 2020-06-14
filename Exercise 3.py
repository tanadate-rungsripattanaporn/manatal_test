def int2roman(input_num):
    roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    var=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    output_roman=''
    for i in range(len(roman)):
        for _ in range(input_num//var[i]): #greedy
            input_num-=var[i]
            output_roman+=roman[i]
    return output_roman
test1=39 #XXXIX
test2=246 #CCXLVI
test3=789 #DCCLXXXIX
test4=2421 #MMCDXXI
print(test1,'>',int2roman(test1))
print(test2,'>',int2roman(test2))
print(test3,'>',int2roman(test3))
print(test4,'>',int2roman(test4))