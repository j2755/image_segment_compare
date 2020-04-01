
import numpy as np
import PIL
from PIL import Image
import math
from image_segmentation import image_segmentation

def get_average_of_array(array):
	return np.mean(array)


def mean_squared_error(list_of_values1,list_of_values2):
	n = len(list_of_values1)
	summation=0
	for i in range (0,n):  
		difference = list_of_values1[i] - list_of_values2[i] 
		squared_difference = difference**2  
		summation = summation + squared_difference  

	return summation/n

def compare_array_dicts(set_of_dicts):
	aver_dict={}
	for key in set_of_dicts[0].keys():
		list_of_aver=[]
		for entry in set_of_dicts:


			list_of_aver.append(get_average_of_array(entry[key]))
		mean_of_values=[np.mean(list_of_aver)]*len(list_of_aver)
		aver_dict.update({key:mean_squared_error(mean_of_values,list_of_aver)})
	return(aver_dict)


def convert_images_to_np_arrays(list_of_image_directories):
	array_list=[]

	for i in list_of_image_directories:
		with Image.open(i).convert('L') as im:

			temp=np.asarray(im)
			print(temp.shape)
			array_list.append(temp)
	return array_list

def compare_images(list_of_image_directories):
	#Only works properly with sets of images whose dimensions have a large gcd
	#Too slow for large scale use
	array_list=convert_images_to_np_arrays(list_of_image_directories)
	dict_list=image_segmentation.segment_list_of_arrays(array_list)
	return compare_array_dicts(dict_list)

