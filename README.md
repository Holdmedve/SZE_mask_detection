# SZE_mask_detection
##(Optional)
create a python virtual env

##Install packages
'''
pip install -r requirements.txt
'''

##Usage

mask detection with webcam
'''
python video_mask_detection.py
'''

face detection on image
'''
python image_face_detection.py -i ventura.jpg -p deploy.prototxt -m res10_300x300_ssd_iter_140000.caffemodel
'''

face detection with webcam
'''
python video_face_detection.py -p deploy.prototxt -m res10_300x300_ssd_iter_140000.caffemodel
'''

##Training

train the mask detector model
'''
python train_mask_detector.py -d dataset
'''

