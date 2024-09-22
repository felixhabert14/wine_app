import pandas as pd

data = {
    "Vin": [
        "Cotes du Rhone", "Beaujolais Villages", "Bordeaux Superieur", "Chinon", 
        "Saint Nicolas de Bourgueil", "Faugeres", "Costieres de Nimes", "Lirac", 
        "Brouilly", "Fitou", "Sancerre", "Muscadet Sevre et Maine", "Chablis", 
        "Vouvray", "Macon Villages", "Entre deux Mers", "Alsace Riesling", 
        "Pouilly Fume", "Viognier (Pays dOc)", "Petit Chablis"
    ],
    "Cepage": [
        "Grenache, Syrah", "Gamay", "Merlot, Cabernet Sauvignon", "Cabernet Franc",
        "Cabernet Franc", "Syrah, Grenache, Mourvedre", "Syrah, Grenache", 
        "Grenache, Syrah, Mourvedre", "Gamay", "Carignan, Grenache, Syrah",
        "Sauvignon Blanc", "Melon de Bourgogne", "Chardonnay", "Chenin Blanc", 
        "Chardonnay", "Sauvignon Blanc, Semillon", "Riesling", "Sauvignon Blanc", 
        "Viognier", "Chardonnay"
    ],
    "Adjectifs": [
        "Rond, epice, gourmand", "Leger, fruite, vif", "Structure, genereux, elegant", 
        "Frais, souple, legerement tannique", "Fruite, frais, delicat", 
        "Puissant, epice, chaleureux", "Expressif, charnu, equilibre", 
        "Genereux, rond, epice", "Leger, frais, fruite", "Rustique, epice, charpente", 
        "Mineral, vif, frais", "Sec, vif, leger", "Mineral, vif, elegant", 
        "Demi-sec, frais, floral", "Souple, fruite, floral", "Leger, frais, floral", 
        "Sec, vif, mineral", "Mineral, fume, frais", "Floral, rond, aromatique", 
        "Leger, vif, mineral"
    ],
    "Aromes": [
        "Cerise, mure, framboise", "Fraise, cerise, framboise", "Cassis, prune, groseille", 
        "Framboise, poivron, cerise noire", "Fraise, framboise, cerise", "Mure, cassis, prune", 
        "Cerise, mure, reglisse", "Fruits noirs, figue, poivre", "Cerise, framboise, mure", 
        "Prune, mure, epices", "Pomme verte, agrumes, groseille a maquereau", 
        "Pomme, citron, poire", "Pomme verte, agrumes, fleurs blanches", 
        "Pomme, poire, miel", "Peche, poire, agrumes", "Pamplemousse, citron, fleurs blanches", 
        "Pomme, citron, peche", "Pamplemousse, citron, herbes", "Abricot, peche, fleur doranger", 
        "Pomme verte, citron, noisette"
    ]
}


# Création du DataFrame
df = pd.DataFrame(data)

# # Sauvegarde dans un fichier CSV
# file_path = "/mnt/data/selection_vins_francais.csv"
# df.to_csv(file_path, index=False, sep=';')

# file_path
additional_data = {
    "Vin": [
        "Corbieres", "Minervois", "Cahors", "Bandol", "Madiran", "Cotes de Bourg", 
        "Cotes de Blaye", "Montagne Saint Emilion", "Pomerol", "Graves", 
        "Alsace Gewurztraminer", "Quincy", "Saint Veran", "Pouilly Loche", "Touraine", 
        "Menetou Salon", "Cote de Beaune", "Petit Manseng", "Jurancon", "Cotes du Jura", 
        "Tavel", "Cotes de Provence", "Luberon", "Cabernet dAnjou", "Bandol Rose", 
        "Gris de Toul", "Rose dAnjou", "Coteaux dAix en Provence", "Clairet de Bordeaux", 
        "Coteaux Varois en Provence"
    ],
    "Cepage": [
        "Carignan, Syrah, Grenache", "Syrah, Grenache, Carignan", "Malbec", "Mourvedre", 
        "Tannat", "Merlot, Cabernet Sauvignon", "Merlot, Cabernet Sauvignon", 
        "Merlot, Cabernet Franc", "Merlot, Cabernet Franc", "Cabernet Sauvignon, Merlot", 
        "Gewurztraminer", "Sauvignon Blanc", "Chardonnay", "Chardonnay", "Sauvignon Blanc", 
        "Sauvignon Blanc", "Chardonnay", "Petit Manseng", "Gros Manseng, Petit Manseng", 
        "Chardonnay, Savagnin", "Grenache, Cinsault", "Grenache, Cinsault, Syrah", 
        "Grenache, Syrah", "Cabernet Franc, Cabernet Sauvignon", "Mourvedre, Grenache", 
        "Gamay, Pinot Noir", "Grolleau, Cabernet Franc", "Grenache, Syrah, Cinsault", 
        "Merlot, Cabernet Sauvignon", "Grenache, Syrah"
    ],
    "Adjectifs": [
        "Riche, charpente, epice", "Fruite, structure, epice", "Puissant, tannique, profond", 
        "Corse, puissant, tannique", "Robuste, tannique, corse", "Riche, fruite, rond", 
        "Elegant, fruite, souple", "Genereux, structure, veloute", "Puissant, riche, onctueux", 
        "Complexe, charpente, elegant", "Aromatique, ample, exotique", "Vif, mineral, elegant", 
        "Fruite, floral, frais", "Mineral, elegant, vif", "Leger, fruite, frais", "Mineral, vif, frais", 
        "Riche, equilibre, aromatique", "Moelleux, exotique, riche", "Suave, doux, fruite", 
        "Mineral, frais, elegant", "Puissant, fruite, genereux", "Leger, frais, fruite", 
        "Fruite, frais, leger", "Doux, fruite, frais", "Sec, elegant, puissant", "Leger, frais, fruite", 
        "Doux, fruite, gourmand", "Leger, vif, floral", "Fruite, genereux, vif", "Leger, frais, fruite"
    ],
    "Aromes": [
        "Mure, prune, epices", "Cerise, mure, poivre noir", "Cassis, mure, truffe", 
        "Fruits noirs, poivre, epices", "Prune, cassis, epices", "Prune, cerise noire, groseille", 
        "Cassis, framboise, mure", "Cerise, prune, cassis", "Prune, truffe, cerise noire", 
        "Cassis, prune, poivre", "Litchi, rose, epices", "Pamplemousse, citron, pomme verte", 
        "Peche, poire, agrumes", "Pomme, citron, fleurs blanches", "Pomme, poire, agrumes", 
        "Pamplemousse, citron, fleurs blanches", "Pomme, noisette, agrumes", 
        "Ananas, mangue, abricot", "Peche, abricot, agrumes", "Pomme, citron, noix", 
        "Fraise, groseille, cerise", "Fraise, peche, agrumes", "Framboise, cerise, agrumes", 
        "Fraise, groseille, framboise", "Fraise, peche, agrumes", "Peche, framboise, fraise", 
        "Fraise, framboise, cerise", "Peche, agrumes, fleurs blanches", "Cerise, fraise, framboise", 
        "Fraise, agrumes, peche"
    ]
}

# Conversion en DataFrame
additional_df = pd.DataFrame(additional_data)

# Ajout des nouvelles données au DataFrame initial
df_extended = pd.concat([df, additional_df], ignore_index=True)

# Sauvegarde dans un fichier CSV avec les 50 vins
file_path_extended = "./selection_vins_francais.csv"
df_extended.to_csv(file_path_extended, index=False, sep=';', encoding='utf-8')

file_path_extended