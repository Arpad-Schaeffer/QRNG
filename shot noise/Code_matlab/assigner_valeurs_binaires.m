function bin_indices = assigner_valeurs_binaires(values, limites, n)
    k = 2^n;  % Nombre d'intervalles
    bin_indices = zeros(size(values));

    for idx = 1:length(values)
        for i = 1:k
            if limites(i) <= values(idx) && values(idx) < limites(i+1)
                bin_indices(idx) = i;
                break;
            end
        end
        
    end

end
