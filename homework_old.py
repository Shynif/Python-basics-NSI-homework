# Welcome to this simple python project

import random as r
test = [r.randrange(-100, 100) for i in range(100)]
print(test)

def maxi(tab : list) -> tuple :
    """
    Description ici
    """
    
    assert len(tab) > 0, "Erreur : le tableau doit contenir au minimum 1 valeur"

    _id_ = 0
    _max = tab[0]

    for i in range(len(tab)) :
        if (tab[i] > _max) :
            _id_ = i
            _max = tab[i]

    return (_max, _id_)

#print("\n")
#print(maxi(test))
#print("vérification :", max(test))


def RechercheMinMax(tab : list) -> dict :
    """
    Description here
    """

    if (len(tab) == 0) :
        return {"min" : None, "max" : None}

    _min = tab[0]
    _max = tab[0]

    for i in tab :
        if (i > _max) :
            _max = i
        if (i < _min) :
            _min = i
    
    return {"min" : _min, "max" : _max}

#print("\n")
#print(RechercheMinMax(test))
#print("vérification :", {"min" : min(test), "max" : max(test)})
#print(RechercheMinMax([]))


"""def recherche(tab : list, n : int) -> int :
    
    Description here

    assert len(tab) > 0, "Erreur : le tableau doit contenir au minimum 1 valeur"

    _id = len(tab)

    for i in range(len(tab)) : 
        if (tab[i] == n) :
            _id = i
    
    print(_id)"""

def recherche(tab, n) :
    
    


#print("\n")
print(recherche(test, 50))


def moyenne(tab : list) :
    """
    Description here
    """

    if (len(tab) == 0) :
        print("erreur")
        return None
    
    total = 0

    for i in tab :
        total += i
    
    print(total/len(tab))

#print("\n")
#moyenne(test)
#moyenne([])