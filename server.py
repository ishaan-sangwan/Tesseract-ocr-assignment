'''module providing the API server that extracts text from images and bbox from them'''
from utils import *
from flask import Flask, request, jsonify
from PIL import Image, UnidentifiedImageError
import pytesseract as pt
# import pan

app = Flask(__name__)

@app.route("/api/get-text", methods=['POST'])
def get_text():
    '''
        function to extract text from images 
        input: base46 encoded image
        output: text in the image
    '''
    try:
        data = request.get_json()
        assert data
        image = decode_b64_image(data)
        extraction = extract_text_from_image(image)
        return jsonify({"success":True,
                'result':{
                    "text":extraction
                }})
    except ( UnidentifiedImageError, ValueError):
        return jsonify({'success':False,
                        "error":{
                            "message":"Invalid base64_image."
                        }})


@app.route("/api/get-bboxes", methods=["POST"])
def get_bboxes():
    '''
        function to return the bounding box according to the heirarchy of OCR provided in input
    '''
    
    try:
        data = request.get_json()
        assert data
        level = extract_box_type(data)
        image = decode_b64_image(data)
        extract_text_from_image(image)
        boxes = extract_bounding_boxes(image, level)
        
        return jsonify({'success':True, 'result':{"bboxes":boxes}})
    
    except KeyError:
        # print(KeyError)
        return jsonify({"success":False, "error":{"message":"Invalid bbox_type."}})
            
    except (UnidentifiedImageError , ValueError):
        return jsonify({"success":False, "error":{"message":"Invalid base64_image."}})

if __name__ == "__main__":
    app.run()
