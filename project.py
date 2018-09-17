import psycopg2

invalid_input = True

# Function to create a connection to the DB, since we'll need to do it three times.
def db_connection():
    dbName = "dbname=news"
    try:
        db = psycopg2.connect(dbName)
        return db
    except psycopg2.Error as e:
        print("An error was made with the message: " + e)

# Function  to answer question: "What are the most popular three articles of all time?"
def three_articles():
    db = db_connection()
    cur = db.cursor()
		
    query = '''
        SELECT a.title, count(b.path) AS num 
        FROM articles a 
        JOIN log b 
            ON b.path LIKE CONCAT ('%', a.slug) 
        WHERE b.path <> '/' 
        GROUP BY a.title 
        ORDER BY num DESC LIMIT 8;
        '''
		
    cur.execute(query)
    rows = cur.fetchall()

    print
    print "Most popular articles:"
    for row in rows:
        print " ", row[0], "-", row[1], "views"

    cur.close()
    db.close()

# Function to answer question: "Who are the most popular articles authors of all time?"
def three_authors():
    db = db_connection()
    cur = db.cursor()
		
    query = '''
        SELECT authors.name, count(log.path) AS views 
        FROM articles 
        JOIN authors 
            ON articles.author = authors.id 
        JOIN log 
            ON log.path LIKE CONCAT('%', articles.slug) 
        GROUP BY authors.name 
        ORDER BY views DESC;
        '''
		
    cur.execute(query)
    rows = cur.fetchall()

    print
    print "Most popular authors:"
    for row in rows:
        print " ", row[0], "-", row[1], "views"

    cur.close()
    db.close()

# Function to answer question: "On which days did more than 1% of requests lead to errors"
def request_errors():
    db = db_connection()
    cur = db.cursor()
		
    query = '''
    SELECT successcount.date, CAST(Fail AS float)/CAST(Success AS float) AS Percent 
    FROM successcount, failcount 
    WHERE successcount.date = failcount.date 
        AND CAST(Fail as float)/CAST(Success as float) >.01;
    '''
		
    cur.execute(query)
    rows = cur.fetchall()

    print
    print "Days on which more than 1% of requests lead to errors:"
    for row in rows:
        print " ", row[0], "-", round((row[1] * 100), 1), "%", "errors"

    cur.close()
    db.close()

def main(response):
    if response == "1":
        three_articles()
        invalid_input = False
    elif response == "2":
        three_authors()
        invalid_input = False
    elif response == "3":
        request_errors()
        invalid_input = False;        
    else:
        print("Enter a valid number or quit")

while invalid_input:
    print
    print("Article Analysis Program")
    print
    print("1. What are the most popular three articles of all time?")
    print("2. Who are the most popular articles authors of all time?")
    print("3. On which days did more than 1% of requests lead to errors?")
    userInput = raw_input(
        "Please enter the number of the query you want answered or Q to quit:")
    if userInput == "q":
        import sys
        sys.exit()
    reponse = int(userInput)
    main(userInput)