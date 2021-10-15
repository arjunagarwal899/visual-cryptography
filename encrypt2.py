from PIL import Image
import random
import time


def print_progress(percentage=0):
    percentage = int(percentage * 100)
    print('\r[%-20s] %d%%' % ('=' * (percentage // 5), percentage), end='')


def encrypt(filename):

    print()
    n = int(input("N: "))

    start_time = time.time()

    output_images_path = r'encrypted_images/'

    input_image = None
    output_images = []

    try:
        input_image = Image.open(filename)
    except IOError:
        print('Input image does not exist')
        exit(1)

    input_image = input_image.convert('1')
    if input_image.mode != '1':
        print('Image could not be interpreted as a black and white image')
        exit(2)

    sizex, sizey = input_image.size

    for i in range(n):
        output_images.append(Image.new('1', (sizex, sizey), 0))

    for x in range(sizex):
        for y in range(sizey):

            pixel = input_image.getpixel((x, y))

            if pixel == 0:
                p = 1
                p = random.randint(0, n)
                if p % 2 == 0: p = (p + 1) % (n + 1)
            else:
                p = random.randint(0, n)
                if p % 2 == 1: p = (p + 1) % (n + 1)

            share_dist = [1] * p + [0] * (n - p)
            random.shuffle(share_dist)

            for i in range(n):
                output_images[i].putpixel((x, y), (1 - share_dist[i]) * 255)

        print_progress((x + 1) / sizex)

    for i in range(n):
        output_images[i].save(output_images_path + f'share_{i + 1}.png')

    print(f'\nTime taken: {round(time.time() - start_time, 2)}s')

if __name__ == '__main__':
    encrypt(r'input_images/arjun.jpg')
