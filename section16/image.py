
print('\n***************** Image with Python *******************')

'''
work with images with the Pillow library
%pip install pillow
how to open and save image files and interact with images 
https://pillow.readthedocs.io/en/stable/

'''

from PIL import Image
mac = Image.open('C:\\Users\\amelkhodary\\Downloads\\img.jfif')
print(type(mac))
'''
<class 'PIL.JpegImagePlugin.JpegImageFile'>
'''
mac.show()
print(mac.size)
print(mac.filename)
mac.crop((0,0,25,25))
mac.show()


'''
* COLOR TRANSPARENCY
* RGBA
* Red , Green , Blue , Alpha

'''

red = Image.open('C:\\Users\\amelkhodary\\Downloads\\img.jfif')
red.putalpha(128)
red.show()

