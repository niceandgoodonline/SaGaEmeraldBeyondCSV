import os
import pandas as pd

BATTLE_DATA_ROOT = "./PlanDataTable/Battle"
BATTLE_TEXT_ROOT = "./TextTableData/Battle"

EXTENSION = ".csv"

TEXT_PREFIX = "TextTableData_"
TEXT_SUFFIX = "__en_.csv"

OUTPUT_ROOT = "./clean"

NS = "_NOT_SPECIFIED_"

def get_file_names(_path: str) -> set:
	_items = os.listdir(_path)
	r = {}
	for item in _items:
		if EXTENSION in item:
			_key = item.replace(EXTENSION, "")
			r[_key] = f"{_path}/{item}"
	return r


def get_dir_names(_path: str) -> set:
	_items = os.listdir(_path)
	r = {}
	for item in _items:
		if EXTENSION not in item:
			r[item] = get_file_names(f"{_path}/{item}")
	return r

def get_text_file_names(_path: str) -> set:
	_items = os.listdir(_path)
	r = {}
	for item in _items:
		if EXTENSION in item:
			_key = item.replace(TEXT_PREFIX, "").replace(TEXT_SUFFIX, "")
			r[_key] = f"{_path}/{item}"
	return r

def convert_to_list(_obj):
	_l = [x.split(" ") for x in _obj]
	return _l

def replace_ns(_obj):
	_l = [str(x).replace(NS, "None").replace("nan", "None") for x in _obj]
	return _l


def process_group(group, group_name: str):
	for k,v in group.items():
		df = df = pd.read_csv(v, encoding='utf_8')
		for col in df.columns:
			df[col] = replace_ns(df[col])
			# if " " in str(df[col][0]):
			# 	df[col] = convert_to_list(df[col])
		df.to_csv(f"{OUTPUT_ROOT}/{group_name}/{k}.csv", index=False)


if __name__ == "__main__":
	common = get_file_names(BATTLE_DATA_ROOT)
	groups = get_dir_names(BATTLE_DATA_ROOT)
	groups['Common'] = common
	text_battle = get_text_file_names(BATTLE_TEXT_ROOT)
	groups['Text'] = text_battle

	_key = 'Text'
	process_group(groups[_key], _key)
