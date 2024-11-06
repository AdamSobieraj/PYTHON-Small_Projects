import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = x ** 2

plt.plot(x,y)

# plt.plot(x,y, color='red') # zmieniamy kolor poprzedniej linii
# plt.plot(x,y-10,color='blue',ls='dashed') # dodajemy drugą linię na tym samym wykresie
# plt.xlabel('oś X', size=15, color='indigo') # dodajemy opis osi X
# plt.ylabel('oś Y', size=15, color='indigo') # dodajemy opis osi Y
# plt.title('Tytuł wykresu', size=20, color='navy') # dodajemy tytuł wykresu
# plt.xticks(color='indigo')
# plt.yticks(color='indigo')
# plt.grid()
# plt.axhline(y=50, color='k', linestyle='--')
# plt.axvline(x=5, color='k', linestyle='--')
# plt.show()
#
#
#
# plt.subplot(1,2,1)
# plt.plot(x,y,color='red')
#
# plt.subplot(1,2,2)
# plt.plot(y,x,color='blue')
#
# plt.show()
#
# ##############################################
# def koch_snowflake(order, scale=10):
#
#     """
#     Return two lists x, y of point coordinates of the Koch snowflake.
#     Parameters
#     ----------
#     order : int
#         The recursion depth.
#     scale : float
#         The extent of the snowflake (edge length of the base triangle).
#     """
#
#     def _koch_snowflake_complex(order):
#         if order == 0:
#
#             # initial triangle
#             angles = np.array([0, 120, 240]) + 90
#             return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
#
#         else:
#
#             ZR = 0.5 - 0.5j * np.sqrt(3) / 3
#             p1 = _koch_snowflake_complex(order - 1)  # start points
#             p2 = np.roll(p1, shift=-1)  # end points
#             dp = p2 - p1  # connection vectors
#             new_points = np.empty(len(p1) * 4, dtype=np.complex128)
#             new_points[::4] = p1
#             new_points[1::4] = p1 + dp / 3
#             new_points[2::4] = p1 + dp * ZR
#             new_points[3::4] = p1 + dp / 3 * 2
#
#             return new_points
#
#     points = _koch_snowflake_complex(order)
#     x, y = points.real, points.imag
#     return x, y
#
# x, y = koch_snowflake(order=5)
# plt.fill(x, y)
# plt.axis('equal')
# plt.show()
#
# plt.fill(x-2, y-2, color='red', alpha=0.5)
# plt.fill(x+2, y+2, color='green', alpha=0.5)
# plt.fill(x, y, color='blue', alpha=0.5)
# plt.axis('equal')
# plt.show()

######################################################
# rand_arr = np.random.randint(1,1000,2000).reshape(1000,2)
#
# plt.scatter(rand_arr[:,0],rand_arr[:,1])
#
# cmap = np.empty(rand_arr.shape,dtype='object')
# cmap[:] = 'blue'
# cmap[rand_arr.min(axis=1)>500] = 'red'
#
# plt.scatter(rand_arr[:,0],rand_arr[:,1],c=cmap[:,0])
#
# plt.figure(figsize=(10,5))
# plt.scatter(rand_arr[:,0],rand_arr[:,1],c=cmap[:,0])
#
# pie_data = np.array([30,20,20,40,10])
# labels = ['A','B','C','D','E']
#
# plt.pie(pie_data,labels=labels,autopct='%1.1f%%')
# plt.show()
###################################################

fig = plt.figure()
axes = fig.add_axes([0,0,1,1]) # left, bottom, width, height

fig = plt.figure()
axes = fig.add_axes([0,0,1,1]) # left, bottom, width, height
x = np.arange(11)
y = x ** 2
axes.plot(x,y)
axes.set_xlabel('oś X')
axes.set_ylabel('oś Y')
axes.set_title('Tytuł wykresu')

fig = plt.figure()
axes1 = fig.add_axes([0,0,1,1])
axes2 = fig.add_axes([.2,.2,.8,.8])
axes1.plot(x,y)
axes2.scatter(rand_arr[:,0],rand_arr[:,1])
axes1.set_xlabel('Exponential')
axes2.set_xlabel('Random')
