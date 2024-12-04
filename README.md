# Capstone-6806-Group-1

## Group Member, ID, and Email: 
Daozheng Qu, 2073879, d.qu@student.fdu.edu;
Yuchuan Wang, 2083927, y.wang9@student.fdu.edu;
Min Luo, 2091360, m.luo1@student.fdu.edu;
Chu Liu, 2072044, c.liu1@student.fdu.edu;
Hang Su, 2088646, h.su@student.fdu.edu.

## MSC Algorithm:
Daozheng Qu, Chu Liu, Yuchuan Wang, Hang Su, Min Luo.

## Integrating MSC with Threshold-Based Convergence
Yuchuan Wang, Hang Su.

## Integrating MSC with Random Sampling with Heuristics
Daozheng Qu, Chu Liu, Min Luo. 

## Overview

This project integrates Markov Similarity Clustering (MSC) with a threshold-based convergence approach for community detection in graph data. The implementation computes community structures based on node similarity, and visualizes initial and final community graphs.

## Features

- **Community Detection:** Utilizes Markov Similarity to iteratively detect communities until a convergence threshold or maximum number of iterations is reached.
- **Threshold-Based Convergence:** Uses the Frobenius norm to measure convergence between similarity matrices across iterations.
- **Visualization:** Graphs of both the initial and final community structures are generated and saved as images.
- **Community Merging:** Small communities can be merged with larger ones based on similarity metrics to refine the community structure.
- **Modularity Calculation:** Calculates the modularity (Q) value of the community structure to evaluate the quality of detected communities.

## How to Use

1. Prepare an file containing an adjacency matrix representing your graph data. Ensure that relationships are indicated with `1`s and non-relationships with `0`s.

2. Run the main function with appropriate parameters:

   ```python
   main_community_detection_from_xls_file('dataset.xlsx', lambda_val=5, max_iterations=100, tolerance=1e-5)
   ```

   - **`lambda_val`**: Threshold for deciding whether a community is small and should be merged.
   - **`max_iterations`**: Maximum number of iterations for convergence.
   - **`tolerance`**: Convergence threshold for the Frobenius norm.

## Functions

### `main_community_detection_from_xls_file(filename, lambda_val, max_iterations, tolerance)`
Reads an `.xls` file and performs community detection.

### `read_xls_as_adjacency_matrix(filename)`
Converts the `.xls` file into an adjacency matrix.

### `compute_markov_similarity_from_adj_matrix_with_threshold(A, max_iterations, tolerance)`
Computes node similarity using a threshold-based Markov process until convergence or max iterations.

### `find_communities(R_n)`
Identifies communities based on node similarity.

### `merge_small_communities(initial_communities, A, lambda_val)`
Merges small communities with larger ones based on similarity metrics.

### `calculate_modularity(communities, A)`
Calculates the modularity score to evaluate community quality.

### Visualization Functions
- `plot_initial_community_graph(initial_communities, most_similar_pairs, filename)`
- `plot_final_community_graph(A, final_communities, filename)`
