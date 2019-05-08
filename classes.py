import pickle
class Composant():
    def __init__(self,n,a,v,e):
        self.nom = n
        self.allergenes = a
        self.vegan = v
        self.epice = e

    def estEpice(self):
        return self.epice

    def estVegan(self):
        return self.vegan

    def estAllergene(self):
        return self.allergenes,self.nom

    def saveComposant(self):
        new_Plat = open("Conso/Composant_"+self.nom+".txt","w")
        new_Plat.write("Nom "+self.nom+"\n")
        new_Plat.write("Allergenes "+str(self.allergenes)+"\n")
        new_Plat.write("Vegan "+str(self.vegan)+"\n")
        new_Plat.write("Epice "+str(self.epice)+"\n")
        new_Plat.close()


class Consommations():
    def __init__(self,n,p,comp,pa,com):
        self.nom = n
        self.prix = p
        self.comp = comp
        self.parametres = pa
        self.commentaire = com

    def estVegan(self):
        for i in self.comp:
            if(not i.estVegan):
                return False
        return True

    def getPrix(self):
        return self.prix

    def getComp(self):
        return self.comp

    def allergen(self):
        a = []
        al = False
        for i in self.comp:
             bo , iA = i.estAllergene()
             if(bo):
                 al = True
                 a.append(iA)
        return al,a


class Boisson(Consommations):
    def __init__(self,n,p,comp,pa,com,a,q):
        super(Boisson,self).__init__(n,p,comp,pa,com)
        self.alcoolise = a
        self.quantite = q

    def estAlcoolise(self):
        return self.alcoolise

    def saveBoisson(self):
        new_Plat = open("Conso/Boisson_"+self.nom+".txt","w")
        new_Plat.write("Nom "+self.nom+"\n")
        new_Plat.write("Prix "+str(self.prix)+"\n")
        a=[]
        for i in self.comp:
            a.append(i.nom)
        new_Plat.write("Composants "+str(a)+"\n")
        new_Plat.write("Parametre "+str(self.parametres)+"\n")
        new_Plat.write("Accompagnements "+str(a)+"\n")
        new_Plat.close()
        for i in self.comp:
            i.saveComposant()


class Plat(Consommations):
    def __init__(self,n,p,c,pa,com,acc):
        super(Plat,self).__init__(n,p,c,pa,com)
        self.vegan = True
        self.epice = False
        self.accompagnements = acc

        for i in self.comp:
            if(i.estEpice()):
                self.epice = True
            if(not i.estVegan()):
                self.vegan = False

        for j in self.accompagnements:
            for k in j.comp:
                if(i.estEpice()):
                    self.epice = True
                if(not i.estVegan()):
                    self.vegan = False

    def estEpice(self):
        return self.epice

    def estVegan(self):
        return self.vegan

    def savePlat(self):
        new_Plat = open("Conso/Plat_"+self.nom+".txt","w")
        new_Plat.write("Nom "+self.nom+"\n")
        new_Plat.write("Prix "+str(self.prix)+"\n")
        a=[]
        for i in self.comp:
            a.append(i.nom)
        new_Plat.write("Composants "+str(a)+"\n")
        new_Plat.write("Parametre "+str(self.parametres)+"\n")
        new_Plat.write("Vegan "+str(self.vegan)+"\n")
        new_Plat.write("Epice "+str(self.epice)+"\n")
        a=[]
        for i in self.accompagnements:
            a.append(i.nom)
        new_Plat.write("Accompagnements "+str(a)+"\n")
        new_Plat.close()
        for i in self.comp:
            i.saveComposant()
        for i in self.accompagnements:
            i.savePlat()


class Menu():
    def __init__(self,nom,p,b,pr):
        self.nom = nom
        self.plats = p
        self.boisson = b
        self.prix = pr
        self.epice = False
        self.vegan = True
        self.avecBoisson= False

        if(b != None):
            self.avecBoisson = True
        for i in self.plats:
            if(not i.estVegan()):
                self.vegan = False
            if(i.estEpice()):
                self.epice = True

    def saveMenu(self):
        new_Plat = open("Conso/Menu_"+self.nom+".txt","w")
        new_Plat.write("Nom "+self.nom+"\n")
        new_Plat.write("Prix "+str(self.prix)+"\n")
        a=[]
        for i in self.plats:
            a.append(i.nom)
        new_Plat.write("Plat "+str(a)+"\n")
        new_Plat.write("Boisson "+str(self.avecBoisson)+"\n")
        new_Plat.write("Vegan "+str(self.vegan)+"\n")
        new_Plat.write("Epice "+str(self.epice)+"\n")
        new_Plat.close()
        for i in self.plats:
            i.savePlat()
        if(self.boisson!= None):
            self.boisson.saveBoisson()


class Commande():
    def __init__(self,m,p,b,tab):
        self.menus = m
        self.plats = p
        self.boissons = b
        self.table = tab
        self.pret = False

viande = Composant("Viande_Mouton",False,False,False)
salade = Composant("Salade",True,False,False)
tomate = Composant("Tomate",True,False,False)
oignon = Composant("Oignon",True,False,False)
patate = Composant("Patate",True,False,False)
coca = Boisson("Coca",1,[],[],"",False,25)
f = Plat("Frite",1,[patate],[],"",[])
a = Plat("Kebab",6,[viande,salade,tomate,oignon],[],"",[f])
m = Menu("Kebab_Frites",[a],coca,6.5)
#m.saveMenu()
