import numpy as np

import PIL





def segment_into_n_squared_tiles(n,array):
	rows,columns=np.shape(array)
	array_list={}

	if int(rows % n)==0 or int(columns % n)==0:
		iterator_rows=int(rows/n)

		iterator_columns=int(columns/n)
		for i in range(1,n+1):
			temp=n
			for j in range(1,n+1):

				array_list.update({(i,j):array[iterator_rows*(i-1):iterator_rows*(i),iterator_columns*(j-1):iterator_columns*(j)]})

	else:
		print('Column length or row length is not divisible by {} '.format(n))
	return array_list

def segment_into_maximum_num_of_tiles(array):
	rows,columns=np.shape(array)
	num_of_tiles=np.gcd(rows,columns)
	return(segment_into_n_squared_tiles(num_of_tiles,array))
z=np.arange(0,int(1080*720))
z=np.reshape(z,(1080,720))
print(len(segment_into_n_squared_tiles(360,z)))
