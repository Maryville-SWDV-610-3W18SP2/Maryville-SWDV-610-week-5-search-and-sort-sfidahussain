# Research perfect has functions. Using a list of names
# (classmates, family, etc. generate the hash values using
# the perfect hash algorithm.

def hash(list, tablesize):
    htable = dict([(i,None) for i,x in enumerate(range(tablesize))])
    sum = 0
    for name in list: 
        for pos in range(len(name)):
            sum = sum + ord(name[pos])
        slot =  sum % tablesize
        if htable[slot] == None:
           htable[slot] = name
        else:
            while htable[slot] != None:
                slot = slot + 1 % tablesize
            htable[slot] = name
    return htable

def main():
    list = ['Suzy', 'Bo', 'Henry', 'V', 'Lee', 'Jimin']
    htable = hash(list, 11)
    print(htable)
    
main()
