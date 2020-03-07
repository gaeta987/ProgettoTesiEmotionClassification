package it.tirocinio.server.arduino;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;

public class ConnectionPool {

	private static volatile MongoDatabase database = null;

	public ConnectionPool(){

	}

	public static MongoDatabase connect(String dbName) {
		if(database == null) {
			synchronized (ConnectionPool.class) {
				if(database == null) {
					MongoClient client = new MongoClient("localhost", 27017);
					database = client.getDatabase(dbName);
				}
			}
		}
		return database;
	}

}
