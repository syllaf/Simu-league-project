import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 
import Equipe
import League
import MonteCarloSimulator

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Application(ctk.CTk):
    def __init__(self): # création de l'interface graphique
        super().__init__()
        self.title("Simu-League")
        self.geometry("950x550")
        self.protocol("WM_DELETE_WINDOW", self.fermer_application)
        self.resizable(False,False)
        
        self.frame_gauche=ctk.CTkFrame(self,width=360, corner_radius=10)
        self.frame_gauche.pack_propagate(False)
        self.frame_gauche.pack(side="left",fill="y",padx=15, pady=15)
        
        self.frame_droite=ctk.CTkFrame(self, corner_radius=10)
        self.frame_droite.pack(side="right", fill="both", expand=True, padx=15, pady=15)
        
        self.lignes_equipes=[]
        
        self.construire_panneau_gauche()
        self.initialiser_graphique()
    
    def construire_panneau_gauche(self): # construction du panneau gauche
        titre=ctk.CTkLabel(self.frame_gauche, text="Configuration", font=ctk.CTkFont(size=18,weight="bold"),)
        titre.pack(pady=(15,10))
        
        lbl_n=ctk.CTkLabel(self.frame_gauche, text="Nombre de saison (N):")
        lbl_n.pack(anchor="w", padx=20, pady=(5,0))
        
        self.entry_n =ctk.CTkEntry(self.frame_gauche)
        self.entry_n.insert(0,"1000")
        self.entry_n.pack(fill="x", padx=20, pady=(0,15))
        
        lbl_eq=ctk.CTkLabel(self.frame_gauche, text="Équipes et Niveau:",font=ctk.CTkFont(weight="bold"),)
        lbl_eq.pack(anchor="w", padx=20, pady=(5,5))
        
        self.scroll_equipes=ctk.CTkScrollableFrame(self.frame_gauche, width=300,height=220,fg_color="transparent")
        self.scroll_equipes.pack(fill="both",expand=True, padx=10,pady=5)
        
        
        equipes_base=[("Arsenal","4.5"),("Man-U","3.5"),("PSG","5.0"),("Real","4.0"),]
        for nom, note in equipes_base:
            self.ajouter_ligne_equipe(nom,note)
        
        self.btn_ajouter=ctk.CTkButton(self.frame_gauche,text="+ Ajouter une équipe",fg_color="#2b7a4b",hover_color="#1e5836",command=lambda: self.ajouter_ligne_equipe("Club","3.0"),)
        self.btn_ajouter.pack(padx=20,pady=(5,10),fill="x")
        self.lbl_erreur=ctk.CTkLabel(self.frame_gauche,text="",text_color="#ff5555")
        self.lbl_erreur.pack(padx=20, pady=(0,5))
        
        self.bouton_lancer=ctk.CTkButton(self.frame_gauche,text="Lancer la simulation",command=self.lancer_simulation,)
        self.bouton_lancer.pack(pady=(0,15), padx=20, fill="x")
        
        
    
    def ajouter_ligne_equipe(self, nom="", note=""): # option pour ajouter une equipe à la ligue
        ligne=ctk.CTkFrame(self.scroll_equipes, fg_color="transparent")
        ligne.pack(fill="x",pady=3)
        
        e_nom=ctk.CTkEntry(ligne,width=120,placeholder_text="Nom")
        e_nom.insert(0,nom)
        e_nom.pack(side="left",padx=(0,5))
        
        e_note=ctk.CTkEntry(ligne, width=50, placeholder_text="Note")
        e_note.insert(0,note)
        e_note.pack(side="left",padx=(0,5))
        
        donnees_ligne={"frame": ligne, "nom":e_nom, "note": e_note}
        
        btn_suppr=ctk.CTkButton(ligne, text="x",width=30,fg_color="#992b2b",hover_color='#6e1f1f',command=lambda: self.supprimer_ligne_equipe(donnees_ligne),)
        btn_suppr.pack(side="left",padx=(5,0))
        self.lignes_equipes.append(donnees_ligne)
    
    def supprimer_ligne_equipe(self, donnees_ligne): # option pour supprimer une equipe de la ligue
        if len(self.lignes_equipes)<=2:
            self.lbl_erreur.configure(text="Minimum 2 équipes requises !")
            return
        self.lbl_erreur.configure(text="")
        donnees_ligne["frame"].destroy()
        self.lignes_equipes.remove(donnees_ligne)
        
    def initialiser_graphique(self): # dessin du graphique des pourcentage de victoire au championnat
        self.fig, self.ax= plt.subplots(figsize=(6,4.5))
        self.fig.patch.set_facecolor("#2b2b2b")
        self.ax.set_facecolor("#2b2b2b")
        
        self.canvas=FigureCanvasTkAgg(self.fig, master=self.frame_droite)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
        
        self.ax.text(0.5,0.5,"Lancer la simulation pour afficher le graphique", color="gray",ha="center",va="center",fontsize=12,)
        self.ax.axis("off")
        self.canvas.draw()
        
        
    def lancer_simulation(self): # lancement du simulateur
        self.lbl_erreur.configure(text="")
        try:
            nb_iter=int(self.entry_n.get())
            if nb_iter<=0:
                raise ValueError
        except ValueError:
            self.lbl_erreur.configure(text="Le nombre N doit être un entier positif.")
            return
        liste_equipes=[]
        try:
            for item in self.lignes_equipes:
                nom=item["nom"].get().strip()
                note=float(item["note"].get().strip())
                if not nom:
                    self.lbl_erreur.configure(text="Chaque équipe doit avoir un nom.")
                if not note<=5.0:
                    self.lbl_erreur.configure(text="Chaque note doit être inférieur ou égale à 5.0.")
                    return
                liste_equipes.append(Equipe.Equipe(nom,note))
        except ValueError:
            self.lbl_erreur.configure(text="Les notes doivent être des décimaux.")
            return
        
        if len(liste_equipes)%2!=0:
            self.lbl_erreur.configure(text=f"Nombre d'équipes impair ({len(liste_equipes)}).\nAjoutez ou retirez une équipe.")
            return
        ligue=League.League(liste_equipes)
        simu=MonteCarloSimulator.MonteCarloSimulator(ligue,nb_iter)
        simu.simuler()
        self.actualiser_graphique(simu.pourcentage)
    
    def actualiser_graphique(self, donnees_pourcentage): #actualisation du graphique avec les nouvelle information
        self.ax.clear()
        self.ax.axis("on")
        self.ax.set_facecolor("#2b2b2b")
        
        clubs=list(donnees_pourcentage.keys())
        pourcentages=list(donnees_pourcentage.values())
        
        couleur_barres="#1f6aa5"
        barres= self.ax.barh(clubs,pourcentages,color=couleur_barres, height=0.55)
        
        self.ax.set_xlim(0,100)
        self.ax.set_xlabel("Chances de titre (%)", color="white", fontsize=11)
        self.ax.set_title("Probabilité de sacre final", color="white", fontsize=13)
        self.ax.tick_params(colors="white")
        
        for bordure in ["top", "right", "left", "bottom"]:
            self.ax.spines[bordure].set_visible(False)
        
        for barre, val in zip(barres,pourcentages):
            self.ax.text(val+1.5,barre.get_y()+barre.get_height()/2,f"{val:.1f}%",color="white",va="center",fontweight="bold",)
        
        self.fig.tight_layout()
        self.canvas.draw()
    
    def fermer_application(self): # fermeture de la fenetre
        plt.close("all")
        self.quit()
        self.destroy()

# test du bon fonctionnement de la classe
if __name__=="__main__":
    app=Application()
    app.mainloop()
