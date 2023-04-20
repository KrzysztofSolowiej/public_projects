# Semantic segmentation project

The project is an implementation of the Mask R-CNN algorithm aimed to detect and segment rectangular shapes in paintings of Mark Rothko.

The training set consisted of 128 and the validation set of 22 different images with coco style annotations in JSON format.

The training process was stopped after seven epochs consisting of 128 steps. The resulting model detects two classes of objects:

    'rectangle' - a large rectangle with a distinctive color
    'band' - a horizontal strip of distinctive color

By using segmentation, the following properties of the detected region can be calculated:

    Class
    Average color
    Brightness of color (bright/dull)
    Max horizontal pixels
    Max vertical pixels
    Region surface
    Percentage share in the area of the whole image

Resources:

https://github.com/ahmedfgad/Mask-RCNN-TF2

https://github.com/bnsreenu/python_for_microscopists/blob/master/286-Object%20detection%20using%20mask%20RCNN%20-%20end%20to%20end/286-marbles_maskrcnn_coco_style_labels.py
