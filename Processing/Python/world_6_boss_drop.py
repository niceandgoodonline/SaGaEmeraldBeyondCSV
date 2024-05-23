import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util

IN_ROOT = "./in"
text_file = "BattleTextDictionary"
nme_data_file = "BtEnemyDataTable"
nme_set_file = "BtEnemySetDataTable"
nme_set_pattern_file = "BtEnemySetPatternDataTable"

IN_FORMAT = ".json"
OUT_FORMAT = ".json"
OUT_ROOT = "./out"

boss_keys = ["E_W06_EVILCELL_A",
			"E_W06_EVILCELL_B",
			"E_W06_SAFED_A",
			"E_W06_VALKOINEN_A",
			"E_W06_CANCER_A",
			"E_W06_CANCER_B",
			"E_W06_PARASITE_A",
			"E_W06_SUPERPARASITE_A",
			"E_W06_SUPERPARASITE_B"]

if __name__ == "__main__":
	_nme_data        = f_util.load_json(f"{IN_ROOT}/{nme_data_file}{IN_FORMAT}")
	_nme_set         = f_util.load_json(f"{IN_ROOT}/{nme_set_file}{IN_FORMAT}")
	_nme_set_pattern = f_util.load_json(f"{IN_ROOT}/{nme_set_pattern_file}{IN_FORMAT}")

	_text_data       = f_util.load_json(f"{IN_ROOT}/{text_file}{IN_FORMAT}")
	nme_text         = _text_data['Battle_EnemyName']['name']
	nme_name_keys    = list(nme_text.keys())
	item_names       = _text_data['Battle_ItemEquip']['name']
	item_desc        = _text_data['Battle_ItemEquip']['desc']	

	world_6_bosses = {}
	for k,v in nme_text.items():
		_slice = k[4::]
		if _slice in boss_keys:
			world_6_bosses[_slice] = {"displayName": v}

	for k,v in world_6_bosses.items():
		if k in _nme_data:
			v['data'] = _nme_data[k]
		if k in _nme_set.keys():
			_array = []
			_s = _nme_set[k]['SetPattern']
			for char in _s:
				_array.append(char)
			if "1" in _array:
				print(k, " has set pattern")
				count = 0
				for elem in _array:
					if elem == "1":
						print(count)
					count += 1
