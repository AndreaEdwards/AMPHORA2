import subprocess
from util import FileHandlers
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO

file_handlers = FileHandlers()
#file_paths = file_handlers.search_directory()
#fasta_files = file_handlers.find_files(file_paths, 'faa')

#for path in fasta_files:
#	cmd = ['perl ./Scripts/MarkerScanner.pl -Bacteria ' + path]
#	subprocess.call(cmd, shell=True)

file_paths = file_paths = file_handlers.search_directory()
pep_files = file_handlers.find_files(file_paths, 'pep')

for path in pep_files:
	file_name = file_handlers.get_file_name(path)
	name_list = file_name.split('.')
	out_file = ''.join([name_list[0] + '_out.' + name_list[1]])
	cmd = ['muscle -in ' + path + ' -out ' + out_file]
	subprocess.call(cmd, shell=True)

#aln = AlignIO.read('path/to/alignnment/file', 'format (i.e. phylip)')
#calculator = DistanceCalculator('identity') # identity is the name of the model(scoring matrix) to calculate the distance. The identity model is the default one and can be used both for DNA and protein sequence.
#dm = calculator.get_distance(aln)