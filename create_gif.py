"""
Created by: louisenaud on 5/5/22 at 12:57 PM for python_toold.
"""
import glob

from PIL import Image


def make_gif(frame_folder):
    frame_list = sorted(glob.glob(f"{frame_folder}/*.jpg"))
    frames = [Image.open(image) for image in frame_list]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)


if __name__ == "__main__":
    make_gif("./frames")