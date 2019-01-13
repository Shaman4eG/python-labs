import os
import sqlite3
import urllib.request
from bs4 import BeautifulSoup


class BusinessLogic:
  def cache_rss_and_return_it(self, link):
    with urllib.request.urlopen(link) as url:
      rss_data = url.read()
    
    self.create_tables()
    self.parse_rss_data_and_insert_to_db(link, rss_data)
    rss_feed = self.get_rss(link)

    return rss_feed

  def parse_rss_data_and_insert_to_db(self, source, rss_data):
    os.chdir(os.getcwd() + '\\src\\lab6\\database')
    connectionToDb = sqlite3.connect('rss.db')
    cursor = connectionToDb.cursor()

    doc = BeautifulSoup(rss_data)
    for item in doc.findAll('item'):
      title = item.find('title').text
      link = item.find('guid').text
      description = item.find('description').text
      pub_date = item.find('pubdate').text
      
      article = (source, title, link, description, pub_date)
      cursor.execute('INSERT INTO rss_feed VALUES (?,?,?,?,?)', article)

    connectionToDb.commit()
    connectionToDb.close()
    os.chdir(os.getcwd() + '\\..\\..\\..')


  def create_tables(self):
    os.chdir(os.getcwd() + '\\src\\lab6\\database')
    connectionToDb = sqlite3.connect('rss.db')
    cursor = connectionToDb.cursor()

    cursor.execute('DROP TABLE IF EXISTS rss_feed')
    cursor.execute('CREATE TABLE rss_feed (source, title, link, description, pub_date)')

    connectionToDb.close()
    os.chdir(os.getcwd() + '\\..\\..\\..')


  def get_rss(self, source):
    os.chdir(os.getcwd() + '\\src\\lab6\\database')
    connectionToDb = sqlite3.connect('rss.db')
    cursor = connectionToDb.cursor()

    cursor.execute('SELECT * FROM rss_feed WHERE source = ? ORDER BY pub_date DESC', (source,))
    all_articles = cursor.fetchall()

    connectionToDb.close()
    os.chdir(os.getcwd() + '\\..\\..\\..')

    return all_articles

