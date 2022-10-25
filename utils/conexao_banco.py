import psycopg2 as pg

def connectar():
    con = pg.connect(host='ec2-54-147-36-107.compute-1.amazonaws.com',
                           database='d45cl2103817o3',
                           user='lsottatjfyeluh',
                           password='cab1c44d49503426eca5afbc0c2dd4a8042284ca121c7d69b0b903dcfeb5df47')
    return con
