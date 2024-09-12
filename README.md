# Tesseract OCR Assignment 
### Submition by Ishaan Sangwan

This repo contains all the code for tesseract ocr assignment written by ishaan sangwan, this is a flask server with two valid endpoints 
```
/api/get-text
/api/get-bboxes
```

## Setup

### 1. Docker 
The user can run the server using docker by using the following commands 

```bash
docker pull j1roscope/assignment
docker run docker.io/j1roscope/assignment
```
the docker image can also be found at 
https://hub.docker.com/repository/docker/j1roscope/assignment

The user will need docker to be installed in their machine. Please refer to the documentation to do so on https://docs.docker.com/engine/install/

### 2. Run manually 
To run the code manually using python the user needs to ensure that python and tesseract-ocr is installed on their machine

#### Linux
Run the following commands to install Tesseract-ocr3  on debian linux or ubuntu

```bash
sudo apt install -y tesseract-ocr  tesseract-ocr-eng  libtesseract-dev libleptonica-dev 

```
#### Windows
Download tesseract exe from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki).
run this exe file to install the tesseract binaries

## Running code
Follow the given steps to run the code 

1. create a virtual enviroment using python venv if already not existing 
```bash
python -m venv ./venv
```
2. activate the virtual environment 
	if in Linux use 
	```bash 
	source venv/bin/activate
	```
	if in windows use 
	```cmd
	venv/Scripts/activate
	``` 
3. install the dependancies 
	```bash 
	pip install -r requirements.txt
	```
4. run the ```server.py``` file
	```python server.py```

## Testing 
This repo contains code for testing the API end points.
Run the server using the steps mentioned above and then open a different terminal to run the command
```bash
python testing.py
```


 

 
