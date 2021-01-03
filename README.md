# SZE_mask_detection
The main pourpose of this project is to detect masks on human faces. This is done in real time with a video stream. But you can also find python scripts for face detection only, both on a single image and on a video stream.


## First step
open a terminal and clone this repo
```
git clone https://github.com/Holdmedve/SZE_mask_detection
```

## (Optional)
create a python virtual env
use **conda** for example
```
conda activate ENVNAME
```
[conda cheat sheet](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)

## Install packages
```
pip install -r requirements.txt
```

## Usage

mask detection with webcam
```
python video_mask_detection.py
```

face detection on image
```
python image_face_detection.py -i ventura.jpg -p deploy.prototxt -m res10_300x300_ssd_iter_140000.caffemodel
```

face detection with webcam
```
python video_face_detection.py -p deploy.prototxt -m res10_300x300_ssd_iter_140000.caffemodel
```

## Training

train the mask detector model
```
python train_mask_detector.py -d dataset
```

