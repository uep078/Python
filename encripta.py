import sys
import base64
import hashlib
print base64.b64encode(hashlib.sha1(sys.argv[1]).digest())
