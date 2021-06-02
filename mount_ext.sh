#!/bin/sh

umount /dev/pmem0
mkfs.ext4 /dev/pmem0
mount -o dax /dev/pmem0 /mnt/pmem_emul

