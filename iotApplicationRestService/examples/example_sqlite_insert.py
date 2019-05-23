import sqlite3

conn = sqlite3.connect('iot_cluster.db')
c = conn.cursor()
c.execute("INSERT INTO raw_sensor_data VALUES(1,'00:00',2,0)")
conn.commit()
c.close()
conn.close()


