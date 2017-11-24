"""Author: Hector Fernando Arredondo Sanchez"""

import psycopg2
from config import config


def insert_vendor(vendor_name):
    """Insert a new vendor into the vendors table"""
    sql = """INSERT INTO vendors(vendor_name)
              VALUES(%s)RETURNING vendor_id;"""
    connection = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the INSERT statment
        cursor.execute(sql, (vendor_name,))
        # get the generated id back
        vendor_id = cursor.fetchone()[0]
        # commit the changes to the database
        connection.commit()
        # Close the communication with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return vendor_id


def insert_vendor_list(vendor_list):
    """insert multiple vendors into the vendor table"""
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    connection = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the Insert statement
        cursor.executemany(sql, vendor_list)
        # commint the chnages to the database
        connection.commit()
        # close communitcation with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    # insert one vendor
    # print(insert_vendor('3M Co.'))
    insert_vendor_list([('AKM Semiconductor Inc.',),
                        ('Asahi Glass Co Ltd.',),
                        ('Daiki Industries Ltd',),
                        ('Dvnacast International Inc.',),
                        ('Foster Electri Co. Ltd.',),
                        ('Murata Manufacturing Co. Ltd.',)])


# if __name__ =='__main__':
# insert one vendor
# print(insert_vendor('3M Co.'))
