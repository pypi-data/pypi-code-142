'''Implements EBJ2 encoding and decoding.
'''


import io
import struct


INT8 = 0x00
INT16 = 0x01
INT32 = 0x02
INT64 = 0x03
FLOAT32 = 0x04
FLOAT64 = 0x05
STR8 = 0x06
STR32 = 0x07
REF8 = 0x08
REF32 = 0x09
TRUE = 0x0A
FALSE = 0x0B
NULL = 0x0C
ARRAY = 0x0D
END = 0x0E
OBJECT = 0x0F


TYP2FMT = [
  # INT
  '<b', '<h', '<i', '<q',
  # FLOAT
  '<f', '<d',
  # STR
  '<B', '<I',
  # REF
  '<B', '<I'
]


def _encode(val, ebuf, sbuf, /):
  # INT
  if isinstance(val, int) and not isinstance(val, bool):
    if val < 0:
      ran = -val - 1
    else:
      if val <= 0xEF:
        ebuf.write(struct.pack('<B', val + 0x10))
        return
      ran = val
    if ran <= 0x7FFF:
      if ran <= 0x7F:
        typ = INT8
      else:
        typ = INT16
    else:
      if ran <= 0x7FFFFFFF:
        typ = INT32
      else:
        typ = INT64
    ebuf.write(struct.pack('<B', typ))
    ebuf.write(struct.pack(TYP2FMT[typ], val))
  # FLOAT
  elif isinstance(val, float):
    # XXX: FLOAT32
    typ = FLOAT64
    ebuf.write(struct.pack('<B', typ))
    ebuf.write(struct.pack(TYP2FMT[typ], val))
  # STR
  elif isinstance(val, str):
    # REF
    try:
      idx = sbuf[val]
      if idx <= 0xFF:
        typ = REF8
      else:
        typ = REF32
      ebuf.write(struct.pack('<B', typ))
      ebuf.write(struct.pack(TYP2FMT[typ], idx))
      return
    except KeyError:
      pass
    byts = val.encode('utf-8')
    len_ = len(byts)
    if len_ <= 0xFF:
      typ = STR8
    else:
      typ = STR32
    ebuf.write(struct.pack('<B', typ))
    ebuf.write(struct.pack(TYP2FMT[typ], len_))
    ebuf.write(byts)
    sbuf[val] = len(sbuf)
  # TRUE, FALSE and NULL
  elif val == True:
    ebuf.write(struct.pack('<B', TRUE))
  elif val == False:
    ebuf.write(struct.pack('<B', FALSE))
  elif val == None:
    ebuf.write(struct.pack('<B', NULL))
  # ARRAY
  elif isinstance(val, (list, tuple)):
    ebuf.write(struct.pack('<B', ARRAY))
    for val_ in val:
      _encode(val_, ebuf, sbuf)
    ebuf.write(struct.pack('<B', END))
  # OBJECT
  elif isinstance(val, dict):
    ebuf.write(struct.pack('<B', OBJECT))
    for key in val:
      _encode(key, ebuf, sbuf)
      _encode(val[key], ebuf, sbuf)
    ebuf.write(struct.pack('<B', END))
  else:
    raise NotImplementedError


def encode(val):
  ebuf = io.BytesIO()
  _encode(val, ebuf, {})
  ebuf.seek(0)
  return ebuf.read()


def encode_fp(val, fp):
  return _encode(val, fp, {})


TYP2LEN = [
  # INT
  1, 2, 4, 8,
  # FLOAT
  4, 8,
  # STR
  1, 4,
  # REF
  1, 4
]


TYP2VAL = [
  # INT
  None, None, None, None,
  # FLOAT
  None, None,
  # STR
  None, None,
  # REF
  None, None,
  # TRUE, FALSE and NULL
  True, False, None
]


class StopDecoding(Exception):
  pass


def _decode(ebuf, sbuf, /):
  typ = struct.unpack('<B', ebuf.read(1))[0]
  # INT
  if typ <= 0x05:
    val = struct.unpack(TYP2FMT[typ], ebuf.read(TYP2LEN[typ]))[0]
  # STR
  elif typ <= 0x07:
    len_ = struct.unpack(TYP2FMT[typ], ebuf.read(TYP2LEN[typ]))[0]
    val = ebuf.read(len_).decode('utf-8')
    sbuf.append(val)
  # REF
  elif typ <= 0x09:
    idx = struct.unpack(TYP2FMT[typ], ebuf.read(TYP2LEN[typ]))[0]
    val = sbuf[idx]
  # TRUE, FALSE and NULL
  elif typ <= 0x0C:
    val = TYP2VAL[typ]
  # ARRAY
  elif typ == ARRAY:
    val = []
    while True:
      try:
        val.append(_decode(ebuf, sbuf))
      except StopDecoding:
        break
  # END
  elif typ == END:
    raise StopDecoding
  # OBJECT
  elif typ == OBJECT:
    val = {}
    while True:
      try:
        key = _decode(ebuf, sbuf)
        val[key] = _decode(ebuf, sbuf)
      except StopDecoding:
        break
  else:
    return typ - 0x10
  return val


def decode(byts):
  return _decode(io.BytesIO(byts), [])


def decode_fp(fp):
  return _decode(fp, [])
