def afficher_taches(taches):
    print("Liste des tâches :")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}.{tache}_")
        
        
def nbre_taches(taches):
	print("nombre taches: ", len(taches))
