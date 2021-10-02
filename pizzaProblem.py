def cutPizza(n):
 
    # Case 1
    if(360 % n == 0):
        print("1", end = "")
    else:
        print("0", end = "");
 
    # Case 2
    if(n <= 360):
        print("1", end = "")
    else:
        print("0", end = "");
 
    # Case 3
    if(((n * (n + 1)) / 2) <= 360):
        print("1", end = "")
    else:
        print("0", end = "");
 
 

n = 7;
cutPizza(n);
