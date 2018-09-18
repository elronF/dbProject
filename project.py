#!/usr/bin/env python3

import psycopg2

invalid_input = True


def db_connection():
    """Creates a connection to the specified DB."""
    dbName = "dbname=news"
    try:
        db = psycopg2.connect(dbName)
        return db
    except psycopg2.Error as e:
        print("An error was made with the message: " + e)


def execute_query(query):
    """
    execute_query takes an SQL query as a parameter, 
    executes the query and returns the results as a list of tuples.

    args:
      query - (string) an SQL query statement to be executed.

    returns:
      A list of tuples containing the results of the query.
    """
    try:    
        db = db_connection()
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        db.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def three_articles():
    """Function to answer first question"""
    query = '''
        SELECT a.title, count(b.path) AS num
        FROM articles a
        JOIN log b
            ON b.path = '/article/' || a.slug
        WHERE b.path <> '/'
        GROUP BY a.title
        ORDER BY num DESC LIMIT 3
        '''
    results = execute_query(query)
    print()
    print("Most popular articles:")
    for title, views in results:
        print('"{}" - {} views'.format(title, views))


def three_authors():
    """Function to answer second question"""
    query = '''
        SELECT b.name, count(c.path) AS views
        FROM articles a
        JOIN authors b
            ON a.author = b.id
        JOIN log c
            ON c.path = '/article/' || a.slug
        GROUP BY b.name
        ORDER BY views DESC;
        '''
    results = execute_query(query)
    print()
    print("Most popular authors:")
    for authors, views in results:
        print('{} - {} views'.format(authors, views))


def request_errors():
    """Function to answer third question"""
    query = '''
    SELECT successcount.date,
        CAST(Fail AS float)/(CAST(Fail AS float)+CAST(Success AS float)) AS Percent
    FROM successcount, failcount
    WHERE successcount.date = failcount.date
        AND CAST(Fail as float)/(CAST(Fail as float)+CAST(Success as float)) > .01;
    '''
    results = execute_query(query)
    print()
    print("Days on which more than 1% of requests lead to errors:")
    for dates, percents in results:
        print(" ", "{:%B %d, %Y}".format(dates), "-", "{:.2%}".format(percents))


def main(response):
    """Logic to run the program"""
    if response == "1":
        three_articles()
        invalid_input = False
    elif response == "2":
        three_authors()
        invalid_input = False
    elif response == "3":
        request_errors()
        invalid_input = False
    else:
        print("Enter a valid number or quit")

if __name__ == '__main__':
    while invalid_input:
        """Get the user input for which question to answer"""
        print()
        print("Article Analysis Program")
        print()
        print("1. What are the most popular three articles of all time?")
        print("2. Who are the most popular articles authors of all time?")
        print("3. On which days did more than 1% of requests lead to errors?")
        userInput = input(
            "Please enter the number of the query you want answered or Q to quit:")
        if userInput == "q":
            import sys
            sys.exit()
        reponse = int(userInput)
        main(userInput)
