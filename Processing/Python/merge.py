import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util

IN_ROOT = "./in"
group = "Arts"
base_file = "BtArtsBaseDataTable"
text_file = "BattleTextDictionary"
magic_file = "BtArtsMagicDataTable"
rank_file = "BtArtsRankDataTable"
inherit_file = "BtArtsInheritArtsDataTable"

IN_FORMAT = ".json"
OUT_FORMAT = ".json"
OUT_ROOT = "./out"

# STR_PROPS = ['Attribute',
# 			 'AddEffect',
# 			 'EffectType',
# 			 'BaseElement',
# 			 'BaseParameter']

# INT_PROPS = ['AddEffectParam',
# 			 'EffectParam']

# BOOL_PROPS = ["MonsterArts",
# 			"Magic",
# 			"Rankup",
# 			"OriginalArts",
# 			"SoulArts",
# 			"BloodArts",
# 			"InheritArts",
# 			"Invalid",
# 			"Inspiration"]

# EXTRA_PROPS = ["Sequence",
# 	        "DisableSelect",
# 	        "DisableOutActor",
# 	        "DisableOutActorObject",
# 			"Sortindex",
# 			"ArtsName",
# 			"ArtsText",
# 			"OverAttackFirst",
# 			"OverAttackLast",
# 			"BaseArts",
# 			"label"]

# ZERO_PROPS = ["Attack",
# 			"AttackCount",
# 			"AddSingleStageDamage",
# 			"AddOverAttackDamage",
# 			"BP",
# 			"Hit",
# 			"SureHit",
# 			"Hate",
# 			"Weapon",
# 			"WeaponSub",
# 			"Speed",
# 			"AfterCasterSpeed",
# 			"AfterTargetSpeed",
# 			"BeforeGuard",
# 			"AfterGuard",
# 			"OverAttack",
# 			"OverAttackLeft",
# 			"OverAttackRight",
# 			"OverAttackSelf",
# 			"Bump",
# 			"Limit",
# 			"HitArea",
# 			"Penetration",
# 			"RaceSlayer",
# 			"Random",
# 			"ReserveType",
# 			"ReserveProb",
# 			"ReserveCancel",
# 			"Trace",
# 			"TraceDifficulty",
# 			"Turn",
# 			"AddEffectSequence"]

# NONE_PROPS = ["BaseElement",
# 			"EffectType",
# 			"AddEffect"]

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def clean_props(_data: dict):
	for k,v in _data.items():
		for prop in STR_PROPS:
			if v[prop][0] == 0:

				v[prop] = ['None']
				continue
			else:
				_ls = []
				for ele in v[prop]:
					if ele == 0:
						break
					else:
						_ls.append(ele)
				v[prop] = _ls

		for prop in INT_PROPS:
			_ls = []
			for ele in v[prop]:
				if is_float(ele):
					_as_float = float(ele)
					_as_int = int(_as_float)
					if abs(_as_float - _as_int) > 0:
						_ls.append(int(float(vv)))
					else:
						_ls.append(_as_int)
			_len = len(v['EffectType'])
			if prop == 'AddEffectParam':
				_len = len(v['AddEffect'])
			v[prop] = _ls[0:_len]


		for prop in BOOL_PROPS:
			if not v[prop]:
				v.pop(prop)

		for prop in EXTRA_PROPS:
			v.pop(prop)

		for prop in NONE_PROPS:
			if v[prop][0] == 'None':
				v.pop(prop)
				if prop == 'EffectType':
					v.pop('EffectParam')
				elif prop == 'AddEffect':
					v.pop('AddEffectParam')

		for prop in ZERO_PROPS:
			if v[prop] == 0:
				v.pop(prop)

def inject_ui_text(_data):
	_text_data = f_util.load_json(f"{IN_ROOT}/{text_file}{IN_FORMAT}")
	_arts_text = _text_data['Battle_Arts']
	_arts_text_keys = list(_arts_text['name'].keys())
	_arts_desc_keys = list(_arts_text['desc'].keys())
	_arts_first_keys = list(_arts_text['first'].keys())
	_arts_last_keys = list(_arts_text['last'].keys())
	for k,v in _data.items():
		if k in _arts_text_keys:
			v.update({'ArtsName': _arts_text['name'][k]})
		if k in _arts_desc_keys:
			v.update({'ArtsText': _arts_text['desc'][k]})
		if k in _arts_first_keys:	
			v.update({'OverAttackFirst': _arts_text['first'][k]})
		if k in _arts_last_keys:
			v.update({'OverAttackLast': _arts_text['last'][k]})

def add_rank_info(_data, _keys):
	_target = f_util.load_json(f"{IN_ROOT}/{rank_file}{IN_FORMAT}")
	_target_keys = list(_target.keys())
	for k,v in _target.items():
		if k in _keys:
			_data[k]['RankInfo'] = v

def add_monster_info(_data, _keys):
	_target = f_util.load_json(f"{IN_ROOT}/{monster_file}{IN_FORMAT}")
	_target_keys = list(_target.keys())
	for k,v in _target.items():
		if k in _keys:
			v.pop('Actor')
			_base[k]['MonsterInfo'] = v

def add_magic_info(_data, _keys):
	_target = f_util.load_json(f"{IN_ROOT}/{magic_file}{IN_FORMAT}")
	_target_keys = list(_target.keys())
	for k,v in _target.items():
		if k in _keys:
			_data[k]['ElementLv'] = v['ElementLv']

def add_inherit_info(_data):
	_target = f_util.load_json(f"{IN_ROOT}/{inherit_file}{IN_FORMAT}")
	for item in _target:
		_data[item['ID']]["InheritType"] = item['Type']

def merge_target_into_base():
	_base        = f_util.load_json(f"{IN_ROOT}/{base_file}{IN_FORMAT}")
	_base_keys   = _base.keys()

	inject_ui_text(_base)
	add_rank_info(_base, _base_keys)
	add_magic_info(_base, _base_keys)
	add_inherit_info(_base)

	_new_data = []
	for k,v in _base.items():
		v["ID"] = k
		_new_data.append(v)

	
	with open(f"{OUT_ROOT}/ArtsBase{OUT_FORMAT}", "w", encoding="utf-8") as outfile: 
	    json.dump(_new_data, outfile, indent = 4)

if __name__ == "__main__":
	merge_target_into_base()
