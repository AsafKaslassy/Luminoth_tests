import re
import os
import sys
import cv2
import time
import json
import glob
import click
import numpy as np
import tensorflow as tf
from time import strftime
from luminoth import Detector, read_image, vis_objects


__author__ = "Asaf Kaslassy"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "V_0.0.1+pep_8"
__maintainer__ = "Asaf Kaslassy"
__email__ = "Asaf.kaslassy@gmail.com"
__status__ = "Tests"



IMAGE_FORMATS = ['tif', 'tiff', 'png', 'jpg', 'jpeg']
VIDEO_FORMATS = ['mov', 'avi', 'mp4']


def get_file_type(filename):
    """Returns the image or video if extension's format exists.
        Args:
            file name
        Returns:
            'image' or 'video' if extension is in the Formats
        """
    extension = filename.split('.')[-1].lower()
    if extension in IMAGE_FORMATS:
        return 'image'

    elif extension in VIDEO_FORMATS:
        return 'video'

print('possible Image formats are ',IMAGE_FORMATS )
print('possible Video formats are ',VIDEO_FORMATS )


def resolve_files(path_or_dir):
    """Returns the file paths for `path_or_dir`.
    Args:
        path_or_dir: String or list of strings for the paths or directories to
            run predictions in. For directories, will return all the files
            within.
    Returns:
        List of strings with the full path for each file.
    """
    if not isinstance(path_or_dir, tuple):
        path_or_dir = (path_or_dir,)
    paths = []
    for entry in path_or_dir:
        if tf.gfile.IsDirectory(entry):
            paths.extend([
                os.path.join(entry, f)
                for f in tf.gfile.ListDirectory(entry)
                if get_file_type(f) in ('image', 'video')
            ])
        elif get_file_type(entry) in ('image', 'video'):
            if not tf.gfile.Exists(entry):
                click.echo('Input {} not found, skipping.'.format(entry))
                continue
            paths.append(entry)

    return paths


def run_module():
    """Runs Luminoth module to simulate perception outputs.
     Args:
         images: String or list of strings for the paths or directories to
             run predictions in. For directories, will return all the files
             within.
     Returns:
         List of objects detected (bounding box with probabaility and name of object.
     """

    images = [cv2.imread(file) for file in glob.glob(r'E:\CarTests\*.' +'IMAGE_FORMATS')]
    detector = Detector(checkpoint='cars')
    # Returns a dictionary with the detections.
    objects = detector.predict(images)
    print(objects)
    vis_objects(images, objects).save(r'E:\CarTests\objects')

    return objects

def read_luminoth_log(log_file_path):
    """reads and parses the Luminoth Log.
        Args:
            log_file_path
        Returns:
             parsed Luminoth  Log 
        """
    log_file_path = r"E:\CarTests\Luminoth.log"
    export_file_path = r"C:\ios logs\filtered"

    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file

    regex = '(<property name="(.*?)">(.*?)<\/property>)'

    parse_data(log_file_path, export_file, regex, read_line=True, reparse=True)

def parse_data(log_file_path, export_file, regex, read_line=True, reparse=True):
    with open(log_file_path, "r") as file:
        match_list = []
        while read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)

        else:
            data = file.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
    file.close()

    if reparse == True:
        match_list = reparse_data(match_list, '(property name="(.{1,50})">(Enabled)<\/property>)')

        with open(export_file, "w+") as file:
            file.write("EXPORTED DATA:\n")
            match_list_clean = list(set(match_list))
            for item in range(0, len(match_list_clean)):
                print (match_list_clean[item])
                file.write(match_list_clean[item] + "\n")
        file.close()
        return match_list_clean

def reparse_data(parsed_data, regex):
    data_string = ''.join(parsed_data)
    match_list = []
    for match in re.finditer(regex, data_string, re.S):
        match_text = match.group()
        match_list.append(match_text)
    return match_list
