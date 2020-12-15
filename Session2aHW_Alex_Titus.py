import os
from PIL import Image
from PIL import ImageFilter 
from PIL.Image import new

#the original folder 
#old_folder = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2\\session2a-image\\raw"

#where we want to move the images
#processed folder
Processed = "C:\\Users\\Gebruiker\\OneDrive\\CLS PhD\\MPI\\Python_workshop\\Session_2a_image_processing\\session2a-image\\PROCESSED"

#make a new directory
#os.mkdir(Processed)

#Now we want to list all of the things in the old folder
#image_list = os.listdir(old_folder)

#loop over images and save images in new folder as .png files
# for images in image_list:
#     filename, extension = os.path.splitext(images)
#     if extension == ".jpg":
#         image_path = os.path.join(old_folder, images)
#         image_open = Image.open(image_path)
#         png_outfile = filename + ".png"
#         image_open.save(png_outfile, "PNG")
#         image_open.save(os.path.join(Processed, png_outfile))
#     else:
#         if extension == ".png":
#             image_path = os.path.join(old_folder, images)
#             image_open = Image.open(image_path)
#             image_open.save(os.path.join(Processed, images))

new_image_list = os.listdir(Processed)

#check it 
#print(new_image_list)

for images in new_image_list:
    #once in the folder, the below finds the specific file
    image_path = os.path.join(Processed, images)
    #then access the image, but does not display it anywhere.
    img = Image.open(image_path)
    # we need to variables that extract the width and the length this needs to go in the for loop
    width = img.width
    height = img.height
    #we also need the coordinates of the center of the image. 
    center = (width/2, height/2)
#we need to determine if the image is in portrait or landscape using the min function
    shortest_side = min([width, height])
    distance_from_center = shortest_side/2

    #we need empy lists to store the center data related to the images
    #left most coordinates and right most coordinates
    left = []
    right = []

    #the below will loop over the images and find their center
    #Need to rewatch this to understand the coordinates better and getting to the center of an image and storing the data. 
    #we can append the results and store the data in the empty lists from above
    for number in center:
        left.append(number - distance_from_center)
        right.append(number + distance_from_center)

    #the above creates a squared box at the center of the image. 

    # Now we want to crop the image we just took the coordinates from
    img_square = img.crop((left[0], left[1], right[0], right[1]))

    image_resize = img_square.resize((100, 100))
    image_resize.save(os.path.join(Processed, images))
    #print(os.listdir(Processed))
    #image_resize.show()


