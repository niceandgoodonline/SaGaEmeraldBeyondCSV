import re,json,os

CLEAN_ROOT = "./clean"
LIST_REGEX = "\[[a-zA-Z0-9',]*\]"
POP_TEXT = "POP_LIST_HERE"
JSON_OUT = "./json"
IN_FORMAT = ".csv"
OUT_FORMAT = ".json"

def get_file_names(_path: str) -> set:
	_items = os.listdir(_path)
	r = []
	for item in _items:
		if IN_FORMAT in item:
			_key = item.replace(IN_FORMAT, "")
			r.append(item.replace(IN_FORMAT, ""))
	return r


def get_dir_names(_path: str) -> set:
	_items = os.listdir(_path)
	r = {}
	for item in _items:
		if IN_FORMAT not in item:
			r[item] = get_file_names(f"{_path}/{item}")
	return r

def dump_clean_to_json(group: str, file_name: str):
	f = open(f"{CLEAN_ROOT}/{group}/{file_name}{IN_FORMAT}", "r", encoding="utf8")
	keys = f.readline().replace("\n", "").split(",")
	_array = []
	count = 0
	as_list = list(f)
	for row in as_list:
		_lists = re.findall(LIST_REGEX, row)
		flat_row = re.sub(LIST_REGEX, POP_TEXT, row)
		split_row = flat_row.replace("\n", "").split(",")
		_data = {}
		for index in range(len(keys)):
			_entry = split_row[index]
			if _entry == POP_TEXT:
				_entry = _lists.pop(0).replace("'", "").replace("[", "").replace("]", "").split(",")
			_data[keys[index]] = _entry
		_array.append(_data)

	with open(f"{JSON_OUT}/{group}/{file_name}{OUT_FORMAT}", "w", encoding="utf-16-be") as outfile: 
	    json.dump(_array, outfile, indent = 4)

if __name__ == "__main__":
	groups = get_dir_names(CLEAN_ROOT)

	for k,v in groups.items():
		for file in v:
			dump_clean_to_json(k, file)