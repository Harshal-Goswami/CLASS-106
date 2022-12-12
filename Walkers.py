import cv2


# Create our body classifier
body_classifier = cv2.CascadeClassifier('haarcascade_fullody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale



    bodies = body_classifier.detectMultiScale('gray', 1, 2)    
    
    
    for (x, y, w,h) in bodies:
     cv2.rectangle(bodies(x,y), (x+w,y+h),(255,0,0),2)

    if cv2.waitKey(1) == 32: 
        break


cap.release()
cv2.destroyAllWindows()
cv2.imshow()