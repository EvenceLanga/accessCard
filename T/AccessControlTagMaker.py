from math import ceil
from PIL import Image, ImageFont, ImageDraw
from fpdf import FPDF
from PyPDF2 import PdfMerger
merger = PdfMerger()


#####################################################
# Options
#####################################################
NetNineNine = True
names = [
    #["Moltelo Segota", "Installs"],
    #["Elewani Mutandanyi","Support"],
    #["Theo Mampuru","Support"],
    #["Mbedzi Tshimangadza","Marketing"], 
    #["Kgomotso Moholola","IT and Systems"],
    #["Evence Mohau","IT and Systems"],
    #["Phenyo More","Planning"],
    #["Nokubonga Tshabalda","Marketing"]
    #["Robert Watt","Sales"],
    #["Songo Jizana","Marketing"]
    ["Amanda Reichert", "Sales"]
    ]
font_size = 95 # Defult is 95

#####################################################
path = "New office Tags Dunce 2.png"
if NetNineNine:
    shadowcolor = "white"
    path = "New office Tags.png"
else:
    shadowcolor = "black"
    path = "New office Tags Evotel-01.png"

#Special
#path = "Evotel 2.png"
##################
try: 
    img_main  = Image.open(path) 
except IOError:
    pass
images = []

#3508 x 2480


area = (58, 58, 1065, 699)


count = 0
images = []
for name,department in names:

    img  = img_main.crop(area)
    draw = ImageDraw.Draw(img)
    if NetNineNine:
        font = ImageFont.truetype("AllRoundGothic-Demi.ttf", font_size)
        font_for_department = ImageFont.truetype("AllRoundGothic-MediumOblique.ttf", 44)
    else:
        font = ImageFont.truetype("AvenirLTStd-Black.otf", 95)
        font_for_department = ImageFont.truetype("Avenir (10).ttc", 44)
    width, height = img.size
    if NetNineNine:
        fill_1 = (37,32,86,255)
        fill_2 = (0,0,0,255)
    else:
        fill_1 = (255,255,255,255)
        fill_2 = (255,255,255,255)

    width_of_txt, height_of_txt = draw.textsize(name,font=font)    
    x = (width-width_of_txt)/2
    y = (height-height_of_txt)/2+20
    
    draw.text((x-1, y), name, font=font, fill=shadowcolor)
    draw.text((x+1, y), name, font=font, fill=shadowcolor)
    draw.text((x, y-1), name, font=font, fill=shadowcolor)
    draw.text((x, y+1), name, font=font, fill=shadowcolor)
    draw.text((x,y), name, font=font, fill=fill_1)

    width_of_txt, height_of_txt = draw.textsize(department,font=font_for_department)
    x = (width-width_of_txt)/2
    y = (height-height_of_txt)/2-80
 
    draw.text((x-1, y), department, font=font_for_department, fill=shadowcolor)
    draw.text((x+1, y), department, font=font_for_department, fill=shadowcolor)
    draw.text((x, y-1), department, font=font_for_department, fill=shadowcolor)
    draw.text((x, y+1), department, font=font_for_department, fill=shadowcolor)
    draw.text((x,y), department, font=font_for_department, fill= fill_2)
    images.append(img)
    print("saved:",count+1)
    count = count + 1
print(len(names))
names_of_pdf = []
for pdf_page in range(ceil(len(names)/10)):
    print(pdf_page)
    if True:    
        size_of_A4 = (2480,3508)
        a4im = Image.new('RGB',
                         size_of_A4,     # A4 at 72dpi
                         (255, 255, 255))  # White
        size = list(img.getbbox())
        count = 0
        print(len(images))
        for i in range(2):
            for j in range(4):
                print(count)
                if not(count + 1 > len(images)) and not(count+1 > 10):
                    a4im.paste(images[count], 
                        [
                        int(size[0] + i * size[2] + (size_of_A4[0]/210)*15), 
                        int(size[1] + j * size[3] + (size_of_A4[1]/297)*15), 
                        int(size[2] + i * size[2] + (size_of_A4[0]/210)*15), 
                        int(size[3] + j * size[3] + (size_of_A4[1]/297)*15) 
                        ])
                    count = count + 1
                else: 
                    print("issue")
        try:
            images = images[10:]
        except Exception as e:
            print(e)
        pdf_name = f"test_{pdf_page}.pdf"
        print("saving:",pdf_name)
        a4im.save(pdf_name, 'PDF', quality=100)
        names_of_pdf.append(pdf_name)
for pdf in names_of_pdf:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()