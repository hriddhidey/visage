"""
Created on Mon Mar 20 12:28:21 2017
@author: Hriddhi Dey

This module contains the DetectLandmark class.
"""

import os.path
import sys
from urllib.request import urlretrieve
import cv2
import dlib
import numpy

PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
CASC_PATH = "haarcascade_frontalface_default.xml"


class DetectLandmarks(object):
    """
    This is the class responsible for landmark detection on a human face.

    Functions available for use:
        1. get_face_data: Returns all detected landmarks for a face.
        2. get_lips: Returns points of lips for a face.
        3. get_upper_eyelids: Returns points of eyeliner for a face.
    """

    IMAGE_DATA = 'IMAGE_DATA'
    FILE_READ = 'FILE_READ'
    NETWORK_BYTE_STREAM = 'NETWORK_BYTE_STREAM'



    def __init__(self):
        """ Initiator for DetectLandmarks class.
        Downloads the predictor file if not available.
        Raises:
            `Exception`, if download of predictor fails.
        """
        if not os.path.isfile(PREDICTOR_PATH):
            try:
                print ('Predictor not found. Downloading...this may take a while...')
                url = 'https://github.com/hriddhidey/visage/blob/master/visage/shape_predictor_68_face_landmarks.dat?raw=true'
                def dl_progress(count, block_size, total_size):
                    """ Show download progress bar. """
                    percent = int(count*block_size*100/total_size)
                    sys.stdout.write("\r" + 'Progress:' + "...%d%%" % percent)
                    sys.stdout.flush()
                urlretrieve(
                    url,
                    PREDICTOR_PATH,
                    reporthook=dl_progress
                )
                print ('Predictor downloaded.')
            except IOError:
                print ('Download failed. Try again with reliable network connection.')
                raise IOError
        self.predictor = dlib.shape_predictor(PREDICTOR_PATH)
        self.cascade = cv2.CascadeClassifier(CASC_PATH)
        self.detector = dlib.get_frontal_face_detector()



    def __get_landmarks(self, image):
        """ Extract the landmarks from a given image. 
        Returns `None` if no landmarks found.
        """
        try:
            rects = self.detector(image, 1)
            size = len(rects)
            if size == 0:
                return None, None
            return numpy.matrix([[p.x, p.y] for p in self.predictor(image, rects[0]).parts()])
        except Exception:
            return None



    def get_face_data(self, image_file, flag):
        """
        Returns all facial landmarks in a given image.
        ______________________________________________
        Args:
            1. `image_file`:
                Either of three options:\n
                    a. (int) Image data after being read with cv2.imread()\n
                    b. File path of locally stored image file.\n
                    c. Byte stream being received over multipart network request.\n\n
            2. `flag`:
                Used to denote the type of image_file parameter being passed.
                Possible values are IMG_DATA, FILE_READ, NETWORK_BYTE_STREAM respectively.
                By default its value is IMAGE_DATA, and assumes imread() image is passed.

        Returns:
            String with list of detected points of lips.

        Error:
            Returns `None` if face not found in image.

        """
        image = 0
        if flag == self.FILE_READ:
            image = cv2.imread(image_file)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif flag == self.NETWORK_BYTE_STREAM:
            image = cv2.imdecode(
                numpy.fromstring(image_file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED
            )
        elif flag == self.IMAGE_DATA or flag is None:
            image = image_file
        landmarks = self.__get_landmarks(image)
        if landmarks[0] is None or landmarks[1] is None:
            return None
        return landmarks



    def get_lips(self, image_file, flag=None):
        """
        Returns points for lips in given image.
        _______________________________________
        Args:
            1. `image_file`:
                Either of three options:\n
                    a. (int) Image data after being read with cv2.imread()\n
                    b. File path of locally stored image file.\n
                    c. Byte stream being received over multipart network reqeust.\n\n
            2. `flag`:
                Used to denote the type of image_file parameter being passed.
                Possible values are IMG_DATA, FILE_READ, NETWORK_BYTE_STREAM respectively.
                By default its value is IMAGE_DATA, and assumes imread() image is passed.

        Returns:
            String with list of detected points of lips.

        Error:
            Returns `None` if face not found in image.

        """
        landmarks = self.get_face_data(image_file, flag)
        if landmarks is None:
            return None
        lips = ""
        for point in landmarks[48:]:
            lips += str(point).replace('[', '').replace(']', '') + '\n'
        return lips



    def get_upper_eyelids(self, image_file, flag=None):
        """
        Returns points for upper eyelids in given image.
        ________________________________________________
        Args:
            1. `image_file`:
                Either of three options:\n
                    a. (int) Image data after being read with cv2.imread()\n
                    b. File path of locally stored image file.\n
                    c. Byte stream being received over multipart network reqeust.\n\n
            2. `flag`:
                Used to denote the type of image_file parameter being passed.
                Possible values are IMG_DATA, FILE_READ, NETWORK_BYTE_STREAM respectively.
                By default its value is IMAGE_DATA, and assumes imread() image is passed.

        Returns:
            String with list of detected points of lips.

        Error:
            Returns `None` if face not found in image.

        """
        landmarks = self.get_face_data(image_file, flag)
        if landmarks is None:
            return None
        liner = ""
        for point in landmarks[36:40]:
            liner += str(point).replace('[', '').replace(']', '') + '\n'
        liner += '\n'
        for point in landmarks[42:46]:
            liner += str(point).replace('[', '').replace(']', '') + '\n'
        return liner
