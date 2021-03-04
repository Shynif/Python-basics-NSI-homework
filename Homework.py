# NOM : T
# Prénom : Antoine



# Exerice 1
def maxi(tab : list) -> tuple :
    """
    Fonction maxi prend une liste non vide comme argument.
    L'algorithme va créer une valeur maximale égale à la première valeur de la liste,
    puis va regarder pour chaque valeurs de la liste si la valeur est plus grande que
    la valeur maximale. à la fin la fonction retourne la valeur maximale.

    Argument : liste
    Retourne : tuple
    """
    
    assert len(tab) > 0, "Erreur : le tableau doit contenir au minimum 1 valeur"

    _id_ = 0
    _max = tab[0]

    for i in range(len(tab)) :
        if (tab[i] > _max) :
            _id_ = i
            _max = tab[i]

    return (_max, _id_)



# Exerice 2
def rechercheMinMax(tab : list) -> dict :
    """
    Fonction rechercheMinMax prend une liste non vide comme argument.
    L'algorithme va créer une valeur maximum et minimum égales à la première valeur de la liste,
    puis va regarder pour chaque valeurs de la liste si la valeur est plus grande/petite que
    la valeur maximum/minimum. à la fin la fonction retourne la valeur maximum et minimum.

    Argument : liste
    Retourne : dictionnaire
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



# Exercice 3
def recherche(tab : list, n : int) -> int :
    """
    Fonction recherche prend une liste non vide et un entier comme arguments.
    L'algorithme va créer une valeur égale à la longueur de la liste, puis va regarder 
    pour chaque valeurs de la liste si la valeur est égal à l'entier fournit en argument.
    à la fin la fonction retourne l'index où l'entier a été trouvé ou celle de la longueur
    de la liste.

    Arguments : liste et entier
    Retourne  : entier
    """

    assert len(tab) > 0, "Erreur : le tableau doit contenir au minimum 1 valeur"

    """
    Cette solution ne retourne pas la dernière occurence.
    Assez fourbe mais bien joué. Pas de cheese pour moi...

    if (not(n in tab)) :
        return len(tab)
    else :
        return tab.index(n)
    """
    
    _id = len(tab)

    for i in range(len(tab)) : 
        if (tab[i] == n) :
            _id = i
    
    return _id



# Exercice 4
def moyenne(tab : list) :
    """
    Fonction moyenne prend une liste non vide comme argument.
    L'algorithme va créer une valeur égale à 0 qui sera le total, puis va ajouter chaque 
    valeurs de la liste. à la fin la fonction retourne le total divisé par la longueur de
    la liste.

    Arguments : liste
    Retourne  : flotant
    """

    if (len(tab) == 0) :
        return "erreur"
    
    total = 0

    for i in tab :
        total += i
    
    return total/len(tab)



if __name__ == "__main__" :
    # Décommentez les lignes suivantes afin de tester vos fonctions

    # Exercice 1
    print(maxi([1,5,6,9,1,2,3,7,9,8]))
    
    # Exercice 2
    tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
    resultat = rechercheMinMax(tableau)
    print(resultat)
    tableau = []
    resultat = rechercheMinMax(tableau)
    print(resultat)

    # Exercice 3
    print(recherche([5, 3],1))
    print(recherche([2,4],2))
    print(recherche([2,3,5,2,4],2))

    # Exercice 4
    print(moyenne([1]))
    print(moyenne([1,2,3,4,5,6,7]))
    print(moyenne([1,2]))
