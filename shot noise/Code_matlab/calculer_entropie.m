function H = calculer_entropie(bin_indices)
    total = numel(bin_indices);
    counts = histcounts(bin_indices, 'BinMethod', 'integers');
    probs = counts / total;
    probs(probs == 0) = [];
    H = -sum(probs .* log2(probs));
    
end
