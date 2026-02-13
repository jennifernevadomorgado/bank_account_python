from CompteBancaire import CompteB

compte = None

def saisir_float(message):
    while True:
        valeur = input(message).strip()
        if valeur == "":
            print("Veuillez entrer une valeur.")
            continue
        try:
            return float(valeur)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")


while True:
    print("\n=== Menu Gestion de Compte Bancaire ===")
    print("1. Ajouter un compte")
    print("2. Versement d'un montant")
    print("3. Retrait d'un montant")
    print("4. Appliquer l'agios de 5%")
    print("5. Afficher un compte")
    print("6. Quitter")

    choix = input("Votre choix : ")

    match choix:
        case "1":
            numero = input("Entrez le numéro du compte : ")
            nom = input("Entrez le nom du propriétaire : ")
            # solde = saisir_float("Entrez le solde initial : ")
            solde = float(input("Entrez le solde initial : "))
            compte = CompteB(numero, nom, solde)
            print("Compte ajouté avec succès !")

        case "2":
            if compte is not None:
                montant = float(input("Entrez le montant à verser : "))
                # montant = saisir_float("Entrez le montant à verser : ")
                compte.Versement(montant)
            else:
                print("Vous n'avez pas encore introduit un compte !!")
                            
        case "3":
            if compte is not None:
                montant = float(input("Entrez le montant à retirer : "))
                montant = saisir_float("Entrez le montant à retirer : ")
                compte.Retrait(montant)
            else:
                print("Vous n'avez pas encore introduit un compte !!")

        case "4":
            if compte is not None:
                compte.Agios()
            else:
                print("Vous n'avez pas encore introduit un compte !!")

        case "5":
            if compte is not None:
                compte.afficher()
            else:
                print("Vous n'avez pas encore introduit un compte !!")
            
        case "6":
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break

        case _:
            print("Option invalide. Veuillez réessayer.")

# if __name__ == "__main__":
#     main()