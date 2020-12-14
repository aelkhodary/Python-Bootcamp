'''
* Work with images with Python
* The Pillow library which is afork of the PIL (Python Imaging Library)
* https://pillow.readthedocs.io/en/stable/
>>   pip install pillow 'at your command line'

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
