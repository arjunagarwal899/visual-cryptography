from encrypt import encrypt
from decrypt import decrypt


def main():
	print('Beginning encryption:')
	filename = input('Please enter filename (arjun.jpg): ')
	encrypt(r'input_images/' + filename)

	while input('\nBegin decryption? [y/n]: ') != 'y':
		pass

	decrypt(r'decrypted_images/' + filename)


if __name__ == '__main__':
	main()