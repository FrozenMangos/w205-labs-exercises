from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import re


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
       

    def process(self, tup):
        #words = tup.values[0]
        #words = re.sub(r'[^a-zA-Z0-9]','', word)
        words = re.sub(r'[^a-zA-Z0-9]','', tup.values[0])
        
        conn = psycopg2.connect(database="tcount", user="w205", password="", host="localhost", port="5432")
        cur = conn.cursor()

        #Insert
        cur.execute("INSERT INTO tweetwordcount (word, count) \
            SELECT %s,0 WHERE NOT EXISTS (SELECT * FROM tweetwordcount WHERE word=%s)", (words, words))
        conn.commit()

        #Update
        cur.execute("UPDATE tweetwordcount \
            SET count=count + 1 WHERE word=%s", (words,))
        conn.commit()
        

        # Increment the local count
        self.counts[words] += 1
        self.emit([words, self.counts[words]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (words, self.counts[words]))
