'''
    util functions for the server to use in API's 
'''
from io import BytesIO
from base64 import b64decode
from PIL import Image, UnidentifiedImageError
import pytesseract as pt


BBOX_TYPES =  {"word":5, "line":4, "paragraph":3, "block":2, "page":1}

def decode_b64_image(data):
    '''
        decodes base 64 image 
        input : data ( directory ) - the json recieved from client side
        output : image from the base64encoding of data
    ''' 
    try:
        image_data = b64decode(data['base64_image'])
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        raise UnidentifiedImageError("failed to decode image") from e

def extract_text_from_image(image):
    '''
        extracts text from image using the python wrapper
        for tesseract engine

        input: image recieved from client
        output: string of text from image 
    '''
    
    extraction = pt.image_to_string(image)
    if not extraction:
        raise ValueError("Text not extracted")
    return extraction

def extract_box_type(data):
    '''
        extract the level needed for extraction from data request
    '''


    try:
        type = data['bbox_type']
    except Exception as e:
        raise KeyError("invalid request") from e
    try:
        level = BBOX_TYPES[type]
        return level
    except Exception as e:
        raise KeyError("type not found") from e 

def extract_bounding_boxes(image, level):
    '''
        extract bounding according to level using python 
        wrapper for tesseract engine

        image: input image for client 
        level: level according to bounding box type
    '''

    df = pt.image_to_data(image, output_type=pt.Output.DATAFRAME)
    print(level)
    df = df[df['level']==level]
    boxes = []

    for row in df.iterrows():
        x_min,y_min = row[1]['left'], row[1]['top'] 
        x_max, y_max = x_min + row[1]['width'], y_min + row[1]['height']
        boxes.append(
            {
                            "x_min": x_min,
                            "y_min": y_min,
                            "x_max": x_max,
                            "y_max": y_max
                        }
        )
       
    return boxes