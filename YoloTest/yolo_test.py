from ultralytics import YOLO


# this is a basic combination of lines that opens up the webcam
# and the computer recognizes the objects that appear on the screen
modelo = YOLO('yolov8n.pt')
modelo.predict(source='0', show=True)

