import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

# Miles_car=[]
# m_test=[]
# Miles = []
# Purchase_price = []
# with_discount = []
# Discount = []
# name_car = []
# b=20
# for i in range(1,b+1):
#     url='https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true'+'&page='+str(i)
#     print(url)
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#
#     # print(res)
#     # print(soup)
#     miles = []
#     price = []
#     name = []
#     t = []
#
#
#     Books = soup.find_all('div', attrs={'class': 'linkable card card-shadow vehicle-card'})
#     # print(Books[1].text)
#
#     machin_name = soup.find_all('div', attrs={'class': 'vehicle-card-top'})
#     # print(machin_name[6].text)
#
#     machin_miles = soup.find_all('div', attrs={'class': 'mt-2-5 w-full border-t pt-2-5'})
#     # print(machin_miles[0].text)
#
#     machin_price = soup.find_all('div', attrs={'class': 'text-sm line-through'})
#     # print(machin_price[0].text)
#
#     machin_takhfif = soup.find_all('div', attrs={'class': 'heading-3 font-bold'})
#     # print(machin_takhfif[0].text)
#     for i in range(len(Books)):
#         miles.append(re.findall('(\d.+)[m]', machin_miles[i].text))
#     a = 0
#     for i in range(len(Books)):
#         # print(Books[i].text)
#         price.append(re.findall('[$](\d{1}[,]\d{3}|\d{2}[,]\d{3}|\d{3}[,]\d{3}|\d{4}[,]\d{3}|\d{5}[,]\d{3}|\d{6}[,]\d{3})[$](\d{1}[,]\d{3}|\d{2}[,]\d{3}|\d{3}[,]\d{3}|\d{4}[,]\d{3}|\d{5}[,]\d{3}|\d{6}[,]\d{3})\d|[$](\d{1}[,]\d{3}|\d{2}[,]\d{3}|\d{3}[,]\d{3}|\d{4}[,]\d{3}|\d{5}[,]\d{3}|\d{6}[,]\d{3})\d', Books[i].text))
#
#
#     for j in range(len(Books)):
#         name.append(re.findall('Sponsored....(.+)|(.+)', machin_name[j].text))
#     # print(price)
#     # print(name)
#
#     s = 0
#     g = 0
#     m = 0
#     n = 0
#
#     # print(len(name))
#     # print(name)
#     # print(price)
#     # if len(price) < 33:
#     #     g = 33 - len(price)
#     #     for i in range(g):
#     #         # print(i)
#     #         price.append(('none','none','none'))
#
#
#     for i in range(len(price)):
#         for j in range(len(price[i])):
#             t.append(price[i][j])
#     #
#     # if len(t) < 33:
#     #     m = 33 - len(t)
#     #     for i in range(m):
#     #         # print(i)
#     #         # print(i)
#     #         t.append(('none','none','none'))
#
#     # print(t)
#     # print(price)
#     for i in range(len(t)):
#         if t[i][1] == '':
#             Discount.append('none')
#
#         else:
#             Discount.append(t[i][1])
#
#     # print(Discount)
#
#
#     for i in range(len(t)):
#         if t[i][0] == '':
#             with_discount.append('none')
#
#         else:
#             with_discount.append(t[i][0])
#     # print(with_discount)
#
#
#     for i in range(len(t)):
#         if t[i][2] == '':
#             Purchase_price.append('none')
#
#         else:
#             Purchase_price.append(t[i][2])
#     # print(Purchase_price)
#
#
#     for i in range(len(name)):
#         for j in range(len(name[i])):
#             for h in range(len(name[i][j])):
#                 if name[i][j][h] == '':
#                     continue
#                 else:
#                     name_car.append(name[i][j][h])
#     # if len(name) < 33:
#     #     s = 33 - len(name)
#     #     for i in range(s):
#     #         # print(i)
#     #         name_car.append('none')
#     # if len(miles) < 33:
#     #     n = 33 - len(miles)
#     #     print(n)
#     #     for i in range(n):
#     #
#     #         # print(i)
#     #         # print(i)
#     #         miles.append(['none'])
#
#     for i in range(len(miles)):
#         for j in range(len(miles[i])):
#             if miles[i][j] == []:
#                 Miles.append('none')
#             else:
#                 Miles.append(miles[i][j])
#
#     print(len(name_car))
#     print(len(Miles))
#     print(len(Purchase_price))
#     print(len(with_discount))
#     print(len(Discount))
#     print(price)
#
#
#
#
# for i in range(len(Miles)):
#
#     m_test.append(re.findall('(\d.+?)[m]|(\d.+)', Miles[i]))
#
# for i in range(len(m_test)):
#     for j in range(len(m_test[i])):
#         for h in range(len(m_test[i][j])):
#             if  m_test[i][j][h] == '':
#                continue
#
#             else:
#                Miles_car.append(m_test[i][j][h])
#
#
# print(len(name_car))
# print(len(Miles_car))
# # # print(len(Miles))
# print(len(Purchase_price))
# print(len(with_discount))
# print(len(Discount))
#
#
# dict={'Name_Car' : name_car,'Miles':Miles_car,'Discount':Discount,'With_Discount':with_discount,'Purchase_price':Purchase_price }
# df = pd.DataFrame(dict)
# # print(df)
# df.to_csv('BuyPriceCar20rows.csv',index=False)
#


# /////////////////////////////////////// Databases ///////////////////////////////////////////////////////////////
empdata = pd.read_csv('C:\\Users\\peyman\\pythonProject16\\BuyPriceCar20rows.csv')
print(empdata.head())
# print(empdata)
# try:
#     con = msql.connect(host='127.0.0.1',user='root',password='peiman2012')
#     if con.is_connected():
#         cursor = con.cursor()
#         cursor.execute("create database BuyCar20rows")
#         print("Databases is created....")
#
# except Error as e :
#     print("Error while connecting to MYSQL",e)

try:
    con = msql.connect(host='127.0.0.1',
                       user='root',
                       password='peiman2012',
                       database='BuyCar20rows'
                       )
    if con.is_connected():
        cursor=con.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('drop table if exists BuyCar20rows;')
        print('Creating table....')
        cursor.execute("create table BuyCar20rows (Name_Car char(255), Miles char(20) ,Discount char(20),With_Discount char(20),Purchase_Price char(20))")
        print("Table is created....")

        for i,row in empdata.fillna(-1).iterrows():
            sql="INSERT INTO BuyCar20rows VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            # print("Record inserted")
            con.commit()
except Error as e :
    print("Error while connecting to MYSQL",e)

sql = "SELECT * FROM BuyCarComplate "
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
con.close()





