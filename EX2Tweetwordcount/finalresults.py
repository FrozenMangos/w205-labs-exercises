import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) > 1: #Checks to see if the user input something
  
  for arg in sys.argv:  #For every argument supplied by the user, we return the word and number of occurrences
    cur.execute("SELECT count FROM tweetwordcount WHERE word=%s",(arg,))
    for record in cur:
      print "The total number of occurances of %s is: %s" %(arg, record[0])

else:
  #Just returns all words in ascending order with their counts
  cur.execute("SELECT * FROM tweetwordcount ORDER BY word ASC")
  for row in cur:
    print row
