import json
import csv
import pandas as pd
import numpy as np



files = ["/home/asdhruv2/scratch/mag_authors_" + str(i) + ".txt" for i in range(13)]

i = 0

with open('affiliations.csv', mode='w') as affiliations:
    affiliations_writer = csv.writer(affiliations, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    affiliations_writer.writerow([':START_ID',':END_ID',':TYPE' ,'NAME', 'N_NAME', 'N_PUBS:int'])


print("Starting csv job;...")
failures = []
with open('affiliations.csv', mode='a') as affiliations:
    affiliations_writer = csv.writer(affiliations, delimiter=',', quotechar='"')
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    id_ = obj["id"] if "id" in obj else "None"
                    name_ = obj["name"] if "name" in obj else "None"
                    n_name_ = obj["normalized_name"]if "normalized_name" in obj else "none"
                    orgs_ = obj["orgs"] if "orgs" in obj else []
                    n_pubs_ = obj["n_pubs"] if "n_pubs" in obj else -1
                    if orgs_ != []:
                        org_list = [[id_,org,'AFFILIATED', name_, n_name_,  n_pubs_] for org in orgs_]
                        for org in org_list:
                            affiliations_writer.writerow(org)
                except:
                    i += 1
                    failures.append(line)


print("Failures: " , i)

print("sucess...")
with open("failures2.txt", "w") as file:
    for line in failures:
        file.write(line)
        file.write("\n")








