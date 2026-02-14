import json
import os
with open("modules.json",'r')as f:
    data = json.load(f)
newData = '\n'.join(data["MANAGED"].keys())
print(newData)
