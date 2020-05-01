# Genome-Viz
3300 Term Project for Processing and Visualization of Genomic Data

# MergePackage
TSV file data handler operating using argparse command line.

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/641011410977030154/unknown.png)


**Example**

```
python3 Genome_Viz.py test_data/ test -d MPXVInfected2wks MPXVInfected8wks -b 0 1  
```

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/705905500717318244/unknown.png)

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/705912357234409562/unknown.png)

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

**Sprint 3 Burndown**

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/705823231034130573/unknown.png)

Tasks: (6 Tasks, 2 Weeks)
- Line separation should be mutable between \t and ,.
- Column specification should be mutable through argparse specification.
- Filetype should be mutable through argparse specification.
- Institute filtering of relevant data for classification.
- Mutable line separation variable is employed on a line by line basis when processing data.
- Dataset specification will allow for multiple datasets to be joined from a single directory specified in the command line.

**Sprint 4 Burndown**

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/705823231034130573/unknown.png)

Tasks: (9 Tasks, 2 Weeks)
- Cohort data frames should be processed and interpreted as floats.
- Cohort representations should be created through concatenation of all labeled files.
- The joining of this genomic data should be done by averaging sequence expression over the cohort.
- For each shared sequence between the two cohorts I want to calculate a percentage deviation.
- To avoid skewed data the percentage deviation should be normalized between 0 and 100%/
- The mean of these normalized percentages will be displayed as the overall deviation between cohorts.
- These normalized percentages should be appended to the dataframe.
- The sequences with the largest deviations should be presented as high-impact characteristic sequences.
- The program should display the 50 highest impact sequences and their mean representation in each cohort.

**Sprint 5 Burndown**

![Command Line Format](https://cdn.discordapp.com/attachments/215581700556718080/705823397237620736/unknown.png)

Tasks: (12 Tasks, 1 Week)
- The program needs to import dash and dash_bio for their visualization capabilities.
- The program should have an html template and dash app for server creation.
- The dash app object should be created with coherent text and color.
- The visualization process should receive the data of the 50 highest impact sequences, sorted by cohort deviation.
- The cohorts should be visualized side by side in a clustergram to properly visualize differences.
- The clustergram colors should be distinct and conductive towards differentiation.
- The clustergram should identify possible clusters and recurrent behavior.
- Cohort columns should be labelled appropriately.
- Rows should be identified by sequence.
- The graph should be fitted to the screen while being large enough to distinguish individual rows.
- The graph should be added to the template in the app object.
- The server should be run without debugging to maintain an interactive single-run visualization.




