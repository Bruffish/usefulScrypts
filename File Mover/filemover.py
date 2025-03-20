import os
import shutil

# Specify the source and destination paths
src_path = '/PATH/TO/SOURCE' #source folder
dst_path = '/PATH/TO/DESTINATION' #destination folder
file_extension ='.mp3' #file extension to move
# Create the destination directory if it doesn't exist
if not os.path.exists(dst_path):
    os.makedirs(dst_path)

# Move defined files matching the file type above from source to destination
for root, dirs, files in os.walk(src_path):
    for file in files:
        src_file = os.path.join(root, file)
        if file.endswith(file_extension):
            dst_file = os.path.join(dst_path, file)
            shutil.move(src_file, dst_file)