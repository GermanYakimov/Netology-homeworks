import subprocess
from os import path, listdir, getcwd, mkdir


def photo_resize(photo_names):
    for photo in photos_names:
        input_photo = path.abspath(path.join('Source', photo))
        output_photo = path.abspath(path.join('Result', photo))
        subprocess.call(['convert', input_photo, '-resize', '200', output_photo])


photos_names = listdir(path.join(getcwd(), 'Source'))

if not path.exists(path.abspath(path.join(getcwd(), 'Result'))):
    mkdir(path.abspath(path.join(getcwd(), 'Result')))

photo_resize(photos_names)
