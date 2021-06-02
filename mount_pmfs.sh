#!/bin/sh

umount /dev/pmem0
#mkfs.ext4 /dev/pmem1
#insmod ./pmfs/pmfs.ko
#insmod ./pmfs/pmfs.ko
mount -t pmfs -o init /dev/pmem0 /mnt/pmem_emul
dd if=/dev/zero of=/mnt/pmem_emul/.log bs=1M count=8
