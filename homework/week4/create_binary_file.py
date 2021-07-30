import io

#initialize string
strApiKey = "0b5c1be8-9695-4aa9-be95-d52483109ec9"

#convert string to bytes
strBytes = strApiKey.encode()

#open file as a binary file
f = open('api_file.bin', 'wb')

#write byte string to binary file
f.write(strBytes)
f.close()

