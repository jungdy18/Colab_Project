import cv2

global count
count = 0
img_name = 'a'


# https://www.youtube.com/watch?v=-Hz2jA9nHec



def mouse_callback(event, x, y, flags, param):
    global old_x, old_y, new_x, new_y
    global model
    img_result = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        old_x, old_y = x,y
        new_x = old_x + 24
        new_y = old_y + 24
        # cv2.rectangle(img_result, (old_x,old_y), (new_x,new_y),(0,0,0),thickness=3)
        outline_image = cv2.rectangle(img_result, (old_x,old_y), (new_x,new_y),(0,0,0),thickness=3)
        cv2.imshow("image", img_result)
        
        cropped_image = img_result[old_y:new_y, old_x:new_x].copy()
        cv2.imwrite('/content/drive/MyDrive/image_compare/sorted_image/%d.png' %count, cropped_image)
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     cropped_image = img_result[old_y:new_y, old_x:new_x].copy()
    #     cv2.imwrite(r'C:\Users\jungd\Documents\dyeon\python\image_slicer\saved_image\%s\%s%d.png' %(model,img_name,count), cropped_image)
        


while True:
    img = cv2.imread('/content/drive/MyDrive/image_compare/sliced_image/%d.png' %count, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', mouse_callback)
    while True:
        key = cv2.waitKey()
        if key == 32:
            break

    cv2.destroyAllWindows()
    count += 1