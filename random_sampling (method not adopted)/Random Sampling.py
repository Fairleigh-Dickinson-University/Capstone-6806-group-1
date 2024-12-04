import numpy as np

def random_sampling_with_heuristics(adj_matrix, current_similarity_matrix, n_iterations, sampling_rate, heuristic='degree'):
    """
    Perform random sampling with heuristics for similarity computations.
    
    Parameters:
        adj_matrix (np.ndarray): Adjacency matrix of the graph.
        current_similarity_matrix (np.ndarray): Current similarity matrix (R_n).
        n_iterations (int): Number of iterations.
        sampling_rate (float): Proportion of nodes to sample (e.g., 0.1 for 10%).
        heuristic (str): Sampling heuristic, 'degree' or 'random'.

    Returns:
        np.ndarray: Updated similarity matrix after sampling-based iterations.
    """
    n_nodes = adj_matrix.shape[0]
    sampled_similarity_matrix = current_similarity_matrix.copy()
    degrees = np.sum(adj_matrix, axis=1)

    for iteration in range(n_iterations):
        print(f"Iteration {iteration + 1}/{n_iterations}: Performing sampling...")

        # Step 1: Select nodes based on sampling rate and heuristic
        n_sampled = int(sampling_rate * n_nodes)
        if heuristic == 'degree':
            sampled_nodes = np.argsort(degrees)[-n_sampled:]  # Top nodes by degree
        elif heuristic == 'random':
            sampled_nodes = np.random.choice(n_nodes, size=n_sampled, replace=False)
        else:
            raise ValueError("Invalid heuristic. Use 'degree' or 'random'.")

        # Step 2: Update similarity matrix for sampled nodes
        new_similarity_matrix = np.zeros_like(sampled_similarity_matrix)
        for i in sampled_nodes:
            for j in range(n_nodes):
                if i != j:
                    new_similarity_matrix[i, j] = compute_node_similarity(i, j, adj_matrix, sampled_similarity_matrix)

        # Step 3: Normalize the updated matrix
        row_sums = np.sum(new_similarity_matrix, axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1  # Avoid division by zero
        sampled_similarity_matrix = new_similarity_matrix / row_sums

    return sampled_similarity_matrix

def compute_node_similarity(i, j, adj_matrix, similarity_matrix):
    """
    Compute the similarity between two nodes using a Jaccard-based approach.
    """
    neighbors_i = set(np.where(adj_matrix[i] > 0)[0])
    neighbors_j = set(np.where(adj_matrix[j] > 0)[0])
    intersection = len(neighbors_i & neighbors_j)
    union = len(neighbors_i | neighbors_j)
    return intersection / union if union > 0 else 0
