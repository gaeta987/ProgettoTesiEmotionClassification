package it.tirocinio.server.arduino;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import javax.swing.*;
import javax.swing.JFrame;

public class Interface extends JFrame{

	private JButton buttonStart;
	private JButton buttonStop;
	private JPanel panel;
	private ThreadServer t;
	private JButton buttonSave;
	private JButton buttonNoSave;

	public Interface() throws IOException {
		JFrame frame=new JFrame();
		frame.setSize(500, 100);
		frame.setDefaultCloseOperation(EXIT_ON_CLOSE);

		createPanel();
		frame.add(panel);
		frame.setVisible(true);


	}

	public void createPanel() {
		buttonStart = new JButton("Start");

		buttonStart.addActionListener(y -> {
			try {
				t = new ThreadServer();
				t.start();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		});

		buttonStop = new JButton("Stop");

		buttonStop.addActionListener(c->{
			t.shutDown();
			t.setBooleanFalse();
		});

		buttonSave = new JButton("Save");

		buttonSave.addActionListener(s -> {
			t.setBooleanTrue();
		});

		buttonNoSave = new JButton("Stop Save");

		buttonNoSave.addActionListener(a -> {
			t.setBooleanFalse();
		});

		panel = new JPanel();
		panel.add(buttonStart);
		panel.add(buttonStop);
		panel.add(buttonSave);
		panel.add(buttonNoSave);
	}

}
