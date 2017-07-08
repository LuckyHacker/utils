import sys
import difflib

with open(sys.argv[1], "rb") as f:
	dataset1 = f.read()

with open(sys.argv[2], "rb") as f:
	dataset2 = f.read()

def compare(dataset1, dataset2):
	match = difflib.SequenceMatcher(None,dataset1,dataset2)
	print("Data match percent: {}%".format(match.ratio() * 100))

compare(dataset1, dataset2)
