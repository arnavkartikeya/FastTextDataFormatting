import sys
import pandas as pd
pd.options.mode.chained_assignment = None 
import os
import csv
import re
from sklearn.model_selection import train_test_split

script_input = sys.stdin.read()
script_input = script_input.rstrip("\n")
script_input= script_input.split(" ")
ratio = 0.2
if(len(script_input)==4):
    ratio = float(script_input[3])
    
csv_path = script_input[0]

input_headers = script_input[1]
input_headers = input_headers.split(",")

output_header = script_input[2]

input_headers.append(output_header)

data = pd.read_csv(csv_path)

input_df = data[input_headers]

def strip_formatting(string):
    string = string.lower()
    string = re.sub(r"([.!?,'/()])", r" \1 ", string)
    return string

for i in range(len(input_df)):
    for col in input_df.columns:
        if(str(col) != output_header):
            input_df.at[i, col] = strip_formatting(input_df.at[i, col])


count = -1
hashtable = {}
for i in range(len(input_df)):
    if(input_df[output_header][i] in hashtable):
        input_df[output_header][i] = hashtable[input_df[output_header][i]]
    else:
        count += 1
        hashtable[input_df[output_header][i]] = "__label__" + str(count)
        input_df[output_header][i] = hashtable[input_df[output_header][i]]

input_df, test_df = train_test_split(input_df, test_size=ratio)

with open('train.txt', 'w') as f:
    dfAsString = input_df.to_string(header=False, index=False)
    f.write(dfAsString)

with open('test.txt', 'w') as f:
    dfAsString = test_df.to_string(header=False, index=False)
    f.write(dfAsString)

sys.stdout.write("keys for labels:")
sys.stdout.write("\n")
for i in hashtable: 
    sys.stdout.write(str(i) + "-->"  + hashtable[i] + "\n")


#print(data.head(5))
