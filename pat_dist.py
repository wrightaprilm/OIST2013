import sys
import dendropy
from dendropy import treecalc
import Bio
import urllib2
from Bio import Entrez
import re

Entrez.email = 'wright.aprilm@gmail.com'

#def genetic_dist():
#	tree= dendropy.Tree.get_from_path("/Users/aprilwright/Desktop/projectfiles/MorphSim/Trees/amph_tree.tre", "newick")
#	label_1 = tree.taxon_set.get_taxon(label=sys.argv[1])
#	label_2 = tree.taxon_set.get_taxon(label=sys.argv[2])
#
#	d = treecalc.patristic_distance(tree,label_1, label_2)
#	print sys.argv[1], sys.argv[2], d
#	return label_2


def query_date_life():
	handle = Entrez.efetch(db="taxonomy", id=sys.argv[1])	
	record = Entrez.read(handle)
	species1 = "Homo_sapiens"
	species2= sys.argv[1]
	url_string = "http://www.itis.gov/ITISWebService/services/ITISService/getScientificNameFromTSN?tsn="
	newrl = url_string + species2
	response = urllib2.urlopen(newrl)	
	name_record = response.read()
	split_cord = re.split('<', name_record)
	for item in split_cord:
		if re.search('combinedName>', item):
			genus = re.findall('\w+ ', item)
			for item in genus:
				genus = str(genus)
			species = re.findall(' \w+' , item)
			for item in species:
				species = str(species)
				formatted_name = genus + species		
				print formatted_name
	print genus
query_date_life()	
