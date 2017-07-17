'''
CHAMP (Convex Hull of Admissible Modularity Partitions) implementation
'''
from .champ_functions import create_coefarray_from_partitions
from .champ_functions import create_halfspaces_from_array
from .champ_functions import get_intersection
from .champ_functions import get_random_halfspaces
from .louvain_ext import PartitionEnsemble
from .louvain_ext import parallel_louvain
from .louvain_ext import run_louvain
from .plot_domains import plot_2d_domains
from .plot_domains import plot_single_layer_modularity

