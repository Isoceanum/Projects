import csv
import itertools
import time 
import random
import statistics 
import matplotlib.pyplot as plt




with open('european_cities.csv' , 'r') as fil:
    filreader = csv.reader(fil, delimiter=";")
    byer = next(filreader)
    rows = list(filreader)

    # using random sample we pick n number of starting individuals. 
    def permutasoner(antall_byer,antall_permuta):
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

    # mutasion works by randomly selecting two cities and swaping them with probability as an parameter. 
    def mutasjon(liste,probability):
        permuta = list(liste) 
        for gene in permuta:
            if random.random() < probability:
                muta = random.choice(liste)
                index1 = permuta.index(muta)
                index2 = permuta.index(gene)
                permuta[index1]= gene
                permuta[index2]= muta

        return permuta

    # making 1 child from two parenst        
    def crossover(par1,par2):
        child = []
        parent1 = list(par1) 
        parent2 = list(par2)
        
        # split is random whole slice from par1 and inserting it into child in order
        split = random.randint(1,len(parent1)-1)
        index = 0
        while index < split:
            child.append(parent1[index])
            index+=1
       
       # to make child a valid soulution all missing citys are then inserted in the order they apper in par2
        for gen in parent2:
            if gen not in child:
                child.append(gen)
    
        return child

    #selecting parents using a tournament 
    def p_select(pop,probability,num_tournament ,num_particepenc):
        selected_parenst = []
        
        # runs a number of tournament by selecting n number of particepenc from population at random
        for i in range(num_tournament):
            tournament = random.sample(pop, num_particepenc)


            #finding and adding the best solutions to a linup as we find them. 
            shortestkm = 0
            shortestur = []
            linup = []
            for permutasoner in tournament:
                sum = avstand(permutasoner,0,1)
                if sum < shortestkm or shortestkm==0:
                    shortestur=permutasoner
                    shortestkm = sum
                    linup.append(permutasoner)

            #adding the best winner of the tournement to pool of parents 
            selected_parenst.append(shortestur)

            p = probability
            found_gen = False

            #using probabilaty to append the winner of tournement but not always 
            for n in reversed(linup):
                if random.random() < p:
                    selected_parenst.append(n)
                    found_gen=True
                    break
                #the probabilaty is decrising 
                if p > probability/100:
                    p-= probability/100

            # there is a probabilaty that no winner is selected, if so we select one at random 
            if not found_gen:
                selected_parenst.append(random.choice(linup))

        return selected_parenst

    #natural selection 
    def select(pop,size_population):
        fittnes= {}
        survivals = []

        for n in pop:
            fittnes[avstand(n,0,1)]=n

        teller = 0
        #calculats the fittness in a list and sort it. adds the best indiv to the next generation 
        for i in sorted (fittnes.keys()) :  
            if teller < int(len(pop)/2):
                survivals.append(fittnes[i])
                teller +=1
            else:
                break
        # the rest of the survivers are selected at random 
        for i in range(size_population-int(len(pop)/2)):
            survivals.append(random.choice(pop))

        return survivals

    #uses crossover on parents selected at random 
    def reproduce(population,parets,num_children):
        next_gen = list(population)
        for i in range(num_children):
            index1= random.randint(0,len(parets)-1)
            index2= random.randint(0,len(parets)-1)
            next_gen.append(crossover(parets[index1],parets[index2]))

        return next_gen
 
    #main method that takes all arguments from user and combine all above functions to a GA 
    def evolution(num_citys,size_population,P_mutation,P_tournament,num_children,num_generation):

        #start with a population selected at random 
        population = permutasoner(num_citys,size_population)

        #generation runs recursivly with a counter
        def generation(pop,num_generation):
            #base case terminats the recursion 
            if(num_generation==0):
                return pop

            #we run mutasjon() on the whole population 
            mutated_population = []
            for indiv in pop:
                mutated_population.append(mutasjon(indiv,P_mutation))

            #we select parents from the mutated population 
            selected_par = p_select(mutated_population,P_tournament,30,20)

            #we make all children from selected parens and add them to the population 
            gen1= reproduce(mutated_population,selected_par,num_children)
            
            #we use select to choose survivers for next generation 
            selected_avkom = select(gen1,size_population)
           
           #recursiv call with num_generation-1
            return generation(selected_avkom,num_generation-1)

        #last generation 
        siste= generation(population,num_generation)
  
        #we evaluate the fittness of the last gen and return it in a list 
        resul = []
        for n in siste:
            resul.append(avstand(n,0,1))

        return resul 
       

start = time.time()
res = []
#using for range to run GA multiple times to account for randomness 
for i in range(20):
    resultat =evolution(24,50,0.05,0.7,25,100) 
    res.append(min(resultat))

end = time.time()

print(f"Runtime of the program is {end - start}")      
print("best =", min(res))

print("worst=",max(res))

print("mean=",statistics.mean(res)) 

print("deviant",statistics.stdev(res))       


