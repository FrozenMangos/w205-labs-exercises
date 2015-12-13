1. Make sure you're user 'w205'

2. Navigate to the folder where you cloned my project (make sure you're user w205)

3. Run the following to set up a new database: 
createdb -h localhost -p 5432 -U postgres tcount

4. Switch to the postgres prompt with: 
psql -U postgres

5. Change the database owner to w205 with: 
ALTER DATABASE tcount OWNER TO w205;

6. Quit back to the command prompt with: 
\q

7. Now enter the new database as w205 with: 
psql tcount

8. Create the table we'll use to store tweets with:
CREATE TABLE tweetwordcount (
word varchar(144),
count int);

9. Quit back to the main command prompt again: 
\q

10. Now you can start executing the normal code.  To stream tweets into tweetwordcount use: 
sparse run

11. After streaming for a bit, you can use Ctrl+C to cancel the stream.

12. Run the commands listed in final results section:
python finalresults.py love
python finalresults.py
python histogram.py 50 55
