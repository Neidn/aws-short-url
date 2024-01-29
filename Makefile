# Makefile for making zip file to upload to lambda
TARGET = lambda.zip

zip:
	rm -f $(TARGET)
	zip -r $(TARGET) *.py

# Path: Makefile
# Makefile for making zip file to upload to lambda

.PHONY: zip
