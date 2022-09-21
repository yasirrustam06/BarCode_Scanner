

## FOR STATIC IMAGE




# import cv2
# import numpy as np
# from pyzbar.pyzbar import  decode
# img=cv2.imread("Qrcode1.png")
# code= decode(img)
# print(code)
#
#
# for barcode in decode(img):
#     # print(barcode.rect)
#     print(barcode.data)
#     myData=barcode.data.decode('utf-8')
#     print(myData)
#




#########555555##########5555555555555555####################3########################3####################3##################3

             ######  WEBCAM OR VIDEO  #####
##################%%%%%%%%%%%$$$$$$$4##################################################3333



import cv2
import numpy as np
from pyzbar.pyzbar import  decode

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    ret,img=cap.read()
    # code=decode(img)
    ####
    # to acquire seperate information about an barcode or qrcode image
    for barcode in decode(img):
        print(barcode.rect)
        ###################
        print(barcode.data)
        #####################
        # myData=barcode.data.decode('uft-8')
########  for adding the bounding boxes   ########3

        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,0),5)
        pts2=barcode.rect
        cv2.putText(img,str(barcode.data),(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    3,(255,0,0),2)



        # print(myData)

    cv2.imshow("image",img)
    cv2.waitKey(1)












