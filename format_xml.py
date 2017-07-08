import lxml.etree as etree, sys

x = etree.parse(sys.argv[1])
with open(sys.argv[1] + ".txt", "w") as f:
	f.write(str(etree.tostring(x, pretty_print = True), "utf-8"))
	
