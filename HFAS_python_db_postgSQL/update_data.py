"""Author: Hector Fernando Arredondo Sanchez"""

import psycopg2
from config import config


def update_vendor(vendor_id, vendor_name):
    """update vendor name based on the vendor id"""
    sql = """UPDATE vendors
            SET vendor_name=%s
            WHERE vendor_id=%s"""

    try:
        connection = None
        update_rows = 0

        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(sql, (vendor_name, vendor_id))
        update_rows = cursor.rowcount
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return update_rows


if __name__ == '__main__':
    update_vendor(1, '3M Corp.')
