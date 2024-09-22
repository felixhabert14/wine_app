import pandas as pd

data = {
    "Vin": [
        "Côtes-du-Rhône", "Beaujolais-Villages", "Bordeaux Supérieur", "Chinon", 
        "Saint-Nicolas-de-Bourgueil", "Faugères", "Costières de Nîmes", "Lirac", 
        "Brouilly", "Fitou", "Sancerre", "Muscadet Sèvre-et-Maine", "Chablis", 
        "Vouvray", "Mâcon-Villages", "Entre-deux-Mers", "Alsace Riesling", 
        "Pouilly-Fumé", "Viognier (Pays d’Oc)", "Petit Chablis"
    ],
    "Cépage": [
        "Grenache, Syrah", "Gamay", "Merlot, Cabernet Sauvignon", "Cabernet Franc",
        "Cabernet Franc", "Syrah, Grenache, Mourvèdre", "Syrah, Grenache", 
        "Grenache, Syrah, Mourvèdre", "Gamay", "Carignan, Grenache, Syrah",
        "Sauvignon Blanc", "Melon de Bourgogne", "Chardonnay", "Chenin Blanc", 
        "Chardonnay", "Sauvignon Blanc, Sémillon", "Riesling", "Sauvignon Blanc", 
        "Viognier", "Chardonnay"
    ],
    "Adjectifs": [
        "Rond, épicé, gourmand", "Léger, fruité, vif", "Structuré, généreux, élégant", 
        "Frais, souple, légèrement tannique", "Fruité, frais, délicat", 
        "Puissant, épicé, chaleureux", "Expressif, charnu, équilibré", 
        "Généreux, rond, épicé", "Léger, frais, fruité", "Rustique, épicé, charpenté", 
        "Minéral, vif, frais", "Sec, vif, léger", "Minéral, vif, élégant", 
        "Demi-sec, frais, floral", "Souple, fruité, floral", "Léger, frais, floral", 
        "Sec, vif, minéral", "Minéral, fumé, frais", "Floral, rond, aromatique", 
        "Léger, vif, minéral"
    ],
    "Arômes": [
        "Cerise, mûre, framboise", "Fraise, cerise, framboise", "Cassis, prune, groseille", 
        "Framboise, poivron, cerise noire", "Fraise, framboise, cerise", "Mûre, cassis, prune", 
        "Cerise, mûre, réglisse", "Fruits noirs, figue, poivre", "Cerise, framboise, mûre", 
        "Prune, mûre, épices", "Pomme verte, agrumes, groseille à maquereau", 
        "Pomme, citron, poire", "Pomme verte, agrumes, fleurs blanches", 
        "Pomme, poire, miel", "Pêche, poire, agrumes", "Pamplemousse, citron, fleurs blanches", 
        "Pomme, citron, pêche", "Pamplemousse, citron, herbes", "Abricot, pêche, fleur d'oranger", 
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
        "Corbières", "Minervois", "Cahors", "Bandol", "Madiran", "Côtes de Bourg", 
        "Côtes de Blaye", "Montagne-Saint-Émilion", "Pomerol", "Graves", 
        "Alsace Gewurztraminer", "Quincy", "Saint-Véran", "Pouilly-Loché", "Touraine", 
        "Menetou-Salon", "Côte de Beaune", "Petit Manseng", "Jurançon", "Côtes du Jura", 
        "Tavel", "Côtes de Provence", "Luberon", "Cabernet d'Anjou", "Bandol Rosé", 
        "Gris de Toul", "Rosé d'Anjou", "Coteaux d'Aix-en-Provence", "Clairet de Bordeaux", 
        "Coteaux Varois en Provence"
    ],
    "Cépage": [
        "Carignan, Syrah, Grenache", "Syrah, Grenache, Carignan", "Malbec", "Mourvèdre", 
        "Tannat", "Merlot, Cabernet Sauvignon", "Merlot, Cabernet Sauvignon", 
        "Merlot, Cabernet Franc", "Merlot, Cabernet Franc", "Cabernet Sauvignon, Merlot", 
        "Gewurztraminer", "Sauvignon Blanc", "Chardonnay", "Chardonnay", "Sauvignon Blanc", 
        "Sauvignon Blanc", "Chardonnay", "Petit Manseng", "Gros Manseng, Petit Manseng", 
        "Chardonnay, Savagnin", "Grenache, Cinsault", "Grenache, Cinsault, Syrah", 
        "Grenache, Syrah", "Cabernet Franc, Cabernet Sauvignon", "Mourvèdre, Grenache", 
        "Gamay, Pinot Noir", "Grolleau, Cabernet Franc", "Grenache, Syrah, Cinsault", 
        "Merlot, Cabernet Sauvignon", "Grenache, Syrah"
    ],
    "Adjectifs": [
        "Riche, charpenté, épicé", "Fruité, structuré, épicé", "Puissant, tannique, profond", 
        "Corsé, puissant, tannique", "Robuste, tannique, corsé", "Riche, fruité, rond", 
        "Élégant, fruité, souple", "Généreux, structuré, velouté", "Puissant, riche, onctueux", 
        "Complexe, charpenté, élégant", "Aromatique, ample, exotique", "Vif, minéral, élégant", 
        "Fruité, floral, frais", "Minéral, élégant, vif", "Léger, fruité, frais", "Minéral, vif, frais", 
        "Riche, équilibré, aromatique", "Moelleux, exotique, riche", "Suave, doux, fruité", 
        "Minéral, frais, élégant", "Puissant, fruité, généreux", "Léger, frais, fruité", 
        "Fruité, frais, léger", "Doux, fruité, frais", "Sec, élégant, puissant", "Léger, frais, fruité", 
        "Doux, fruité, gourmand", "Léger, vif, floral", "Fruité, généreux, vif", "Léger, frais, fruité"
    ],
    "Arômes": [
        "Mûre, prune, épices", "Cerise, mûre, poivre noir", "Cassis, mûre, truffe", 
        "Fruits noirs, poivre, épices", "Prune, cassis, épices", "Prune, cerise noire, groseille", 
        "Cassis, framboise, mûre", "Cerise, prune, cassis", "Prune, truffe, cerise noire", 
        "Cassis, prune, poivre", "Litchi, rose, épices", "Pamplemousse, citron, pomme verte", 
        "Pêche, poire, agrumes", "Pomme, citron, fleurs blanches", "Pomme, poire, agrumes", 
        "Pamplemousse, citron, fleurs blanches", "Pomme, noisette, agrumes", 
        "Ananas, mangue, abricot", "Pêche, abricot, agrumes", "Pomme, citron, noix", 
        "Fraise, groseille, cerise", "Fraise, pêche, agrumes", "Framboise, cerise, agrumes", 
        "Fraise, groseille, framboise", "Fraise, pêche, agrumes", "Pêche, framboise, fraise", 
        "Fraise, framboise, cerise", "Pêche, agrumes, fleurs blanches", "Cerise, fraise, framboise", 
        "Fraise, agrumes, pêche"
    ]
}

# Conversion en DataFrame
additional_df = pd.DataFrame(additional_data)

# Ajout des nouvelles données au DataFrame initial
df_extended = pd.concat([df, additional_df], ignore_index=True)

# Sauvegarde dans un fichier CSV avec les 50 vins
file_path_extended = "/mnt/data/selection_vins_francais_extended.csv"
df_extended.to_csv(file_path_extended, index=False, sep=';')

file_path_extended