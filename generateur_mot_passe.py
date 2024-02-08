import random

#Demander à l'utilisateur de saisir la longueur du MDP
longpass=int(input('donner la longeur du mot de passe '))

#La liste des lettres, chiffres et symboles à randomiser
s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-.:;<=>?@^_`{|}~'

#Regrouper les caractères aléatoires en 1 seul mot
password="".join(random.sample(s,longpass))
print(password)