import itchat
import math
import PIL.Image asImage
import os

itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

num = 0fori in friends:img = itchat.get_head_img(userName=i["UserName"])
 fileImage = open('文件夹'+ "/"+ str(num) + ".jpg",'wb')
 fileImage.write(img)
 fileImage.close()
 num += 1ls= os.listdir('文件夹')
each_size = int(math.sqrt(float(640*640)/len(ls)))
lines = int(640/each_size)
image = Image.new('RGBA', (640, 640)) x= 0y= 0fori in range(0,len(ls)+1): try:
 img = Image.open('文件夹'+ "/"+ str(i) + ".jpg")
 except IOError: print("Error") else:
 img = img.resize((each_size, each_size), Image.ANTIALIAS)
 image.paste(img, (x* each_size, y* each_size)) x+= 1ifx== lines:x= 0y+= 1image.save('文件夹'+ "/"+ "all.jpg")
itchat.send_image('文件夹'+ "/"+ "all.jpg", 'filehelper')