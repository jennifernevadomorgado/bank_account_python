from CompteBancaire import CompteB

# def main():
comptes = []

while True:
    print("\n=== Menu Gestion de Compte Bancaire ===")
    print("1. Ajouter un compte")
    print("2. Versement d'un montant")
    print("3. Retrait d'un montant")
    print("4. Appliquer l'agios de 5%")
    print("5. Afficher un compte")
    print("6. Afficher tous les comptes")
    print("7. Quitter")

    choix = input("Votre choix : ")

    match choix:
        case "1":
            numero = input("Entrez le numéro du compte : ")
            nom = input("Entrez le nom du propriétaire : ")
            solde = float(input("Entrez le solde initial : "))
            comptes.append(CompteB(numero, nom, solde))
            print("Compte ajouté avec succès !")

        case "2":
            numero = input("Entrez le numéro du compte : ")

            # ---------------Première possibilité-------------
            compteur = 0
            for compte in comptes:
                if compte:
                     if compte.numeroCompte == numero:   
                        montant = float(input("Entrez le montant à verser : "))
                        compte.Versement(montant)
                        compteur = 1           
            if compteur == 0   :
                print("Compte introuvable.")
            
            # ---------------2ème possibilité-------------
            # for compte in comptes:
            # compte = next((c for c in comptes if c.numeroCompte == numero), None)
            # if compte:
            #     montant = float(input("Entrez le montant à verser : "))
            #     compte.Versement(montant)
            # else:
            #     print("Compte introuvable.")
                            
        case "3":
            numero = input("Entrez le numéro du compte : ")
            compte = next((c for c in comptes if c.numeroCompte == numero), None)
            if compte:
                montant = float(input("Entrez le montant à retirer : "))
                compte.Retrait(montant)
            else:
                print("Compte introuvable.")

        case "4":
            numero = input("Entrez le numéro du compte : ")
            compte = next((c for c in comptes if c.numeroCompte == numero), None)
            if compte:
                compte.Agios()
            else:
                print("Compte introuvable.")

        case "5":
            numero = input("Entrez le numéro du compte : ")
            # ---------------Première possibilité-------------
            # compte = next((c for c in comptes if c.numeroCompte == numero), None)
            # if compte:
            #     compte.afficher()
            # else:
            #     print("Compte introuvable.")

            # ---------------2ème possibilité-------------
            isExiste = False
            for c in comptes :
                if c.numeroCompte == numero : 
                    c.afficher()
                    isExiste = True
            if isExiste == False  :
                print("Compte introuvable.")

        case "6":
            for c in comptes :
                c.afficher()                 

        case "7":
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break

        case _:
            print("Option invalide. Veuillez réessayer.")

