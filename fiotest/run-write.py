#!/usr/bin/python

import re
import sys
import os
import time

def main():
	os.system("fio fio-write-1")
	os.system("fio fio-write-2")
	os.system("fio fio-write-4")
	os.system("fio fio-write-6")
	os.system("fio fio-write-8")
	os.system("fio fio-write-10")
	os.system("fio fio-write-12")
	os.system("fio fio-write-16")
	os.system("fio fio-write-20")
	print "done."
	return

main()
