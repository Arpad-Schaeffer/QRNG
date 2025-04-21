function limites = decoupe_gaussienne(mu, sigma, n)
    k = 2^n;  % Nombre d'intervalles
    quantiles = linspace(0, 1, k + 1);
    limites = norminv(quantiles, mu, sigma);
    limites(1) = -inf;
    limites(end) = inf;
end
