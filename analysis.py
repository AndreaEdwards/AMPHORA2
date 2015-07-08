import os
import subprocess
from util import FileHandlers

file_handlers = FileHandlers()
file_paths = file_handlers.search_directory()
fasta_files = file_handlers.find_files(file_paths, 'faa')
print len(fasta_files)

#path = '/Users/andrea/repositories/AMPHORA2/all.faa/Aggregatibacter_actinomycetemcomitans_D11S_1_uid41333/NC_013416.faa'
#cmd = ['perl ./Scripts/MarkerScanner.pl -Bacteria ' + path]
#print cmd
#subprocess.call(cmd, shell=True)


for path in fasta_files:
	cmd = ['perl ./Scripts/MarkerScanner.pl -Bacteria ' + path]
	subprocess.call(cmd, shell=True)

#echo = "echo"
#for path in fasta_files:
#	os.system(echo + " perl ./Scripts/MarkerScanner.pl -Bacteria " + path)
#	os.system(echo + "\n")