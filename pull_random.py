import sys
import Bio
import urllib2
from Bio import Entrez
import re
Entrez.email = 'wright.aprilm@gmail.com'

if len(sys.argv[1]) > 0:
	try:
		handle = Entrez.esearch(db="taxonomy", term=sys.argv[1])	
		record = Entrez.read(handle)
#		print record['IdList']
		t_id = record['IdList']
#		print t_id
	except urllib2.HTTPError, e:
		if e.code == 404:
			print "whoops"
		if e.code == 400:
			print "oh neaux"
	t_handle = Entrez.esearch(db="taxonomy", term=t_id)	
	t_record = Entrez.read(t_handle)
	print t_record
		