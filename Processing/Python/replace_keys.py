import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util

IN_ROOT = "./json"
IN_FORMAT = ".json"
OUT_FORMAT = ".json"
OUT_ROOT = "./merged-json"

TEXT_ROOT = f"{IN_ROOT}/Text"

substrings = [
	"_ArtsName",
	"_ArtsExp",
	"_OverAttackFirst",
	"_OverAttackLast",
	"_EnemyName",
	"_FormationName",
	"_FormationExp",
	"_ItemName",
	"_ItemExp",
	"_RoleName",
	"_RoleDescription"
]

if __name__ == "__main__":
	text_files_names = f_util.get_file_names(TEXT_ROOT)
	translate = {}
	text_collection = {}
	for file_name in text_files_names:
		_obj = f_util.load_json(f"{TEXT_ROOT}/{file_name}{IN_FORMAT}")
		text_collection[file_name] = _obj
		match file_name:
			case "Battle_Arts":
				translate[file_name] = {'name': {}, 'desc': {}, 'first': {}, 'last': {}}
			case "Battle_EnemyName":
				translate[file_name] = {'name': {}}
			case _:
				translate[file_name] = {'name': {}, 'desc': {}}


	for k,v in text_collection.items():
		for kk,vv in v.items():
			for substring in substrings:
				if substring in kk:
					match substring:
						case "_ArtsName":
							translate[k]['name'].update({kk.replace(substring, ""): vv['text']}) 
						case "_ArtsExp":
							translate[k]['desc'].update({kk.replace(substring, ""): vv['text']}) 
						case "_OverAttackFirst":
							translate[k]['first'].update({kk.replace(substring, ""): vv['text']}) 
						case "_OverAttackLast":
							translate[k]['last'].update({kk.replace(substring, ""): vv['text']}) 
						case "_EnemyName":
							translate[k]['name'].update({kk.replace(substring, ""): vv['text']}) 
						case "_FormationName":
							translate[k]['name'].update({kk.replace(substring, ""): vv['text']}) 
						case "_FormationExp":
							translate[k]['desc'].update({kk.replace(substring, ""): vv['text']}) 
						case "_ItemName":
							translate[k]['name'].update({kk.replace(substring, ""): vv['text']}) 
						case "_ItemExp":
							translate[k]['desc'].update({kk.replace(substring, ""): vv['text']}) 
						case "_RoleName":
							translate[k]['name'].update({kk.replace(substring, ""): vv['text']}) 
						case "_RoleDescription":
							translate[k]['desc'].update({kk.replace(substring, ""): vv['text']}) 

	f_util.write_dict_to_json(f"{OUT_ROOT}/TextNamesDescptionsMerged{OUT_FORMAT}", translate)