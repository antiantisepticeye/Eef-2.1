from fuzzywuzzy import process 

def fuzzy_search(query, choices):
	res = process.extract(query, choices, limit=15)
	return sorted([ i[0] for i in res if i[1] > 80 ], key=lambda a: a[1], reverse=True)