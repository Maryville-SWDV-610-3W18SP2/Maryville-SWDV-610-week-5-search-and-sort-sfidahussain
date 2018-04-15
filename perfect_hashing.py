# Research perfect has functions. Using a list of names
# (classmates, family, etc. generate the hash values using
# the perfect hash algorithm.

def hash(list, tablesize):
    # Initializing hash table. I used a dictionary, setting each key through looping based on the tablesize, and setting each item intially to None
    # This idea was derived from:
    # https://docs.python.org/3/tutorial/datastructures.html
    # https://edhenry.github.io/2016/12/21/Hashing-in-Python/
    
    htable = dict([(i,None) for i,x in enumerate(range(tablesize))])
    
    # From the lecture: used ordinal hashing.
    sum = 0
    for name in list: 
        for pos in range(len(name)):
            sum = sum + ord(name[pos])
        # Assigns a hash value based on the sum of the ordinal hashing moding from the tablesize to fit in the hash table
        slot =  sum % tablesize
        # If there's nothing in that spot, place the name there. 
        if htable[slot] == None:
           htable[slot] = name
        # If there is something already in that spot, a collision occurs. 
        else:
            # Used linear probing. Go the next slot until a spot is open. 
            while htable[slot] != None:
                slot = slot + 1 % tablesize
                print('Collision occured with {0} now placing in slot {1}'.format(name, slot))
            htable[slot] = name
    return htable

def main():
    list = ['Suzy', 'Bo', 'Henry', 'V', 'Lee', 'Jimin']
    htable = hash(list, 11)
    print(htable)
    
main()
