# Makefile for making zip file to upload to lambda
TARGET = lambda.zip

zip:
	zip -r $(TARGET) *.py
	zip -r $(TARGET) *.env

# Path: Makefile
# Makefile for making zip file to upload to lambda

.PHONY: zip
