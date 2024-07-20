import pyxel

class Briques:
    def __init__(self):
       self.taille_brique = (25,9)
       self.coordonnes_bloc = (18,30)
       self.blocx , self.blocy = self.coordonnes_bloc
    
    def coordonnees_brique(self,matrice):
        self.liste = []
        for k in range (len(matrice)):
            self.liste.append([])
            for j in range (len(matrice[k])):
                self.liste[k].append(((18+k*(self.taille_brique[1])),(30+j*(self.taille_brique[0]))))
        
        return self.liste







class Jeu:
    def __init__(self):
        
        pyxel.init(192,256,title="Jeu de briques")
        
        #joueur
        self.taille_pltfm = (38,7)
        self.joueurxy = (96-(self.taille_pltfm[0]//2),256-(30+self.taille_pltfm[1]))
        self.joueurx , self.joueury = self.joueurxy

        #balle
        self.ballexy = (96,256-(30+4+self.taille_pltfm[1]))
        self.ballex , self.balley = self.ballexy
        self.vitesse = 3
        self.direction_x = True 
        self.direction_y = True 
        

        #briques
        self.briques = Briques()
        self.matrice = [[True for k in range(6)] for j in range(10)] #création de la matrice de briques
        self.co_briques = self.briques.coordonnees_brique(self.matrice) 

        pyxel.run(self.update, self.draw)



    def deplacement_balle(self):
        #deplacement vertical
        if self.direction_y == True:
            self.balley -= 4
        else:
            self.balley += 4

        if self.plafond_esttouche() and self.direction_y == True:
           self.direction_y = False
        
        elif self.brique_touchee() and self.direction_y == True:
            self.direction_y = False

        if self.plateforme_touchee() and self.direction_y == False:
           self.direction_y = True
        

        #deplacement horizontal





    def brique_touchee(self):
        for ligne in self.matrice:
            for brique in self.matrice: 
                if brique == True:
                    if self.ballex in range(self.co_briques(brique[0]) , 
                                            self.co_briques(brique[0]) + self.briques.taille_brique[0] and 
                                            self.balley in range(self.co_briques(brique[1]) , 
                                            self.co_briques(brique[1]) + self.briques.taille_brique[1])):
                        print(True)
                        return True
                else:
                    print(False)
                    return False
        

    
    def bord_esttouche(self):
        if self.ballex >= 189:
            return True
        elif self.ballex <= 3:
            return True
        else:
            return False
        
    def plafond_esttouche(self):
        if self.balley <= 5:
            return True 
        else:
            return False
        
    def plateforme_touchee(self):
        if self.balley >= self.joueury-6 and self.balley <= self.joueury and self.ballex in range(self.joueurx , self.joueurx + self.taille_pltfm[0]):
            return True
        else:
            return False



    def deplacement_pltfm(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.joueurx < 192 - self.taille_pltfm[0] - 4 :
            self.joueurx += 3
        elif pyxel.btn(pyxel.KEY_LEFT) and self.joueurx > 4:
            self.joueurx -= 3
    
      
    def draw(self):
        pyxel.cls(15)
        pyxel.rect(self.joueurx , self.joueury , self.taille_pltfm[0], self.taille_pltfm[1],8) #plateforme
        pyxel.circ(self.ballex, self.balley, 3, 3)

        for k in range(len(self.matrice)):
            for i in range(len(self.matrice[k])): #implémentation des briques dans le jeu 
                pyxel.rect(self.briques.blocx+(self.briques.taille_brique[0]+1)*i, self.briques.blocy+(self.briques.taille_brique[1]+1)*k, 
                           self.briques.taille_brique[0], self.briques.taille_brique[1], 2)
                

    
    def update(self):
        self.deplacement_pltfm()
        self.deplacement_balle()
        self.brique_touchee()


Jeu()



"""briques = Briques()
mat = [[True for k in range(6)] for j in range(10)]
briques.coordonnees_brique(mat)"""