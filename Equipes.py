class Equipe:
    def __init__(self,nom,lvl):
        self.nom=nom
        self.lvl=lvl
        self.points=0
        self.rank=0
        self.nb_match=0
        self.but_marquer=0
        self.but_encaisser=0
    @property
    def diff_but(self):
        return self.but_marquer-self.but_encaisser
    
    def actualiser_stat(self,but_marquer,but_encaisser):
        self.but_marquer+=but_marquer
        self.but_encaisser+=but_encaisser
        if but_marquer>but_encaisser:
            self.points+=3
        elif but_marquer==but_encaisser:
            self.points+=1
        self.nb_match+=1
    
        
    def __str__(self):
        return f"Equipes : nom:{self.nom}, lvl:{self.lvl}, pts:{self.points}, rank:{self.rank}, nb_match:{self.nb_match}, but:{self.but_marquer}, diff_but:{self.diff_but}"
    

if __name__=="__main__":
    team=Equipe("Arsenal",4.0)
    print(team)
    team.actualiser_stat(4,2)
    print(team)
    print(team.diff_but)

        
