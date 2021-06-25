# UN-Data-Processing
A public repository with scripts that aid in the retrieval, processing, and classification of numerous surveys.

# Requirements
- Python 3 installed, preferably the newest version available
- The following modules: pip, requests, [TableauScraper](https://pypi.org/project/TableauScraper/)

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

# If you're a developer
If you would like to contribute to the project, feel free to send me an email to willzs@umich.edu or william.zhangsam@un.org. If you would like to be added as a contributor to the repository, send me an email with your username and I'll add you promptly!

# Issues
- The following websites have unique, one-time use download links: MICS-UNICEF, UNPopulation. Due to this, the code in the respective repositories is not functional. For now, we are resorting to manual downloads for the survey files.
- UNODC doesn't have a direct download link, but they do have a public Tableau page. We are currently looking into how to scrape these resources using TableauScraper. Tableau does provide download links for their data, but they use a concept of "sessions", which expire after a certain amount of time. 
- UNStats, like UNODC, also uses Tableau and thus has session links, which expire. We are looking into using TableauScraper for UNStats.
