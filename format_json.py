import json, sys
try:
	with open(sys.argv[1], "r") as f:
		data = f.read()

	parsed = json.loads(data)
	data = json.dumps(parsed, indent=4, sort_keys=True)

	with open(sys.argv[1], "w") as f:
		f.write(data)
except:
	print("python3 %s filepath" % sys.argv[0])
