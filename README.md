# FastTextDataFormatting
A script and python file for quickly converting csv files to fastText ready txt files for command line training

## How to run
Add the two files into your fastText folder, instructions for building on the [fastText github page](https://github.com/facebookresearch/fastText)

Give appropriate permissions to the generate_txt.sh file using:
```
chmod +x generate_txt.sh
```

Add your csv dataset (will be called data.csv for this example) to the fastText directory. 

Run 
```
./generate_txt -c data.csv -f header1,header2 -l header3 -t 0.2
```

## Flags for generate_txt

`-c`: Path to the csv file\
`-f`: Features, which columns are inputs for fastText training. If there are multiple features, seperate them with commas but not spaces\
`-l`: Labels, which columns is the label for fastText training.\
`-t`: Train_test ratio, what ratio of the data should be used for testing. This is optional, the default value is 0.2 if not specified 

## Outcome of script
After running the script, it will print to the console a key for what labels indicate which outputs: 

```
keys for labels:
5-->__label__0
4-->__label__1
3-->__label__2
2-->__label__3
1-->__label__4
```
In this example the dataset used is a Yelp star rating csv, and the key indicates that 5 stars is associated with `__label__0`. A `label_key.txt` file is made for referencing this key at a later time. 

`generate_txt.sh` will also create a `test.txt` and `train.txt` file for testing and training respectively in the proper format that fastText requires. `generate_txt.sh` will format text data according to nlp standards by making all text lower case and adding spaces between punctuations (you're becomes you ' re) 

## Full example:
The following is an example usecase of the script given a csv file with yelp review data, which has features of text and user_id, and the outcome being a 1 to 5 star rating.

```
(base) arnavkartikeya@Arnavs-MacBook-Pro-2:~/Desktop/fastText-0.9.2$ ./generate_txt.sh -c yelpdataset.csv -f text,user_id -l stars -t 0.4
(base) arnavkartikeya@Arnavs-MacBook-Pro-2:~/Desktop/fastText-0.9.2$ ./fasttext supervised -input train.txt -output model
Read 0M words
Number of words:  7006
Number of labels: 5
Progress: 100.0% words/sec/thread:  246695 lr:  0.000000 avg.loss:  1.613683 ETA:   0h 0m 0s
(base) arnavkartikeya@Arnavs-MacBook-Pro-2:~/Desktop/fastText-0.9.2$ ./fasttext test model.bin test.txt 1
N	273
P@1	0.498
R@1	0.498
```
## Libraries needed to run:
The `print.py` file needs the following libraries to be accessable to it in order to run (pandas is most likely the only one needed to be installed):
  - re
  - pandas
  - csv
  - os
  - sys
