Project Title:

Log analysis

Prerequisites:

To run this project:
1. Linux base virtual machine
2. Python interpreter

Files:

1. report.py

How it works:

report.py connects to the news database through postgresql.
it runs some queries on the database. the queries help to 
find popular articles of all time. popular authors of all time
and on which days more than 1% of requests lead to errors. 
report.py then fetch all the resuls of the queries and prints
on the display in a formatted way.

Steps for running the program:

1. save the file report.py where the news database file is kept
2. got to git bash 
3. start the virtual machine using command 
			vagrant up
4. login to the VM using 
			vagrant ssh
5. using cd command go to the path where report.py was saved
6. now enter the following command to execute the program
			python report.py
7. user can see the report generated on the news database

Git access:

https://github.com/szasohel/reporting_tool.git

Created by:

Sayed Zahed Abdullah Sohel
