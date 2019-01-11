import os,sys
import Tkinter
import tkMessageBox

x=raw_input("Enter file name that you want to compress\n")

while (not os.path.isfile(x)):
    x=raw_input("Please enter a file name that exists\n")
file = open(x, 'r')
print

class Huffman:
  def __init__(self,freq_of_char):
    self.freq_of_char=freq_of_char

  def sort(self,l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i][1]>l[j][1]:
                t=l[i]
                l[i]=l[j]
                l[j]=t
    return l

  def encode(self,message):
    s=''            #stores the encoded text in the form of 1s and 0s
    for i in message:
        if i!='\n':
            arr=self.makeCodeMap(finalTree)
            s+=(arr[i])
    return s

  def compressed_path(self):
    print "Path of compressed file:",os.path.abspath("Compressed")
    return os.path.abspath("Compressed")

  def padding(self,encoded):
    extra=8-len(encoded)%8      #no. of zeros that need to be added
    for i in range(extra):
        encoded+="0"
    encoded="{0:08b}".format(extra)+encoded  #binary representation of padding occupying 8 bits
    return encoded

  def createEncoding(self,encoded):
    b = bytearray()
    for i in range(0, len(encoded), 8):
        eightBitChunk = encoded[i:i+8]    #binary representation of the given 8 bits
        ascii=int(eightBitChunk,2)     #gives decimal value of the given binary no
        b.append(ascii)  #appends character equivalent to given ascii value

    return b

  def writeFile(self,text):
    f=open("Decompressed","w+")
    for i in text:
        f.write(i)
    f.close()

  def decompressed_path(self):
    return os.path.abspath("Decompressed")

  def decode_text(self,encoded_text):
    current_code = ""
    decoded_text = ""
    code_list=[]    #list containing all the codes
    char_list=[]    #list containing all the characters
    arr1=self.makeCodeMap(self.makeTree(freq_of_char))
    for i in arr1:
        code_list.append(arr1[i])
        char_list.append(i)
    for bit in encoded_text:
        current_code += bit
        if(current_code in code_list):
            character = char_list[code_list.index(current_code)]
            decoded_text += character
            current_code = ""
    self.writeFile(decoded_text)
    return decoded_text

  def remove_padding(self,padded_encoded_text):
    padded_info = padded_encoded_text[:8]
    decimal=i=0
    binary=int(padded_info)
    while(binary != 0):
        d = binary% 10
        decimal = decimal + d * pow(2, i)
        binary/=10
        i += 1
    extra=decimal
    padded_encoded_text = padded_encoded_text[8:]
    encoded_text = padded_encoded_text[:-1*extra]
    k=self.decode_text(encoded_text)

  def createFile(self,freq_of_char,codeMap):
    file = open(x, 'r')
    message=''
    for i in file:
        message+=i
    encoded=self.encode(message)
    pad=self.padding(encoded)
    self.remove_padding(pad)
    k=self.createEncoding(pad)
    cmpr=open("Compressed","w+")
    cmpr.write(k)
    self.writeFile(message)

  def generateCode(self,finalTree,codeMap,binaryCode):
    if(len(finalTree)==2 and type(finalTree[1]) == type("")):
        codeMap[finalTree[1]]=binaryCode
    else:
        value=finalTree[0]
        lnode=finalTree[1][0]
        rnode=finalTree[1][1]
        self.generateCode(lnode,codeMap,binaryCode+"0")
        self.generateCode(rnode,codeMap,binaryCode+"1")

  def makeCodeMap(self,finalTree):
    codeMap=dict()
    self.generateCode(finalTree,codeMap,'')
    return codeMap

  def makeTree(self,freq_of_char) :
    while len(freq_of_char) > 1 :
        smallest = (freq_of_char[0],freq_of_char[1])       # get the 2 characters of lowest frequencies
        nodes  = freq_of_char[2:]                          # all the other nodes
        totalNodeVal = smallest[0][0] + smallest[1][0]     # value of the parent node of subtree
        freq_of_char   = nodes + [(totalNodeVal,smallest)]     # adding new parent node  to freq_of_char
        self.sort(freq_of_char)
    return freq_of_char[0]

def size_of_file(path):
  if os.path.isfile(path):
    information=os.stat(path)
    return information.st_size

freq_dict={}
while True:
    c=file.read(1)
    if not c:break
    if c in freq_dict.keys():
        freq_dict[c]+=1
    else:freq_dict.update({c:1})


freq_of_char=[]  #list of tuples containing character and frequency
for i in freq_dict:
    freq_of_char.append((freq_dict[i],i))

ob=Huffman(freq_of_char)

finalTree=ob.makeTree(freq_of_char)
codeMap={}
ob.createFile(freq_of_char,codeMap)
f1=ob.compressed_path()
f2=ob.decompressed_path()
print "Path of decompressed file:",f2

print"Size of compressed file:",size_of_file(f1),"bytes"
print"Size of decompressed file:",size_of_file(f2),"bytes"
tkMessageBox.showinfo("Size of compressed file (in bytes):",size_of_file(f1))
tkMessageBox.showinfo("Size of decompressed file (in bytes):",size_of_file(f2))
