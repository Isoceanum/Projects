import csv
import itertools
import time 
import random
import statistics 

start = time.time()

with open('european_cities.csv' , 'r') as fil:
    filreader = csv.reader(fil, delimiter=";")
    byer = next(filreader)
    rows = list(filreader)

# insted of itertools.permutations which takes a lot of time we use  random.sample to select starting points
    def permutasoner(antall_byer, antall_permuta):
        newbyer=[]
        results = []
        i=0
        while i < antall_byer:
            newbyer.append(byer[i])
            i+=1

        n =0
        while n < antall_permuta:
            results.append(random.sample(newbyer, len(newbyer)))
            n+=1

        return results

# same as exhaustive search 
    def avstand(tur,start,slutt):

        if start == len(tur)-1:
            return float(rows[byer.index(tur[start])][byer.index(tur[0])])

        else:
            avst = float(rows[byer.index(tur[start])][byer.index(tur[slutt])])
            start+=1
            slutt+=1
            return avst + float(avstand(tur,start,slutt))

    #we use random to sample a number of starting solutions  
    valgte_losninger = permutasoner(24, 2000)
 
#takes a solution and number of times to improve it and returns the new distance of the tour 
    def finn_nabo(liste, times):
        #base case is the counter times is 0 and we return 
        if times == 0:

            return float(avstand(liste,0,1))

        else:
            # we select two cities at random and switch there places in the tour. 
            permuta = list(liste) 
            avstand1 = (avstand(permuta,0,1))

            nabo = random.sample(permuta, 2)
            index1 = permuta.index(nabo[0])
            index2 = permuta.index(nabo[1])
            permuta[index1]= nabo[1]
            permuta[index2]= nabo[0]

            avstand2 =(avstand(permuta,0,1))

            #if the switched tour is an improvment over the original we 
            #send the new back to finn_nabo() and try to futher improve it 
            if avstand2 < avstand1:
                return finn_nabo(permuta,times-1)
                
            else:
            #if new is not better then original we discard new and try finn_nabo() again with original 
               return finn_nabo(liste,times-1)

    result = []
    def run():
     
        

    # find shortest tour after allowing some improvement 
        shortestkm = 0
        for n in valgte_losninger:
            sum = finn_nabo(n,500)
            if sum < shortestkm or shortestkm == 0:
                shortestkm= sum
            
        

        result.append(shortestkm)

        
    for i in range(2):
        run()

    res = sorted(result)

    end = time.time()
    print("best =", res[0])

    print("worst=",res[len(res)-1])

    print("mean=",statistics.mean(result)) 

    print("deviant",statistics.stdev(result))
        
    print(f"Runtime of the program is {end - start}")

