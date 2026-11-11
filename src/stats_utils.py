import pandas as pd
import numpy as np

sales=pd.read_csv("data/sales.csv")
print(sales)
# On crée un masque sur le DataFrame et on filtre les lignes
masque = sales["montant"] > 0
sales_propre = sales[masque]
print("\nDataFrame après filtrage :")
print(sales_propre)

def analyser_ventes(transactions) :
    # Le filtrage des montants invalides
    mask=transactions["montant"] > 0
    transactions_propre=transactions[mask]
    print(transactions_propre)
    # Calculs statistiques :
    nb=len(transactions_propre)
    total=sum(transactions_propre["montant"])
    moyenne=round(total/nb, 2)
    min, med, max=np.percentile(transactions_propre["montant"], [0, 50, 100]).round(2)
    print(f"Nombre total de transactions valides {nb}")
    print(f"Somme totale des ventes {total}")
    print(f"Moyenne {moyenne}")
    print(f"std {np.std(transactions_propre, ddof=1).round(2)}")
    print(f"Min {min}, Médiane {med}, Max {max}")
    # Outliers: Identifier toutes les transactions supérieures à 2 fois la moyenne.
    outliers=transactions_propre["montant"] >= 2*moyenne
    print(f"Transactions supérieures à 2 fois la moyenne : {len(transactions_propre[outliers])}")
    dict_result={
        "nb": nb,
        "total": total,
        "moyenne": moyenne,
        "std": np.std(transactions_propre, ddof=1).round(2),
        "min": min,
        "med": med,
        "max": max,
        "outliers": len(transactions_propre[outliers])
    }
    return(dict_result)

resultat=analyser_ventes(sales)
print(resultat)

# Petit coucou que je te fas Tiba, je modifie cette code pour voir si on peut faire le merge de ton coté :)