#############################################################################


#############################################################################

a = 1
b = 2

(a, b) = (b, a)
#a, b = b, a    # equivalent to above line
#a, b = (b, a)  # equivalent to above line
#(a, b) = b, a   # equivalent to above line
#print(a, b)


############## Assigning tuple variable to ##########################################

#julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

#name, surname, birth_year, movie, movie_year, profession, birth_place = julia

#############################################################################




############## Tuple Unpacking in FOR loop ##########################################

#authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
#for first_name, last_name in authors:
#for (first_name, last_name) in authors:      #equivalent to above line
#    print("first name:", first_name, "last name:", last_name)


#############################################################################



################### Enumerate Object ####################################

#fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

#for item in enumerate(fruits):
#    print(item[0], item[1])

#############################################################################


######################### Unpacking Tuples ###################################

#def add(x, y):
#    return x + y

#print(add(3, 4))
#z = (5, 4)
#print(add(*z)) # this line will cause the values to be unpacked
#############################################################################



def stop_at_four(lst1):
    idx =0
    new_lst=[]
    while idx < len(lst1):
        if lst1[idx] !=4:
            new_lst.append(lst1[idx])
        else:
            return new_lst
        if lst1[idx]==lst1[-1]:
            #new_lst.append(lst1[idx])
            return new_lst
        idx=idx+1


cityNames = ['Detroit', 'Ann Arbor', 'Pitts', 'Mars', 'NYC']
populations = [4568575, 5889746, 4886526, 5846235, 4782965]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = zip(cityNames, populations, states)

class City:
    def __init__(self, n, p, s):
        self.name = n
        self.population = p
        self.state = s
    def __str__(self):
        return '{}, {} (pop: {})'.format(self.name, self.state, self.populatio)

cities = []
for city_tup in city_tuples:
    name, pop, state = city_tup
    city = City(name, pop, state) #instance of City class
    cities.append(city)  # create a list of City objects

# Another way of doing the same thing

##cities = [City(*city_tup) for city_tup in city_tuples]

#################  OR #################################

##cities = [City(n,p,s) for (n,p,s) in city_tuples]

print(cities)
