import json
# import hashlib
import pandas as pd
import numpy as np



df = pd.DataFrame(columns=['AuID', 'AuN', 'AuNN', 'AuF', 'AuP'])

i = 0

files = ["/home/asdhruv2/scratch/mag_authors_" + str(i) + ".txt" for i in range(13)]

print("Starting...")

failures = []
for file in files:
    print(file)
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                newobj = {
                 'AuID': obj["id"] if "id" in obj else "None",
                 'AuN': obj["name"] if "name" in obj else "None",
                 'AuNN' : obj["normalized_name"]if "normalized_name" in obj else "none",
                 'AuF' : obj["orgs"] if "orgs" in obj else [],
                 'AuP' : obj["n_pubs"] if "n_pubs" in obj else -1
                }
                df = df.append(newobj, ignore_index=True)


            except:
                i += 1
                failures.append(line)
        print("sucess")

print("Failures: " , i)


with open("/home/asdhruv2/scratch/failures.txt", "r+") as file:
    for line in failures:
        file.write(line)
        file.write("\n")


df.to_pickle("/home/asdhruv2/scratch/mag_databse.pkl")
