
import os
import pickle
class Composant():
    nom =""
    allergenes = False
    vegan = False
    epice = 0
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
    nom = ""
    prix = 0
    comp = []
    parametres = dict()
    commentaire = ""
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
    alcoolise = False
    quantite = 0
    def __init__(self,n,p,pa,com,a,q):
        super(Boisson,self).__init__(n,p,[],pa,com)
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
        a='[%s]' % ','.join(map(str, a))
        a=a[1:-1]
        new_Plat.write("Composants "+str(a)+"\n")
        new_Plat.write("Parametre "+str(self.parametres)+"\n")
        new_Plat.write("Accompagnements "+str(a)+"\n")
        new_Plat.close()
        for i in self.comp:
            i.saveComposant()

class Plat(Consommations):
    vegan = True
    epice = False
    def __init__(self,n,p,c,pa,com,acc):
        super(Plat,self).__init__(n,p,c,pa,com)
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
        strAcc='[%s]' % ','.join(map(str, a))
        strAcc=strAcc[1:-1]
        new_Plat.write("Composants "+strAcc+"\n")
        new_Plat.write("Parametre "+str(self.parametres)+"\n")
        new_Plat.write("Vegan "+str(self.vegan)+"\n")
        new_Plat.write("Epice "+str(self.epice)+"\n")
        a=[]
        for i in self.accompagnements:
            a.append(i.nom)
        strAcc='[%s]' % ','.join(map(str, a))
        strAcc=strAcc[1:-1]
        new_Plat.write("Accompagnements "+strAcc+"\n")
        new_Plat.close()
        for i in self.comp:
            i.saveComposant()
        for i in self.accompagnements:
            i.savePlat()

class Menu():
    nom=""
    plats=[]
    prix = 0
    avecBoisson= False
    boisson= None
    vegan = True
    epice = False
    def __init__(self,nom,p,b,pr):
        self.nom = nom
        self.plats = p
        self.boisson = b
        self.prix = pr
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
        a='[%s]' % ','.join(map(str, a))
        a=a[1:-1]

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
    menus=[]
    plats=[]
    boissons=[]
    table = 0
    pret = False
    def addPlatByName(self,name):
        self.plats.append(readPlat(name))
    def addMenuByName(self,name):
        self.menus.append(readMenu(name))
    def addBoissonByName(self,name):
        self.boissons.append(readBoisson(name))

    def __init__(self,tab,m=[],p=[],b=[]):
        self.menus = m
        self.plats = p
        self.boissons = b
        self.table = tab
        self.pret = False
    def __init__(self,tab):
        self.menus = []
        self.plats = []
        self.boissons = []
        self.table = tab
        self.pret = False
    
    def calculatePrice(self):
        total = 0
        nb_boisson = 0
        for i in self.menus:
            total+=i.prix
            if(i.avecBoisson):
                nb_boisson+=1
        for i in self.plats:
            total+=i.prix
            if(i.avecBoisson):
                nb_boisson+=1
        for i in self.boissons:
            nb_boisson-=1
            if(nb_boisson<0):
                total += self.boisson.prix

        return total
    def saveCommande(self):
        new_Plat = open("Commandes/Commande_"+str(self.table)+".txt","w")
        new_Plat.write("Table "+str(self.table)+"\n")
        a=[]
        for i in self.plats:
            a.append(i.nom)
        a='[%s]' % ','.join(map(str, a))
        a=a[1:-1]
        new_Plat.write("Plat "+str(a)+"\n")
        a=[]
        for i in self.menus:
            a.append(i.nom)
        a='[%s]' % ','.join(map(str, a))
        a=a[1:-1]
        new_Plat.write("Menu "+str(a)+"\n")
        a=[]
        for i in self.boissons:
            a.append(i.nom)
        a='[%s]' % ','.join(map(str, a))
        a=a[1:-1]
        new_Plat.write("Boisson "+str(a)+"\n")
        new_Plat.close()
        
        for i in self.menus:
            i.saveMenu()        
        for i in self.plats:
            i.savePlat()
        for i in self.boissons:
            i.saveBoisson()
            

def readBoisson(fileName):
    if(not (".txt" in fileName)):
        fileName+=".txt"
    if(not ("Boisson_" in fileName)):
        fileName="Boisson_"+fileName
    if(not ("Conso/" in fileName)):
        fileName="Conso/"+fileName
    try:
        fichier = open(fileName,'r')
    except FileNotFoundError:
        print("La Boisson desire n'existe pas : "+fileName)
        return None
    nom = ""
    prix =0.0
    param=[]
    f1 = fichier.readlines()
    for l in f1:
        if("\n" in l):
            l = l[:-1]
        mots  = l.split(" ")
        if(mots[0] == "Nom"):
            nom = mots[1]
        if(mots[0] == "Prix"):
            prix = float(mots[1])
        if(mots[0] == "Parametre"):
            if("\n" in mots[1]):
                mots[1] = mots[1][:-1]
            
            
            for i in mots[1].split(","):
                if(i!=""):
                    param.append(i)
    return Boisson(nom,prix,param,[],False,25)


def readCompo(fileName):
    if(not (".txt" in fileName)):
        fileName+=".txt"
    if(not ("Composant_" in fileName)):
        fileName="Composant_"+fileName
    if(not ("Conso/" in fileName)):
        fileName="Conso/"+fileName
    try:
        fichier = open(fileName,'r')
    except FileNotFoundError:
        print("Le Composant desire n'existe pas : "+fileName)
        return None
    nom = ""
    allergenes = False
    veg = False
    epice = False
    f1 = fichier.readlines()
    for l in f1:
        if("\n" in l):
            l = l[:-1]
        mots  = l.split(" ")
        if(mots[0] == "Nom"):
            nom = mots[1]
        if(mots[0] == "Allergenes"):
            allergenes = (mots[1]=="True")
        if(mots[0] == "Vegan"):
            veg = (mots[1]=="True")
        if(mots[0] == "Epice"):
            epice = (mots[1]=="True")
    return Composant(nom,allergenes,veg,epice)
        
def readPlat(fileName):
    if(not (".txt" in fileName)):
        fileName+=".txt"
    if(not ("Plat_" in fileName)):
        fileName="Plat_"+fileName
    if(not ("Conso/" in fileName)):
        fileName="Conso/"+fileName
    try:
        fichier = open(fileName,'r')
    except FileNotFoundError:
        print("Le Plat desire n'existe pas : "+fileName)
        return None
    f1 = fichier.readlines()
    nom =""
    prix = 0
    comp=[]
    parametres = []
    veg = False
    epice = False
    accomp = []
    for l in f1:
        if("\n" in l):
            l = l[:-1]
        mots  = l.split(" ")
        if(mots[0] == "Nom"):
            nom = mots[1]
        if(mots[0] == "Prix"):
            prix = float(mots[1])
        if(mots[0] == "Vegan"):
            veg = (mots[1]=="True")
        if(mots[0] == "Epice"):
            epice = (mots[1]=="True")
        if(mots[0] == "Composants"):
            if("\n" in mots[1]):
                mots[1] = mots[1][:-1]
            
            
            for i in mots[1].split(","):
                if(i!=""):
                    c = readCompo(i)
                    if(c!= None):
                        comp.append(c)
                    else:
                        print("Le composant desire n'existe pas : "+i)
        if(mots[0] == "Parametre"):
            if("\n" in mots[1]):
                mots[1] = mots[1][:-1]
            
            
            for i in mots[1].split(","):
                if(i!=""):
                    parametres.append(i)
        if(mots[0] == "Accompagnements"):
            if("\n" in mots[1]):
                mots[1] = mots[1][:-1]
            
            for i in mots[1].split(","):
                if(i!=""):
                    c = readPlat(i)
                    if(c!= None):
                        accomp.append(c)
                    else:
                        print("Le plat desire n'existe pas : "+i)
    return Plat(nom,prix,comp,parametres,"",accomp)
        
def readMenu(fileName):
    if(not (".txt" in fileName)):
        fileName+=".txt"
    if(not ("Menu_" in fileName)):
        fileName="Menu_"+fileName
    if(not ("Conso/" in fileName)):
        fileName="Conso/"+fileName
    try:
        fichier = open(fileName,'r')
    except FileNotFoundError:
        print("Le Menu desire n'existe pas : "+fileName)
        return None
    f1 = fichier.readlines()
    nom =""
    prix = 0
    plat=[]
    veg = False
    epice = False
    boisson = False
    for l in f1:
        if("\n" in l):
            l = l[:-1]
        mots  = l.split(" ")
        if(mots[0] == "Nom"):
            nom = mots[1]
        if(mots[0] == "Prix"):
            prix = float(mots[1])
        if(mots[0] == "Vegan"):
            veg = (mots[1]=="True")
        if(mots[0] == "Epice"):
            epice = (mots[1]=="True")
        if(mots[0] == "Boisson"):
            boisson = (mots[1]=="True")
        if(mots[0] == "Plat"):

            if("\n" in mots[1]):
                mots[1] = mots[1][:-1]
            
            for i in mots[1].split(","):
                if(i!=""):
                    c = readPlat(i)
                    if(c!= None):
                        plat.append(c)
                    else:
                        print("Le plat desire n'existe pas : "+i)
    return Menu(nom,plat,boisson,prix)
        
def getPlats():
    root_dir = "Conso"  # Path relative to current dir (os.getcwd())
    plats = []
    for i in [item for item in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, item))] : # Filter items and only keep files (strip out directories)
        if("Plat_" in i):
            plats.append(readPlat(i))
    return plats
def getMenus():
    root_dir = "Conso"  # Path relative to current dir (os.getcwd())
    plats = []
    for i in [item for item in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, item))] : # Filter items and only keep files (strip out directories)
        if("Menu_" in i):
            plats.append(readMenu(i))
    return plats
def getBoissons():
    root_dir = "Conso"  # Path relative to current dir (os.getcwd())
    plats = []
    for i in [item for item in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, item))] : # Filter items and only keep files (strip out directories)
        if("Boisson_" in i):
            plats.append(readBoisson(i))
    return plats
def getComposants():
    root_dir = "Conso"  # Path relative to current dir (os.getcwd())
    plats = []
    for i in [item for item in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, item))] : # Filter items and only keep files (strip out directories)
        if("Composant_" in i):
            plats.append(readCompo(i))
    return plats
print(getPlats())
print(getBoissons())
print(getMenus())
print(getComposants())
"""
c = Commande(0)
c.addPlatByName("Frite")
c.addPlatByName("Kebab")
        
c1 = Commande(1)
c1.addPlatByName("Frite")
c1.addPlatByName("Frite")
c1.addPlatByName("Frite")
c1.addPlatByName("Frite")
print(len(c1.plats))
viande = Composant("Viande_Mouton",False,False,False)
salade = Composant("Salade",True,False,False)
tomate = Composant("Tomate",True,False,False)
oignon = Composant("Oignon",True,False,False)
patate = Composant("Patate",True,False,False)
coca = Boisson("Coca",1,[],"",False,25)
f = Plat("Frite",1,[patate],[],"",[])
a = Plat("Kebab",6,[viande,salade,tomate,oignon],[],"",[])  
m = Menu("Kebab_Frites",[a,f],coca,6.5) 
m.saveMenu()       
readMenu("Kebab_Frites")
readCompo("Patate")
readPlat("Kebab")"""