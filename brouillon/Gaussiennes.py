import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def decoupe_gaussienne(mu, sigma, k):
    """
    Découpe une gaussienne de moyenne mu et d'écart-type sigma en k intervalles d'aires égales,
    couvrant toute la distribution de -infini à +infini.
    """
    # Calcul des quantiles qui divisent la loi normale en k parties égales (aire cumulée égale)
    quantiles = np.linspace(0, 1, k + 1)  # Bornes des intervalles de -inf à +inf
    limites = stats.norm.ppf(quantiles, loc=mu, scale=sigma)  # Points de découpe
    limites[0], limites[-1] = -np.inf, np.inf  # Garantir que toute la gaussienne est couverte
    return limites

def tracer_gaussienne_et_decoupe(mu, sigma, k):
    """
    Trace la gaussienne avant et après découpe en k intervalles de même aire.
    """
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = stats.norm.pdf(x, loc=mu, scale=sigma)
    
    limites = decoupe_gaussienne(mu, sigma, k)
    
    # Calcul et affichage des aires de chaque portion
    aires = [stats.norm.cdf(limites[i+1], loc=mu, scale=sigma) - stats.norm.cdf(limites[i], loc=mu, scale=sigma) for i in range(k)]
    print("Aires des intervalles:", aires)
    print("Bornes des intervalles:", limites[1:-1])
    
    # Tracé de la gaussienne initiale
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label="Densité de la gaussienne", color='blue', linewidth=2)
    
    # Ajout des lignes de découpe
    colors = plt.cm.viridis(np.linspace(0, 1, k))  # Palette de couleurs pour les zones
    for i in range(1, k):  # On ignore -inf et +inf dans le tracé des lignes
        plt.axvline(limites[i], color='black', linestyle='--', alpha=0.7, label=f'Borne {i}: x = {limites[i]:.2f}')
    
    for i in range(k):
        x_fill = np.linspace(max(limites[i], mu - 4*sigma), min(limites[i+1], mu + 4*sigma), 100)
        y_fill = stats.norm.pdf(x_fill, loc=mu, scale=sigma)
        plt.fill_between(x_fill, y_fill, alpha=0.3, color=colors[i], label=f'Zone {i+1} (Aire ≈ {aires[i]:.3f})')
    
    plt.title(f"Découpe de la gaussienne en {k} intervalles de même aire")
    plt.xlabel("x")
