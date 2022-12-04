import CyberBook

dr = CyberBook.DecoderRing(data='test')

print(
    dr.encrypt_md5(),
    CyberBook.Identify.os_specs(),
    sep='\n'
)
