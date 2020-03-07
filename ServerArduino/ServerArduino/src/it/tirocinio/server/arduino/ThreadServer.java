package it.tirocinio.server.arduino;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadServer extends Thread{
	
	private static ServerSocket ss;
	private ExecutorService service;
	private boolean flag;
	private ArrayList<ThreadArduino> threads;
	private boolean db;
	
	public ThreadServer() throws IOException {
		ss = new ServerSocket(9080);
		System.out.println("In attesa di connessione");
		flag = true;
		threads = new ArrayList<ThreadArduino>();
		db = false;
	}
	
	public void shutDown(){
		flag = false;
	}
	
	public void setBooleanTrue() {
		db = true;
	}
	
	public void setBooleanFalse() {
		db = false;
	}

	
	@Override
	public void run() {
		Socket x;
		int core = Runtime.getRuntime().availableProcessors();
		// TODO Auto-generated method stub
		while(flag) {
			try {
				x = ss.accept();
				ThreadArduino thread = new ThreadArduino(x);
				if(db) {
					thread.setBooleanTrue();
				} else {
					thread.setBooleanFalse();
				}
				service=Executors.newScheduledThreadPool(core);
				service.execute(thread);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		System.out.println();
		System.out.println("Connessione interrotta");
		System.out.println();
		
		for(int i = 0;i<threads.size();i++) {
			try {
				threads.get(i).join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		try {
			ss.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
