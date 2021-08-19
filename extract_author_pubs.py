import json
import csv
import pandas as pd
import numpy as np



files = ["/home/asdhruv2/scratch/mag_authors_" + str(i) + ".txt" for i in range(13)]

i = 0
j = 0
k = 0
with open('pubs.csv', mode='w') as pubs:
    pubs_writer = csv.writer(pubs, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    pubs_writer.writerow(['author_id','name','normalized_name' ,'pub'])


print("Starting extracting pubs job...")
failures = []

with open('pubs.csv', mode='a') as pubs:
    pubs_writer = csv.writer(pubs, delimiter=',', quotechar='"')
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            print("opening file " + file)
            for line in f:
                k += 1
                try:
                    obj = json.loads(line)
                    _id = obj["id"] if "id" in obj else "None"
                    _name = obj["name"] if "name" in obj else "None"
                    _n_name = obj["normalized_name"]if "normalized_name" in obj else "none"
                    _pubs = obj["pubs"] if "pubs" in obj else []
                    if _pubs != []:
                        j += 1
                        pubs_list = [[_id,_name, _n_name, pub['i']] for pub in _pubs]
                        for pub in pubs_list:
                            pubs_writer.writerow(pub)
                except:
                    i += 1
                    failures.append(line)

            print("next file...")    
print("Failures: " , i)
print("Total records: " , k)
print("Unique records: " , j)
print("Success... completed job.")
with open("failures_pubs.txt", "w") as file:
    for line in failures:
        file.write(line)
        file.write("\n")








