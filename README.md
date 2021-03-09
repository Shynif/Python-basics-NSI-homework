# Python-basics-NSI-homework


Homework NSI - 20/02/2021

Langage : Python



**Ex 1 :**

On a une fonction maxi qui prend une liste non vide comme argument.
L'algorithme va créer une valeur maximale égale à la première valeur de la liste,
puis va regarder pour chaque valeurs de la liste si la valeur est plus grande que
la valeur maximale. à la fin la fonction retourne la valeur maximale et son index.

Argument : liste
Retourne : tuple

--------------------------------------

	Fonction maxi(tab) :    # La fonction prend une liste et retourne un tuple (l'index et la valeur)

	    Donne une erreur si le tableau est vide

	    Assigner 0 à la variable _id_                                       # L'index du maximum
	    Assigner la valeur à l'index 0 de la liste tab à la variable _max   # La valeur du maximum

	    Pour i allant de 0 à longueur de tab - 1 :                   # Inclus
		Si la valeur de tab à l'index i est supérieur à _max :   # Regarde si la valeur est supérieure
		    Assigner i à _id_                                    # Assigne l'index du nouveau maximum
		    Assigner la valeur de tab à l'index i à _max         # Assigne la nouvelle valeur maximum

	    Retourne un tuple avec _id_ et _max

--------------------------------------

Version Bis sans _max :

	Fonction maxi2(tab) : # La fonction prend une liste et retourne un tuple (l'index et la valeur)

	    Donne une erreur si le tableau est vide

	    Assigner 0 à la variable _id_

	    Pour i allant de 0 à longueur de tab - 1 : # Inclus
		Si la valeur de tab à l'index i est supérieur à la valeur de tab à l'index _id_ :
		    Assigner i à _id_

	    Retourne un tuple avec _id_ et la valeur de tab à l'index _id_







**Ex 2 :**

On a une fonction rechercheMinMax qui prend une liste comme argument.
L'algorithme va créer une valeur maximum et minimum égales à la première valeur de la liste,
puis va regarder pour chaque valeurs de la liste si la valeur est plus grande/petite que
la valeur maximum/minimum. à la fin la fonction retourne la valeur maximum et minimum.

Argument : liste
Retourne : dictionnaire

--------------------------------------

	Fonction rechercheMinMax(tab) : # La fonction prend une liste et retourne un dictionnaire

	    Si tab est vide :
		Retourne un dictionnaire avec None dans la catégorie "min" et None dans la catégorie "max"

	    Assigner la valeur à l'index 0 de la liste tab à la variable _min
	    Assigner la valeur à l'index 0 de la liste tab à la variable _max

	    Pour toutes les valeurs de tab nommées i :
		Si i est supérieur à _max :
		    Assigner i à _max
		Si i est inférieur à _min :
		    Assigner i à _min

	    Retourne un dictionnaire avec _min dans la catégorie "min" et _max dans la catégorie "max"







**Ex 3 :**

On a une fonction recherche qui prend une liste non vide et un entier comme arguments.
L'algorithme va créer une valeur égale à la longueur de la liste, puis va regarder 
pour chaque valeurs de la liste si la valeur est égal à l'entier fournit en argument.
à la fin la fonction retourne l'index où l'entier a été trouvé ou celle de la longueur
de la liste.

Arguments : liste et entier
Retourne  : entier

--------------------------------------

	Fonction recherche(tab, n) : # La fonction prend une liste et un entier et retourne un entier

	    Donne une erreur si le tableau est vide

	    Assigner la longueur de la liste à _id

	    Pour i allant de 0 à longueur de tab - 1 : # Inclus
		Si la valeur de tab à l'index i est égale à n :
		    Assigner i à _id

	    Retourne _id







**Ex 4 :**

On a une fonction moyenne qui prend une liste non vide comme argument.
L'algorithme va créer une valeur égale à 0 qui sera le total, puis va ajouter chaque 
valeurs de la liste. à la fin la fonction retourne le total divisé par la longueur de
la liste.

Arguments : liste
Retourne  : flotant

--------------------------------------

	Fonction moyenne(tab) : # La fonction prend une liste et retourne un nombre flotant

	    Si tab est vide :
		Retourne la chaîne de caractère "erreur"

	    Assigner 0 à total

	    Pour toutes les valeurs de tab nommées i :
		Ajouter i au total

	    Retourne le total divisé par la longueur de tab







**Ex 5 (Bonus ex 3 bis)**

Fonction faite sur mesure pour un tricheur.
Avec la sympathique aide de Nico du studio Eko pour le i++.

--------------------------------------

	Fonction recherche(tab, n) : # La fonction prend une liste et un entier et retourne un entier

	    Donne une erreur si le tableau est vide

	    Assigner la longueur de la liste à id_
	    Assigner Faux à fin
	    Assigner 0 à i

	    Tant que fin est égal à Faux :
		Si i est supérieur ou égal à la longueur de tab : # Si i est à la fin de la liste
			Assigner Vrai à fin                       # Sort de la boucle
		Sinon :
			Si la valeur de tab à l'indice i est égal à n :
				Assigner i à id_  # Actualise le dernier/premier n trouvé
			Ajouter 1 à i             # Continu vers le prochain élément de la liste

	    Retourne id_

--------------------------------------

Comment ajouter 1 de façon rigolote ?
XOR + modulo 2 = i++ !

i=(i^7876^7877)+2*(i%2!=0)

- i^7876^7877 : 
En évitant les détails, ici ce XOR avec 3 arguments retourne i+1 quand i est pair et i-1 quand i est impair

- 2*(i%2!=0) : 
Avec ce modulo 2 on a 2\*0 quand i est pair et 2\*1 quand i est impair

- (i^7876^7877)+2*(i%2!=0) : 
Donc quand i est pair on a i+1 + 2\*0 = i+1, et quand i est impair on a i-1 + 2\*1 = i+1

Nous avons donc toujours i += 1



