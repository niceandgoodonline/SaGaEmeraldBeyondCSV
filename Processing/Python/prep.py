import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util

IN_ROOT = "./in"
base_file = "ArtsBase"

IN_FORMAT = ".json"
OUT_FORMAT = ".json"
OUT_ROOT = "./out"

nameless_blood_keys = {
	"THS_WH000_B01_BLD01": {"ArtsName": "Sanguine Wind", },
	"OHG_GL000_B03_BLD02": {},
	"THG_GH000_B02_BLD01": {},
	"MAR_MA000_B06_BLD01": {}
}

nameless_soul_keys = [
	"THS_WH000_A02_SOUL_BASE",
	"THS_WH000_A04_SOUL_BASE",
	"THG_GH000_B02_SOUL_BASE"
]

nameless_custom_keys = [
	"OHS_WLAXE_B03_EX1_BASE",
	"THS_WHSSW_B04_EX1_BASE",
	"THS_WHPSW_A01_EX1_BASE",
	"THS_WHPSW_B04_EX1_BASE"
]

sparse_keys = [
	"Random",
	"Penetration",
    "ElementLv",
    "AttackCount",
    "RaceSlayer"
]

main_keys = [
    "ID",
    "ArtsName",
    "ArtsText",
    "BP",
    "BaseParameter",
    "Attribute",
    "Hate",
    "Attack",
    "AddSingleStageDamage",
    "AddOverAttackDamage",
    "TargetType",
    "TargetParty",
    "HitArea",
    "RankInfo",
    "RankMax",
    "AfterTargetSpeed",
    "AfterCasterSpeed",
    "Bump",
    "Limit",
    "Trace",
    "TraceDifficulty",
    "ReserveType",
    "ReserveProb",
    "ReserveCancel",
    "OverAttack",
    "OverAttackFirst",
    "OverAttackLast",
    "OverAttackSelf",
    "OverAttackLeft",
    "OverAttackRight",
    "Random",
	"Penetration",
    "ElementLv",
    "AttackCount",
    "RaceSlayer"
]

join_keys = {
	"GuardType": ["AfterGuard","BeforeGuard"],
	"AttackType": ["Weapon", "WeaponSub", "InheritType", "BaseElement"],
	"HitType": ["Hit", "SureHit"],
	"SpeedType": ["Turn", "Speed"],
}

effect_keys = {
	"EffectInfo": ["EffectType", "EffectParam"],
	"AddEffectInfo": ["AddEffect", "AddEffectParam"]
}


def generate_rank_string(rankData):
	rankData.pop(0)
	count = 1
	rkstr = ""
	for rkdata in rankData:
		rkstr += f" Rank{count}: Count {rkdata['Count']}"
		if rkdata['BP'] > 0:
			rkstr += f", BP -{rkdata['BP']}"
		if rkdata['Turn'] > 0:
			rkstr += f", Turn -{rkdata['Turn']}"
		count += 1
		rkstr += ","
	return trim_trailing_comma(rkstr)

def trim_trailing_comma(value: str) -> str:
	return value[0:len(value)-1].strip()

def dump_keys(_data):
	key_set = set()
	for elem in _data:
		for k,v in elem.items():
			key_set.add(k)
	with open(f"{OUT_ROOT}/key_dump{OUT_FORMAT}", "w", encoding="utf-8") as outfile: 
	    json.dump(list(key_set), outfile, indent = 4)


if __name__ == "__main__":
	_base    = f_util.load_json(f"{IN_ROOT}/{base_file}{IN_FORMAT}")
	_out_player_array = []
	# _out_monster_array = []
	# _out_dummy_array = []
	count = 0
	for elem in _base:
		_keys = elem.keys()
		if "AddEffects" in _keys:
			if len(elem["AddEffects"]) != len(elem["AddEffectParam"]):
				print(elem["ID"])
		# if "ArtsName" not in _keys:
		# 	print(elem['ID'])


	# for item in _base:
	# 	_new_data = {}
	# 	_id = item["ID"]
	# 	_new_data["ID"] = _id
	# 	if _id == 'THS_WH000_B01_BLD01':
	# 		_new_data['ArtsName'] = "Sanguine Wind"
	# 		# _new_data['ArtsText'] = 

	# 	item_keys = item.keys()
		
	# 	for key in main_keys:
	# 		if key in item_keys:
	# 			_value = item[key]
	# 			if key == 'Weapon' and 'WeaponSub' in item_keys:
	# 				_value += f":{item['WeaponSub']}"
	# 			elif key == 'RankInfo':
	# 				_new_data['RankMax'] = _value['MaxRank']
	# 				_new_data['RankEffects'] = generate_rank_string(_value['RankEffects'])
	# 				continue
	# 			elif key == "EffectType":
	# 				_effect_str = ""
	# 				_index = 0
	# 				for item in _value:
	# 					_effect_str += f" {_value[_index]}: {item['EffectParam'][_index]},"
	# 				if _effect_str != "":
	# 					_new_data['Effects'] = trim_trailing_comma(_effect_str)
	# 				continue
	# 			elif key == "AddEffect":
	# 				_effect_str = ""
	# 				_index = 0
	# 				for item in _value:
	# 					_effect_str += f" {_value[_index]}: {item['AddEffectParam'][_index]},"
	# 				if _effect_str != "":
	# 					_new_data['AddEffect'] = trim_trailing_comma(_effect_str)
	# 				continue
	# 			elif isinstance(_value, list):
	# 				if _value[0] == "None":
	# 					continue
	# 				else:
	# 					_str = ""
	# 					for elem in _value:
	# 						_str += f" {elem},"
	# 					if _str != "":
	# 						_new_data[key] = trim_trailing_comma(_str)
	# 						continue
	# 			elif isinstance(_value, bool):
	# 				if _value:
	# 					_value = "True"
	# 				else:
	# 					_value = "False"

	# 			_new_data[key] = _value

	# 	_sparse_str = ""	
	# 	for key in sparse_keys:
	# 		if key in item_keys:
	# 			if key == "Random":
	# 				_sparse_str += f" Random: {item['Random']},"
	# 			elif key == "Penetration":
	# 				_sparse_str += f" Penetration: {item['Penetration']},"

	# 	if _sparse_str != "":
	# 		_new_data['RareProperty'] = trim_trailing_comma(_sparse_str)

	# 	art_type = "p"
	# 	if "EN_M" in _id:
	# 		art_type = "m"
	# 	elif "ARTS_0" in _id:
	# 		art_type = "d"

	# 	if art_type == "p":
	# 		_out_player_array.append(_new_data)
	# 	elif art_type == "m":
	# 		_out_monster_array.append(_new_data)
	# 	else:
	# 		_out_dummy_array.append(_new_data)

	# with open(f"{OUT_ROOT}/MinimalPlayerArtsBase{OUT_FORMAT}", "w", encoding="utf-8") as outfile: 
	#     json.dump(_out_player_array, outfile, indent = 4)

	# with open(f"{OUT_ROOT}/MinimalEnemyArtsBase{OUT_FORMAT}", "w", encoding="utf-8") as outfile: 
	#     json.dump(_out_monster_array, outfile, indent = 4)

	# with open(f"{OUT_ROOT}/MinimalDummyArtsBase{OUT_FORMAT}", "w", encoding="utf-8") as outfile: 
	#     json.dump(_out_dummy_array, outfile, indent = 4)
