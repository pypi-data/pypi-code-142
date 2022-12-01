import stern
def sumAB(a,b):
    return a - b
def SealN():
    n=5
    string="Hello beautiful world of programming! "
    print(string * n)
def flip():
    a = "stern"
    print(a[::-1])
def IPS():
    x = 91
    y = 56
    print(x,y)
    x, y = y, x
    print(x,y)
def letters():
    string = "Stern"
    print(string.swapcase())
    print(string.lower())
    print(string.upper())
def listletters():
    s = "stern"
    print(list(s))
def unique():
    x = [1,9,9,1]
    if(len(x) == len(set(x))):
        print("The list is unique")
    else:
        print("The list is NOT unique")
def forelse():
    numbers = [2,4,6,8,1]
    for number in numbers:
        if number % 2 == 1:
            print(number)
            break
        else:
            print("No odd numbers")
def difference():
    first = [1,2,3]
    second = [1,2,3]
    print(first == second)
    print(first is second)
    third = first
    print(first is third)
def duplicates():
    items = [2, 2, 3, 3, 1]
    print(list(set(items)))
def EVT():
    a, b = 1, 2
    print(a, b)
    a, b = b, a
    print(a, b)
def StringConcatenation():
    a = ["stern", "-", "is good", "module."]
    print(" ".join(a))
def DictionaryGenerators():
    S = {i**2 for i in range(10)}
    D = {i: i**2 for i in range(10)}
    print(S)
    print(D)
def Output():
    for part in ["stern ", "is ", "good", "\n"]:
        print(part, end='')
def FMDIL():
    a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
    print(max(set(a), key=a.count))
def Kwargs():
    dictionary = {"a": 1, "b": 2}
    def some_function(a, b):
        print(a + b)
        return
    some_function(**dictionary)
    some_function(a=1, b=2)
while True:
    print("1. Welcome")
    print("2. sum0391")
    print("3. SealN")
    print("4. Flip")
    print("5. In-Place Swapping")
    print("6. Case of Letters")
    print("7. Word to spell")
    print("8. Unique")
    print("9. For Else construct")
    print("10. Difference between == u is")
    print("11. Removing duplicates")
    print("12. Exchanging Values with Tuples")
    print("13. String Concatenation")
    print("14. Dictionary and set generators")
    print("15. Output with print")
    print("16. Finding the Most Duplicate Items in a List")
    print("17. Kwargs")
    print("0. Quit")
    cmd = input("Select an item: ")
    
    if cmd == "1":
        print("Welcome to the module Stern! Thank you for downloading this module!")
    elif cmd == "2":
        print(sumAB(2003, 1991))
    elif cmd == "3":
        SealN()
    elif cmd == "4":
        flip()
    elif cmd == "5":
        IPS()
    elif cmd == "6":
        letters()
    elif cmd == "7":
        listletters()
    elif cmd == "8":
        unique()
    elif cmd == "9":
        forelse()
    elif cmd == "10":
        difference()
    elif cmd == "11":
        duplicates()
    elif cmd == "12":
        EVT()
    elif cmd == "13":
        StringConcatenation()
    elif cmd == "14":
        DictionaryGenerators()
    elif cmd == "15":
        Output()
    elif cmd == "16":
        FMDIL()
    elif cmd == "17":
        Kwargs()
    elif cmd == "0":
        exit()
    else:
        print("You entered an invalid value")