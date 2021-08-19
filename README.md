# UN-Data-Processing
A public repository with scripts that aid in the retrieval, processing, and classification of numerous surveys.

# Requirements
- Python 3 installed, preferably the newest version available
- Check the libraries.txt file to see all the libraries that were used in this project

# Setup guide
1. Start by creating a folder to save this repository. This setup guide assumes that you know how to navigate through directories.
2. This is an example navigation on my machine, where I run Windows Subsystem for Linux (WSL)
```
>cd /mnt/c/users/[username]/Desktop/UN/
# Where /UN/ is an empty folder. 
>git init
>git clone https://github.com/willzs03/UN-Data-Processing.git
```
3. Example run below
```
# from the UN/ folder
>cd UN-Data-Processing/FAO
>python3 FAO.py
```

# Issues
- The following websites have unique, one-time use download links: MICS-UNICEF, UNPopulation. Due to this, the code in the respective repositories is not functional. For now, we are resorting to manual downloads for the survey files.
- UNODC doesn't have a direct download link, but they do have a public Tableau page. Tableau does provide download links for their data, but they use a concept of "sessions", which expire after a certain amount of time. 
- UNStats, like UNODC, also uses Tableau and thus has session links, which expire.
- UNODC provided a private 'master' excel sheet. However, all of the information there is in Spanish. We attempted to use a Google Translate library, but we were rate limited due to the sizes of the files.


# Directory
```
.
├── Barry		# Co-worker's code in Jupyter Notebook and .py formats. The scripts here specific data columns from FAO, IHSN, and ILO
├── Download Guide	# A guide on how to manually download datasets from various websites alongside picture instructions
├── FAO			# Scripts related to automatic survey data and metadata download
├── FinalMerge		# Scripts that clean up all data collected and a 'master' file with basic information from each data entry
├── IHSN		# Script that downloads survey data. Excel sheet that contains metadata for every IHSN entry
├── ILO			# Scritps that download survey data and metadata.
├── Luis-Repo		# Scripts that focus on downloading metadata from IHSN. All other metadata-gathering scripts were based on the files in this folder
├── Metadata		# Testing files. Nothing really useful here. Kept for logging purposes
├── MICS-UNICEF		# Data gathering scripts. Conversion from .csv -> .xlsx might be necessary
├── UNODC		# Data gathering and translation scripts. See Issues section for translation issues
├── UNPopulation	# Test files, refer to the "Barry" folder for functional code on UNPopulation
├── UNStats		# Scrapped projects, we didn't end up using UNStats' information
├── UNWomen		# Scripts which collect and cleanup data. Raw and modified excel files
├── libraries.txt	# Required libraries to run all programs
└── README.md
```
