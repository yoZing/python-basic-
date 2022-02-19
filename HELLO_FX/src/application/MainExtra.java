package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;



public class MainExtra extends Application {
	TextField tf;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main9.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			
			Button btn1 = (Button) scene.lookup("#btn1");
			Button btn2 = (Button) scene.lookup("#btn2");
			Button btn3 = (Button) scene.lookup("#btn3");
			Button btn4 = (Button) scene.lookup("#btn4");
			Button btn5 = (Button) scene.lookup("#btn5");
			
			Button btn6 = (Button) scene.lookup("#btn6");
			Button btn7 = (Button) scene.lookup("#btn7");
			Button btn8 = (Button) scene.lookup("#btn8");
			Button btn9 = (Button) scene.lookup("#btn9");
			Button btn0 = (Button) scene.lookup("#btn0");
			Button btnCall = (Button) scene.lookup("#btnCall");
			
			tf = (TextField) scene.lookup("#tf");
			
			
			
			btn1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick(event);
				}
			});
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				
				@Override
				public void handle(Event event) {
					myCall();

				}
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	void myCall() {
		String str_tel = tf.getText();
		Alert alert = new Alert(AlertType.INFORMATION, "Calling\n" + str_tel);
		
		alert.setTitle("전화걸기");
		alert.setHeaderText("Calling" + str_tel);
		alert.showAndWait();
	}
	void myClick(Event evnet) {
		Button imsi = (Button) evnet.getSource();
		String strNew = imsi.getText();
		String strOld = tf.getText();
		tf.setText(strOld + strNew);
		System.out.println(imsi.getText());
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}