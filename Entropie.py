import matplotlib.pyplot as plt

# Données d'exemple
shot_noise = [0.999999002902380, 1.999994219079088, 2.999993720192213, 3.999988910046850, 4.999983607415463, 5.999958552979077, 6.999887333388171, 7.999664037084800]
elec_noise = [0.999998018953857, 1.798076440964921, 2.720303818071622, 3.696653530581686, 4.689975030737737, 5.688254202670185, 6.687720484499577, 7.687306596765112]

# Calcul de la différence
difference = [a - b for a, b in zip(shot_noise, elec_noise)]
ratio = [a / b for a, b in zip(elec_noise, shot_noise)]

# Indices pour l'abscisse
x = range(1,len(shot_noise)+1)
plt.style.use('bmh')  # Utilisation du style 'bmh' pour le graphique
plt.plot(x, shot_noise, label=r"$H(X)_{tot}$", color='blue', marker='o')  # Ronds pour Shot Noisea
plt.plot(x, elec_noise, label=r"$H(X)_{elec}$", color='red', marker='s')  # Carrés pour Elec Noise
plt.legend(fontsize = 12)
plt.xlabel('Nombre de bits associés')
plt.ylabel('Entropie (bits)')
plt.title(r"Entropies totale $H(X)_{tot}$ et électrique $H(X)_{elec}$ en fonction du nombre de bits associés")
plt.show()
# Création de la figure et des sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Tracé des deux listes sur le premier graphique avec des symboles
ax1.scatter(x, difference, label=r"Entropie quantique $H(X)_{tot}-H(X)_{elec}$", color='blue', marker='o')  # Ronds pour Shot Noise
ax1.set_ylabel('Entropie quantique (bits)')
ax1.legend()

# Tracé de la différence sur le deuxième graphique avec des carrés reliés par des traits
ax2.plot(x, ratio, color='green', marker='s', linestyle='')  # Carrés pour la différence
ax2.set_xlabel('Nombre de bits associés')
ax2.set_ylabel(r"$\frac{H(X)_{elec}}{H(X)_{tot}}$",fontsize = 15)
ax2.set_ylim(0.7, 1.1)  # Limite de l'axe y pour le deuxième graphique
ax2.legend()

# Ajustement de l'espacement entre les sous-graphiques
plt.tight_layout()

# Affichage du graphique
plt.show()