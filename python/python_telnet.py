#!/usr/bin/python3
# -*- coding: utf-8 -*-

from telnetlib import Telnet
import sys
import os
import getopt
'''
import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-u', type=str, default=None)
parser.add_argument('-t', type=bool, default=False)
args = parser.parse_args()
print(args.u)
print(args.t)
'''
HOST = '120.79.175.209'
TEST_HOST = '47.107.191.43'
PORT = 3019
CMD = 'if [ -f \"/bak/debugTool\" ];then\n \
            /bak/debugTool outputOpen\n \
        elif [ -f \"/bak/bin/debugTool\" ];then\n \
            /bak/bin/debugTool outputOpen\n \
        elif [ -f \"/home/debugTool\" ];then\n \
            /home/debugTool outputOpen\n  \
        elif [ -f \"/home/bin/debugTool\" ];then\n \
            /home/bin/debugTool outputOpen\n\
        fi\n'
cmd = 'ls /tmp;cat /tmp/TG-INFO\n \
if [ -d /mnt/mmc0/0 ];then\n \
    cd /mnt/mmc0/0;ls\n \
    for file in /mnt/mmc0/0/ipc.log*;do\n \
        echo $file\n \
        tm=`stat -c %Y /mnt/mmc0/0/ipc.log.cont.3 | date \'+%Y-%m-%d %H:%M:%S\'`\n \
        echo $tm\n \
        lin=`awk \'END{print NR}\' $file`\n \
        awk \'NR==\'$((lin-20))\',NR==\'$lin\'{print}\' $file\n \
        sleep 1\n \
    done\n\
fi\n'
def debugTelnet(uuid, istest=False):

    tn = Telnet()
    for i in range(2):
        try:
            if(istest):
                tn.open(TEST_HOST, PORT, timeout=60)
            else :
                tn.open(HOST, PORT, timeout=60)
            break
        except socket.timeout:
            if(i<1):
                continue
            else:
                return -1
    print("CONNECT",uuid)
    tn.write(b"CONNECT "+uuid.encode('utf-8'))
    for i in range(3):
        try:
            print('wait read server msg')
            ret = tn.expect([b"login:",b'ERROR', b'404'], 60)
            print(ret)
            if(ret[0] == 0):
                tn.write(b'root\n')
                tn.read_until(b"Password:", 60)
                tn.write(b'cxlinux\n')
                break
            elif(ret[0] == 1 or ret[0] == 2 or i == 2):
                tn.close()
                return -1
            else :
                continue
        except EOFError:
            tn.close()
            return -1
    #tn.write(cmd.encode('utf-8'))
    
    tn.write(CMD.encode('utf-8'))
    if not os.path.exists("./log/"):
        os.makedirs(b"./log/")
    size = 0
    cnt = 0
    n = 0
    with open('./log/'+uuid+'.log', 'a', encoding='utf-8') as f: 
        while True:
            try:
                outstr = tn.read_until(b"\n", 60)
                n = f.write(outstr.decode("utf-8"))
                print(outstr.decode('utf-8'))
                if n == 0:
                    cnt+=1
                else:
                    cnt = 0
                if cnt > 3:
                    break
                size += n
                if(size >= 4*1024):
                    f.flush()
                    size = 0
            except EOFError:
                print("EOFError exit")
                break
    tn.close()
    return 0


if __name__=='__main__':
    uuid=''
    istest=False
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hu:t", ["help", "uuid=", "test"])
        print(opts)
    except getopt.GetOptError:
        print(sys.argv[0],"-u uuid [-t]")
        sys.exit(2)
    for opt, arg in opts:
        print(opt, arg)
        if opt == '-h':
            print(sys.argv[0],"-u uuid [-t]")
            sys.exit(1)
        elif opt == '-u':
            print(arg)
            uuid = arg
        elif opt == '-t':
            istest=True

    if uuid == '':
        print(sys.argv[0],"-u uuid [-t]")
        sys.exit(1)
    print(uuid,istest)
    sys.exit(debugTelnet(uuid, istest))


