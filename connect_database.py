# import psycopg2
# import asyncio
# import requests
#
# db_data={
#     'dbname':'valyuta',
#     'user':'postgres',
#     'host':'localhost',
#     'port':5432,
#     'password':'ikrom0315'
# }
#
# conn=psycopg2.connect(**db_data)
# curr=conn.cursor()
#
#
# def create_table():
#     curr.execute(f"""
#     CREATE TABLE IF NOT EXISTS valyutalar_kursi
#     (
#     currency TEXT,
#     nominal int,
#     rate Real
#     )
#     """)
#     conn.commit()
#
#
#
# def insert_table(currency, nominal, rate):
#     curr.execute(f"""
#     INSERT INTO valyutalar_kursi(currency, nominal, rate)
#     values (%s, %s, %s)
#     """, (currency, nominal, rate))
#
#     conn.commit()
#
# def get_all_data():
#     url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
#     r=requests.get(url)
#     data=r.json()
#     for i in data:
#         insert_table(i['Ccy'], i['Nominal'], i['Rate'])
#
# def update_database():
#     get_all_data()
#
# def main():
#     create_table()
#     update_database()
#     conn.close()
#
# if __name__=="__main__":
#     main()