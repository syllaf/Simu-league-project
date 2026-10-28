class Calendrier:
    def __init__(self,equipes): # initialisation de la classe
        self.num_journee=0
        self.equipes=equipes
        self.calendrier=[]
    
    def match_maker_home(self): # attribution des match aller
        team=self.equipes.copy()
        for i in range(len(team)-1):
            day=[]
            for j in range(0,len(team)//2):
                day.append((team[j],team[-j-1]))
            self.calendrier.append(day)
            self.num_journee+=1
            last=team.pop()
            team.insert(1,last)
    
    def match_maker_away(self): # attribution des match retour
        for i in range(len(self.calendrier)):
            journee=self.calendrier[i]
            day=[]
            for j in range(len(journee)):
                match=journee[j]
                day.append((match[1],match[0]))
            self.calendrier.append(day)
            self.num_journee+=1
            
    def match_maker(self): # attribution des match de la saison
        self.match_maker_home()
        self.match_maker_away()
    
    

    def __str__(self): # mise en forme pour l'affichage
     return f"Calendrier: num:{self.num_journee}, equipes:{self.equipes}, calendrier:{self.calendrier}"
     
 
# test du bon fonctionnement de la classe
if __name__=="__main__":
    Equipes=['A','B','C','D']
    Planning=Calendrier(Equipes)
    Planning.match_maker()
    print(Planning)


