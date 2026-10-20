import League
import Equipe

class MonteCarloSimulator:
    def __init__(self,league,N):
        self.league=league
        self.nb_iter=int(N)
        self.historique={}
        self.pourcentage={}
        for i in self.league.equipes:
            self.historique[i.nom]=0
            self.pourcentage[i.nom]=0
    
    
    def simuler(self):
        for i in range(self.nb_iter):
            for j in self.league.equipes:
                j.reinitialiser()
            self.league.simuler_saison()
            self.historique[self.league.classement[1][0]]+=1
        for k in self.historique:
            self.pourcentage[k]=round((self.historique[k]/self.nb_iter)*100,3)
            
    def __str__(self):
        return f" Le pourcentage de victore du championnat pour chaque équipes: {self.pourcentage}"
        
        
if __name__=="__main__":
    Equipes=[Equipe.Equipe("Arsenal",4.5),Equipe.Equipe("Man-U",3.5),Equipe.Equipe("PSG",5.0),Equipe.Equipe("Real",4.0)]
    League_f=League.League(Equipes)
    Simu=MonteCarloSimulator(League_f,10000)
    Simu.simuler()
    
    print(Simu)
    
    
            
            
            
            
