#author:decai.li    2018.01.24
from PIL import Image
from PIL import ImageEnhance
import pytesseract
import re
import time

#对图片进行初步的处理
def cutScreen(imagename):
    im = Image.open(imagename)
    imgsize = im.size
    print("图片宽度和高度分别是{}".format(imgsize))
    #裁剪图片
    region = im.crop((0, imgsize[1]-100, 150, imgsize[1]))

    #对比度+锐利度增强
    enh_con = ImageEnhance.Contrast(region)
    color = 2
    ImageHighBright = enh_con.enhance(color)

    enh_sha = ImageEnhance.Sharpness(ImageHighBright)
    ImageDeveloped = enh_sha.enhance(2)
    result=ImageDeveloped.convert('L')

    cutStr=str(imagename) + "_cut.png"
    result.save(cutStr)

    return cutStr

#调用tesseract引擎进行数字识别

def tesseract(imagename):
    #先用默认的,有空再自行训练
    ext = pytesseract.image_to_string(Image.open(imagename),
                                      config="-l fontyp -psm 7")

    extnum = re.sub("[^\\d.]+", "", ext)
    print("eeeeeeeeeeeee:",ext)
    extnum = float(extnum)
    #识别的明显有问题则抛弃
    if extnum >=100.0 or extnum <=0.0:
        return -1
    else:
        return extnum

def getOverDraw(imagename):
    custr = cutScreen(imagename)
    extnum = tesseract(custr)
    print('该页面名称与过度渲染层级为:',imagename,extnum)
    return extnum


#Baidu OCRAPi
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
