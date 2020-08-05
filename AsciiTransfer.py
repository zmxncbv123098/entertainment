import cv2


def lumToChar(l):
    result = '@'
    if l >= 230.0:
        result = ' '
    elif l >= 200.0:
        result = '.'
    elif l >= 180.0:
        result = '*'
    elif l >= 160.0:
        result = ':'
    elif l >= 130.0:
        result = '.' #o
    elif l >= 100.0:
        result = '@' #&
    elif l >= 70.0:
        result = '8'
    elif l >= 50.0:
        result = '#'
    return result


image = cv2.imread('logo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
res = cv2.resize(gray, (144, 80))


s = ''
for i in res:
    for j in i:
        s += lumToChar(j)
    s += '\n'
print(s)


#cv2.imshow("Resize image", res)
#cv2.waitKey(0)
