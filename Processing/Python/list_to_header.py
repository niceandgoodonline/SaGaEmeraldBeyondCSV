import re,json,os,sys
sys.path.insert(1, './modules/')
import f_util

IN_ROOT = "./in"
IN_FORMAT = ".json"
OUT_FORMAT = ".json"
OUT_ROOT = "./out"

string_list = [
	"Attack",
	"AttackCount",
	"AddSingleStageDamage",
	"AddOverAttackDamage",
	"BP",
	"Hit",
	"SureHit",
	"Hate",
	"Weapon",
	"WeaponSub",
	"Speed",
	"AfterCasterSpeed",
	"AfterTargetSpeed",
	"Attribute",
	"AfterGuard",
	"OverAttack",
	"OverAttackLeft",
	"OverAttackRight",
	"OverAttackSelf",
	"Bump",
	"Limit",
	"HitArea",
	"Penetration",
	"RaceSlayer",
	"Random",
	"ReserveType",
	"ReserveProb",
	"ReserveCancel",
	"TargetType",
	"TargetParty",
	"Trace",
	"TraceDifficulty",
	"Turn",
	"BaseElement",
	"AddEffect",
	"DisableSelect",
	"DisableOutActor",
	"DisableOutActorObject",
	"ArtsName",
	"ArtsText",
	"OverAttackFirst",
	"OverAttackLast",
	"BloodArts",
	"InheritArts",
	"Inspiration",
	"Invalid",
	"Magic",
	"MonsterArts",
	"OriginalArts",
	"Rankup",
	"SoulArts"]


if __name__ == "__main__":
	ComponentHeaderName = "ART_COLUMNS"
	OPEN_FORMAT = "\n\t{\n\t\t"
	PROP_FORMAT = "\n\t\t"
	CLOSE_FORMAT = "\n\t},"
	with open(f"{OUT_ROOT}/{ComponentHeaderName}.js", "w", encoding="utf-8") as f: 
		f.write(f"export const {ComponentHeaderName} = [")
		for item in string_list:
			human_formatted = re.sub('([A-Z])', r' \1', item).strip()
			f.write(f"{OPEN_FORMAT}Header: '{human_formatted}',{PROP_FORMAT}accessor: '{item}'{CLOSE_FORMAT}")
		

