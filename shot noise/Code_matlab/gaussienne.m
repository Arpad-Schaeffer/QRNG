% filepath: c:\Users\padou\OneDrive\Bureau\cours\X\physique\QRNG\data\shotnoise\Données shot noise\gaussienne.m
% --- Ajustement gaussien manuel (sans fitdist) ---
shot = real(evalin('base', 'sn_raw'));
elec = real(evalin('base', 'eln_raw'));
% Paramètres des lois normales
mu1 = mean(shot);
sigma1 = std(shot);

mu2 = mean(elec);
sigma2 = std(elec);

% Vecteur pour l’évaluation des densités
x = linspace(min([shot; elec], [], 'all'), max([shot; elec], [], 'all'), 1000);

% Calcul des densités gaussiennes
y1 = normpdf(x, mu1, sigma1);
y2 = normpdf(x, mu2, sigma2);

legend1 = sprintf('Fit Gaussien 1 (\\mu = %.2e, \\sigma = %.2e)', mu1, sigma1);
legend2 = sprintf('Fit Gaussien 2 (\\mu = %.2e, \\sigma = %.2e)', mu2, sigma2);

% Calcul des limites (exemple avec decoupe_gaussienne)
n = 3;  % Nombre de bits associés
limites = decoupe_gaussienne(mu1, sigma1, n);

figure;
hold on;  % permet d’afficher plusieurs choses sur le même graphe

% Affichage des histogrammes normalisés
histogram(shot, 'Normalization', 'pdf', 'FaceColor', [0.1 0.5 0.8], 'DisplayName', 'Shot noise');
histogram(elec, 'Normalization', 'pdf', 'FaceColor', [0.8 0.2 0.2], 'DisplayName', 'Electrical noise');

% Affichage des courbes ajustées
plot(x, y1, 'Color', [0.1 0.5 0.8], 'LineWidth', 2, 'DisplayName', legend1);
plot(x, y2, 'Color', [0.8 0.2 0.2], 'LineWidth', 2, 'DisplayName', legend2);

% Tracé d'une seule ligne pour la légende des limites
xline(limites(2), '--k', 'LineWidth', 1.5, 'DisplayName', 'Limites');

% Tracé des autres lignes sans légende
for i = 3:length(limites)-1
    xline(limites(i), '--k', 'LineWidth', 1.5, 'HandleVisibility', 'off');
end

% Personnalisation du graphique
xlabel('Valeur');
ylabel('Densité');
title('Courbes gaussiennes ajustées avec limites');
legend('show');
grid on;
hold off;