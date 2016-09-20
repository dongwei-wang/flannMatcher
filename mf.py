# Author: Dongwei Wang
# wdw828@gmail.com

# python file process
# this program parse the original xml file to get the right url for all original and sub images

import os
import sys

# get current directory
cur_dir = os.getcwd()
source = str(sys.argv[1])
strprefix = str(sys.argv[2])
trace = open(source,'r')

dest_tar = str(cur_dir + '/targets/tar_list')
dest_src = str(cur_dir + '/source/src_list')

# write the url to different files
ot_tar = open(dest_tar,'w')
ot_src = open(dest_src,'w')

# the following variables are some keywords which we can employ to get the right url links
strcont = '<Contents>'
strkey = '<Key>'
strkey_slash = '</Key>'

#
strsrc = 'source'
strtar = 'targets'

strsrc_arr = []
strtar_arr = []

for line in trace:
    # find the line of statistics
    if line.find(strcont) != -1:
        strvar = line.split(strcont)
        for i in range(0, len(strvar)):
            strvar2 = strvar[i].split(strkey)
            for j in range(0, len(strvar2)):
                strvar3 = strvar2[j].split(strkey_slash)
                for k in range(0,len(strvar3)):
                    if strvar3[k].find(strsrc) != -1:
                        strvar4 = strvar3[k].split('/')
                        if strvar4[1] != '':
                            strsrc_arr.append(strvar3[k])
                    if strvar3[k].find(strtar) != -1:
                        strvar5 = strvar3[k].split('/')
                        if strvar5[1] != '':
                             strtar_arr.append(strvar3[k])

for i in range(0, len(strsrc_arr)):
    strsrc_arr[i] = strprefix + '/'+strsrc_arr[i]
    ot_src.write(strsrc_arr[i]+'\n')

for i in range(0, len(strtar_arr)):
    strtar_arr[i] = strprefix + '/'+strtar_arr[i]
    ot_tar.write(strtar_arr[i]+'\n')

trace.close()
ot_src.close()
ot_tar.close()
