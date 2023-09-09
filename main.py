import cv2

#configurable parameters
source="sunset.jpg"
destination='newImage.png'
scale_percent= 50

src= cv2.imread("source",cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)
#percent by which the image is resized
#calculate the 50 percent of original dimension

new_width=int(src.shape[1] * scale_percent/100)
new_height=int(src.shape[0] *scale_percent/100)
#resize image

dsize=(new_width,new_height)
output=cv2.resize(src,dsize)

cv2.imwrite(destination,output)
#cv2.waitKey(0)












