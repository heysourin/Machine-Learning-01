import numpy as np
import time

#! NumPy routines which allocate memory and fill arrays with value
# a = np.zeros(4)
# print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
# a = np.zeros((4,))
# print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample(4)
# print(
#     f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")


#! NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument
# a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
# a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")


#! NumPy routines which allocate memory and fill with user specified values: Notice how to initiate a array with float
# a = np.array([5,4,3,2]);  print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}")
# a = np.array([5.,4,3,2]); print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

#!vector indexing operations on 1-D vectors
# a = np.arange(10)
# print(a)

# #? # access an element
# # print(f"a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")

# #? access the last element, negative indexes count from the end
# print(f"a[-1] = {a[-1]}")

# #? # indexs must be within the range of the vector or they will produce and error
# try:
#     c = a[10]
# except Exception as e:
#     print("The error message you'll see is:")
#     print(e)

#! vector slicing operations [start:end:steps]; steps == 1 means print every element till (end-1)
# a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
# print(f"a = {a}")

# # access 5 consecutive elements (start:stop:step)
# c = a[2:7:1]
# print("a[2:7:1] = ", c)

# # access 3 elements separated by two
# c = a[2:7:2]
# print("a[2:7:2] = ", c)

# # access all elements index 3 and above
# c = a[3:]
# print("a[3:]    = ", c)

# # access all elements below index 3
# c = a[:3]
# print("a[:3]    = ", c)

# # access all elements
# c = a[:]
# print("a[:]     = ", c)

#! Single vector operations: There are a number of useful operations that involve operations on a single vector:
# a = np.array([1, 2, 3, 4])
# print(f"a: {a}")
# # negate elements of a
# b = -a                      #TODO
# print(f"b = -a: {b}")

# # sum all elements of a, returns a scalar
# b = np.sum(a)               #TODO
# print(f"b = np.sum(a): {b}")

# b = np.mean(a)              #TODO
# print(f"b = np.mean(a): {b}")

# b = a**2
# print(f"b = a**2: {b}")

# !Vector Vector element-wise operations: Most of the NumPy arithmetic, logical and comparison operations apply to vectors as well. These operators work on an element-by-element basis. For example # $$ c_i = a_i + b_i $$
# a = np.array([ 1, 2, 3, 4])
# b = np.array([-1,-2, 3, 4])
# print(f"Binary operators work element wise: {a + b}")
# #try a mismatched vector operation
# c = np.array([1, 2])
# try:
#     d = a + c
# except Exception as e:
#     print("The error message you'll see is:")
#     print(e)

#!Scalar Vector operations: Vectors can be 'scaled' by scalar values. A scalar value is just a number. The scalar multiplies all the elements of the vector.
# a = np.array([1, 2, 3, 4])

# multiply a by a scalar
# b = 5 * a
# print(f"b = 5 * a : {b}")

#!Vector Vector dot product:The dot product is a mainstay of Linear Algebra and NumPy. This is an operation used extensively in this course and should be well understood. The dot product is shown below.
# def my_dot(a, b):
#     x=0
#     for i in range(a.shape[0]):
#         x = x + a[i] * b[i]
#     return x
# #? test 1-D
# a = np.array([1, 2, 3, 4])
# b = np.array([-1, 4, 3, 2])
# print(f"my_dot(a, b) = {my_dot(a, b)}")

# #? test 1-D
# a = np.array([1, 2, 3, 4])
# b = np.array([-1, 4, 3, 2])
# c = np.dot(a, b)
# print(f"NumPy 1-D np.dot(a, b) = {c}, np.dot(a, b).shape = {c.shape} ")
# c = np.dot(b, a)
# print(f"NumPy 1-D np.dot(b, a) = {c}, np.dot(a, b).shape = {c.shape} ")

#!The Need for Speed: vector vs for loop: np.random.seed(1)
# a = np.random.rand(10000000)  # very large arrays
# b = np.random.rand(10000000)

# tic = time.time()  # capture start time
# c = np.dot(a, b)
# toc = time.time()  # capture end time

# print(f"np.dot(a, b) =  {c:.4f}")
# print(f"Vectorized version duration: {1000*(toc-tic):.4f} ms ")

# tic = time.time()  # capture start time
# c = my_dot(a,b)
# toc = time.time()  # capture end time

# print(f"my_dot(a, b) =  {c:.4f}")
# print(f"loop version duration: {1000*(toc-tic):.4f} ms ")

# del(a);del(b)  #remove these big arrays from memoryWe utilized the NumPy library because it improves speed memory efficiency. Let's demonstrate:
# ?So, vectorization provides a large speed up in this example. This is because NumPy makes better use of available data parallelism in the underlying hardware. GPU's and modern CPU's implement Single Instruction, Multiple Data (SIMD) pipelines allowing multiple operations to be issued in parallel. This is critical in Machine Learning where the data sets are often very large.

#!Vector Vector operations in Course 1
# Vector Vector operations will appear frequently in course 1. Here is why:

# ? Going forward, our examples will be stored in an array, X_train of dimension (m,n). This will be explained more in context, but here it is important to note it is a 2 Dimensional array or matrix (see next section on matrices).

# ? w will be a 1-dimensional vector of shape (n,).

# ? we will perform operations by looping through the examples, extracting each example to work on individually by indexing X. For example:X[i]

# ? X[i] returns a value of shape (n,), a 1-dimensional vector. Consequently, operations involving X[i] are often vector-vector.

# ? That is a somewhat lengthy explanation, but aligning and understanding the shapes of your operands is important when performing vector operations.

# show common Course 1 example
# X = np.array([[1],[2],[3],[4]])
# w = np.array([2])
# c = np.dot(X[1], w)

# print(f"X[1] has shape {X[1].shape}")
# print(f"w has shape {w.shape}")
# print(f"Value of c: {c}")
# print(f"c has shape {c.shape}")

#! Matrices:
# a = np.zeros((1, 5))
# print(f"a shape = {a.shape}, a = {a}")

# a = np.zeros((2, 1))
# print(f"a shape = {a.shape}, a = {a}")

# a = np.random.random_sample((1, 1))
# print(f"a shape = {a.shape[0]}, a = {a}")
# print(f"a shape = {a.shape[1]}, a = {a}")

# NumPy routines which allocate memory and fill with user specified values
# a = np.array([[5], [4], [3]])
# print(f" a shape = {a.shape}, np.array: a = {a}")
# a = np.array([[5],   # One can also
#               [4],   # separate values
#               [3]])  # into separate rows
# print(f" a shape = {a.shape}, np.array: a = {a}")

#! Operations on Matrices: Let's explore some operations using matrices.
# vector indexing operations on matrices
# reshape is a convenient way to create matrices
# a = np.arange(6).reshape(-1, 2)
# print(f"a.shape: {a.shape}, \na= {a}")

# # access an element
# print(
#     f"\na[2,0].shape:   {a[2, 0].shape}, a[2,0] = {a[2, 0]},     type(a[2,0]) = {type(a[2, 0])} Accessing an element returns a scalar\n")

# # access a row
# print(
#     f"a[2].shape:   {a[2].shape}, a[2]   = {a[2]}, type(a[2])   = {type(a[2])}")

#!Slicing: Slicing creates an array of indices using a set of three values (`start:stop:step`). A subset of values is also valid. Its use is best explained by example:
# vector 2-D slicing operations
# a = np.arange(20).reshape(-1, 5)
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

# access 5 consecutive elements (start:stop:step)
# print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =",
    #   a[0, 2:7:1].shape, "a 1-D array")

# # access 5 consecutive elements (start:stop:step) in two rows
# print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =",
    #   a[:, 2:7:1].shape, "a 2-D array")

# # access all elements
# print("a[:,:] = \n", a[:, :], ",  a[:,:].shape =", a[:, :].shape)

# # access all elements in one row (very common usage)
# print("a[1,:] = ", a[1, :], ",  a[1,:].shape =", a[1, :].shape, "a 1-D array")
# # same as
# print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")
