package application;
	
import java.util.ArrayList;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;



public class Main5 extends Application {
	Label lb1;
	Label lb2;
	Label lb3;
	Label lb4;
	Label lb5;
	Label lb6;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main5.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			lb1 = (Label) scene.lookup("#lbl1");
			lb2 = (Label) scene.lookup("#lbl2");
			lb3 = (Label) scene.lookup("#lbl3");
			lb4 = (Label) scene.lookup("#lbl4");
			lb5 = (Label) scene.lookup("#lbl5");
			lb6 = (Label) scene.lookup("#lbl6");
			
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					getLotto();
				}
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		
	}
	public void getLotto() {
		int[] number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
				        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
				        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
				        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
				        41, 42, 43, 44, 45};
		
//		int[] lottoNum = new int[6]; // 로또번호 6개를 담을 배열 선언
		
		ArrayList<Integer> arr6 = new ArrayList<Integer>();

		while(arr6.size() <= 6) {
			int rnd = (int) (Math.random() * 45);
			
			if (number[rnd] > 0) {
				arr6.add(number[rnd]);
				number[rnd] = -1;
			}
		}
		
		lb1.setText(arr6.get(0) + "");
		lb2.setText(arr6.get(1) + "");
		lb3.setText(arr6.get(2) + "");
		lb4.setText(arr6.get(3) + "");
		lb5.setText(arr6.get(4) + "");
		lb6.setText(arr6.get(5) + "");
		
//		for (int i = 0; i < 6; i++) {
//			int rnd = (int) (Math.random() * 45);
//			if (number[rnd] != -1) {
//				lottoNum[i] = number[rnd];
//			} else {
//				i--;
//			}
//		}
//		lb1.setText(lottoNum[0] + "");
//		lb2.setText(lottoNum[1] + "");
//		lb3.setText(lottoNum[2] + "");
//		lb4.setText(lottoNum[3] + "");
//		lb5.setText(lottoNum[4] + "");
//		lb6.setText(lottoNum[5] + "");
		
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}