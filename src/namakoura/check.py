import hashlib 

file="__main__.py"

def get_hash(filename:str=file)->str:
    m = hashlib.sha256()
    with open(filename,"rb") as f:
        file_content=f.read()
    # print(file_content)
    m.update(file_content)
    return m.hexdigest()

# print(get_hash())
# print("C:\\Windows\\notepad.exe")
# print(get_hash("C:\\Windows\\notepad.exe"))
