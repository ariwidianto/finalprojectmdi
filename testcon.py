import pytds
with pytds.connect('localhost', 'finalproject', 'SA', 'mypassword') as conn:
    with conn.cursor() as cur:
        cur.execute("select * from dataset3")
        print (cur.fetchall())
