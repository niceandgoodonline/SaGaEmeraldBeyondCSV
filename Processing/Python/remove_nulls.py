import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util

IN_ROOT = "./in"
base_file = "ArtsBase"

IN_FORMAT = ".json"
OUT_FORMAT = ".json"
OUT_ROOT = "./out"


skip_props = [
	"Sequence",
	"DisableOutActor",
	"DisableOutActorObject",
	"DisableSelect",
	"AddEffectSequence"
]

null_checks = {
	"ArtsName": "None",
	"ArtsText": "None",
	"Weapon": "None",
	"WeaponSub": "None",
	"Attribute": "None",
	"Attack": "0",
	"AttackCount": "0",
	"BP": "0",
	"Turn": "0",
	"Hit": "0",
	"Speed": "0",
	"AfterCasterSpeed": "0",
	"AfterTargetSpeed": "0",
	"Bump": "0",
	"Hate": "0",
	"Random": "0",
	"BaseParameter": "None",
	"BaseElement": "None",
	"EffectType": "None",
	"EffectParam": "0",
	"AddEffect": "None",
	"AddEffectParam": "0",
	"AddEffectSequence": "None",
	"HitArea": "None",
	"SureHit": "0",
	"Penetration": "0",
	"BeforeGuard": "0",
	"AfterGuard": "0",
	"RaceSlayer": "None",
	"ReserveCancel": "0",
	"ReserveType": "None",
	"ReserveProb": "0",
	"DisableSelect": "0",
	"OverAttack": "0",
	"OverAttackLeft": "0",
	"OverAttackSelf": "0",
	"OverAttackRight": "0",
	"AddOverAttackDamage": "0",
	"AddSingleStageDamage": "0",
	"Trace": "0",
	"TraceDifficulty": "0",
	"Limit": "0",
	"TargetParty": "None",
	"TargetType": "None",
	"InheritType": "None"
}

if __name__ == "__main__":
	_base = f_util.load_json(f"{IN_ROOT}/{base_file}{IN_FORMAT}")
	null_keys = null_checks.keys()
	_out_data = []

	dict_count = 0
	unknown_count = 0
	for elem in _base:
		if isinstance(elem, dict):
			dict_count += 1
		else:
			unknown_count += 1
		_new_data = {}
		_id = elem["ID"]
		_new_data["ID"] = _id
		keys = list(elem.keys())
		_k = []
		_v = []
		for key in keys:
			if key in skip_props:
				continue
			if key in null_keys:
				_val = elem[key]
				_null_value = null_checks[key]
				has_value = False
				if isinstance(_val, list):
					for i in _val:
						if i != _null_value:
							has_value = True
				elif _val != _null_value:
					has_value = True

				if has_value:
					_new_data[key] = _val
			else:
				_k.append(key)
				_v.append(elem[key])
		count = 0
		for i in _k:
			_new_data[i] = _v[count]
			count +=1
		_out_data.append(_new_data)

	with open(f"{OUT_ROOT}/MinimalArtsBase{OUT_FORMAT}", "w", encoding="utf-8") as outfile: 
		json.dump(_out_data, outfile, indent = 4)

