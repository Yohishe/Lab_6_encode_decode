print('Dawson Craft')


def encode(pw_enc):
	encode_dictionary= {'0':3, '1':4, '2':5, '3':6, '4':7, '5':8, '6':9, '7':0, '8':1, '9':2 } #dict that changes values to encode them
	encodedlist=[]
	tempnum=[]
	for i in range(0,8):
		tempnum=pw_enc[i]
		encodedlist.append(encode_dictionary[tempnum])
	return encodedlist
def main():
	project=True
	while project==True:
		print('')
		print('Menu')
		print('-------------')
		print('1. Encode')
		print('2. Decode')
		print('3. Quit')
		choice=int(input('Please enter an option: '))
		if choice==1: #encoder
			pw=(str(input('Please enter your password to encode: ')))
			encode(pw)
			print(encodedlist)
			print('Your password has been encoded and stored!')
		elif choice==2: #decoder
			#insert decoder
			pass 
		elif choice==3: #quit
			break
