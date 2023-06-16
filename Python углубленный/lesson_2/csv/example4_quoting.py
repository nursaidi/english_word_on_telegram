import csv

quoting = csv.QUOTE_ALL

with open('data/output.csv', 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['firstname', 'lastname', 'age'],
        quoting=quoting
    )

    writer.wri
