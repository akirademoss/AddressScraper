# AddressScraper
This is a script to help scrape data into a new file to facilitate the process of getting shipping labels to clients

## Prerequisites
This was made with python3.7, but should work with most versions of python3.  You will also need to have venv installed - this is essential for package management and installing python packages locally vs. globally.  This means that the packages you install and use here will only be used in this project, thus it will not cause conflict and will mitigate the need for lengthy troubleshooting of package dependency issues.

#### clone the repository to a directory of your choice using the following commands, and then enter the working directory
```
mclovin@mclovin-Z97MX-Gaming-5:~/Documents/FullStackAppDev Consulting/Glambot$ git clone https://github.com/akirademoss/AddressScraper.git
mclovin@mclovin-Z97MX-Gaming-5:~/Documents/FullStackAppDev Consulting/Glambot$ cd AddressScraper
```

#### once inside your local AddressScraper repository, activate your python virtual environment
```
mclovin@mclovin-Z97MX-Gaming-5:~/Documents/FullStackAppDev Consulting/Glambot/AddressScraper$ python3 -m venv .venv
mclovin@mclovin-Z97MX-Gaming-5:~/Documents/FullStackAppDev Consulting/Glambot/AddressScraper$ source .venv/bin/activate
```

#### Install requirements from requirements.txt and run script
```
mclovin@mclovin-Z97MX-Gaming-5:~/Documents/FullStackAppDev Consulting/Glambot/AddressScraper$ pip3 install -r ./requirements.txt
```

#### Run the extract script
```
mclovin@mclovin-Z97MX-Gaming-5:~/Documents/FullStackAppDev Consulting/Glambot/AddressScraper$ python3 extract.py
```