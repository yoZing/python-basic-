package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;



public class Main7 extends Application {
	
	TextField tf_mine;
	TextField tf_com;
	TextField tf_result;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main7.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf_mine = (TextField) scene.lookup("#tf_mine");
			tf_com = (TextField) scene.lookup("#tf_com");
			tf_result = (TextField) scene.lookup("#tf_result");
			
			Button btn = (Button) scene.lookup("#btn");
			
			tf_mine.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
					if (event.getCode().equals(KeyCode.ENTER)) {
						rocSisPa();
					}
				}
			});
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					rocSisPa();
				}
				
				
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void rocSisPa() {
		String mine = tf_mine.getText();
		String result = "";
		
		// com의 가위 또는 바위 또는 보를 결정하는 로직
		String[] com = {"가위", "바위", "보"};
		
		int rnd = (int) (Math.random() * 3);
		
		tf_com.setText(com[rnd]);
		
		if (mine.equals("가위") && com[rnd].equals("바위")) { result += "Com 승리!"; }
		if (mine.equals("가위") && com[rnd].equals("가위")) { result += "무승부!"; }
		if (mine.equals("가위") && com[rnd].equals("보")) { result += "나 승리!"; }
		if (mine.equals("바위") && com[rnd].equals("보")) { result += "Com 승리!"; }
		if (mine.equals("바위") && com[rnd].equals("바위")) { result += "무승부!"; }
		if (mine.equals("바위") && com[rnd].equals("가위")) { result += "나 승리!"; }
		if (mine.equals("보") && com[rnd].equals("가위")) { result += "Com 승리!"; }
		if (mine.equals("보") && com[rnd].equals("보")) { result += "무승부!"; }
		if (mine.equals("보") && com[rnd].equals("바위")) { result += "나 승리!"; }
		
		tf_result.setText(result);
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}