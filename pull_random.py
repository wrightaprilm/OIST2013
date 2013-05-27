import sys
import Bio
import urllib2
from Bio import Entrez
import re
import tempfile

Entrez.email = 'wright.aprilm@gmail.com'
def get_species():
	if len(sys.argv[1]) > 0:
		try:
			url_start = "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name="
			new_rl = url_start + sys.argv[1]
			response = urllib2.urlopen(new_rl)	
			name_record = response.read()
			binom = re.search(r'<STRONG>(\w+ \w+)', name_record).groups()
		except urllib2.HTTPError, e:
			if e.code == 404:
				print "whoops"
			if e.code == 400:
				print "oh neaux"
		return binom
		
		
def query_date_life():
	i=0

	species1 = "Homo_sapiens"
	species2= get_species()
	if len(species2) >= 1:
		binom = re.search(r'(\W+)', species2).groups()
#		final_name = genus[0] + '_' + species[0]	
#		final_name = final_name.replace(' ', '')
#		dl_string = "http://datelife.org/cgi-bin/R/result?input="
#		seps = "%2C+"
#		capper = "&format=bestguess&partial=liberal&useembargoed=yes&uncertainty=100&usetnrs=yes&tnrssource=NCBI"
#		dl_query = dl_string + species1 + seps + final_name + capper
#		dl_response = urllib2.urlopen(dl_query)	
#		dl_read = dl_response.read()
#		print dl_read
#		with open("output.txt", 'w') as f: f.write(dl_response.read())
#		i=i+1
#		print i

#	except urllib2.HTTPError, e:
#		if e.code == 404:
#			print "whoops"
#		else:
#			pass
	

query_date_life()	

	