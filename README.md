# dataManager
The repository contains all the scripts about using the files and manipulating these files. 

1. databaseRenaming : The file is designed to rename the DJI recording sessions. The files have to be already placed in the format of folders for project MELA. The empty folder set can be created using createFolderStucture.py 
The program also has special command for removing the hidden files from the folder. This is a big problem for renaming if hidden files exists in the structure and thus one has to be careful of the argument. 

2. training_frame_extractor : This script mainly extracts training data from specific videos mentioned in the csv file that is given in the input.
Note* The file was designed to work with orignial names of the videos, now the video names have changed as per the unique naming convention.  

3. createFolderStructure : Given a directory and date, the dir creator will create a default folder structure requited for project MELA. General format is YYYYMMDD/S(Y)_Lek(X)/P(X)D(X), where X is a number and Y is "M" or "E" signifying morning or evening. 