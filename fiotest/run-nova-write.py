#!/usr/bin/python

import re
import sys
import os
import time

def main():
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-1")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-2")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-4")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-6")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-8")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-10")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-12")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-16")
	os.system("bash /root/yang/mount_nova.sh")
	os.system("fio fio-rwrite-20")
	print "done."
	return

main()
