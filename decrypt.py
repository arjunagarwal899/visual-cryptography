from PIL import Image
import time


def print_progress(percentage = 0):
	percentage = int(percentage * 100)
	print('\r[%-20s] %d%%' % ('=' * (percentage // 5), percentage), end='')


def decrypt(filename):
	print()
	start_time = time.time()

	input_images = []
	try:
		input_images.append(
			Image.open(rf'encrypted_images/share_1.png')
		)
		input_images.append(
			Image.open(rf'encrypted_images/share_2.png')
		)
	except IOError:
		print('Could not open input image')
		exit(1)

	sizex, sizey = input_images[0].size
	output_image = Image.new('1', (sizex, sizey), 0)

	for x in range(sizex):
		for y in range(sizey):
			i = input_images[0].getpixel((x, y)) or input_images[1].getpixel((x, y))

			output_image.putpixel((x, y), (1 - i) * 255)

		print_progress((x + 1) / sizex)

	output_image.save(filename)

	print(f'\nTime taken: {round(time.time() - start_time, 2)}s')

	output_image.show()


if __name__ == '__main__':
	decrypt(r'decrypted_images/arjun.png')
