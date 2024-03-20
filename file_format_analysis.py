import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_rows = 300
from pathlib import Path

# Recursively find all siegfried.csv and add their full paths to list
all_csv = []
for path in Path('/Users/syblack/Desktop/sf_fits').rglob('*siegfried.csv'):
    all_csv.append(str(path))
#print(all_csv)

# Read all siegfried.csv into dataframe
df1 = pd.concat((pd.read_csv(f, encoding = "ISO-8859-1") for f in all_csv))

# Recursively find all *fits.xml and add their full paths to list
all_fits = []
for path in Path('/Users/syblack/Desktop/sf_fits').rglob('*fits.xml'):
    all_fits.append(str(path))
#print(all_fits)

# Read all *fits.xml into dataframe. First occurence of <identity> tag is included.
df2 = pd.concat((pd.read_xml(xml, xpath="/*[name()='fits']/*[name()='identification']/*[name()='identity'][1]") for xml in all_fits))
# Re-name *fits.xml columns to match siegfried
df2.rename(columns={'mimetype': 'mime', 'externalIdentifier': 'id'}, inplace=True)
df2.to_csv('/Users/syblack/Desktop/df2.csv', index=False)

# Concatenate the 2 DataFrames
df = pd.concat([df1, df2], ignore_index=True, sort=False)
#print(df.columns.tolist())
# Save file format counts to CSV
#(df['format'].value_counts().to_csv('/Users/syblack/Desktop/file_format_counts.csv', index=True, header=True))

# Make a simple plot by adding .plot() to DataFrame
# ax = df['format'].value_counts().plot(kind='pie', figsize=(20, 20), title='File Formats')
# plt.tight_layout()
# ax.figure.savefig('/Users/syblack/Desktop/file_formats_pie.pdf')