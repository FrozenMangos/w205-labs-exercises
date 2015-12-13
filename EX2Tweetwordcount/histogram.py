import psycopg2
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
cur = conn.cursor()


cur.execute("SELECT * FROM tweetwordcount WHERE count BETWEEN %s AND %s",(num1, num2))
for row in cur:
  print row
