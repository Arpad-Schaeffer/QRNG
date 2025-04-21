function plot_entropies_from_variables(n)
    % Définition des variables à analyser
    var_names = {'shot_noise', 'elec_noise'};
    
    % Initialisation de la structure pour stocker les entropies
    entropies_struct = struct();

    figure; hold on;
    
    try
        % Calcul des limites à partir de la variable 'shot_noise'
        shot_noise_values = evalin('base', var_names{1});  % Récupère 'shot_noise' depuis le workspace
        mu = mean(shot_noise_values);
        sigma = std(shot_noise_values);
        limites = cell(1, n);
        for j = 1:n
            limites{j} = decoupe_gaussienne(mu, sigma, j);  % Calcul des limites pour chaque k
        end
    catch ME
        error('Erreur lors du calcul des limites à partir de ''shot_noise'' : %s', ME.message);
    end

    for i = 1:length(var_names)
        var_name = var_names{i};
        try
            values = evalin('base', var_name);  % Récupère la variable depuis le workspace

            entropies = zeros(1, n);

            for j = 1:n
                bin_indices = assigner_valeurs_binaires(values, limites{j}, j);
                entropies(j) = calculer_entropie(bin_indices);
            end

            % Stockage des entropies dans la structure
            entropies_struct.(var_name) = entropies;

            % Tracé des entropies
            plot(1:n, entropies, '-o', 'DisplayName', var_name);
        catch ME
            warning('Erreur avec la variable %s : %s', var_name, ME.message);
        end
    end

    % Calcul de la différence des entropies entre 'shot_noise' et 'elec_noise'
    if isfield(entropies_struct, 'shot_noise') && isfield(entropies_struct, 'elec_noise')
        entropies_struct.difference = entropies_struct.shot_noise - entropies_struct.elec_noise;
    else
        warning('Impossible de calculer la différence des entropies : une ou plusieurs variables manquent.');
    end

    % Sauvegarde des entropies dans un fichier .mat
    save('entropies.mat', 'entropies_struct');

    legend('show');
    title('Entropie vs Nombre de bits');
    xlabel('Nombre de bits (n)');
    ylabel('Entropie');
    grid on;
end
