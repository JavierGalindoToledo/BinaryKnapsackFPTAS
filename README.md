# BinaryKnapsackFPTAS
A Fully Polynomial Time Approximation Scheme (FPTAS) for the 0/1 knapsack problem provides a solution that can be made arbitrarily close to optimal in polynomial time. Below, is a summary a common FPTAS for the 0/1 knapsack problem and suggest improvements to make it faster.
### FPTAS Overview
The basic idea is to scale down the profits to make the dynamic programming table smaller and solve the scaled version of the problem. The steps are:
  1. Let 𝜖 > 0 be the desired approximation factor.
  2. Scale profits: For each item with profit $p_i$, replace $p_i$ with a scaled value $p'_i$ such that
                                                $p'_i = floor{p_i}{K}$
