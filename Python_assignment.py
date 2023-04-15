import pandas as pd
users_df = pd.read_csv('D://Python_assignment//Copy of Python Assignment - (Input) User IDs.csv')
rigor_df = pd.read_csv('D://Python_assignment//Copy of Python Assignment - (Input) Rigorbuilder RAW.csv')
merged_df = pd.merge(users_df.rename(columns={'User ID': 'uid'}), rigor_df, on='uid')
grouped_df = merged_df.groupby('Team Name').mean().reset_index()
sorted_df = grouped_df.sort_values(['total_statements', 'total_reasons'], ascending=[False, False]).reset_index(drop=True)
sorted_df['Team Rank'] = sorted_df.index + 1

output_df = sorted_df[['Team Rank', 'Team Name', 'total_statements', 'total_reasons']].rename(columns={'total_statements': 'Average Statements', 'total_reasons': 'Average Reasons'})

output_df.to_csv('output.csv', index=False)

print('Output saved to output.csv')
print(output_df)
import csv


def sort_key(row):
    return (-int(row['total_statements']), -int(row['total_reasons']), row['name'])


with open('D://Python_assignment//Copy of Python Assignment - (Input) Rigorbuilder RAW.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)


rows.sort(key=sort_key)


print('Rank'.ljust(5), 'Name'.ljust(15), 'UID'.ljust(8), 'No. of Statements'.ljust(20), 'No. of Reasons')


with open('output2.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Rank', 'Name', 'UID', 'No. of Statements', 'No. of Reasons'])
    for i, row in enumerate(rows):
        rank = i + 1
        writer.writerow([str(rank), row['name'], row['uid'], row['total_statements'], row['total_reasons']])
        print(str(rank).ljust(5), row['name'].ljust(15), row['uid'].ljust(8), row['total_statements'].ljust(20), row['total_reasons'])
