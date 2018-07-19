import math

valid = 0
total = 0

start = input("Press any key to begin\n")
for i in range(1,100000000):
    for a in range ((100*(i-1)+1),(100*i)+1):
        for j in range(1,10000):
            for b in range ((100*(j-1)+1), (100*j)+1):
                for k in range(1,10000):
                    for c in range ((100*(k-1)+1), (100*k)+1):
                        d = math.sqrt((math.pow(a,2))+(math.pow(b,2))+(math.pow(c,2)))
                        if ((math.ceil(d) == d)&(a!=0)&(b!=0)&(c!=0)&(d!=0)):
                            print(str(a)+","+str(b)+","+str(c)+","+str(int(d))+"  (space diagonal #"+str(int(valid))+"/"+str(int(total))+" checked)")
                            valid = valid+1
                        total = total+1
                        if ((math.ceil(total/1000000) == (total/1000000))&(total<1000000000)):
                            print(str(int(total/1000000))+" million space diagonals checked. "+str(int(valid))+" valid. Just checked combination "+str(a)+","+str(b)+","+str(c)+","+str(int(d)))
                        elif (total == 1000000000):
                            print("1 billion space diagonals checked. "+str(int(valid))+" valid.")
                        elif (total == 1000000000000):
                            print("1 trillion space diagonals checked. "+str(int(valid))+" valid.")
