import sqlite3, time, datetime, Adafruit_DHT
from sqlite3 import Error
from time import sleep
from gpiozero import MotionSensor

node_name = 'Node 2'

def create_connection(db_file):
    try:
        db = sqlite3.connect(db_file)
        return db
    except Error as e:
        print(e)
    return None

def create_database(conn):
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS node''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS node(nod_id INTEGER PRIMARY KEY,
                   nod_name TEXT, nod_time_unit TEXT, nod_time INTEGER)''')
    time_unit = 'S'
    time = 15
    cursor.execute('''INSERT INTO node(nod_name, nod_time_unit, nod_time)
                      VALUES(?,?,?)''', (node_name, time_unit, time))
    cursor.execute('''DROP TABLE IF EXISTS node_sensor''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS node_sensor(nse_id INTEGER PRIMARY KEY,
                   nse_name TEXT, nse_abbreviation TEXT)''')
    sensors = [('Temperature', 'TEM'),
              ('Humidity', 'HUM'),
              ('Movement', 'MOV'),
              ('Light', 'LGH')]
    cursor.executemany('''INSERT INTO node_sensor(nse_name, nse_abbreviation)
                            VALUES(?,?)''', sensors)
    cursor.execute('''DROP TABLE IF EXISTS node_data''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS node_data(nda_id INTEGER PRIMARY KEY,
                   nse_id TEXT, nda_time TEXT, nda_value TEXT)''')
    conn.commit()
    
def get_node_time(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT nod_time FROM node WHERE nod_name=?", (node_name,))
    data = cursor.fetchall()
    return data

def get_node_sensors(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT nse_abbreviation FROM node_sensor")
    data = cursor.fetchall()
    return data

def get_node_data(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM node_data")
    data = cursor.fetchall()
    return data

def do_insert_data(conn, data):
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO node_data(nse_id, nda_time, nda_value)
                       VALUES(?,?,?)''', data)
    conn.commit()
    
def do_read_temperature():
    print('TEM')
    sensor=Adafruit_DHT.DHT11
    gpio=17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if temperature is not None:
        return '{0:0.1f}*C'.format(temperature)
    else:
        return None
    
def do_read_humidity():
    print('HUM')
    sensor=Adafruit_DHT.DHT11
    gpio=17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None:
        return '{0:0.1f}%'.format(humidity)
    else:
        return None    
    
def do_read_movement():
    print('MOV')
    pir = MotionSensor(4)
    return '1'
    
def do_read_light():
    print('LGH')
    return '1'
 
if __name__ == '__main__':
    #database = "C:\\data\iot_data.db"
    database = "iot_data.db"
    conn = create_connection(database)
    create_database(conn)
    time_rows = get_node_time(conn)
    delay_time = 0;
    for row in time_rows:
        delay_time = row["nod_time"]
    sensor_rows = get_node_sensors(conn)
    for row in sensor_rows:
        print(row["nse_abbreviation"])
    while True:
        now = datetime.datetime.now()
        print(str(now))
        temperature = do_read_temperature()
        humidity = do_read_humidity()
        movement = do_read_movement()
        light = do_read_light()
        data = [('1',str(now),temperature),
                ('2',str(now),humidity),
                ('3',str(now),movement),
                ('4',str(now),light)]
        do_insert_data(conn, data)
        sleep(delay_time)
    
