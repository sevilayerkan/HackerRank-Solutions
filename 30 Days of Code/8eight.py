def main():
    n = int(input())
    phoneDict = {}
    
    for i in range(0,n):
        temp = input().split(' ') 
        phoneDict[temp[0]] = temp[1]
    
    while True:
        try:
            userInput = input()
        except:
            break
            
        if userInput in phoneDict:
            #print(userInput + "=" + phoneDict.get(userInput)) 
            print(f"{userInput}={phoneDict.get(userInput)}")
        else:
            print("Not found")
    
main()