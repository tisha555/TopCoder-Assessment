# Qwen Model Runs for Problem "Maximizing Tree Diameter with Removals"

All runs used Qwen3-235B-A22B-2507 with thinking disabled. The model failed on all test cases for each attempt due to incorrect handling of DP states for removals and path computations.

- Run 1: https://chat.qwen.ai/conversation/run01-failed (Failed on test case 1: Incorrectly ignored paths through nodes, only considered subtree diameters.)
- Run 2: https://chat.qwen.ai/conversation/run02-failed (Failed on test case 2: Misdistributed removals in downward paths, leading to overestimation.)
- Run 3: https://chat.qwen.ai/conversation/run03-failed (Failed on test case 3: Forgot to handle cases with fewer than 2 children for paths through nodes.)