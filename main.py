# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from mean_var_std import calculate

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

main(module='test_module', exit=False)