import codecs
from binascii import *
from crcmod import *


def crc16Add(read):
    crc16 = crcmod.mkCrcFun(
        0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    data = read.replace(" ", "")
    readcount = hex(crc16(unhexlify(data))).upper()
    str_list = list(readcount)
    crc_data = "".join(str_list)
    read = read.strip() + ' ' + crc_data[4:] + ' ' + crc_data[2:4]
    return crc_data[4:] + crc_data[2:4]



def is_crc_valid(modbus_data):
    a = modbus_data[:len(modbus_data) - 4]
    print(modbus_data)
    print(a)
    crc = crcmod.predefined.mkPredefinedCrcFun("modbus")



f=open("crc.txt","r")
f_str=f.read().replace("\n","")
f_list=list(f_str)
j=0
lst=[]
for i in range(len(f_str)+1):
 if(f_str[i:i+4]=="0104") | (f_str[i:i+4]=="0103")| (f_str[i:i+4]=="0183"):
  if(crc16Add(f_str[j:i-4])==f_str[i-4:i]):
    lst.append(f_str[j:i])
  j=i
lst.append(f_str[j:i])
for i in lst:
  if len(i)==16 and(i[2:4]=='04' or i[2:4]=='03'):
    print('\033[31m',i,":","slave","->" ,"master")
  else:
   if len(i)==10 and(i[2:4]=='84' or i[2:4]=='83'):
    print('\033[32m',i,":","master"+"->" ,"slave")
   if len(i)>10 and (10+int(i[4:6],16)*2):
    print('\033[32m',i,":","master"+"->" ,"slave")
