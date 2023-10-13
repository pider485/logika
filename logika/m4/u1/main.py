from PIL import Image, ImageFilter

with Image.open('da.jpg') as original: 
    print(original.size)
    print(original.format)
    print(original.mode)

    #bw_original = original.convert('L')
#
    #bw_original.show()
#
    #blur_original = original.filter(ImageFilter.BLUR)
#
    #left_original = original.transpose(Image.ROTATE_180)
#
    #left_original.show()

    for i in range(100):
        original.save(f'da{i}.jpg')