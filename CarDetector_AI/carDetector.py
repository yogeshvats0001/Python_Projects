import cv2

#get the image of the car in which we need to investigate
file_name1 = cv2.imread('car5.jpeg')

#convert the image into gray for faster computation
dark_file_name1 = cv2.cvtColor(file_name1, cv2.COLOR_BGR2GRAY)

#get the classifier file
classifier_file = 'car_classifier.xml';

#apply cascadeClassifier on the classifier file
car_cascade = cv2.CascadeClassifier(classifier_file)

#apply detectMultiScale on dark file
car = car_cascade.detectMultiScale(dark_file_name1)

#draw the rectangle 
for(x,y,w,h) in car:
    cv2.rectangle(file_name1, (x,y), (x+w,y+h), [0,0,255],2)

#display the image with cars spotted
cv2.imshow('Yogesh Detector', file_name1);

#hold the screen
cv2.waitKey()

print('Program Completed : Happy Coding')