package it.tirocinio.server.arduino;

import java.io.IOException;
import java.net.Socket;
import java.util.Date;
import java.util.NoSuchElementException;
import java.util.Scanner;
import org.bson.Document;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

public class ThreadArduino extends Thread {

	private Socket socket;
	private Scanner input;
	private MongoDatabase database;
	private static boolean db;

	public ThreadArduino(Socket s) throws IOException {
		socket = s;	
		database = ConnectionPool.connect("mydb");
		db = false;
	}

	public void setBooleanTrue() {
		db = true;
	}

	public void setBooleanFalse() {
		db = false;
	}

	public void run() {

		try {
			input = new Scanner(socket.getInputStream());
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		String stringId;

		try {
			stringId = input.nextLine();
		} catch (NoSuchElementException e) {
			stringId = "";
		}

		if(stringId.equals("non ci sono messaggi") || stringId.equals("")) {

		} else {
			int id = Integer.parseInt(stringId);
			switch(id) {
			case 1: pulseSensor();
			break;
			case 2: 
				try {
					dhtSensor();
					socket.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case 5: 
				try {
					buttonChose();
					socket.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case 4: voiceAndGyroscopeSensor();
			try {
				socket.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			break;
			} 

		}


	}

	private void pulseSensor() {
		String pulseSensor = input.nextLine();
		if(Integer.parseInt(pulseSensor)>40) {
			if(db) {
				MongoCollection<Document> collection = database.getCollection("pulseSensor");
				Document document = new Document("Ora",getOraAttuale()).append("Battito",Integer.parseInt(pulseSensor));
				collection.insertOne(document);
			}	  
			System.out.println("BPM = "+pulseSensor);
			System.out.println();
		}
	}

	private void dhtSensor() throws IOException {
		String dhtSensorTemp = input.nextLine();
		String dhtSensorUmidity = input.nextLine();
		String x = input.nextLine();
		String y = input.nextLine();
		String z = input.nextLine();

		int x1 = Integer.parseInt(x);
		int y1 = Integer.parseInt(y);
		int z1 = Integer.parseInt(z);
		if(db) {
			MongoCollection<Document> collection = database.getCollection("dhtSensor");
			Document document = new Document("Ora",getOraAttuale()).append("Temperatura",Integer.parseInt(dhtSensorTemp)).append("Umidit√†", Integer.parseInt(dhtSensorUmidity));
			collection.insertOne(document);
			collection = database.getCollection("gyroscopeSensor");
			document = new Document("Ora",getOraAttuale()).append("x",Integer.parseInt(x)).append("y", Integer.parseInt(y)).append("z", Integer.parseInt(z));
			collection.insertOne(document);
			System.out.println(getOraAttuale());
		}
		System.out.println("umidit‡† = "+dhtSensorUmidity);
		System.out.println("Temperatura = "+dhtSensorTemp);
		System.out.println();
		System.out.println("X = "+x);
		System.out.println("Y = "+y);
		System.out.println("Z = "+z);
		System.out.println();
	}


	private void voiceAndGyroscopeSensor() {
		String x = input.nextLine();
		String y = input.nextLine();
		String z = input.nextLine();
		String voiceSensor = input.nextLine();
		if(db) {
			MongoCollection<Document> collection = database.getCollection("gyroscopeSensor1");
			Document document = new Document("Ora",getOraAttuale()).append("x1",Integer.parseInt(x)).append("y1", Integer.parseInt(y)).append("z1", Integer.parseInt(z));
			collection.insertOne(document);
			collection = database.getCollection("voiceSensor");
			document = new Document("Ora",getOraAttuale()).append("suono",Integer.parseInt(voiceSensor));
			collection.insertOne(document);
			System.out.println(getOraAttuale());
		}

		System.out.println("X1 = "+x);
		System.out.println("Y1 = "+y);
		System.out.println("Z1 = "+z);
		System.out.println();

		System.out.println("Suono = "+voiceSensor);
		System.out.println();
	}

	public String getOraAttuale(){
		java.util.TimeZone t=java.util.TimeZone.getTimeZone("ECT");
		java.util.Calendar oggi = java.util.Calendar.getInstance(t);

		String s = "";
		String secondi = "" + oggi.get(oggi.SECOND);
		String minuti = "" + oggi.get(oggi.MINUTE);
		String ora = "" +oggi.get(oggi.HOUR_OF_DAY);

		if (secondi.length() == 1)
			secondi = "0" + secondi;
		if (minuti.length() == 1)
			minuti = "0" + minuti;
		if (ora.length() == 1)
			ora = "0" + ora;

		s=ora + ":" + minuti + ":" + secondi;

		return s;
	}

	public void buttonChose() {
		String button1 = input.nextLine();
		int button = Integer.parseInt(button1);

		if(db) {
			MongoCollection<Document> collection = database.getCollection("oracolo");
			Document document;
			switch(button) {
			case 1:
				document = new Document("Ora",getOraAttuale()).append("Oracolo","Happy");
				collection.insertOne(document);
				break;
			case 2:
				document = new Document("Ora",getOraAttuale()).append("Oracolo","Sad");
				collection.insertOne(document);
				break;
			case 3:
				document = new Document("Ora",getOraAttuale()).append("Oracolo","Angry");
				collection.insertOne(document);
				break;
			case 4:
				document = new Document("Ora",getOraAttuale()).append("Oracolo","Fear");
				collection.insertOne(document);
				break;
			} 
		}

		System.out.println(button);

	}

}
