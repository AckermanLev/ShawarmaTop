import sqlite3


def BaseData():
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM shawarmaTop ORDER BY star DESC"
    cursor.execute(sql)
    b = cursor.fetchall()
    return b


def addBaseData(name,star,id_user,address):
    #INSERT INTO users VALUES (2, 'Bob', 41)
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = f"INSERT INTO shawarmaTop (name, address, star) VALUES ('{name}', '{address}', {star})"
    cursor.execute(sql)
    conn.commit()
    sql = "SELECT * FROM shawarmaTop ORDER BY id DESC"
    cursor.execute(sql)
    b = cursor.fetchall()
    sql = f"INSERT INTO users VALUES ({id_user}, '{b[0][0]}', {star})"
    cursor.execute(sql)
    conn.commit()
    

def findBaseData(id):
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = f"SELECT * FROM shawarmaTop WHERE id = {id}"
    cursor.execute(sql)
    b = cursor.fetchall()
    return b


def addStarBaseData(id,star,id_user):
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = f"INSERT INTO users VALUES ({id_user}, '{id}', {star})"
    cursor.execute(sql)
    conn.commit()
    sql = f"SELECT * FROM users WHERE id_shawarma = {id}"
    cursor.execute(sql)
    b = cursor.fetchall()
    count = 0
    for i in range(len(b)):
        count += int(b[i][2])
    
    sql = f"UPDATE shawarmaTop SET star = {round(count/(len(b)),1)} WHERE id = {id}"
    cursor.execute(sql)
    conn.commit()


def userInBaseData(id_user,id_shawarma):
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = f"SELECT * FROM users WHERE id_shawarma = {id_shawarma}"
    cursor.execute(sql)
    b = cursor.fetchall()
    f = True
    for i in range(len(b)):
        if int(id_user) == int(b[i][0]):
            f = False
    if not f:
        return True
    else:
        return False


def deleteOtzivBaseData(id_user,id_shawarma):
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = f"DELETE FROM users WHERE id_shawarma = {id_shawarma} AND id_users = {id_user}"
    cursor.execute(sql)
    conn.commit()
    sql = f"SELECT * FROM users WHERE id_shawarma = {id_shawarma}"
    cursor.execute(sql)
    b = cursor.fetchall()
    if len(b) == 0:
        sql = f"UPDATE shawarmaTop SET star = 'нет оценок' WHERE id = {id_shawarma}"    
    else:
        count = 0
        for i in range(len(b)):
            count += int(b[i][2])
        
        sql = f"UPDATE shawarmaTop SET star = {round(count/(len(b)),1)} WHERE id = {id_shawarma}"
    cursor.execute(sql)
    conn.commit()


def amountBaseData(id):
    conn = sqlite3.connect("shawarmaTop_database.db")
    cursor = conn.cursor()
    sql = f"SELECT * FROM users WHERE id_shawarma = {id}"
    cursor.execute(sql)
    b = cursor.fetchall()
    return len(b)