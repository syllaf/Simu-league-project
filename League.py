import Equipe
import Calendrier
import numpy as np

class League:
    def __init__(self,Equipes): #initialisation du constructeur
        self.equipes=Equipes
        
        cal=Calendrier.Calendrier(self.equipes)
        cal.match_maker()
        self.calendrier=cal.calendrier
        
        self.classement={}
    
    def esp_equipe(self,delta): #calcul de l'esperence d'une équipe
        lambda_base=1.35
        beta=0.25
        return lambda_base*np.exp(beta*delta)
        
        
    def simuler_match(self,equipe1,equipe2): #simulation d'un match à l'aide de la loi de poisson
        delta1=equipe1.lvl-equipe2.lvl
        delta2=equipe2.lvl-equipe1.lvl
        
        goal1=np.random.poisson(self.esp_equipe(delta1))
        goal2=np.random.poisson(self.esp_equipe(delta2))
        
        equipe1.actualiser_stat(goal1,goal2)
        equipe2.actualiser_stat(goal2,goal1)
    
    def rang(self): # actualisationn du rang pour le classement
        trier=sorted(self.equipes, key=lambda equipe:(equipe.points,equipe.diff_but,equipe.but_marquer), reverse=True)
        for i in range(len(self.equipes)):
            self.classement[i+1]=(trier[i].nom,trier[i].points)
    
    def simuler_saison(self): # simulation d'une saison
        for day in self.calendrier:
            for j in day:
                self.simuler_match(j[0],j[1])
        self.rang()

    def __str__(self): # mise en forme de l'affichage
       return f"Classement : {self.classement}"


#test du  bon fonctionnement de la classe
if __name__=="__main__":
    Equipes=[Equipe.Equipe("Arsenal",4.5),Equipe.Equipe("Man-U",3.5),Equipe.Equipe("PSG",5.0),Equipe.Equipe("Real",4.0)]
    League_f=League(Equipes)

    League_f.simuler_saison()
    print(League_f)

