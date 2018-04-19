import leveldb
import sys

path = sys.argv[1]

db = leveldb.LevelDB(path)

print db

for x in db.RangeIter():
	print x
