import json
import csv
import pandas as pd
import numpy as np



files = ["/home/asdhruv2/scratch/mag_papers_" + str(i) + ".txt" for i in range(11)]

i = 0
k = 0
with open('papers.csv', mode='w') as papers:
    papers_writer = csv.writer(papers, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
    papers_writer.writerow(['paper_id','title','year'])


print("Starting extracting papers job...")
failures = []
with open('papers.csv', mode='a') as papers:
    papers_writer = csv.writer(papers, delimiter=',', quotechar='"')
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            print("opening file " + file)
            for line in f:
                k += 1
                try:
                    obj = json.loads(line)
                    _id = obj["id"] if "id" in obj else "None"
                    _title = obj["title"] if "title" in obj else "None"
                    _year = obj["year"]if "year" else -1
                    papers_writer.writerow([_id, _title, _year])
                except:
                    i += 1
                    failures.append(line)
            print("next file...")

print("Failures: " , i)
print("Total records: " , k)
print("Success... completed job.")
with open("failures_papers.txt", "w") as file:
    for line in failures:
        file.write(line)
        file.write("\n")








