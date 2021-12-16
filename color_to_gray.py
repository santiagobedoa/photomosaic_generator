import cv2
import os


# convert color image to gray scale image
def Color2Gray(image_path, name_to_save, path_to_save):

    original_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    os.chdir(path_to_save)
    cv2.imwrite(f'{name_to_save}.jpg', gray_image)


# convert each images to gray scale
def gray_image_pool():

    working_directory = os.getcwd()

    # delete existing folder
    if os.path.exists(working_directory+'/image_pool'):
        os.rename('image_pool', 'color_image_pool')

    # create folder to save images
    os.mkdir('image_pool')
    images_names = os.listdir(working_directory+'/color_image_pool')
    for image in images_names:
        Color2Gray(f'{working_directory}/color_image_pool/{image}', str(image), f'{working_directory}/image_pool')