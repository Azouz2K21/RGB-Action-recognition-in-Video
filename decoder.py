import cv2
import os

directory_in_str =os.path.join(os.getcwd(),".\data_set_1")
decoded_directory_in_str =os.path.join(os.getcwd(),".\extracted_data_set_1")
directory = os.fsencode(directory_in_str)

for action_directory in os.listdir(directory):
    action_directory_path = os.path.join(directory_in_str, os.fsdecode(action_directory))
    new_action_directory_path = os.path.join(decoded_directory_in_str, os.fsdecode(action_directory))
    os.mkdir(new_action_directory_path, 0o777)
    print(action_directory_path)
    for i,file in enumerate(os.listdir(action_directory_path)) :
         if i == 5:
             break 
         filename = os.fsdecode(file)
         new_folder_directory = os.path.join(new_action_directory_path, filename)
         os.mkdir(new_folder_directory, 0o777)
         if filename.endswith(".avi"):
            vidcap = cv2.VideoCapture(os.path.join(action_directory_path, filename))
            success,image = vidcap.read()
            count = 0
            success = True
            while success:
                success,image = vidcap.read()
                if success:
                    cv2.imwrite(os.path.join(new_folder_directory, "frame%d.jpg" % count), image)     # save frame as JPEG file
                    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
                        break
                    count += 1
         else:
             print(filename)
             continue

