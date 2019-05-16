import sqlite3, models#, time, datetime, Adafruit_DHT
from sqlite3 import Error
from flask import make_response, abort
from config import db
#from time import sleep
#from gpiozero import MotionSensor

def get_sense_time():
	networkMetadata = NetworkMetadata.query.all()
	networkMetadataSchema = NetworkMetadataSchema(many=False)
	data = networkMetadataSchema.dump(networkMetadata).data
	return data


if __name__ == '__main__':

	senseTime = get_sense_time()
	print(senseTime)
