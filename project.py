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

# Function to answer question: "Who are the most popular articles authors of all time?"
def three_authors():
	db = db_connection()


# Function to answer question: "On which days did more than 1% of requests lead to errors"
def request_errors():
	db = db_connection()

# define query
# cursor object
# execute query with cursor object, place into rows variable?