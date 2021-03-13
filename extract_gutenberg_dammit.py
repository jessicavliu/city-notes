import gzip, json

all_lines = []
for line in gzip.open("gutenberg-poetry-v001.ndjson.gz"):
    all_lines.append((json.loads(line.strip())['s']))#.encode('utf-8'))

for i in range(10):
	print(all_lines[i])

print("Unprocessed lines:")

unprocessed = 0
'''f = open("poetry.txt", "w", encoding="utf-8")
for i in range(10):
	f.write(all_lines[i])
f.close()'''
'''f = open("poetry.txt", "w", encoding="utf-8")
for line in all_lines:
	try:
		f.write(line + "\n")
	except:
		unprocessed += 1
		print(line)
f.close()'''

print()
print(str(len(all_lines)) + " lines total")
print(str(len(all_lines) - unprocessed) + " lines processed")