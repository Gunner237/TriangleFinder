import math

valid = 0
total = 0

for i in range(1,100000000):
    for a in range ((100*(i-1)),(100*i)):
        for j in range(1,10000):
            for b in range ((100*(j-1)), (100*j)):
                c = math.sqrt((math.pow(a,2))+(math.pow(b,2)))
                #print("c = "+str(c))
                if ((math.ceil(c) == c)&(a!=0)&(b!=0)&(c!=0)):
                    print(str(a)+","+str(b)+","+str(int(c))+"  (triangle #"+str(int(valid))+"/"+str(int(total))+" checked)")
                    valid = valid+1
                total = total+1
                if (total == 1000000):
                    print("1 million triangles checked. "+str(int(valid))+" valid.")
                elif (total == 1000000000):
                    print("1 billion triangles checked. "+str(int(valid))+" valid.")
                elif (total == 1000000000000):
                    print("1 trillion triangles checked. "+str(int(valid))+" valid.")
