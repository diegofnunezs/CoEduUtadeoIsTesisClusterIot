package co.edu.utadeo.is.tesis.iotCentralCluster.model.impl;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import co.edu.utadeo.is.tesis.iotCentralCluster.entity.RawSensorData;
import co.edu.utadeo.is.tesis.iotCentralCluster.model.ISensorDAO;

@Repository
public class SensorDAO implements ISensorDAO {

	@Autowired
	private SessionFactory sessionFactory;
	
	@Override
	public void saveData(RawSensorData rawSensorData) {
		sessionFactory.openSession().save(rawSensorData);
	}

}
