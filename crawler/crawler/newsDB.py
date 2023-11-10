import sqlite3

class newsDB():
    def __init__(self):
        print ("start DB Manager")
        self.DBName = 'googleNews.db'
        self.db = sqlite3.connect(self.DBName, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.googleNews_table = 'googleNews'
        self.keyword_table = 'keyword'
        self.googleNews_columns = {
            'published': 'text',
            'source': 'text PRIMARY KEY',
            'title': 'text',
            'link': 'text',
        }
        self.keyword_columns = {
            'keyword': 'text PRIMARY KEY',
            'country': 'text',
        }

    def __del__(self):
        self.stop()

    def stop(self):
        try: self.db.close()
        except: pass
    #주어진 키워드에 맞는 Google News 테이블을 생성합니다.
    def queryCreateGoogleNewsTable(self, keyword):
        self.googleNews_table = 'googleNews_' + keyword.lower()
        cursor = self.db.cursor()
        colum_info = ",".join(col_name + ' ' + col_type for col_name, col_type in self.googleNews_columns.items())
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(self.googleNews_table, colum_info)
        cursor.execute(query)
        self.db.commit()
    #주어진 키워드에 맞는 Google News 테이블에 값을 삽입합니다.
    def queryInsertGoogleNewsTable(self, values):
        cursor = self.db.cursor()
        colums = ','.join(self.googleNews_columns.keys())
        values = '","'.join(str(values[col_name]).replace('"',"'") for col_name in self.googleNews_columns.keys())
        query = 'INSERT OR IGNORE INTO {} ({}) VALUES ("{}")'.format(self.googleNews_table, colums, values)
        cursor.execute(query)
        self.db.commit()
    #주어진 키워드에 맞는 Google News 테이블을 삭제합니다.
    def queryDeleteAllGoogleNewsTable(self, keyword):
        googleNews_table = 'googleNews_' + keyword.lower()
        query = "DROP TABLE IF EXISTS {}".format(googleNews_table)
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()
    #주어진 키워드에 맞는 Google News 테이블의 모든 값을 가져옵니다.
    def querySelectAllGoogleNewsTable(self, keyword):
        googleNews_table = 'googleNews_' + keyword.lower()
        query = "SELECT * FROM {}".format(googleNews_table)
        cursor = self.db.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    #키워드 테이블을 생성합니다.
    def queryCreateKeywordTable(self):
        cursor = self.db.cursor()
        colum_info = ",".join(col_name + ' ' + col_type for col_name, col_type in self.keyword_columns.items())
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(self.keyword_table, colum_info)
        cursor.execute(query)
        self.db.commit()
    #키워드 테이블에 값을 삽입합니다.
    def queryInsertKeywordTable(self, values):
        cursor = self.db.cursor()
        colums = ','.join(self.keyword_columns.keys())
        values = '","'.join(str(values[col_name]).replace('"',"'") for col_name in self.keyword_columns.keys())
        query = 'INSERT OR IGNORE INTO {} ({}) VALUES ("{}")'.format(self.keyword_table, colums, values)
        cursor.execute(query)
        self.db.commit()
    #키워드 테이블의 값을 삭제합니다.
    def queryDeleteKeywordTable(self, keyword):
        cursor = self.db.cursor()
        query = "DELETE FROM {} WHERE KEYWORD='{}'".format(self.keyword_table, keyword)
        cursor.execute(query)
        self.db.commit()
    #키워드 테이블의 모든 값을 가져옵니다.
    def querySelectAllKeywordTable(self):   
        query = "SELECT * FROM {}".format(self.keyword_table)
        cursor = self.db.cursor()
        cursor.execute(query)
        return cursor.fetchall()