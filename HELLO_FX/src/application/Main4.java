package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;



public class Main4 extends Application {
	TextField tfMine;
	TextField tfCom;
	TextField tfResult;
	
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main4.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			tfMine = (TextField) scene.lookup("#tfMine");
			tfCom = (TextField) scene.lookup("#tfCom");
			tfResult = (TextField) scene.lookup("#tfResult");
			
			Button btn = (Button) scene.lookup("#btn");
			
			
			
			tfMine.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
					System.out.println(event.getCode());
					if (event.getCode().equals(KeyCode.ENTER)) {
						playGame();
					}
					
				}
				
			});
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					playGame();
				}
				
			});
			
			
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		
	}
	public void playGame() {
		// 선언부
		
		String mine = tfMine.getText();
		String comSelc = "";
		
		double rnd = Math.random();
		
		// 비즈니스 로직
		if (rnd > 0.5) {
			comSelc = "홀";
		} else {
			comSelc = "짝";
		}
		
		// 출력부
		tfCom.setText(comSelc);
		
		if (mine.equals(comSelc)) {
			tfResult.setText("나 승리.");
		} else {
			tfResult.setText("나 패배 / 컴 승리.");
		}

	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}