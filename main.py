import json

from deepface import DeepFace


#face matching

#result = DeepFace.verify(img1_path ="m4.jpg", img2_path ="m5.jpg")

#print(json.dumps(result, indent=2))

#find face in db

#dfs = DeepFace.find(img_path = "a1.jpg", db_path = "./db")

#print(dfs)


import json
import numpy as np

def convert(o):
    if isinstance(o, np.generic):
        return o.item()
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
objs = DeepFace.analyze(img_path = "m2.jpg")
print(json.dumps(objs, indent=2, default=convert))
