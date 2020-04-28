import pandas as pd
import os
import glob
import time as tm
import argparse
import csv
import statistics
import dash
import dash_bio as dashbio
import dash_html_components as html
import dash_core_components as dcc


parser = argparse.ArgumentParser()
parser.add_argument("input", type = str, help = "Input directory selection.")
parser.add_argument("output", type = str, help = "Name of output csv file.")
parser.add_argument('-d','--data', nargs = '+', help='<Required> Data Folder', required=True)
parser.add_argument('-b','--binary', nargs = '+', help='<Required> Binary Value for Data Folder', required=True)
args = parser.parse_args()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {'background': '#111111',
                'text': '#7FDBFF'}
os.chdir(args.input)
start_time = tm.time()


def loadData():
	input_data = []
	binarylist = []
	length_modifier = 0
	extension = 'tsv'
	for j in range(len(args.data)):
		input_data = input_data + sorted([i for i in glob.glob(args.data[j] + '/*.{}'.format(extension))])
		data_length = len(input_data) - length_modifier
		#print(data_length)	
		binarylist = binarylist + data_length * [args.binary[j]]
		length_modifier = len(input_data) 
	binarylist.insert(0, 'Binary')
	#print(input_data)
	#print(binarylist)
	return input_data, binarylist

def getNames(input_data):
	namelist = ['AminoAcids']
	for file in input_data:	
		namelist.append(file[:-4])
	#print(namelist)
	return namelist

def fillDict(input_data):
	data_dict = dict()
	for i in range(len(input_data)):
		f = open(input_data[i], 'r')
		for line in f:
			if line.startswith('#'):
				continue
			x = line.split('\t')
			if x[1] == '':
				continue
			if x[4].isnumeric() == False:
				continue
			key, value = x[1], x[2]
			data_dict.setdefault(key, {})
			if i in data_dict[key].keys():
				data_dict[key][i] += int(value)
			else:
				data_dict.setdefault(key,{})[i] = int(value)
		f.close()
	return data_dict

def writeCSV(namelist, binarylist, data_dict, length):
        print('Dictionary built, forming dataframe.')
        with open(args.output + '.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(namelist)
                writer.writerow(binarylist)
                for key1, key2 in data_dict.items():
                        filt = list(key2.keys())
                        if len(filt) < (len(binarylist) * 0.05):
                                continue
                        row = []
                        row.append(key1)
                        i = 0
                        for i in range(length):
                                if i in key2.keys():
                                        row.append(key2[i])
                                else:
                                        row.append(0)
                        writer.writerow(row)
def getPercentDiff(column):
        a = column[0] 
        b = column[1]
        if (a == 0):
                return 0.5;
        else:
                c = abs(b-a)/a
                return c
def normalizeData(pct_list):
        amin, amax = min(pct_list), max(pct_list)
        for i, val in enumerate(pct_list):
                pct_list[i] = (val-amin) / (amax-amin)
        return pct_list
# Main body
filelist, blist = loadData()
nlist = getNames(input_data = filelist)
ddict = fillDict(input_data = filelist)
writeCSV(namelist = nlist, binarylist = blist, data_dict = ddict, length = len(filelist))
data = pd.read_csv(args.output + '.csv')

#Data Handling
data = data.T
data.columns = data.iloc[0]
data = data.iloc[1:,:]
data = data.astype(float)
data.sort_values(by='Binary')
data = data.groupby(['Binary']).mean()
print("Data processed, calculating deviation.")

#Percent Deviation Calculation
amino = data.columns
pct_row = []
for name in amino:
    pct_row.append(getPercentDiff(list(data[name])))
pct_row = normalizeData(pct_row)
data = data.append(pd.Series(pct_row, index = data.columns ), ignore_index = True)
print("Percent difference between cohorts is " + str(100 * statistics.mean(pct_row)) + '%\n')

#Data Visualization Preprocessing
visual = data.T
visual = visual.sort_values(by = [2], ascending = False)
visual = visual.iloc[0:50,0:2]
visual.columns = ["Cohort 1", "Cohort 2"]
print("The fifty highest deviation AminoAcids:")
print(visual)
print('Running time: ', tm.time() - start_time, '\n')


