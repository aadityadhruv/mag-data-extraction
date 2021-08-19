import json
import csv
import pandas as pd
import numpy as np

files = ["/home/asdhruv2/scratch/mag_authors_" + str(i) + ".txt" for i in range(13)]

i = 0
j = 0
k = 0
with open('affiliations.csv', mode='w') as affiliations:
    affiliations_writer = csv.writer(affiliations, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    affiliations_writer.writerow(['author_id','name','normalized_name' ,'orgs', 'n_pubs'])

print("Starting affiliations job...")
failures = []
with open('affiliations.csv', mode='a') as affiliations:
    affiliations_writer = csv.writer(affiliations, delimiter=',', quotechar='"')
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
                    _orgs = obj["orgs"] if "orgs" in obj else []
                    _n_pubs = obj["n_pubs"] if "n_pubs" in obj else -1
                    if _orgs != []:
                        j += 1
                        org_list = [[_id,_name, _n_name, org,  _n_pubs] for org in _orgs]
                        for org in org_list:
                            affiliations_writer.writerow(org)
                except:
                    i += 1
                    failures.append(line)
            print("next file...")    

print("Failures: " , i)
print("Total records: " , k)
print("Unique records: " , j)
print("Success... completed job.")
with open("failures_affiliations.txt", "w") as file:
    for line in failures:
        file.write(line)
        file.write("\n")








