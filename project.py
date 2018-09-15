import psycopg2

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
		
		query = '''SELECT a.title, count(b.path) AS num 
				   FROM articles a 
				   JOIN log b 
						ON b.path LIKE CONCAT ('%', a.slug) 
				   WHERE b.path <> '/' 
				   GROUP BY a.title 
				   ORDER BY num DESC LIMIT 8;'''
		
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
		
		query = '''SELECT authors.name, count(log.path) AS views 
		FROM articles 
		JOIN authors 
			ON articles.author = authors.id 
		JOIN log 
			ON log.path LIKE CONCAT('%', articles.slug) 
		GROUP BY authors.name 
		ORDER BY views DESC;'''
		
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

three_articles()
three_authors()