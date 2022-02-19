package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
	


public class Main6 extends Application {
	TextField tf;
	TextArea ta;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main6.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			tf = (TextField) scene.lookup("#tf");
			ta = (TextArea) scene.lookup("#ta");
			
			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					calculate();
					
				}
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void calculate() {
		String number = tf.getText();
		int bundle = Integer.parseInt(number);
		String result = number + "단" + "\n";
		
		for (int quotient = 1; quotient < 10; quotient++) {
			result += number + " x " + quotient + " = " + bundle * quotient + "\n";
		}
		ta.setText(result);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}