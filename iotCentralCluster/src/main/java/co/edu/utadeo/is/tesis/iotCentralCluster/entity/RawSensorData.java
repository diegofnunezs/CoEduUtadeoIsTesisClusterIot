package co.edu.utadeo.is.tesis.iotCentralCluster.entity;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "raw_sensor_data")
public class RawSensorData {

	private Integer nodeId;
	private Integer sensorId;
	private Date time;
	private Double value;
	private Boolean migrated;

	@Id
	@Column(name = "node_id")
	public Integer getNodeId() {
		return nodeId;
	}

	public void setNodeId(Integer nodeId) {
		this.nodeId = nodeId;
	}

	@Id
	@Column(name="node_id")
	public Integer getSensorId() {
		return sensorId;
	}

	public void setSensorId(Integer sensorId) {
		this.sensorId = sensorId;
	}

	@Id
	@Column(name="time")
	public Date getTime() {
		return time;
	}

	public void setTime(Date time) {
		this.time = time;
	}

	@Column(name="value")
	public Double getValue() {
		return value;
	}

	public void setValue(Double value) {
		this.value = value;
	}

	@Column(name="migrated")
	public Boolean getMigrated() {
		return migrated;
	}

	public void setMigrated(Boolean migrated) {
		this.migrated = migrated;
	}
}
