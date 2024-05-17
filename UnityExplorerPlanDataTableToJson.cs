var d = CurrentTarget as Il2Cpp.WorldAreaDataTable;
string table_name = d.name;
Dictionary<string, Dictionary<string, string>> dump = new Dictionary<string, Dictionary<string, string>>();

string _skip = "System.IntPtr";
string _str_array_type = "Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppStringArray";
string _bool_array_type = "Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppStructArray`1[System.Boolean]";
string _int_array_type = "Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppStructArray`1[System.Int32]";
string _int_ref_array_type = "Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppReferenceArray`1[Il2Cpp.InspirationInfo]";
string _diff_ref_array_type = "Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppReferenceArray`1[Il2Cpp.DifficultyInfo]";
bool _sparse_string_array = false;
string _sparse_string_match = "_NOT_SPECIFIED_";

bool _sparse_bool_array = false;
bool _spare_bool_match = false;

bool _sparse_int_array = false;
int _sparse_int_match = 0;

string[] reject_prop = {"WasCollected", "autoLineBreak", "label", "price"};
for (int j = 0; j < d.Length; j++) {
	var x = d[j];
	var t = x.GetType();
	List<PropertyInfo> props = new List<PropertyInfo>(t.GetProperties());
	Dictionary<string, string> rebuild = new Dictionary<string, string>();
	Dictionary<string, Dictionary<string, string>> _dump = new Dictionary<string, Dictionary<string, string>>();
	var label = "";
	foreach (PropertyInfo prop in props)
	{
		var prop_t = prop.PropertyType.ToString();
		if (prop_t != _skip)
		{
			var val = prop.GetValue(x, null);
			var val_s = val.ToString();
			string name = prop.Name;
			bool skip_prop = false;
			
			if (name == "label")
			{
				label = val_s;
			}
			
			foreach (string _reject in reject_prop)
			{
				if (_reject == name) 
				{
					skip_prop = true;
				}
			}
					
			if (skip_prop == true)
			{
				continue;
			}
			
			if (val_s == _str_array_type)
			{
				var _ls = val as Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppStringArray;
				var _s = "[";
				for (int i = 0; i < _ls.Length; i++)
				{
					if (_ls[i] == _sparse_string_match)
					{
						if (_sparse_string_array)
						{
							_s += $"'{i}:{_ls[i]}',";
						}
						else
						{
							continue;
						}
					}
					else
					{
						_s += $"'{_ls[i]}',";
					}
				}
				_s = _s.Substring(0, _s.Length - 1) + "]";
				if (_s == "]") {
					_s = "['None']";
				}
				rebuild.Add(name, _s);
			}
			else if (val_s == _bool_array_type)
			{
				var _ls = val as Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppStructArray<bool>;
				var _s = "[";
				for (int i = 0; i < _ls.Length; i++)
				{
					_s += $"'{_ls[i]}',";
				}
					_s = _s.Substring(0, _s.Length - 1) + "]";
					rebuild.Add(name, _s);
			}
			else if (val_s == _int_array_type)
			{
				var _ls = val as Il2CppInterop.Runtime.InteropTypes.Arrays.Il2CppStructArray<int>;
				var _s = "[";
				for (int i = 0; i < _ls.Length; i++)
				{
					_s += $"'{_ls[i]}',";
				}
					_s = _s.Substring(0, _s.Length - 1) + "]";
					rebuild.Add(name, _s);
			}
			// else if (val_s == _diff_ref_array_type)
			// {
			// 	var _diff_array = x.DifficultyInfo;
			// 	for (int i = 0; i < _diff_array.Length; i++)
			// 	{
			// 		rebuild.Add($"RewardItem{i}", _diff_array[i].Reward);
			// 		rebuild.Add($"RewardAmount{i}", $"{_diff_array[i].Num}");
			// 	}
			// }
			else
			{
				rebuild.Add(name, val_s);
			}
		}
	}
	dump.Add(label, rebuild);
}
var json_options = new JsonSerializerOptions { WriteIndented = true };
System.IO.File.WriteAllText($"{table_name}.json", JsonSerializer.Serialize(dump, json_options));