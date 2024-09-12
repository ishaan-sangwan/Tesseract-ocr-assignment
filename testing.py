import unittest
from PIL import Image
import requests
from base64 import b64encode
import utils
url = 'http://localhost:5000'

valid_image = ''
with open("1.jpg", 'rb') as f:
    valid_image = b64encode(f.read()).decode('utf-8')

invalid_image = ''
with open("2.jpg",'rb') as f:
    invalid_image =  b64encode(f.read()).decode('utf-8')

non_image = ''
with open("1.txt",'rb') as f:
    non_image =  b64encode(f.read()).decode('utf-8')

class TestTextAPI(unittest.TestCase):
    def test_invalid_image(self):
        resp =requests.post(url+'/api/get-text', json={"base64_image":invalid_image})
        
            
        expected = {
            'success':False,
            'error':{
                'message':"Invalid base64_image."
            }
        }
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        self.assertDictEqual(resp.json(), expected)

    def test_non_image(self):
        resp = requests.post(url+"/api/get-text", json={"base64_image":non_image})
        expected = {
            'success':False,
            'error':{
                'message':"Invalid base64_image."
            }
        }
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        self.assertDictEqual(expected, resp.json())
    def test_valid_image(self):
        resp = requests.post(url+"/api/get-text", json={"base64_image":valid_image})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        self.assertEqual(resp.json()['success'], True)

class Test_BBox_API(unittest.TestCase):
    def test_invalid_image(self):
        resp = requests.post(url+"/api/get-bboxes", json={"base64_image":invalid_image,'bbox_type':'word'})
        expected = {
            'success':False,
            'error':{
                'message':"Invalid base64_image."
            }
        }
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        self.assertDictEqual(expected, resp.json())

    def test_non_image(self):
        resp = requests.post(url+"/api/get-bboxes", json={"base64_image":non_image,'bbox_type':'word'})
        expected = {
            'success':False,
            'error':{
                'message':"Invalid base64_image."
            }
        }
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        self.assertDictEqual(expected, resp.json())
    def test_invalid_box_type(self):
        resp = requests.post(url+"/api/get-bboxes", json={"base64_image":valid_image, 'bbox_type':'foo'})
        expected = {
            'success':False,
            'error':{
                'message':"Invalid bbox_type."
            }
        }
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers['Content-Type'], 'application/json')
        self.assertDictEqual(expected, resp.json())

    def test_valid_image(self):
        for type in utils.BBOX_TYPES:
            resp = requests.post(url+"/api/get-bboxes", json={'base64_image':valid_image, 'bbox_type':type})
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.headers['Content-Type'], 'application/json')
            self.assertEqual(resp.json()['success':True])
if __name__ == "__main__":
    unittest.main()