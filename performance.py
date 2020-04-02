from game import *
from timeit import default_timer as timer
import random 
import matplotlib.pyplot as plt

brute_force = []
method_2 = []
elimination = []
size_list = list(range(2,10))

for n in size_list:
    avg1,avg2,avg3 = 0,0,0
    iterations = 100
    for i in range(iterations):
        game1 = game(n,n)
        u1 = [[ random.randint(1,2) for i in range(n) ] for j in range(n)]
        u2 = [[ random.randint(1,2) for i in range(n) ] for j in range(n)]
        game1.set_utility_1(u1)
        game1.set_utility_2(u2)


        s1 = timer()
        dump = game1.nash_brute_force()
        e1  = timer()

        avg1 += e1-s1


        s2 = timer()
        dump = game1.nash_method_2()
        e2  = timer()

        avg2 += e2 - s2

        s3 = timer()

        
        dump = game1.nash_elimination()

        e3  = timer()
        
        
        avg3 += e3 - s3
    
    avg1 = avg1/iterations
    avg2 = avg2/iterations
    avg3 = avg3/iterations

    brute_force.append(avg1)
    method_2.append(avg2)
    elimination.append(avg3)


plt.plot(size_list, brute_force,'r')
plt.plot(size_list, method_2,'g')
plt.plot(size_list, elimination,'b')

plt.show()