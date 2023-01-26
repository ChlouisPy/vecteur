# vecteur
Implémentation de vecteurs en Python
Support des vecteur en 2 et 3 dimensions.

# Installation 

### Etape 1 : Récupération
Téléchargez vecteur, et ouvre l'archive

### Etape 2 : Ajout dans un script 
Selectionnez le dossier ou se trouve votre script Python qui va nécéssiter le module vecteur. Glissez y le fichier `vecteur.py`.

### Etape 3 : Import dans le script 

```python
from vecteur import Vecteur
```

# Documentation 

## Creation d'un vecteur 

### Vecteur à 2 dimensions :
Méthode 1 :
```python
u = Vecteur(2, 3)
```

Méthode 2 :
```python
v = Vecteur(x=2, y=3)
```

### Vecteurs à 3 dimensions :
Méthode 1 :
```python
u = Vecteur(2, 3, 5)
```

Méthode 2 :
```python
v = Vecteur(x=2, y=3, z=5)
```

### Remarque :

`x`, `y` et `z` peuvent être des flotants, des entiers ou des fraction (Via le module `fraction` de Python) 

## Propriétés sur les vecteurs 
Dans toute cette partie on prendra `u` et `v` deux vecteurs 

### Norme d'un vecteur 

```python
norme_de_u = u.norme
```

### Angle d'un vecteur par rapport à un autre vecteur/un axe :

Par rapport à un autre vecteur :

```python
angle_uv = u.angle(v)
```

Par rapport à un axe :
```python
u_angle_x = u.angle("x")
u_angle_y = u.angle("y")
u_angle_z = u.angle("z")
```

Remarque : 
Les angles sont en radian 

### Vecteur sour forme complexe 
Méthode 1 :
```python
z_u = u.complexe
```

Méthode 2:
```python
z_u = complex(u)  # fonction python de base 
```

Remarque :
Cette fonction ne fonctionne qu'avec des vecteurs en 2 dimensions 

### Nombre de dimensions du vecteur 
```python
u_dim = u.dimension # 2 ou 3
```

### Coordonées d'un vecteur 
Méthode 1 :
```python
u_x = u.x
u_y = u.y
u_z = u.z
```

Méthode 2 :
```python
u_coord = u.coord # u_coord = (x, y, z)
```

## Operations sur les vecteurs 

### Addition :
Méthode 1:
```python
w = u + v
```

Méthode 2 :
```python
u += v
```

### Soustration :
Méthode 1:
```python
w = u - v
```

Méthode 2 :
```python
u -= v
```

### Produit scalaire :
```python
x = u * v
```

### Multiplication par un réel :
Méthode 1 :
```python
a = 5.3

x = u * 5.3
```
Méthode 2 :
```python
a = 5.3

u *= 5.3
```

### Produit vecttoriel :
```python
w = u ^ v
```

Remarque : 
Le produit vectoriel ne fonctionne qu'avec des vecteurs en 3 dimensions 
Le produit vectoriel ne fonctionne pas avec des fraction et utilise le module NumPy

### Vecteur négatif :
```python
w = -u
```

### Egalité entre deux vecteurs :
```python
u == v # True/False
```

### Vecteurs collinéaires 
```python
u // v # True/False
```

### Vecteurs orthogonaux :
```python
u & v # True/False
```

### Arrondi de vecteur 
```python
u = round(u, nd) # avec nd un nombre de décimale 
```
*Arrondie toutes les coordonées du vecteur*

Remarque : 
Cette fonction n'a aucune rigueure mathématique. Elle n'est présente que pour simplifier certains calculs 
