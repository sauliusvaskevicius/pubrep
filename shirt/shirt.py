from sys import argv
import sys
from PIL import Image , ImageOps


def main():

    n=len(argv)

    if n<3:
        sys.exit('Too few command-line arguments')
    elif n>3:
        sys.exit('Too many command-line arguments')
    else:
        if argv[1][-4:].lower() in ['.jpg','jpeg','.png'] or argv[2][-4:].lower() in ['.jpg','jpeg','.png']:
            try:
                shirt=Image.open('shirt.png')
                background=Image.open(argv[1]).convert('RGBA')
            except FileNotFoundError:
                sys.exit('File not found')
            else:
                if argv[1][-4:]==argv[2][-4:]:

                    width,height = shirt.size
                    resized_bg = ImageOps.fit(background, (width, height))
                    resized_bg.paste(shirt,(0,0),shirt)
                    resized_bg = resized_bg.convert("RGB")
                    resized_bg.save(argv[2])
                else:
                    sys.exit('Input and output have different extensions')

        else:
            sys.exit('Invalid output')

if __name__=="__main__":
    main()
