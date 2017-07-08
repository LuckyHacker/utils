import sys
import sqlite3

try:
    filepath = sys.argv[1]
    to_file = filepath.split(".")[0] + ".sql"
except:
    print("python3 dumpsql.py <filepath>")
    sys.exit()

conn = sqlite3.connect(filepath)
with open(to_file, "wb") as f:
    for line in conn.iterdump():
        f.write(bytes("%s\n" % line, "utf-8"))
