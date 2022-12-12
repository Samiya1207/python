def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

str1 = ["a","abb","sfs", "oo", "de", "sfde"]
print("list:")
print(str1)
print("Check the nth-1 string is a proper substring of nth string:")
print(test(str1))