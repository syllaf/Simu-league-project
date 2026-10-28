# SIMU-LEAGUE : Simulation d'une ligue à l'aide de la méthode Monte-Carlo

## Contexte & Objectifs
Ce projet a pour but de développer mes compétences en programmation et en modélisation mathématique en concevant l'intégralité du code de manière autonome.

Il s'agit d'un simulateur de championnat capable d'estimer les probabilités de sacre final de chaque équipe à partir de critères réalistes (niveaux relatifs, scores stochastiques). Le projet intègre une interface graphique interactive permettant de paramétrer la compétition et de visualiser les résultats sous forme de graphiques.

## Fonctionnalités clés

- **Moteur de match**: Modélisation stochastique des scores via une loi de Poisson paramétrée par la différence de niveau ($\Delta$) entre les deux équipes : $$\lambda_A=\lambda_{\text{base}} \cdot e^{\beta \cdot \Delta}$$

- **Gestion de la compétition**: Organisation d'un championnat complet en matchs aller-retour générés sous forme de calendrier. Le classement est établi selon les critères officiels : total de points, différence de buts, puis meilleure attaque.

- **Moteur Monte-Carlo**: Exécution répétée de $N$ saisons complètes et indépendantes. La convergence statistique garantie par la loi des grands nombres permet d'estimer les probabilités réelles de titre de chaque club.

- **Interface graphique**: Structure ergonomique en deux volets :
    - **Panneau de configuration** : saisie du nombre d'itérations $N$, ajout et suppression dynamiques d'équipes et ajustement de leurs niveaux.
    - **Panneau de visualisation** : affichage dynamique sous forme de diagramme en barres horizontales représentant les pourcentages de sacre final.

## Modélisation mathématique et statistique

### 1. Modélisation des scores: 
La loi de Poisson est le choix idéal pour générer le score d'un match, car il s'agit d'un événement discret et relativement rare sur un intervalle de temps continu fixé.

L'espérance de buts $\lambda_A$ de l'équipe $A$ face à l'équipe $B$ est calculée selon:
$$\lambda_A=\lambda_{\text{base}} \cdot e^{\beta \cdot \Delta}$$ 

- **$\lambda_{\text{base}}=1,35$** : Représente la moyenne de but par match d'une équipe de football professionnel.
- **$\Delta=\text{Niveau}_A-\text{Niveau}_B$** : Représente la différence de niveau entre les deux équipes
- **$\beta=0,25$**: Représente le coefficient régulateur pour avantager ou non une équipe en fonction de l'écart de niveau

### 2. Estimation des probabilités:
    - La simulation d'un ligue prend en compte plusieurs facteurs et plusieurs critères ce qui rend quasiment impossible sa résolution par calcul direct.
    -Notre algorithme fait jouer $N$ saisons autonomes et indépendantes à chaque itération.
    -C'est là que la loi des grands nombres intervient avec cette formule qui montre que plus le nombre d'itération est grand, plus on se rapproche d'un résulat qui tend vers la probabilité théorique : $$\text{Fréquence}(A) = \frac{\text{Victoires}_A}{N} \xrightarrow[N \to \infty]{} P(\text{Titre}_A)$$
    
## Architecture du projet

```text
Simu_league_project\
├── League.py
├── Calendrier.py
├── Equipe.py
├── MonteCarloSimulator.py
├── Interface.py
└── README.md
```
### Role des modules

- **Equipe.py**: Modélise une équipe, avec son nom, son niveau, ses points, ses buts marqués, ses buts encaissés, son rang et son nombre de matchs joués.

- **Calendrier.py**: Génère le calendrier du championnat avec la phase aller et la phase retour, en utilisant la méthode round-robin.

- **League.py**: Coeur du projet, car cette classe simule les matchs, la ligue entière et établit le classement général multi-critères.

- **MonteCarloSimulator.py**: Pilote la répétition du grand nombre de saisons et calculer les pourcentages de victoires finaux.

- **Interface.py**: Interface graphique interactive (CustomTkinter & Matplotlib) permettant de paramétrer la ligue et d'afficher le diagramme des probabilités.


## Guide d'installation & d'exécution

- **Prérequis/Dépendances**: 
```bash
sudo apt update
sudo apt install python3-tk
python3 -m pip install customtkinter matplotlib --break-system-packages
```

- **Lancement**: 
Commande pour ouvrir l'interface graphique:
```bash
python3 interface.py
```
Commande optionnel pour tester le moteur en ligne de commande:
```bash
python3 MonteCarloSimulator.py
```
