package co.edu.utadeo.is.tesis.iotCentralCluster.model;

import co.edu.utadeo.is.tesis.iotCentralCluster.entity.RawSensorData;

public interface ISensorDAO {
	
	void saveData(RawSensorData rawSensorData);
}
