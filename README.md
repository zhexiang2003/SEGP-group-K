# SEGP-group-K
Development of Automated Sorting System for Germinated Oil Palm Seeds 

Github link: https://github.com/mrmoglin/SEGP-group-K.git

Hardware Components:
1. Odroid H3+
2. Camera - Tecgear Sentinel 2K camera
3. Infrared Sensor
4. Conveyor Belt
5. Tripod stand with lights attached
6. Display device (Monitors)

Setup Instructions: 
1. Download two folders, Odroid and Training. 

Odroid - Contain all python code and past record/images for the sorting system.
Note: For fasterrcnn_resnet50_fpn_state_dict.pth, please download it from Google Drive link provided. It is mentioned in File_Download text file. 

Python Files:
1. camera.py 
2. camera_setting.py 
3. create_csv_files.py
4. detect_predict_image.py
5. illumination.py - Not in use, as new illumination system is replaced
6. ir_sensor.py
7. main.py - GUI
8. preprocess.py
9. seed_classification.py
10. seed_detection.py
11. seed_dataset.py
12. seedxml2csv.py
13. setup.py

Training - The folder includes the images and results for retraining the model.

2. Two IDEs to run the python code, Thonny or Pycharm. 
3. After setting up on the IDE, ensure to change the file path so the code can read the file based on the file directory.
4. Connect all hardware components, such as camera, infrared sensor to Odroid H3+.
5. Press start to run the program, setup.py window will show up to check the camera conditions.
6. If the camera is correctly set up, the setup window closes and the main GUI will show up. 
7. Use 4 buttons to control the system.

- Start button - Start the whole operation. Infrared will start to detect trays.
- Stop button - Stop all the operation, but the GUI remains there. 
- Result button - Past record will display in the GUI.  
- Exit button - Terminate the program. 
