#!/usr/bin/python3

import pytweening
import glob, os, shutil

image_file_pattern = '*.jpg'
total_animation_frames = 70 # The number of frames to complete the animation in
output_dir_name = 'tweened_images'

image_extension = image_file_pattern.split('.')[-1]
os.mkdir(output_dir_name)
 
image_sequence = glob.glob(image_file_pattern) # List of images in the current directory

# The INDEX of the minimum and maximum value of the property being tweened
# Here, the 'min_val' is the first frame of the image sequence, which is at index 0
# And the 'max_val' is the last frame of the image sequence at index 
min_val = 0
max_val = len(image_sequence) - 1

tweened_sequence = []

for i in range(total_animation_frames):
	tween_progress = i / total_animation_frames
	tween_value = pytweening.easeInOutCirc(tween_progress)	
	adjusted_tween_value = (tween_value * max_val) + min_val # The tween value adjusted to the required range
	tween_frame = image_sequence[round(adjusted_tween_value)]
	tweened_sequence.append(tween_frame)

for i in range(len(tweened_sequence)):
	# This loop will copy each image belonging to the tweened_sequence into a new directory
	# The images therein will be named "%05d".extension according to their occurence
	source_image = tweened_sequence[i]
	target_image = '.'.join(["%05d" % i, image_extension])
	shutil.copyfile(source_image, os.sep.join([output_dir_name, target_image]))

print("Done!")


# get the image source dir from command line (argparse)
# os.chdir() into the dir
# take the image file pattern from there as well (or just create a list of that?)
