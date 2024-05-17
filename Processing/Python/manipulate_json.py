import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util
JSON_ROOT = "./json"
IN_FORMAT = ".json"
OUT_FORMAT = ".json"

def get_dir_names(_path: str) -> set:
	_items = os.listdir(_path)
	r = {}
	for item in _items:
		if IN_FORMAT not in item:
			r[item] = get_file_names(f"{_path}/{item}")
	return r

def convert_to_int(_data: dict) -> dict:
	for k,v in _data.items():
		for kk,vv in v.items():
			if isinstance(vv, str):
				if vv.isnumeric():
					v[kk] = int(vv)
				elif is_float(vv):
					_as_float = float(vv)
					_as_int = int(_as_float)
					if abs(_as_float - _as_int) > 0:
						v[kk] = int(float(vv))
					else:
						v[kk] = _as_int
				elif vv == 'False':
					v[kk] = False
				elif vv == 'True':
					v[kk] = True
			elif isinstance(vv, list):
				for index in range(len(vv)):
					if isinstance(vv, str) and vv[index].isnumeric():
						vv[index] = int(vv[index])
					# elif vv[index] == 'None':
					# 	vv[index] = 0
				v[kk] = vv
		_data[k] = v
	return _data

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
	group = 'Trade'
	files = f_util.get_file_names(f"{JSON_ROOT}/{group}")
	for f in files:
		_obj = f_util.load_json(f"{JSON_ROOT}/{group}/{f}{IN_FORMAT}")
		if isinstance(_obj, list):
			_obj = f_util.list_to_dict(_obj, 'label', True)
		inted = convert_to_int(_obj)
		f_util.write_dict_to_json(f"{JSON_ROOT}/{group}/{f}{OUT_FORMAT}", inted)
