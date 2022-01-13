# Traveling salesman problem


## Problem
The traveling salesperson, wishing to disturb the residents of the major cities in some region of the world in
the shortest time possible, is faced with the problem of finding the shortest tour among the cities. A tour
is a path that starts in one city, visits all of the other cities, and then returns to the starting point. The
relevant pieces of information, then, are the cities and the distances between them. In this instance of the
TSP, a number of European cities are to be visited. Their relative distances are given in the data file, *european_cities.csv*,


## Exhaustive Search

Instructions on how to run the program.
```bash
$ pyhton exhaustive_search.py
```

In line 45 of exhaustive_search.py the user can input number of cities to be traveled



Shortest tour amongst first 10 Cities as calculated by exhaustive_search.py is as follows.
('Istanbul', 'Hamburg', 'Dublin', 'Copenhagen', 'Budapest', 'Bucharest', 'Brussels', 'Berlin', 'Belgrade',
'Barcelona')

7486.309999999999 km

Runtime of the program is 58.76999855041504
By plotting the time of calculation of the 10 first cites in GeoGebra regression we get the following
exponential function f(x) = 0 * 8.6661x. we can use this to approximate that TSP with 24 cites would
take 536109837922099 second or 16 988 658.5 years



## Hill Climbing

Instructions on how to run the program.

```bash
$ pyhton hill_climing.py
```

In line 82 the user can control how many neighbors can be checked. In line 43 the user controls the number of
cities and number of starting solutions. Loop in line 98 controls number of times to run the algorithm.

Run with 10 cities with 100 starting locations allowing 100 neighbored checks
best = 7486.309999999999
worst= 7486.3099999999995
mean= 7486.309999999999
deviant 4.4507076830049563e-13
Run with 24 cities with 2000 starting locations allowing 500 neighbored checks
best = 12679.23
worst= 12818.790000000003
mean= 12749.010000000002
deviant 98.68382238239678



## Genetic Algorithm

Instructions on how to run your program.

```bash
$ pyhton Genetic.py
```

```python
evolution(num_citys,size_population,P_mutation,P_tournament,num_children,num_generation):
```

the main function running the algorithm is evolution() taking the following parameters.it returns a
list of distances of all individuals in the last generation.

num_citys = number of cities we want to travel
size_population = the size of the population
P_mutation = probability of a random mutation to occur in any tour
P_tournament = probability that the winner of a given tournament gets picked to be a parent
num_children = number of children to be made
num_generation = number of generations a population gets to live.

Mutation works by looking at all cities in all solutions and with a probability swapping place of two
cites.

Crossover is used in making the child using two parents. A randomly sampled slice from parent1 is
inserted into child. The cities that are missing to make a child a valid solution is inserted one by one
in the order they are appearing in parent2.

P_select uses several tournaments to select the suitable parent from the population. The participants
in the tournament are selected at random. The winner of each is guaranteed to be a parent. But to
ensure more diversity we rank the winners and use a probabilistic function to select a parent. The
probability is constantly decreasing meaning that the higher ranked winners are more likely to be
selected as parents.

Reproduce then is used to applying crossover on two individuals from parents selected at random.
The children are then added back to the original population.

Select is used to choose the best individuals in the whole population to survive to the next
generation. Is operates like natural selection. It calculates the fitness and saves the best 50%
individuals to the next generation. The rest off the survivors are selected at random to ensure some
diversity in the solutions

Evolution combines the functions mentioned above into a GA and returnes the last Generation



An example run with the following arguments

```python
evolution(24,100,0.05,0.7,75,100)
```


I chose the following population sizes with all other parameters being the same. As with Hill Climbing
all algorithms are run 20 times to account for stochastic nature of the GA.

1. Pop_red = 50
2. Pop_green = 100
3. Pop_blue = 200

The following are the results with 24 cities with only pop_size being changed and number of children
to be produced being half the current population size. The graph below shows the runtime and performance.

```python
evolution(24, pop_size,0.05,0.7, pop_size/2,100)
```

| pop_name  | pop_size | best     | worst     | mean       | deviant    | time     |
|-----------|----------|----------|-----------|------------|------------|----------|
| pop_red   | 50       | 14777.14 | 17749.84  | 16132.9985 | 787.088712 | 60.5746  |
| pop_green | 100      | 12820.79 | 16416.100 | 14634.7530 | 999.26815  | 55.8320  |
| pop_blue  | 200      | 12325.93 | 15235.63  | 13748.163  | 954.26920  | 67.75002 |