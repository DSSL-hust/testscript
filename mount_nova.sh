#!/bin/sh

umount /dev/pmem0
#insmod ./nova/nova.ko
mount -t NOVA -o init /dev/pmem0 /mnt/pmem_emul
