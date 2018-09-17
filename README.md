# PYTHON DB PROJECT

This DB project answers three queries from a news article SQL database, utilizing the psycopg2 PostgreSQL adapter for Python, and displays them in a simple text format. This program was written to fulfill the requirements of the first project of Udacity's Fullstack Nanodegree.

## SETUP

**Pyscopg2** will need to be installed to run this module. Instructions can be found at: http://initd.org/psycopg/docs/install.html

A **Linux VM** running **PostgreSQL** will also be required.

## SQL VIEWS REQUIRED

These views will need to be created in the 'news' database in order to run the third query in this program:

`CREATE VIEW successcount AS SELECT date(time) as Date, count(status) AS Success FROM log WHERE status = '200 OK' GROUP BY date(time);`

`CREATE VIEW failcount AS SELECT date(time) as Date, count(status) AS Fail FROM log WHERE status != '200 OK' GROUP BY date(time);`

## RUNNING PROGRAM
To run this program, navigate to the project folder and use python3 project.py command.  You will be presented with a list of questions that can be answered. Use inputs 1, 2 or 3 to get the specific answer needed.

The program will loop back to the list of questions until you type 'q' to quit the program.