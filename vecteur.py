"""
Ce module python contient toutes les fonctions pour les vecteurs
"""
from fractions import Fraction
from math import acos
from math import ceil
from math import floor

import numpy as np


class Vecteur:
    __name__: str = "Vecteur"
    __module__: str = "vecteur"
    __doc__: str = """
    Module Vecteur 
    Documentation pour la class Vecteur :
    
    Implémentation des vecteurs en Python
    Support des vecteur en 2 et 3 dimensions
    
    ##  Initialisation de vecteurs :
    
     - Vecteur à deux dimensions :
        
        u = Vecteur(2, 3)
        &
        v = Vecteur(x=2, y=3)
        
    - Vecteur à trois dimensions :
        
        u = Vecteur(1, 5, 3)
        &
        v = Vecteur(x=1, y=5, z=3)
         
    - Remarque :
    
        x, y, z peuvent être des int, float, ou des fraction (via le module fraction [import fraction]) 
    
    ## Propriété sur les vecteurs 
    
    - Norme du vecteur :
    
        u_norme = u.norme
    
    - Angle du vecteur par rapport à ...:
        
        Par rapport à un axe :

            u_angle_x = u.angle("x")
            u_angle_y = u.angle("y")
            u_angle_z = u.angle("z")
        
        Par rapport à un autre vecteur :
            
            u_angle_v = u.angle(v)
    
        Remarque : les angles sont en Radian
        
    - Vecteur sous forme complexe :
        
        # Uniquement pour les vecteurs 2D
        
        z_u = u.complexe
        &
        z_u = complex(u)  # fonction python de base 
    
    - Nombre de dimension du vecteur :
        
        u_dim = u.dimension # 2 ou 3
    
    - Coordonnées du vecteur :
        
        u_x = u.x
        u_y = u.y
        u_z = u.z
        
        u_coord = u.coord # u_coord = (x, y, z)
    
    ## Operation 
    
        - Addition :
        
            w = u + v
            
            u += v
        
        - Soustraction :
        
            u - v = w
            
            u -= v
        
        - Produit scalaire :
            
            u * v = x
        
        - Produit par un réel :
            
            5 * u = w
            
            u *= 5
            5 *= u
        
        - Produit vectoriel (uniquement pour les vecteurs 3 dimensions) :
        
            u ^ v = w
        
        - Vecteur négatif :
            
            -u = w
        
        - Égalité de vecteur :
            
            u == v # True ou False (Les vecteurs doivent être parfaitement identique)
            
        - Si deux vecteurs sont colinéaires :
        
            u // v # True ou False
        
        - Si deux vecteur sont orthogonaux 
            
            u & v # True ou False
        
        - Arrondi du vecteur 
            # operation peu rigoureuse mais utile 
            
            u = round(u, nd) # avec nd un nombre de décimale 
            
            Exemple :
                
                u = Vecteur(0.1237, 0.56, 5)
                
                >>> round(u, 2)
                (0.12, 0.56, 5.0)
                >> round(u)
                (0, 1, 5)
            
            Les fonction Floor et Ceil du module math sont aussi prisent en compte 
        
    ## Propriétés autres :
    
    - On peut parfaitement print() un Vecteur 
    """

    def __init__(self, x, y, z=None) -> None:
        """
        :param x: Coordonnée en x du vecteur
        :param y: Coordonnée en y du vecteur
        :param z: (optionnelle) Coordonnée en z du vecteur
        """

        # gestion des erreurs pour les vecteurs
        if not isinstance(x, int) and not isinstance(x, float) and not isinstance(x, Fraction):
            raise TypeError("Vecteur ne prend que des int, float ou fraction en valeur pour leur coordonnée en x.")

        if not isinstance(y, int) and not isinstance(y, float) and not isinstance(y, Fraction):
            raise TypeError("Vecteur ne prend que des int, float ou fraction en valeur pour leur coordonnée en y.")

        if z is not None and (not isinstance(z, int) and not isinstance(z, float) and not isinstance(z, Fraction)):
            raise TypeError("Vecteur ne prend que des int, float ou fraction en valeur pour leur coordonnée en z.")

        # creation des variables pour le vecteur
        self.x = x
        self.y = y

        if z is not None:
            self.z = z
            self.dim: int = 3

        else:
            self.z = None
            self.dim: int = 2

    # Toutes les propriétés du vecteur
    @property
    def norme(self):
        """
        Cette fonction retourne la norme du vecteur
        :return: sqrt(x ** 2 + y ** 2 [+ z ** 2])
        """
        if self.dim == 2:
            return (self.x ** 2 + self.y ** 2) ** 0.5

        else:
            return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    @property
    def dimension(self):
        """
        Return la dimension du vecteur
        :return: La dimension du vecteur
        """
        return self.dim

    @property
    def coord(self) -> tuple:
        """
        :return: les coordonnées du vecteur au format Tuple
        """
        if self.dim == 2:
            return self.x, self.y

        else:
            return self.x, self.y, + self.z

    def angle(self, other):
        """
        Cette fonction retourne l'angle entre un axe ou un vecteur et le vecteur self
        :param other: Un vecteur OU "x" ; "y" ; "z"
        :return: l'angle entre les deux element.
        """

        if isinstance(other, str):

            if other == "z" and self.dim == 2:
                raise Exception("Un vecteur en 2 dimensions n'admet pas un axe z")

            if self.dim == 2:
                dic_axe: dict = {"x": Vecteur(1, 0), "y": Vecteur(0, 1)}

                return acos((self * dic_axe[other]) / (self.norme * dic_axe[other].norme))

            else:

                dic_axe: dict = {"x": Vecteur(1, 0, 0), "y": Vecteur(0, 1, 0), "z": Vecteur(0, 0, 1)}

                return acos((self * dic_axe[other]) / (self.norme * dic_axe[other].norme))

        elif isinstance(other, Vecteur):
            if other.dimension == self.dimension:
                return acos((self * other) / (self.norme * other.norme))

            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")

        else:
            raise TypeError("L'angle ne peut se faire qu'entre deux vecteurs ou un axe")

    # operation

    def __add__(self, other):
        """
        Addition de vecteur
        """
        if isinstance(other, Vecteur):
            if other.dimension == self.dimension:

                if self.dim == 2:
                    return Vecteur(other.x + self.x, other.y + self.y)
                else:
                    return Vecteur(other.x + self.x, other.y + self.y, other.z + self.z)

            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")
        else:
            raise TypeError("Seuls les vecteurs peuvent être additionné ensemble")

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        """
        Produit scalaire de vecteur
        """
        if isinstance(other, Vecteur):
            if other.dimension == self.dimension:

                if self.dim == 2:
                    return other.x * self.x + other.y * self.y
                else:
                    return other.x * self.x + other.y * self.y + other.z * self.z

            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")

        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction):
            if self.dim == 2:
                return Vecteur(other * self.x, other * self.y)
            else:
                return Vecteur(other * self.x, other * self.y, other * self.z)
        else:
            raise TypeError("Produit seulement supporté pour v * u ou <int/float/Fraction> * u")

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        """
        Négatif du vecteur
        """
        return self * (-1)

    def __pos__(self):
        """
        Positif du vecteur
        """
        return self

    def __sub__(self, other):
        """
        Soustraction
        """
        return self.__add__(other.__neg__())

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __xor__(self, other):
        """
        Produit vectoriel
        """
        if isinstance(other, Vecteur):
            if other.dimension == self.dimension:
                if self.dim == 3:

                    vec1: np.array = np.array([self.x, self.y, self.z], dtype=float)
                    vec2: np.array = np.array([other.x, other.y, other.z], dtype=float)

                    vec_prod = np.cross(vec1, vec2)

                    return Vecteur(vec_prod[0], vec_prod[1], vec_prod[2])

                else:
                    raise TypeError("Les deux vecteurs doivent être en 3 dimensions")
            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")
        else:
            raise TypeError("Seuls les vecteurs peuvent être multipliés entre eux")

    # comparaison

    def __eq__(self, other) -> bool:
        """
        Égalité entre deux vecteurs
        :param other: Autre vecteur à comparer
        :return: True sir les vecteurs sont identiques ou False s'ils ne se sont pas
        """
        if isinstance(other, Vecteur):
            if other.dimension == self.dimension:

                if self.dim == 2:
                    return other.x == self.x and other.y == self.y
                else:
                    return other.x == self.x and other.y == self.y and other.z == self.z

            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")
        else:
            raise TypeError("Seuls les vecteurs peuvent être comparés")

    # vecteur orthogonal
    def __floordiv__(self, other):
        """
        Vecteur orthogonal
        """
        if isinstance(other, Vecteur):
            if other.dimension == self.dimension:
                return self * other == 0
            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")
        else:
            raise TypeError("Seuls les vecteurs peuvent être comparés")

    # vecteur colinéaire
    def __or__(self, other):
        if isinstance(other, Vecteur):
            if other.dimension == self.dimension:
                if self.dim == 2:
                    return self.x / other.x == self.y / other.y
                else:
                    return self.x / other.x == self.y / other.y and self.y / other.y == self.z / other.z
            else:
                raise TypeError("Les deux vecteurs doivent être de même dimension")
        else:
            raise TypeError("Seuls les vecteurs peuvent être comparés")

    # transformation
    def __str__(self) -> str:
        """
        Donne le vecteur sous le format d'un string
        :return: String du vecteur : (x y z)
        """
        if self.dim == 2:
            return f"({self.x} {self.y})"
        else:
            return f"({self.x} {self.y} {self.z})"

    def __repr__(self) -> str:
        return self.__str__()

    def __format__(self, format_spec) -> str:
        return self.__str__()

    def __complex__(self) -> complex:
        """
        Retourne le vecteur sous forme d'un complexe
        :return: x + yi
        """
        if self.dim == 2:
            return self.x + 1j * self.y

        else:
            raise Exception("Seul les vecteur à deux dimension peuvent être transformé en complexe")

    def __floor__(self):
        """
        Applique la fonction floor à toutes les coordonnées du vecteur
        :return: Le vecteur au format avec ses valeurs en entier.
        """
        x, y = floor(self.x), floor(self.y)

        if self.dim == 3:
            z = floor(self.z)
            return Vecteur(x, y, z)

        return Vecteur(x, y)

    def __ceil__(self):
        """
        Applique la fonction ceil à toutes les coordonnées du vecteur
        :return: Le vecteur au format avec ses valeurs en entier.
        """

        x, y = ceil(self.x), ceil(self.y)

        if self.dim == 3:
            z = ceil(self.z)
            return Vecteur(x, y, z)

        return Vecteur(x, y)

    def __round__(self, n=None):
        """
        Arrondie les valeurs des vecteurs
        :param n:
        :return:
        """
        x, y = round(self.x, n), round(self.y, n)

        if self.dim == 3:
            z = round(self.z, n)
            return Vecteur(x, y, z)

        return Vecteur(x, y)


if __name__ == '__main__':
    u = Vecteur(1, 2, 3)
    v = Vecteur(4, 5, 6)

    print(u ^ v)
