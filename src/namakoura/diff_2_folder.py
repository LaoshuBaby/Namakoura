import os
from check import get_hash

path_1 = "C:\\Games\\MINECRAFT\\星星档案馆\\world-20250107-2125"
path_2 = "C:\\Games\\MINECRAFT\\星星档案馆\\world-20250121-0108-0800"

file_list_1 = os.listdir(path_1)
file_list_2 = os.listdir(path_2)

# print(len(file_list_1))
# print(len(file_list_2))
# print(file_list_1)
# print(file_list_2)

# 假定path2是比path1新的

modified_file=[]
unmodified_file=[]

for file in file_list_2:
    if file not in file_list_1:
        modified_file.append(file)
    else:
        sum_1=get_hash(os.path.join(path_1,file))
        sum_2=get_hash(os.path.join(path_2,file))
        if sum_1 == sum_2:
            unmodified_file.append(file)
        else:
            modified_file.append(file)

print("modified file num:", len(modified_file))
print("unmodified file num:", len(unmodified_file))

print("="*15)

feature_display=True
feature_copy_to_new_folder=True

# for i in modified_file