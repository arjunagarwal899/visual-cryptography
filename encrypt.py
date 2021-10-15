from PIL import Image
import random
import time


def print_progress(percentage = 0):
	percentage = int(percentage * 100)
	print('\r[%-20s] %d%%' % ('=' * (percentage // 5), percentage), end='')


def encrypt(filename):
	print()
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

	output_images.append(Image.new('1', (sizex * 2, sizey * 2), 0))
	output_images.append(Image.new('1', (sizex * 2, sizey * 2), 0))

	for x in range(sizex):
		for y in range(sizey):

			pixel = input_image.getpixel((x, y))

			share1_dist = [1, 1, 0, 0]
			random.shuffle(share1_dist)
			share2_dist = []

			if pixel == 0:      # Black pixel
				share2_dist = []
				for i in share1_dist:
					share2_dist.append(1 - i)
			elif pixel == 255:  # White pixel
				share2_dist = share1_dist
			else:
				print(pixel)
				exit(3)

			output_images[0].putpixel((x * 2, y * 2), share1_dist[0] * 255)
			output_images[0].putpixel((x * 2 + 1, y * 2), share1_dist[1] * 255)
			output_images[0].putpixel((x * 2, y * 2 + 1), share1_dist[2] * 255)
			output_images[0].putpixel((x * 2 + 1, y * 2 + 1), share1_dist[3] * 255)

			output_images[1].putpixel((x * 2, y * 2), share2_dist[0] * 255)
			output_images[1].putpixel((x * 2 + 1, y * 2), share2_dist[1] * 255)
			output_images[1].putpixel((x * 2, y * 2 + 1), share2_dist[2] * 255)
			output_images[1].putpixel((x * 2 + 1, y * 2 + 1), share2_dist[3] * 255)

		print_progress((x + 1) / sizex)

	output_images[0].save(output_images_path + f'share_1.png')
	output_images[1].save(output_images_path + f'share_2.png')

	print(f'\nTime taken: {round(time.time() - start_time, 2)}s')

	output_images[0].show()
	output_images[1].show()



if __name__ == '__main__':
	encrypt(r'input_images/arjun.jpg')