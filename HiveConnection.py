import pyhs2

with pyhs2.connect(host='ec2-3-235-44-213.compute-1.amazonaws.com',
                   port=10000,
                   user='hive',
                   database='default') as conn:
    with conn.cursor() as cur:
        # Show databases
        print(cur.getDatabases())


        # Execute query
        cur.execute("select * from table")

        # Return column info from query
        print (cur.getSchema())

        # Fetch table results
        for i in cur.fetch():
            print(i)