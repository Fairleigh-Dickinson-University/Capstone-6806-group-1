
# Random Sampling with Heuristics

## Overview
This semi-project implements a Python module for integrating random sampling with heuristics into MSC algorithm.

The goal of Random Sampling with Heuristics is to reduce computational cost by focusing computations on a representative subset of nodes, selected based on certain heuristics.

## Implementation Steps:
1. Random Sampling of Nodes: Use random sampling to select a subset of nodes to compute during each iteration.

2. Heuristic-Guided Sampling: Use heuristics such as degree centrality to prioritize influential nodes.

3. Skip or Partial Update: Only perform full similarity and Markov similarity computations for the selected nodes.

## Why This Method Was Not adpoted:
However, this method was not adopted finally, because of:

Loss of Accuracy: By focusing only on a sampled subset of nodes, the algorithm missed important global relationships in the network.

Incomplete Updates: Nodes not selected in the sampled subset will not have their similarity scores updated for that iteration. This does not make full sense.


## Usage

In the MSC code, replace the full similarity computation step with a call to this module:

```python
# Inside the MSC iteration loop
from random_sampling_module import random_sampling_with_heuristics

# Parameters for sampling
sampling_rate = 0.1  # 10% of nodes
heuristic = 'degree'  # Use degree-based sampling

# Compute Markov similarity with sampling
sampled_similarity_matrix = random_sampling_with_heuristics(
    adj_matrix=A,
    current_similarity_matrix=R_n,
    n_iterations=n_iterations,
    sampling_rate=sampling_rate,
    heuristic=heuristic
)

# Update R_n with the sampled similarity matrix
R_n = sampled_similarity_matrix
```


### Example Workflow
```python
import numpy as np
from random_sampling_with_heuristics import random_sampling_with_heuristics

# Example adjacency matrix
adj_matrix = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])

# Initial similarity matrix (R₀)
similarity_matrix = np.identity(4)

# Run the Random Sampling with Heuristics
result = random_sampling_with_heuristics(
    adj_matrix=adj_matrix,
    current_similarity_matrix=similarity_matrix,
    n_iterations=5,
    sampling_rate=0.5,  # Sample 50% of nodes
    heuristic='degree'  # Use degree-based sampling
)

print("Updated Similarity Matrix:")
print(result)
```
