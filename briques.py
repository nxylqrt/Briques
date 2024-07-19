import pyxel

class Briques:
    def __init__(self):
       self.taille_brique = (30,7)
       self.coordonnes_bloc = (30,30)
       self.blocx , self.blocy = self.coordonnes_bloc
       #self.matrice = [[True for k in range(5)] for j in range(5)]
       #print(self.matrice)


Briques()



class Jeu:
    def __init__(self):
        
        pyxel.init(192,256,title="Jeu de briques")
        
        self.taille_pltfm = (38,7)
        self.joueurxy = (96-(self.taille_pltfm[0]/2),256-(30+self.taille_pltfm[1]))
        self.joueurx , self.joueury = self.joueurxy
        self.vitesse = 3
        pyxel.run(self.update, self.draw)


    def deplacement_pltfm(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.joueurx < 192 - self.taille_pltfm[0] - 4 :
            self.joueurx += 3
        elif pyxel.btn(pyxel.KEY_LEFT) and self.joueurx > 4:
            self.joueurx -= 3
       
      
    def draw(self):
        pyxel.cls(15)
        pyxel.rect(self.joueurx , self.joueury , self.taille_pltfm[0], self.taille_pltfm[1],8)
        """for k in range(Briques.matrice):
            pyxel.rect(self.blocx+[30*i] , self.blocky , self.taille_pltfm[0], self.taille_pltfm[1],8)"""
    
    def update(self):
        self.deplacement_pltfm()


       



Jeu()
