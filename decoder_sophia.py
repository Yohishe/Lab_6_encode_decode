# Sophia John
# Decoder


def decode(pw_enc):
    decode_dictionary = {'3':'0', '4':'1', '5':'2', '6':'3', '7':'4', '8':'5', '9':'6', '0':'7', '1':'8', '2':'9' }
    decodedlist=[]
    tempnum=[]
    for i in range(0,8):
        tempnum=pw_enc[i]
        decodedlist.append(decode_dictionary[tempnum])
    return ''.join(decodedlist)
