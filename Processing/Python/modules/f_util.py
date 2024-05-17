import json, os, time, shutil

def check_file_exists(_file_name):
	return os.path.exists(_file_name)

def check_directory(_directory: str):
	if not os.path.exists(_directory):
		os.mkdir(_directory)
		return False
	else:
		return True

def get_file_names(_path: str, _extension = '.json') -> set:
	_items = os.listdir(_path)
	r = []
	for item in _items:
		if _extension in item:
			_key = item.replace(_extension, "")
			r.append(item.replace(_extension, ""))
	return r

def backup_file(_file_name):
	if (check_file_exists):
		shutil.move(_file_name, f"{_file_name}.{time.time()}")

def load_json(_file_name, _mode = "rb"):
	_f = {}
	with open(_file_name, _mode) as _json_file:
			_f = json.load(_json_file)
	_json_file.close()
	return _f

def list_to_dict(_array, _index_key, pop_key = False) -> dict:
	_data = {}
	for item in _array:
		_key = item[_index_key]
		if pop_key:
			item.pop(_index_key)
		_data[_key] = item
	return _data

def write_dict_to_json(_file_name: str, _json: dict, _indent: int = 4, _seperators: tuple = (", ", ": "), _sort_keys: bool = False):
	_t = ".json"
	if check_file_exists(_file_name):
		_t = f".{time.time()}.json"
		print(f"file already exists for {_file_name}. saving as {_file_name.replace('.json', _t)}")
	_file_name = f"{_file_name.replace('.json', _t)}"
	with open(_file_name, 'w+') as f:
		json.dump(_json, f, indent=_indent, separators=_seperators, sort_keys=_sort_keys)
	f.close()
