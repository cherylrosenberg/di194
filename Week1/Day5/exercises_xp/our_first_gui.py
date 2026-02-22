# exercises!
# read through the list and every time you see a zero, display a space. When you see a 1, display a *
 
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# iterate over a picture
    # if 0 -> print ''
    # if 1 -> print *

for image in picture:
    for pixel in image:
        if(pixel) == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# for i in picture[i]:
#     while True:
#         for j in picture[i][j]:
#             if j == 0:
#                 print(' ')
#             else:
#                 print('*')