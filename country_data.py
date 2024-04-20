import psycopg2
import requests

#
db_data={
    'dbname':'valyuta',
    'user':'postgres',
    'host':'localhost',
    'port':5432,
    'password':'ikrom0315'
}

conn=psycopg2.connect(**db_data)
curr=conn.cursor()




def create_table():
    curr.execute("""
    CREATE TABLE IF NOT EXISTS country_capital
    (
    id serial PRIMARY KEY,
    country TEXT,
    capital TEXT
    )
    """)
    conn.commit()




def insert_table(country, capital):
    curr.execute("""
    INSERT INTO country_capital (country, capital)
    VALUES (%s, %s)
    """, (country, capital))
    conn.commit()


def get_all_data():
    url = "http://country.io/capital.json"
    r = requests.get(url)
    data = r.json()

    for country, capital in data.items():
        insert_table(country, capital)

def main():
    create_table()
    get_all_data()
    conn.close()
if __name__=="__main__":
    main()