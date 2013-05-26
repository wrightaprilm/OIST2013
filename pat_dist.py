import sys
import dendropy
from dendropy import treecalc
import Bio
import urllib2
from Bio import Entrez
import re
import csv

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
	with open("ngram_results.csv", 'rw') as f: 
		f_reader = csv.reader(f)
		for row in f_reader:
#			print row[0]
#			handle = Entrez.efetch(db="taxonomy", id=row[0])	
#			handle = Entrez.efetch(db="taxonomy", id=sys.argv[1])	
#			record = Entrez.read(handle)
			species1 = "Homo_sapiens"
			species2= row[0]
			url_string = "http://www.itis.gov/ITISWebService/services/ITISService/getScientificNameFromTSN?tsn="
			newrl = url_string + species2
			response = urllib2.urlopen(newrl)	
			name_record = response.read()
		#	print name_record
			split_cord = re.split('<', name_record)
			for item in split_cord:
				if re.search('combinedName>', item):
					genus = re.findall('\w+ ', item)
					species = re.findall(' \w+' , item)
					if len(genus) == 1:
						final_name = genus[0] + '_' + species[0]
						final_name = final_name.replace(' ', '')
						dl_string = "http://datelife.org/cgi-bin/R/result?input="
						seps = "%2C+"
						capper = "&format=bestguess&partial=liberal&useembargoed=yes&uncertainty=100&usetnrs=yes&tnrssource=NCBI"
						dl_query = dl_string + species1 + seps + final_name + capper
						dl_response = urllib2.urlopen(dl_query)	
						dl_read = dl_response.read()
						print dl_read
						with open("output.txt", 'w') as f: f.write(dl_response.read())

				else:
					break
			
#			print dl_read
#			print dl_query
				
query_date_life()	
