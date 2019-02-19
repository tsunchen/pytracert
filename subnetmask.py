

#! /usr/bin/env python
#coding=utf-8
# get subnet ip withmask()


def subnetmask(mask, ip):
    ip_1 = inetprotocol_first(ip)
    ip_2 = inetprotocol_second(ip)
    ip_3 = inetprotocol_third(ip)
    ip_4 = inetprotocol_forth(ip)

    if mask >= 1 and mask <=8:
        print ("TYPE-A")
        print (getmaskbit(mask))
        print (ip_1)
    elif mask <= 16:
        print ("TYPE-255.B")
        print (getmaskbit(mask - 8))
        print (ip_1)
        print (ip_2)
    elif mask <= 24:
        print ("TYPE-255.255.C")
        print (getmaskbit(mask - 16))
        print (ip_1)
        print (ip_2)
        print (ip_3)
    else:
        print ("TYPE-255.255.255.D")
        print (getmaskbit(mask - 24))
        print(ip_1)
        print(ip_2)
        print(ip_3)
        print(ip_4)


def getmaskbit(maskbit):
    if maskbit == 1:
        x = 0b10000000
    elif maskbit == 2:
        x = 0b11000000
    elif maskbit == 3:
        x = 0b11100000
    elif maskbit == 4:
        x = 0b11110000
    elif maskbit == 5:
        x = 0b11111000
    elif maskbit == 6:
        x = 0b11111100
    elif maskbit == 7:
        x = 0b11111110
    elif maskbit == 8:
        x = 0b11111111
    return (x)


def getbitmask(bitmask):
    if bitmask == 1:
        x = 0b00000001
    elif bitmask == 2:
        x = 0b00000011
    elif bitmask == 3:
        x = 0b00000111
    elif bitmask == 4:
        x = 0b00001111
    elif bitmask == 5:
        x = 0b00011111
    elif bitmask == 6:
        x = 0b00111111
    elif bitmask == 7:
        x = 0b01111111
    elif bitmask == 8:
        x = 0b00000000
    return (x)


def broadcastbit(mbit,masky):
    a = masky
    a2 = bin(~(a) & 255)
    a3 = bin(int(a2, base=2))
    a4 = mbit
    a5 = (int(a3, base=2) | int(a4, base=2))
    return (a5)


def subnetmask_and(mask, ip):
    ip_1 = inetprotocol_first(ip)
    b_ip_1 = bin(int(ip_1))
    ip_2 = inetprotocol_second(ip)
    b_ip_2 = bin(int(ip_2))
    ip_3 = inetprotocol_third(ip)
    b_ip_3 = bin(int(ip_3))
    ip_4 = inetprotocol_forth(ip)
    b_ip_4 = bin(int(ip_4))

    if mask >= 1 and mask <=8:
        print ("TYPE-A")
        print (getmaskbit(mask))
        y = getmaskbit(mask)
        print (ip_1)
        ch1 = b_ip_1
        ch2 = bin(y)
        print (int(ch2 , base = 2))
        print (bin(int(ch1, base=2) & int(ch2, base=2)))
        print ("to be complete")
    elif mask <= 16:
        print ("TYPE-255.B")
        print (getmaskbit(mask - 8))
        y = getmaskbit(mask - 8)
        #print (ip_1)
        #print (ip_2)
        #print (b_ip_2)
        ch1 = b_ip_2
        ch2 = bin(y)
        #print (bin( int(ch1, base = 2) & int (ch2, base = 2) ))
        subinet = (int(ch1, base=2) & int(ch2, base=2))
        #print(bin(subinet))
        #print(subinet)  # print (getbitmask(8 - (mask - 8)))
        sADR = subinet
        #print(broadcastbit(ch1, y))
        bcADR = broadcastbit(ch1, y)
        print ("subADR: " + ip_1 + '.' + str(sADR) + '.'+  '0' + '.' + '0')
        print ("bcastADR: " + ip_1 + '.' + str(bcADR) + '.'+ '255' + '.' + '255')
    elif mask <= 24:
        print ("TYPE-255.255.C")
        print (getmaskbit(mask - 16))
        y = getmaskbit(mask - 16)
        #print (ip_1)
        #print (ip_2)
        #print (ip_3)
        #print (b_ip_3)
        ch1 = b_ip_3
        ch2 = bin(y)
        #print (bin( int(ch1, base = 2) & int (ch2, base = 2) ))
        subinet = (int(ch1, base=2) & int(ch2, base=2))
        #print(bin(subinet))
        #print(subinet)  # print (getbitmask(8 - (mask - 16)))
        sADR = subinet
        bcADR = broadcastbit(ch1, y)
        print("subADR: " + ip_1 + '.' + ip_2 + '.'+ str(sADR) + '.' + '0')
        print("bcastADR: " + ip_1 + '.' + ip_2 + '.' + str(bcADR) + '.' + '255')
    else:
        print ("TYPE-255.255.255.D")
        print (getmaskbit(mask - 24))
        y = getmaskbit(mask - 24)
        #print(ip_1)
        #print(ip_2)
        #print(ip_3)
        #print(ip_4)
        #print(b_ip_4)
        ch1 = b_ip_4
        ch2 = bin(y)
        subinet = ( int(ch1, base = 2) & int (ch2, base = 2) )
        #print (bin(subinet))
        #print (subinet) #print (getbitmask(8 - (mask - 24)))
        #print (broadcastbit(ch1, y))
        sADR = subinet
        bcADR = broadcastbit(ch1, y)
        print("subADR: " + ip_1 + '.' + ip_2 + '.' + ip_3 + '.' + str(sADR))
        print("bcastADR: " + ip_1 + '.' + ip_2 + '.' + ip_3 + '.' + str(bcADR) )




def inetprotocol_forth(ip):
    ip_1, ip_2, ip_3, ip_forth = ip.split('.')
    return ip_forth

def inetprotocol_third(ip):
    ip_1, ip_2, ip_third, ip_4 = ip.split('.')
    return ip_third

def inetprotocol_second(ip):
    ip_1, ip_second, ip_3, ip_4 = ip.split('.')
    return ip_second

def inetprotocol_first(ip):
    ip_first, ip_2, ip_3, ip_4 = ip.split('.')
    return ip_first
    #print(bin(ip_1))




if __name__=='__main__':
    ip = '159.64.56.56'
    #inetprotocol(ip)

    #for i in range(1,33):
    #    subnetmask_and(i, ip)
    #getmaskbit(10)
    #ungetmaskbit(10)
    subnetmask_and(30, ip)
    #subnetmask(30, ip)
    subnetmask_and(22, ip)
    subnetmask_and(10, ip)

