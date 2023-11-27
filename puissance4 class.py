"""
@author : Salson Enzo (contact@enzo-salson.fr)
@version : 2.0
"""

class puissance4:
    def __init__(self) -> None:
        self.remplie = []
        self.matrice = [[0 for _ in range(6)] for t in range(7)]
        self.player1 = input("Choisissez le nom du premier joueur : ")
        self.player2 = input("Choisissez le nom du second joueur : ")
        self.d= {self.player1 : [0,0],self.player2 : [0,0]}
        if self.player1 == "stop" or self.player2 == "stop":
            exit()
        if self.player2 == "ia":
            self.print_ps(self.matrice, [])
            self.playia()
        else:
            print("Bien venue au puissance 4 !")
            print()
            print()
            self.print_ps(self.matrice, [])
            self.play()

    def check_win(self,matrice,j):
        for i in range(7):
            for m in range(6):
                if matrice[i][m] == j:
                    if m+3 < 6:
                        if matrice[i][m+1] == j and matrice[i][m+2] == j and matrice[i][m+3] == j:
                            return True
                    if i+3 < 7:
                        if matrice[i+1][m] == j and matrice[i+2][m] == j and matrice[i+3][m] == j:
                            return True
                    if m+3 < 6 and i+3 < 7:
                        if matrice[i+1][m+1] == j and matrice[i+2][m+2] == j and matrice[i+3][m+3] == j:
                            return True
                    if m-3 > -1 and i+3 < 7:
                        if matrice[i+1][m-1] == j and matrice[i+2][m-2] == j and matrice[i+3][m-3] == j:
                            return True
        return False

    def print_ps(self,matrice,remplie) -> None:
        from os import name,system
        if name == 'posix':
            system('clear')
        if name == 'nt':
            system('cls')
        else:
            pass
        for i in matrice:
            r = ""
            for m in i:
                if m == 0:
                    r+= ".  "
                elif m == 1:
                    r+= "*  "
                elif m == 2:
                    r+= "@  "
            print(r)
        print()
        r= ""
        for i in range(6):
            if i in remplie:
                r += "   "
            else:
                r += str(i+1) + "  "
        print(r)

    def see_column(self,num, matrice):
        if matrice[6][num] == 0:
            return 0
        elif matrice[6][num] in (1,2):
            if matrice[5][num] in (1,2):
                if matrice[4][num] in (1,2):
                    if matrice[3][num] in (1,2):
                        if matrice[2][num] in (1,2):
                            if matrice[1][num] in (1,2):
                                if matrice[0][num] in (1,2):
                                    return 7
                                else:
                                    return 6
                            else:
                                return 5
                        else:
                            return 4
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1

    def number(self,player,remplie):
        tmp = input(player+", choisissez le chiffre d'une colonne !")
        if tmp == "stop":
            exit()
        try:
            tmp = int(tmp)
            if tmp in (1,2,3,4,5,6):
                if tmp-1 not in remplie:
                    return tmp - 1
                else:
                    print("Erreur, la colonne est pleine")
                    return self.number(player,remplie)
            else:
                return self.number(player,remplie)
        except:
            print("Vous n'avez pas tapé quelque chose de bon")
            return self.number(player,remplie)
    
    def choix_nbr(self,matrice):
        from random import randint
        for i in range(7):
            for m in range(6):
                if matrice[i][m] == 1:
                    if m+3 <6:
                        if matrice[i][m+1] == 1 and matrice[i][m+2] == 1:
                            return m+4
                    if 7-(i+3) < 7:
                        if matrice[i-1][m] == 1 and matrice[i-2][m]==1:
                            return m+1
                    if 7-(i+3) < 7 and m+3 < 6:
                        pass
        a = randint(1,6)
        print("random",a)
        return a


    def numberia(self,remplie):
        from random import randint
        tmp = self.choix_nbr(self.matrice)
        if tmp-1 not in remplie:
            return tmp-1
        else:
            print("Erreur, la colonne est pleine")
            return self.numberia(self.remplie)

    def wins(self,win,d={}):
        if win == 1:
            print("Bravo",self.player1,"vous avez gagné la partie !")
            d[self.player1][0]+=1
        elif win == 2:
            print("Bravo",self.player2,"vous avez gagné la partie !")
            d[self.player2][0]+=1
        m = input("Tapez \"re\" pour recommencer sinon entrez !")
        if m.lower() == "re":
            self.remplie = []
            self.matrice = [[0 for _ in range(6)] for t in range(7)]
            self.player1 = input("Choisissez le nom du premier joueur : ")
            self.player2 = input("Choisissez le nom du second joueur : ")
            if self.player1 == "stop" or self.player2 == "stop":
                exit()
            if not(self.player1 in d):
                d[self.player1] = [0,0]
            if not(self.player2 in d):
                d[self.player2] = [0,0]
            print("Bien venue au puissance 4 !")
            print()
            print()
            self.print_ps(self.matrice, [])
            if self.player2 == "ia":
                self.playia(d)
            else:
                self.play(d)
        else:
            for o,q in d.items():
                if o == "ia":
                    o = "L'ordinateur"
                print(o,"a joué",q[1],"parties et en a gagné",q[0])

    def play(self,d={}):
        while True:
            num = self.number(self.player1, self.remplie)
            p = 6 - self.see_column(num,self.matrice)
            self.matrice[p][num] = 1
            if p == 0:
                self.remplie.append(num)
            self.print_ps(self.matrice, self.remplie)
            if self.check_win(self.matrice,1):
                win = 1
                break
            num = self.number(self.player2, self.remplie)
            p = 6 - self.see_column(num,self.matrice)
            if p == 0:
                self.remplie.append(num)
            self.matrice[p][num] = 2
            self.print_ps(self.matrice, self.remplie)
            if self.check_win(self.matrice,2):
                win = 2
                break
        self.d[self.player1][1] +=1
        self.d[self.player2][1] +=1
        self.wins(win,self.d)

    def mettre_pion(self,j):
        num = self.number(self.player1, self.remplie)
        p = 6 - self.see_column(num,self.matrice)
        self.matrice[p][num] = j
        if p == 0:
            self.remplie.append(num)
        self.print_ps(self.matrice, self.remplie)

    def playia(self,d={}):
        while True:
            num = self.number(self.player1, self.remplie)
            p = 6 - self.see_column(num,self.matrice)
            self.matrice[p][num] = 1
            if p == 0:
                self.remplie.append(num)
            self.print_ps(self.matrice, self.remplie)
            if self.check_win(self.matrice,1):
                win = 1
                break
            num = self.numberia(self.remplie)
            p = 6 - self.see_column(num,self.matrice)
            if p == 0:
                self.remplie.append(num)
            self.matrice[p][num] = 2
            self.print_ps(self.matrice, self.remplie)
            if self.check_win(self.matrice,2):
                win = 2
                break
        self.d[self.player1][1] +=1
        self.d[self.player2][1] +=1
        self.wins(win,self.d)


def __main__():
    game=puissance4()
    exit()

__main__()