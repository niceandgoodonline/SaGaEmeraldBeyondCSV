# SaGaEmeraldBeyondCSV
CSV data from the game SaGa Emerald Beyond

# What is it?
The data is split into 2 major categories: PlanDataTable and TextTableData.

PlanDataTables are the raw information the game uses on the back end. Each DataTable has its own data structure.

TextTableData are a uniform data structure and is used to populate the UI text fields.

Many of the PlanDataTables are not human readable -- they contain only numerical data and keys to match with TextTableData. 

# Recommended Use
To transform this raw data into useful information you will need to merge multiple PlanDataTables together, cull many default/null values, and replace maybe keys with their human readable TextTableData. 

Use Python + numpy + pandas or your favourite tool chain.