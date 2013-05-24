import sys
import dendropy
from dendropy import treecalc
tree= dendropy.Tree.get_from_path("/Users/aprilwright/Desktop/projectfiles/MorphSim/Trees/amph_tree.tre", "newick")
label_1 = tree.taxon_set.get_taxon(label=sys.argv[1])
label_2 = tree.taxon_set.get_taxon(label=sys.argv[2])

d = treecalc.patristic_distance(tree,label_1, label_2)
print sys.argv[1], sys.argv[2], d
