# advanced.py

def factoriel(n):
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs.")
    return 1 if n == 0 else n * factoriel(n - 1)

def power(base, exp):
    return base ** exp

def sqrt(n):
    if n < 0:
        raise ValueError("La racine carrée n'est pas définie pour les nombres négatifs.")
    return n ** 0.5
