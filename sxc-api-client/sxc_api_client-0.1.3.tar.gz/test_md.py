from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/dsbowen/docstr-md/blob/master')
soup = PySoup(path='test.py', parser='sklearn', src_href=src_href)
compile_md(soup, compiler='sklearn', outfile='test.md')
