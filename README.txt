#Project Title:

Log analysis

##Prerequisites:

To run this project:
1. Python2 or 3
2. postgresql
3. psycopg2

##Files:

1. report.py

##How it works:

This project sets up a mock PostgreSQL database for a fictional news website. 
The provided Python script uses the psycopg2 library to query the database 
And produce a report that answers the following three questions:
What are the most popular articles of all time?
Who are the most popular authors of all time? 
On which days did more than 1% of requests lead to errors? 
report.py then fetch all the resuls of the queries and prints
On the display in a formatted way.

##Steps for running the program:

1. VirtualBox is the software that actually runs the virtual machine. 
   You can download it from virtualbox.org. Install the platform 
   package for your operating system.
2. Vagrant is the software that configures the VM and lets you share 
   files between your host computer and the VM's filesystem. Download it 
   from vagrantup.com. Install the version for your operating system.
3. Download the database here.
	https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
   You will need to unzip this file after downloading 
   it. The file inside is called newsdata.sql. Put this file into the vagrant 
   directory, which is shared with your virtual machine.
4. Save the file report.py where the news database file is kept
5. Open a Linux-like command line terminal (e.g. Git Bash, MacOS terminal, etc.) 
6. Start the virtual machine using command 
			vagrant up
7. Login to the VM using 
			vagrant ssh
8. Using cd command go to the path where report.py was saved
9. Now enter the following command to execute the program
			python report.py
10. User can see the report generated on the news database

##Git access:

https://github.com/szasohel/reporting_tool.git

##Created by:

Sayed Zahed Abdullah Sohel
