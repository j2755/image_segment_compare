
import numpy as np
import PIL
import math


def get_average_of_array(array):
	return np.mean(array)


def mean_squared_error(list_of_values1,list_of_values2):
	n = len(y)
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
			list_of_aver.append(get_average_of_array(set_of_dicts[key]))
		mean_of_values=[np.mean(list_of_aver)]*len(list_of_aver)
		aver_dict.update({key:mean_squared_error(mean_of_values,list_of_aver)})
	return(aver_dict)

