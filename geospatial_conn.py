# -*- coding: utf-8 -*-
"""geospatial_conn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F4ATH7IenLbA7PpJDfsqXq9UtJKek64U
"""

!pip install pymysql

import pymysql

connection_params={'host' :'database-2.c9mkqis8ciad.ap-south-1.rds.amazonaws.com',
'user' : 'admin',
'password' : 'admin123',
'database' :'flask'}

connection = pymysql.connect(**connection_params)

cursor = connection.cursor()

sql = "SHOW TABLE;"

cursor.execute(sql)

tables = cursor.fetchall()

        # Print the tables
        for table in tables:
            print(table)

!pip install geopy
import geopy.distance
import numpy as np
import pandas as pd

data = pd.read_excel(r'/content/Chaalaang_Gameskraft_Input Data.xlsx', sheet_name='User Preferences')
data

data.columns

pd.read_excel(r'/content/Chaalaang_Gameskraft_Input Data.xlsx', sheet_name='User Preferences').to_csv('Chaalaang_Gameskraft_Input Data.csv',index=False)

data=pd.read_csv(r'/content/Chaalaang_Gameskraft_Input Data.csv')

data.head()

data = data.rename(columns={'MaxDistance for Connection (in Km)\n*Empty means any distance is fine':'MaxDistance'})

data

data=pd.DataFrame(data)

data



data['MaxDistance']=data['MaxDistance'].fillna(0)

data

def calculate_distance(coord1, coord2):
    return geopy.distance.geodesic(coord1, coord2).kilometers

data.head()

data['MaxDistance'] = pd.to_numeric(data['MaxDistance'], errors='coerce')

def find_nearby_users(user_id, data):
    nearby_users = []
    user_row = data[data['UserId'] == user_id]

    if not user_row.empty:  # Check if user exists
        user_location = (user_row['Latitude'].iloc[0], user_row['Longitude'].iloc[0])
        max_distance = user_row['MaxDistance'].iloc[0]  # Retrieve max distance for the user
        print("User Location:", user_location)
        print("Max Distance:", max_distance)

        if max_distance != 0:  # Check if max distance is not zero
            for index, row in data.iterrows():
                if row['UserId'] != user_id:
                    other_location = (row['Latitude'], row['Longitude'])
                    distance = calculate_distance(user_location, other_location)
                    print("Other Location:", other_location)
                    print("Distance:", distance)

                    if distance <= max_distance:  # Apply max distance for the user
                        nearby_users.append({'user_id': row['UserId'], 'distance': distance})

    return nearby_users

user_id = 5
data = pd.DataFrame(data)
nearby_users = find_nearby_users(user_id, data)

nearby_users



def connect_with_users(user_id, suggested_users):
    """
    Connect with the suggested users by sending friend requests or initiating chats.
    """
    for suggested_user_id in suggested_users:

        print(f"Sending friend request from user {user_id} to user {suggested_user_id}")

connect_with_users(user_id, nearby_users)









