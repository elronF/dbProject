#!/usr/bin/env python3

import psycopg2

invalid_input = True


def db_connection():
    """Create a connection to the DB."""
    dbName = "dbname=news"
    try:
        db = psycopg2.connect(dbName)
        return db
    except psycopg2.Error as e:
        print("An error was made with the message: " + e)


def three_articles():
    """Function to answer first question"""
    db = db_connection()
    cur = db.cursor()
    query = '''
        SELECT a.title, count(b.path) AS num
        FROM articles a
        JOIN log b
            ON b.path = '/article/' || a.slug
        WHERE b.path <> '/'
        GROUP BY a.title
        ORDER BY num DESC LIMIT 3
        '''
    cur.execute(query)
    rows = cur.fetchall()
    print()
    print("Most popular articles:")
    for title, views in rows:
        print('"{}" - {} views'.format(title, views))
    cur.close()
    db.close()


def three_authors():
    """Function to answer second question"""
    db = db_connection()
    cur = db.cursor()
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
    cur.execute(query)
    rows = cur.fetchall()
    print()
    print("Most popular authors:")
    for authors, views in rows:
        print('"{}" - {} views'.format(authors, views))
    cur.close()
    db.close()


def request_errors():
    """Function to answer third question"""
    db = db_connection()
    cur = db.cursor()
    query = '''
    SELECT successcount.date,
        CAST(Fail AS float)/(CAST(Fail AS float)+CAST(Success AS float)) AS Percent
    FROM successcount, failcount
    WHERE successcount.date = failcount.date
        AND CAST(Fail as float)/(CAST(Fail as float)+CAST(Success as float)) > .01;
    '''
    cur.execute(query)
    rows = cur.fetchall()
    print()
    print("Days on which more than 1% of requests lead to errors:")
    for row in rows:
        print(" ", row[0], "-", round((row[1] * 100), 2),"%", "errors")
    cur.close()
    db.close()


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
