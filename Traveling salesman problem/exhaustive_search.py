import csv
import itertools
import time 



with open('european_cities.csv' , 'r') as fil:
    filreader = csv.reader(fil, delimiter=";")
    byer = next(filreader)
    rows = list(filreader)
    

    #takes a int of citys and retursn all permutasions of that lenght 
    def permutasoner(antall_byer):
        newbyer=[]

        i=0
        while i < antall_byer:
            newbyer.append(byer[i])
            i+=1
        alt = list(itertools.permutations(newbyer))

        return alt

    #takes a solution to the TSP and returs the lenght in km or 'fittness' recursivly 
    def avstand(tur,start,slutt):

        #the base case is if we are looking at the last city in the tur,
        # if so we simply return the distance from the last city back to the starting point
        if start == len(tur)-1:
            return float(rows[byer.index(tur[start])][byer.index(tur[0])])

        #if base case is not meet we look at the next two againsent adjoining each other.
        # we find the distance in the cvs file and return it + a new call of avstand() looking at the next two citys. 

        else:
            avst = float(rows[byer.index(tur[start])][byer.index(tur[slutt])])
            start+=1
            slutt+=1
            return avst + float(avstand(tur,start,slutt))

    #starting timer
    start = time.time()
    #here we call on permutasoner with 10 as argument
    alle_permutasjoner = permutasoner(10)
    #we define a currently shortes found tur
    shortestkm = 0
    shortestur = []

    # we then loop over all permutasions and if we find a better soloution we save it in shortestur
    for permutasoner in alle_permutasjoner:
        sum = avstand(permutasoner,0,1)

        if sum < shortestkm or shortestkm==0:
            shortestur=permutasoner
            shortestkm = sum

    print("shortest tour found was",shortestkm, "in the following order ",permutasoner )

    end = time.time()

    print(f"Runtime of the program is {end - start}")
    

    


