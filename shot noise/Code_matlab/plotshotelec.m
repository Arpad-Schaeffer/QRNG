% Supposons que eln_raw_time, eln_raw, sn_raw_time et sn_raw soient déjà définis

figure; % Crée une nouvelle figure
plot(elec_noise, 'b-', 'DisplayName', 'eln\_raw'); % Trace la première courbe en bleu
hold on; % Permet de superposer la courbe suivante
plot(shot_noise, 'r-', 'DisplayName', 'sn\_raw'); % Trace la deuxième courbe en rouge

xlabel('Temps');
ylabel('Valeur');
title('eln\_raw et sn\_raw en fonction du temps');
legend show; % Affiche la légende automatiquement selon DisplayName
grid on; % Active la grille
