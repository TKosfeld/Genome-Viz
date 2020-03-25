# Genome-Viz
3300 Term Project for Processing and Visualization of Genomic Data

# MergePackage
TSV file data handler operating using argparse command line.

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/641011410977030154/unknown.png)


**Example**

```
python3 MergePackage.py datasets/ Test -d group1pre group2pre group2post1 group2post6  -b 0 0 1 1 
```

**Sprint 1 Burndown**
![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/681399617467842600/unknown.png)

Tasks:
- Import and utilize Argparse Module to allow flexibility in file selection.
- Evaluate Program efficiency using tm.time.
- Implement file identification, selection, and sorting function under title: loadData().
- Based on file selection, create and identifier row denote sample status as infected or naive.
- Implement a labeling function, getNames(), to appropriately track and identify files in the final data frame.
- Initialize an empty dictionary to hold concatenated data.
- Trim the dictionary filling function fillDict().
- FillDict() should ignore empty sequence entries and disregard non-data columns while processing data for entry.
- FillDict() should be able to process flawed files with unexpected formating.
- FillDict() should store each sequence in a key relevant to the specific file the sequence was read from.
- FillDict() should return a dictionary of dictionaries upon completion.
- Sprint 1 package should print a running time and completely dictionary of dictionaries.


**Sprint 2 Burndown**
![Command Line Format](https://media.discordapp.net/attachments/215581700556718080/692495522832973854/sprint2.png)

Tasks:
- For current coherence, single cohort data frames should be recorded and expressed as .csv files.
- For coherence the prototype should notify the user when single cohort files have been processed into a singular dictionary.
- Argparse functionality should be added to determine location and naming of output single cohort data file.
- The .csv should be written to by line, with column headers of filenames serving as the first written row.
- Column specific exposure based labels should be assigned to each header.
- In an effort to prevent overpopulation of irrelevant data, the .csv writer should require a certain amount of samples expressed for a  TCR sequence to be recognized.
- As in projected dataframe expression, each row should be declared as an empty list and filled from relevant dictionary entries.
- Relevant columns lacking data dictionary entries for a certain sequence should be represented with 0’s in the row.
- Relevant efficiency and timekeeping functions should be updated to accommodate new workloads.

**Sprint 2 Burndown**
![Command Line Format]()

