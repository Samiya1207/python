def test(list):
    return all(i in range(1000) and abs(i-j)>=10 for i in list for j in list if i!=j) and len(set(list))==100
numbers = list(range(0,1000,10))
print("list:")
print(numbers)
print("check whether the said list contains hundred integers 0 and 999 which differs by 10 from another:")
print(test(numbers))    


