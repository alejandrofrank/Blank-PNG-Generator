from PIL import Image, ImageDraw
import os

def create_folders(number:int):
    os.mkdir('test_images')
    for x in range(number):
        os.mkdir(f'test_images/row_{x+1}')
    
def create_picture_placement_in_folder(x:int, y:int, x2:int, y2:int, i:int):
    folders = []
    for item in range(10):
        folders.append((x,y,x2,y2,f'row_{i}'))
        i += 1
        y += 51.2
        y2 += 51.2
    return folders

def create_test_pictures(color_list,x:int, y:int, x2:int, y2:int, folder:str):
    for i, color in enumerate(color_list):
        img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.rectangle(((x, y),(x2, y2)), fill=color)
        img.save(f'test_images/{folder}/{i+1}_{color}.png', 'PNG')
        x += 51.2
        x2 += 51.2

def main():
    color_list = [
        'black',
        'blue',
        'red',
        'green',
        'yellow',
        'orange',
        'gray',
        'white',
        'brown',
        'purple'
    ]
    try:
        create_folders(10)
    except:
        print('Folders already created')
    for item in create_picture_placement_in_folder(x=0,y=0,x2=51.2,y2=51.2,i=1):
        create_test_pictures(color_list, *item)

main()