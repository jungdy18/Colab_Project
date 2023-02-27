import cv2
import matplotlib.pyplot as plt
import numpy as np

image =cv2.imread('/content/drive/MyDrive/image_compare/sliced_image/sample.png', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('/content/drive/MyDrive/image_compare/sorted_image/sample.png', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread("/content/drive/MyDrive/image_compare/sliced_image/sample.png")

result = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
x, y = minLoc
h, w = template.shape
img_height, img_width = image.shape
dst = cv2.rectangle(dst, (x, y), (x +  w - 1, y + h - 1) , (0, 0, 255), 1)
# plt.imshow(dst)
print(template.shape)
img = np.array(image)
img[:img_height, :img_width] = np.zeros((img_height,img_width))
img[y:y+h,x:x+w]=np.ones((h,w))
# plt.imshow(image)
plt.imshow(img)

print('이미지 가로 X 세로 = %d X %d' %(img_width, img_height))
print('템플릿 가로 X 세로 = %d X %d' %(w,h))
print('템플릿 시작 (x,y)  = (%d,%d)' %(x,y))
print('템플릿 종료 (x,y)  = (%d,%d)' %(x+w-1,y+h-1))


begin_x = 0
begin_y = 0


while begin_y<img_height:
  while begin_x<img_width:
    if (img[begin_y,begin_x]==1):
      break
    else:
      begin_x+=1
  if (begin_x==img_width):
    begin_y+=1
    begin_x=0
  else:
    break


print(begin_x, begin_y)


end_x = begin_x
end_y = begin_y

while end_x<img_width:
  if (img[end_y,end_x]==0):
    end_x = end_x-1
    break
  else:
    end_x+=1
while end_y<img_width:
  if (img[end_y,begin_x]==0):
    end_y=end_y-1
    break
  else:
    end_y+=1

print(end_x,end_y)

plt.imshow(dst)

plt.imshow(image)