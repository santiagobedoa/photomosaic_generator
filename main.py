from web_crawler import *
from color_to_gray import *
from photomosaic_generator import *

if __name__ == '__main__':

    download_images("atardeceres", "flores amarillas", "árboles", "pinturas moradas", "océano", "paredes blancas")
    input_type = input("is your input image in black and white? [yes/no]: ")
    if input_type.lower() == 'yes':
        gray_image_pool()
    opt = get_args()
    main(opt)