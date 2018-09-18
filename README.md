# PYTHON DB PROJECT

This DB project answers three queries from a news article SQL database and displays them in a simple text format. This program was written to fulfill the requirements of the first project of Udacity's Fullstack Nanodegree.

The three questions answered are:

1. What are the most popular three articles of all time?
2. Who are the most popular articles authors of all time?
3. On which days did more than 1% of requests lead to errors?

## SETUP REQUIREMENTS

A **Linux VM** running **Python3** and **PostgreSQL**.

**Vagrant** and **Virtual Box** were utilized to develop this project. Installation instructions can be found at:
-https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
-https://www.vagrantup.com/downloads.html

Once Vagrant and Virtual Box are installed, pull the Vagrantfile from this project's repository and place it in a folder called "vagrant". From the terminal, navigate to your vagrant folder and run the command `vagrant up`. An automated setup will run. Once complete, you can log-in to your VM using the command `vagrant ssh`

**Psycopg2**, a PostgreSQL adapter will need to be installed: (http://initd.org/psycopg/docs/install.html). 

## SQL REQUIREMENTS

With your Linux VM installed, the news database schema will need to be added, which can be found in a zipped file called newsdata.zip in this repository.  Unzip the file and place it in the "vagrant" directory you previously created. Navigate to the vagrant folder within your VM environment and use the command `psql -d news -f newsdata.sql` to load the data.

Once the data is loaded, these views will need to be created in the 'news' database in order to run the third query in this program:

```sql
CREATE VIEW successcount AS SELECT date(time) as Date, count(status) AS Success 
FROM log 
WHERE status = '200 OK' 
GROUP BY date(time);
```

```sql
CREATE VIEW failcount AS SELECT date(time) as Date, count(status) AS Fail 
FROM log 
WHERE status != '200 OK' 
GROUP BY date(time);
```

## RUNNING PROGRAM
The project.py file should be placed within a sub-folder of the 'vagrant' folder.

To run this program, navigate to the project folder and use the command `python3 project.py` or `./project.py`. You will be presented with a list of questions that can be answered. Use inputs 1, 2 or 3 to get the specific answer needed.

The program will loop back to the list of questions until you type 'q' to quit the program.