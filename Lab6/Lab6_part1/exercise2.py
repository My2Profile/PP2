
import os
 
# Checking existence
path1 = os.access("row.txt", os.F_OK)
print("Exists the path:", path1)
 
# Checking readaility
path2 = os.access("row.txt", os.R_OK)
print("Access to read the file:", path2)
 
# Checking writability
path3 = os.access("row.txt", os.W_OK)
print("Access to write the file:", path3)
 
# Checking executed
path4 = os.access("row.txt", os.X_OK)
print("Check if path can be executed:", path4)