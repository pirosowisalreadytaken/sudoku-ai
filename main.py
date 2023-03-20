#Import Random 
import random

import time

start = time.time()

essais = 0

j = True

k = True

reponse = True

choix_init = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

test = 0

nb_essais = 0

a_pas_possible = 999

b_pas_possible = 999

c_pas_possible = 999

d_pas_possible = 999

e_pas_possible = 999

f_pas_possible = 999

g_pas_possible = 999

h_pas_possible = 999

i_pas_possible = 999

j_pas_possible = 999

n = 0

nombres = 0

#Les listes qui font le plateau
colonne1 = "/ / /  / / /  / / /"
colonne2 = "/ / /  / / /  / / /"
colonne3 = "/ / /  / / /  / / /"

colonne4 = "/ / /  / / /  / / /"
colonne5 = "/ / /  / / /  / / /"
colonne6 = "/ / /  / / /  / / /"

colonne7 = "/ / /  / / /  / / /"
colonne8 = "/ / /  / / /  / / /"
colonne9 = "/ / /  / / /  / / /"

apaspossible = 9

def peut_jouer(colo, rangée, number):
  global reponse
  reponse = True
  if colo == "i":
    for v in range(len(colonne9)):
      if colonne9[v] == str(number):
        reponse = False
  elif colo == "a":
    for v in range(len(colonne1)):
      if colonne1[v] == str(number):
        reponse = False
  elif colo == "b":
    for v in range(len(colonne2)):
      if colonne2[v] == str(number):
        reponse = False
  elif colo == "c":
    for v in range(len(colonne3)):
      if colonne3[v] == str(number):
        reponse = False
  elif colo == "d":
    for v in range(len(colonne4)):
      if colonne4[v] == str(number):
        reponse = False
  elif colo == "e":
    for v in range(len(colonne5)):
      if colonne5[v] == str(number):
        reponse = False
  elif colo == "f":
    for v in range(len(colonne6)):
      if colonne6[v] == str(number):
        reponse = False
  elif colo == "g":
    for v in range(len(colonne7)):
      if colonne7[v] == str(number):
        reponse = False
  elif colo == "h":
    for v in range(len(colonne8)):
      if colonne8[v] == str(number):
        reponse = False

  
  if not colo == "a":
    if colonne1[rangée] == str(number):
      reponse = False
  
  if not colo == "b":
    if colonne2[rangée] == str(number):
      reponse = False
      
  if not colo == "c":
    if colonne3[rangée] == str(number):
      reponse = False

  if not colo == "d":
    if colonne4[rangée] == str(number):
      reponse = False

  if not colo == "e":
    if colonne5[rangée] == str(number):
      reponse = False

  if not colo == "f":
    if colonne6[rangée] == str(number):
      reponse = False

  if not colo == "g":
    if colonne7[rangée] == str(number):
      reponse = False

  if not colo == "h":
    if colonne8[rangée] == str(number):
      reponse = False

  if not colo == "i":
    if colonne9[rangée] == str(number):
      reponse = False


  if colo == "a" and rangée == 0 or colo == "a" and rangée == 2 or colo == "a" and rangée == 4 or colo == "b" and rangée == 0 or colo == "b" and rangée == 2 or colo == "b" and rangée == 4 or colo == "c" and rangée == 0 or colo == "c" and rangée == 2 or colo == "c" and rangée == 4:
    if colonne1[0] == str(number) or colonne1[2] == str(number) or colonne1[4] == str(number) or colonne2[0] == str(number) or colonne2[2] == str(number) or colonne2[4] == str(number) or colonne3[0] == str(number) or colonne3[2] == str(number) or colonne3[4] == str(number):
      reponse = False

  elif colo == "a" and rangée == 7 or colo == "a" and rangée == 9 or colo == "a" and rangée == 11 or colo == "b" and rangée == 7 or colo == "b" and rangée == 9 or colo == "b" and rangée == 11 or colo == "c" and rangée == 7 or colo == "c" and rangée == 9 or colo == "c" and rangée == 11:
    if colonne1[7] == str(number) or colonne1[9] == str(number) or colonne1[11] == str(number) or colonne2[7] == str(number) or colonne2[9] == str(number) or colonne2[11] == str(number) or colonne3[7] == str(number) or colonne3[9] == str(number) or colonne3[11] == str(number):
      reponse = False

  elif colo == "a" and rangée == 14 or colo == "a" and rangée == 16 or colo == "a" and rangée == 18 or colo == "b" and rangée == 14 or colo == "b" and rangée == 16 or colo == "b" and rangée == 18 or colo == "c" and rangée == 14 or colo == "c" and rangée == 16 or colo == "c" and rangée == 18:
    if colonne1[14] == str(number) or colonne1[16] == str(number) or colonne1[18] == str(number) or colonne2[14] == str(number) or colonne2[16] == str(number) or colonne2[18] == str(number) or colonne3[14] == str(number) or colonne3[16] == str(number) or colonne3[18] == str(number):
      reponse = False

  elif colo == "d" and rangée == 0 or colo == "d" and rangée == 2 or colo == "d" and rangée == 4 or colo == "e" and rangée == 0 or colo == "e" and rangée == 2 or colo == "e" and rangée == 4 or colo == "f" and rangée == 0 or colo == "f" and rangée == 2 or colo == "f" and rangée == 4:
    if colonne4[0] == str(number) or colonne4[2] == str(number) or colonne4[4] == str(number) or colonne5[0] == str(number) or colonne5[2] == str(number) or colonne5[4] == str(number) or colonne6[0] == str(number) or colonne6[2] == str(number) or colonne6[4] == str(number):
      reponse = False

  elif colo == "d" and rangée == 7 or colo == "d" and rangée == 9 or colo == "d" and rangée == 11 or colo == "e" and rangée == 7 or colo == "e" and rangée == 9 or colo == "e" and rangée == 11 or colo == "f" and rangée == 7 or colo == "f" and rangée == 9 or colo == "f" and rangée == 11:
    if colonne4[7] == str(number) or colonne4[9] == str(number) or colonne4[11] == str(number) or colonne5[7] == str(number) or colonne5[9] == str(number) or colonne5[11] == str(number) or colonne6[7] == str(number) or colonne6[9] == str(number) or colonne6[11] == str(number):
      reponse = False

  elif colo == "d" and rangée == 14 or colo == "d" and rangée == 16 or colo == "d" and rangée == 18 or colo == "e" and rangée == 14 or colo == "e" and rangée == 16 or colo == "e" and rangée == 18 or colo == "f" and rangée == 14 or colo == "f" and rangée == 16 or colo == "f" and rangée == 18:
    if colonne4[14] == str(number) or colonne4[16] == str(number) or colonne4[18] == str(number) or colonne5[14] == str(number) or colonne5[16] == str(number) or colonne5[18] == str(number) or colonne6[14] == str(number) or colonne6[16] == str(number) or colonne6[18] == str(number):
      reponse = False

  elif colo == "g" and rangée == 0 or colo == "g" and rangée == 2 or colo == "g" and rangée == 4 or colo == "h" and rangée == 0 or colo == "h" and rangée == 2 or colo == "h" and rangée == 4 or colo == "i" and rangée == 0 or colo == "i" and rangée == 2 or colo == "i" and rangée == 4:
    if colonne7[0] == str(number) or colonne7[2] == str(number) or colonne7[4] == str(number) or colonne8[0] == str(number) or colonne8[2] == str(number) or colonne8[4] == str(number) or colonne9[0] == str(number) or colonne9[2] == str(number) or colonne9[4] == str(number):
      reponse = False

  elif colo == "g" and rangée == 7 or colo == "g" and rangée == 9 or colo == "g" and rangée == 11 or colo == "h" and rangée == 7 or colo == "h" and rangée == 9 or colo == "h" and rangée == 11 or colo == "i" and rangée == 7 or colo == "i" and rangée == 9 or colo == "i" and rangée == 11:
    if colonne7[7] == str(number) or colonne7[9] == str(number) or colonne7[11] == str(number) or colonne8[7] == str(number) or colonne8[9] == str(number) or colonne8[11] == str(number) or colonne9[7] == str(number) or colonne9[9] == str(number) or colonne9[11] == str(number):
      reponse = False

  elif colo == "g" and rangée == 14 or colo == "g" and rangée == 16 or colo == "g" and rangée == 18 or colo == "h" and rangée == 14 or colo == "h" and rangée == 16 or colo == "h" and rangée == 18 or colo == "i" and rangée == 14 or colo == "i" and rangée == 16 or colo == "i" and rangée == 18:
    if colonne7[14] == str(number) or colonne7[16] == str(number) or colonne7[18] == str(number) or colonne8[14] == str(number) or colonne8[16] == str(number) or colonne8[18] == str(number) or colonne9[14] == str(number) or colonne9[16] == str(number) or colonne9[18] == str(number):
      reponse = False
  return reponse

  
#les possibilites de collones
choix = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

#Fonction Pour le Plateau
def joue(colonne, rangee, nb):
#Modifier les variables qui font le plateau
  c = ""
  global colonne1
  global colonne2
  global colonne3
  global colonne4
  global colonne5
  global colonne6
  global colonne7
  global colonne8
  global colonne9
  global reponse
  global essais
  global nb_essais
  global test
  global colonnee
  global n
  global nombres

  colonnee = random.choice(choix)

  test = random.randint(1, 9)

  if int(test) == 1:
    test = 0
  elif test == 2:
    test = 2
  elif test == 3:
    test = 4
  elif test == 4:
    test = 7
  elif test == 5:
    test = 9
  elif test == 6:
    test = 11
  elif test == 7:
    test = 14
  elif test == 8:
    test = 16
  elif test == 9:
    test = 18


  #verifie si il peut vraimnt jouer
  if peut_jouer(colonne, rangee, nb) == True:
    #changer la bonne colonnes et la bonne lettre
    if colonne == "a":
      colonne1 = list(colonne1)
      colonne1[int(rangee)] = int(nb)
      for y in range(len(colonne1)):
        c += str(colonne1[y])
      colonne1 = c
    elif colonne == "b":
      colonne2 = list(colonne2)
      colonne2[int(rangee)] = int(nb)
      for y in range(len(colonne2)):
        c += str(colonne2[y])
      colonne2 = c
    elif colonne == "c":
      colonne3 = list(colonne3)
      colonne3[int(rangee)] = int(nb)
      for y in range(len(colonne3)):
        c += str(colonne3[y])
      colonne3 = c
    elif colonne == "d":
      colonne4 = list(colonne4)
      colonne4[int(rangee)] = int(nb)
      for y in range(len(colonne4)):
        c += str(colonne4[y])
      colonne4 = c
    elif colonne == "e":
      colonne5 = list(colonne5)
      colonne5[int(rangee)] = int(nb)
      for y in range(len(colonne5)):
        c += str(colonne5[y])
      colonne5 = c
    elif colonne == "f":
      colonne6 = list(colonne6)
      colonne6[int(rangee)] = int(nb)
      for y in range(len(colonne6)):
        c += str(colonne6[y])
      colonne6 = c
    elif colonne == "g":
      colonne7 = list(colonne7)
      colonne7[int(rangee)] = int(nb)
      for y in range(len(colonne7)):
        c += str(colonne7[y])
      colonne7 = c
    elif colonne == "h":
      colonne8 = list(colonne8)
      colonne8[int(rangee)] = int(nb)
      for y in range(len(colonne8)):
        c += str(colonne8[y])
      colonne8 = c
    elif colonne == "i":
      colonne9 = list(colonne9)
      colonne9[int(rangee)] = int(nb)
      for y in range(len(colonne9)):
        c += str(colonne9[y])
      colonne9 = c


    

    #afficher le plateau
    if essais == n + 10:
      print(f"    Essais {essais} \n")
      print("   1 2 3  4 5 6  7 8 9 \n")
      print(f"a  {colonne1} \nb  {colonne2} \nc  {colonne3} \n \nd  {colonne4} \ne  {colonne5} \nf  {colonne6}\n \ng  {colonne7} \nh  {colonne8} \ni  {colonne9} \n")
      n = essais
    essais += 1
  else:
    if nombres == 10:
      if random.randint(1, 2) == 1:
        if colonne == "a":
          if not int(test) == a_pas_possible:
            colonne1 = list(colonne1)
            colonne1[int(test)] = "/"
            for y in range(len(colonne1)):
              c += str(colonne1[y])
            colonne1 = c
        elif colonne == "b":
          if not int(test) == b_pas_possible:
            colonne2 = list(colonne2)
            colonne2[int(test)] = "/"
            for y in range(len(colonne2)):
              c += str(colonne2[y])
            colonne2 = c
        elif colonne == "c":
          if not int(test) == c_pas_possible:
            colonne3 = list(colonne3)
            colonne3[int(test)] = "/"
            for y in range(len(colonne3)):
              c += str(colonne3[y])
            colonne3 = c
        elif colonne == "d":
          if not int(test) == d_pas_possible:
            colonne4 = list(colonne4)
            colonne4[int(test)] = "/"
            for y in range(len(colonne4)):
              c += str(colonne4[y])
            colonne4 = c
        elif colonne == "e":
          if not int(test) == e_pas_possible:
            colonne5 = list(colonne5)
            colonne5[int(test)] = "/"
            for y in range(len(colonne5)):
              c += str(colonne5[y])
            colonne5 = c
        elif colonne == "f":
          if not int(test) == f_pas_possible:
            colonne6 = list(colonne6)
            colonne6[int(test)] = "/"
            for y in range(len(colonne6)):
              c += str(colonne6[y])
            colonne6 = c
        elif colonne == "g":
          if not int(test) == g_pas_possible:
            colonne7 = list(colonne7)
            colonne7[int(test)] = "/"
            for y in range(len(colonne7)):
              c += str(colonne7[y])
            colonne7 = c
        elif colonne == "h":
          if not int(test) == h_pas_possible:
            colonne8 = list(colonne8)
            colonne8[int(test)] = "/"
            for y in range(len(colonne8)):
              c += str(colonne8[y])
            colonne8 = c
        elif colonne == "i":
          if not int(test) == i_pas_possible:
            colonne9 = list(colonne9)
            colonne9[int(test)] = "/"
            for y in range(len(colonne9)):
              c += str(colonne9[y])
            colonne9 = c
        nombres = 0
      else:
        if colonnee == "a":
          if not int(test) == a_pas_possible:
            colonne1 = list(colonne1)
            colonne1[int(test)] = "/"
            for y in range(len(colonne1)):
              c += str(colonne1[y])
            colonne1 = c
        elif colonnee == "b":
          if not int(test) == b_pas_possible:
            colonne2 = list(colonne2)
            colonne2[int(test)] = "/"
            for y in range(len(colonne2)):
              c += str(colonne2[y])
            colonne2 = c
        elif colonnee == "c":
          if not int(test) == c_pas_possible:
            colonne3 = list(colonne3)
            colonne3[int(test)] = "/"
            for y in range(len(colonne3)):
              c += str(colonne3[y])
            colonne3 = c
        elif colonnee == "d":
          if not int(test) == d_pas_possible:
            colonne4 = list(colonne4)
            colonne4[int(test)] = "/"
            for y in range(len(colonne4)):
              c += str(colonne4[y])
            colonne4 = c
        elif colonnee == "e":
          if not int(test) == e_pas_possible:
            colonne5 = list(colonne5)
            colonne5[int(test)] = "/"
            for y in range(len(colonne5)):
              c += str(colonne5[y])
            colonne5 = c
        elif colonnee == "f":
          if not int(test) == f_pas_possible:
            colonne6 = list(colonne6)
            colonne6[int(test)] = "/"
            for y in range(len(colonne6)):
              c += str(colonne6[y])
            colonne6 = c
        elif colonnee == "g":
          if not int(test) == g_pas_possible:
            colonne7 = list(colonne7)
            colonne7[int(test)] = "/"
            for y in range(len(colonne7)):
              c += str(colonne7[y])
            colonne7 = c
        elif colonnee == "h":
          if not int(test) == h_pas_possible:
            colonne8 = list(colonne8)
            colonne8[int(test)] = "/"
            for y in range(len(colonne8)):
              c += str(colonne8[y])
            colonne8 = c
        elif colonnee == "i":
          if not int(test) == i_pas_possible:
            colonne9 = list(colonne9)
            colonne9[int(test)] = "/"
            for y in range(len(colonne9)):
              c += str(colonne9[y])
            colonne9 = c
        nombres = 0
    nombres += 1

n = 0



def initialize():
#Modifier les variables qui font le plateau
  c = ""
  global colonne1
  global colonne2
  global colonne3
  global colonne4
  global colonne5
  global colonne6
  global colonne7
  global colonne8
  global colonne9
  global reponse
  global essais
  global nb_essais
  global test
  global colonnee
  global n
  global nombres
  global a_pas_possible
  global b_pas_possible
  global c_pas_possible
  global d_pas_possible
  global e_pas_possible
  global f_pas_possible
  global g_pas_possible
  global h_pas_possible
  global i_pas_possible

  colonnee = random.choice(choix_init)

  nb = random.randint(1, 9)
  
  test = random.randint(1, 9)

  if int(test) == 1:
    test = 0
  elif test == 2:
    test = 2
  elif test == 3:
    test = 4
  elif test == 4:
    test = 7
  elif test == 5:
    test = 9
  elif test == 6:
    test = 11
  elif test == 7:
    test = 14
  elif test == 8:
    test = 16
  elif test == 9:
    test = 18


  #verifie si il peut vraimnt jouer
  if peut_jouer(colonnee, test, nb) == True:
    #changer la bonne colonnes et la bonne lettre
    if colonnee == "a":
      a_pas_possible = int(test)
      colonne1 = list(colonne1)
      colonne1[int(test)] = int(nb)
      for y in range(len(colonne1)):
        c += str(colonne1[y])
      colonne1 = c
    elif colonnee == "b":
      b_pas_possible = int(test)
      colonne2 = list(colonne2)
      colonne2[int(test)] = int(nb)
      for y in range(len(colonne2)):
        c += str(colonne2[y])
      colonne2 = c
    elif colonnee == "c":
      c_pas_possible = int(test)
      colonne3 = list(colonne3)
      colonne3[int(test)] = int(nb)
      for y in range(len(colonne3)):
        c += str(colonne3[y])
      colonne3 = c
    elif colonnee == "d":
      d_pas_possible = int(test)
      colonne4 = list(colonne4)
      colonne4[int(test)] = int(nb)
      for y in range(len(colonne4)):
        c += str(colonne4[y])
      colonne4 = c
    elif colonnee == "e":
      e_pas_possible = int(test)
      colonne5 = list(colonne5)
      colonne5[int(test)] = int(nb)
      for y in range(len(colonne5)):
        c += str(colonne5[y])
      colonne5 = c
    elif colonnee == "f":
      f_pas_possible = int(test)
      colonne6 = list(colonne6)
      colonne6[int(test)] = int(nb)
      for y in range(len(colonne6)):
        c += str(colonne6[y])
      colonne6 = c
    elif colonnee == "g":
      g_pas_possible = int(test)
      colonne7 = list(colonne7)
      colonne7[int(test)] = int(nb)
      for y in range(len(colonne7)):
        c += str(colonne7[y])
      colonne7 = c
    elif colonnee == "h":
      h_pas_possible = int(test)
      colonne8 = list(colonne8)
      colonne8[int(test)] = int(nb)
      for y in range(len(colonne8)):
        c += str(colonne8[y]) 
      colonne8 = c
    elif colonnee == "i":
      i_pas_possible = int(test)
      colonne9 = list(colonne9)
      colonne9[int(test)] = int(nb)
      for y in range(len(colonne9)):
        c += str(colonne9[y])
      colonne9 = c




for r in range(int(input("Entre le nombre de chiffres à générer: "))):
  initialize()

print("        SUDOKU AI\n")
print("   1 2 3  4 5 6  7 8 9 \n")
print(f"a  {colonne1} \nb  {colonne2} \nc  {colonne3} \n \nd  {colonne4} \ne  {colonne5} \nf  {colonne6}\n \ng  {colonne7} \nh  {colonne8} \ni  {colonne9} \n")

time.sleep(5)

while True:
  j = True
  k = True
  for a in range(len(colonne1)):
    if j == True:
      if colonne1[a]  == "/":
        j = False
  for a in range(len(colonne2)):
    if j == True:
      if colonne2[a]  == "/":
        j = False
  for a in range(len(colonne3)):
    if j == True:
      if colonne3[a]  == "/":
        j = False
  for a in range(len(colonne4)):
    if j == True:
      if colonne4[a]  == "/":
        j = False
  for a in range(len(colonne5)):
    if j == True:
      if colonne5[a]  == "/":
        j = False
  for a in range(len(colonne6)):
    if j == True:
      if colonne6[a]  == "/":
        j = False
  for a in range(len(colonne7)):
    if j == True:
      if colonne7[a]  == "/":
        j = False
  for a in range(len(colonne8)):
    if j == True:
      if colonne8[a]  == "/":
        j = False
  for a in range(len(colonne9)):
    if j == True:
      if colonne9[a]  == "/":
        j = False
  if j == True:
    print(f"    Essais {essais}")
    print("   1 2 3  4 5 6  7 8 9 \n")
    print(f"a  {colonne1} \nb  {colonne2} \nc  {colonne3} \n \nd  {colonne4} \ne  {colonne5} \nf  {colonne6}\n \ng  {colonne7} \nh  {colonne8} \ni  {colonne9} \n")
    
    print("Fini!")
    print(f"Temps pris: {round(time.time() - start, 4)} secondes")
    break
  v = 0
  for a in range(len(colonne1)):
    if k == True:
      if colonne1[a]  == "/":
        col = "a"
        rang = a
        k = False
    v += 1
  for a in range(len(colonne2)):
    if k == True:
      if colonne2[a]  == "/":
        col = "b"
        rang = a
        k = False
  for a in range(len(colonne3)):
    if k == True:
      if colonne3[a]  == "/":
        col = "c"
        rang = a
        k = False
    v += 1
  for a in range(len(colonne4)):
    if k == True:
      if colonne4[a]  == "/":
        col = "d"
        rang = a
        k = False
  for a in range(len(colonne5)):
    if k == True:
      if colonne5[a]  == "/":
        col = "e"
        rang = a
        k = False
  for a in range(len(colonne6)):
    if k == True:
      if colonne6[a]  == "/":
        col = "f"
        rang = a
        k = False
  for a in range(len(colonne7)):
    if k == True:
      if colonne7[a]  == "/":
        col = "g"
        rang = a
        k = False
  for a in range(len(colonne8)):
    if k == True:
      if colonne8[a]  == "/":
        col = "h"
        rang = a
        k = False
  for a in range(len(colonne9)):
    if k == True:
      if colonne9[a]  == "/":
        col = "i"
        rang = a
        k = False
  
  #***donnes pour modifier le plateau***#

  #Verifier que la colonne est valide sinon redemander
  while True:
    if col == "a" or col == "b" or col == "c" or col == "d" or col == "e" or col == "f" or col == "g" or col == "h" or col == "i":
      break
    else:
      col = input("Invalide, entre la colonne: ")

  #demander le nombre a mettre au coordonees voulu
  nombre = random.randint(1, 9)
  
  while True:
    if nombre < 10:
      break
    elif nombre > 10:
      nombre = int(input("Invalide, entre le nombre: "))


  #Fonctions principale 
  joue(col, int(rang), nombre)
