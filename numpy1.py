import numpy as np 


############################ Lesson 1 ########################################


# arr = np.array([[0, 1, 2], [3, 4, 5]],  # Numpy arrays are python lists with added features
#                dtype=np.float32)		# to convert a python list into a numpy array, we use np.array()
# 										# dtype takes argument in a NumPy type and casts the array into the type
# print(repr(arr))


# a = np.array([0, 1])					
# b = np.array([9, 8])
# c = a
# print('Array a: {}'.format(repr(a)))
# c[0] = 5
# print('Array a: {}'.format(repr(a)))

# d = b.copy()							# copy function used to create a new copy of an array from an already existing one
# d[0] = 6
# print('Array b: {}'.format(repr(b)))


# arr = np.array([0, 1, 2])
# print(arr.dtype)
# arr = arr.astype(np.float32)			# astype used to convert an array to a new type
# print(arr.dtype)						# NOTE: dtype used to return type of the array


# arr = np.array([np.nan, 1, 2])
# print(repr(arr))

# arr = np.array([np.nan, 'abc'])
# print(repr(arr))

# # Will result in a ValueError
# np.array([np.nan, 1, 2], dtype=np.int32) # np.nan used as a filler value to represent incomplete data



# print(np.inf > 1000000)

# arr = np.array([np.inf, 5]) 			# using np.inf/-np.inf to represent infinity
# print(repr(arr))

# arr = np.array([-np.inf, 1])
# print(repr(arr))

# # Will result in an OverflowError
# np.array([np.inf, 3], dtype=np.int32)


############################ Lesson 2 ########################################

arr = np.arange(5) 				# arange used to assign a range of values to the array instead of manually typing them out
print(repr(arr)) 				# o/p: [0,1,2,3,4]

arr = np.arange(5.1)
print(repr(arr))				# o/p: [0.,1.,2.,3.,4.,5.]

arr = np.arange(-1, 4)
print(repr(arr))				# o/p: [-1,0,1,2,3]

arr = np.arange(-1.5, 4, 2)		# third arguement is called: step size
print(repr(arr))				# o/p: [-1.5, 0.5, 2.5]




arr = np.linspace(5, 11, num=4) # similar to arange, differs in step size
print(repr(arr))				# o/p: [5.,7.,9.,11.]

arr = np.linspace(5, 11, num=4, endpoint=False)
print(repr(arr))				# o/p: [5.,6.5,8.,9.5]

arr = np.linspace(5, 11, num=4, dtype=np.int32)
print(repr(arr))				# o/p: [5,7,9,11]


arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))				# reshape used to change the dimension of an array, has to include all elements
print(repr(reshaped_arr))							# [[0,1,2,3],[4,5,6,7]]
print('New shape: {}'.format(reshaped_arr.shape))	# New shape: (2,4)

reshaped_arr = np.reshape(arr, (-1, 2, 2))			# if you dont know what dimension to use to have a elements in reshaped array, use '-1'
print(repr(reshaped_arr))							# [[[0,1],[2,3],[[4,5],[6,7]]]
print('New shape: {}'.format(reshaped_arr.shape))	# New shape: (2,2,2)


arr = np.arange(8)
arr = np.reshape(arr, (2, 4))
flattened = arr.flatten()							# flattens a multidimensional array back to 1D
print(repr(arr))
print('arr shape: {}'.format(arr.shape))
print(repr(flattened))
print('flattened shape: {}'.format(flattened.shape))


arr = np.arange(8)
arr = np.reshape(arr, (4, 2))
transposed = np.transpose(arr) 						# used to transpose an array
print(repr(arr))
print('arr shape: {}'.format(arr.shape))
print(repr(transposed))
print('transposed shape: {}'.format(transposed.shape))



arr = np.arange(24)
arr = np.reshape(arr, (3, 4, 2))
transposed = np.transpose(arr, axes=(1, 2, 0))
print('arr shape: {}'.format(arr.shape))
print('transposed shape: {}'.format(transposed.shape))

#o.p:
# 	arr shape: (3, 4, 2)
# transposed shape: (4, 2, 3)

arr = np.zeros(4)
print(repr(arr))

arr = np.ones((2, 3))
print(repr(arr))

arr = np.ones((2, 3), dtype=np.int32)
print(repr(arr))


arr = np.array([[1, 2], [3, 4]])
print(repr(np.zeros_like(arr)))

arr = np.array([[0., 1.], [1.2, 4.]])
print(repr(np.ones_like(arr)))
print(repr(np.ones_like(arr, dtype=np.int32)))