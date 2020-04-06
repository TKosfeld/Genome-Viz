import pandas as pd
import os
import glob
import time as tm
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("input", type = str, help = "Input directory selection.")
parser.add_argument("output", type = str, help = "Name of output csv file.")
parser.add_argument('-d','--data', nargs = '+', help='<Required> Data Folder', required=True)
parser.add_argument('-b','--binary', nargs = '+', help='<Required> Binary Value for Data Folder', required=True)
args = parser.parse_args()

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
		print(data_length)	
		binarylist = binarylist + data_length * [args.binary[j]]
		length_modifier = len(input_data) 
	binarylist.insert(0, 'Binary')
	print(input_data)
	print(binarylist)
	return input_data, binarylist

def getNames(input_data):
	namelist = ['AminoAcids']
	for file in input_data:	
		namelist.append(file[:-4])
	print(namelist)
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
        print('Dictionary building done, writing to file.')
        with open(args.output + '.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(namelist)
                writer.writerow(binarylist)
                for key1, key2 in data_dict.items():
                        filt = list(key2.keys())
                        post_length = len([a for a in filt if a > 32])
                        pre_length = len([b for b in filt if b <= 32])
                        if pre_length >= post_length:
                                continue
                        if post_length < 3:
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

# Main body
filelist, blist = loadData()
nlist = getNames(input_data = filelist)
ddict = fillDict(input_data = filelist)
writeCSV(namelist = nlist, binarylist = blist, data_dict = ddict, length = len(filelist))
data = pd.read_csv(args.output + '.csv')
data = data.T
data.columns = data.iloc[0]
data = data.iloc[1:,:]
print(data)
print('Running time: ', tm.time() - start_time)
