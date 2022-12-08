import os
import shutil
import tempfile

import pynibs
import unittest
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def check_xml(xml_fn):
    """Check well-formedness of xml"""
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(xml_fn)


class TestWriteXdmf(unittest.TestCase):
    """This tests pynibs.write_xdmf()"""

    data_fn = os.path.join(pynibs.__testdatadir__, "data.hdf5")
    geo_fn = os.path.join(pynibs.__testdatadir__, "geo.hdf5")
    xml_scheme_fn = os.path.join(pynibs.__testdatadir__, "vtk-unstructured.xsd")
    xdmf_geo_fn = os.path.join(pynibs.__testdatadir__, "geo.xdmf")
    xdmf_data_fn = os.path.join(pynibs.__testdatadir__, "data.xdmf")

    for fn in [xdmf_geo_fn, xdmf_data_fn]:
        try:
            os.remove(fn)
        except OSError:
            pass

    def test_1_write_geo_only(self):
        with tempfile.TemporaryDirectory() as tempdir:
            geo_fn = shutil.copy(self.geo_fn, tempdir)
            fn_xml = pynibs.write_xdmf(geo_fn)
            check_xml(fn_xml)

    def test_2_write_xdmf_exists(self):
        with tempfile.TemporaryDirectory() as tempdir:
            geo_fn = shutil.copy(self.geo_fn, tempdir)
            pynibs.write_xdmf(geo_fn)
            self.assertRaises(FileExistsError, pynibs.write_xdmf, geo_fn)

    def test_3_write_xdmf_overwrite(self):
        with tempfile.TemporaryDirectory() as tempdir:
            geo_fn = shutil.copy(self.geo_fn, tempdir)
            pynibs.write_xdmf(geo_fn)
            pynibs.write_xdmf(geo_fn, overwrite_xdmf=True)

    def test_4_write_datageo(self):
        with tempfile.TemporaryDirectory() as tempdir:
            geo_fn = shutil.copy(self.geo_fn, tempdir)
            data_fn = shutil.copy(self.data_fn, tempdir)
            pynibs.write_xdmf(geo_fn)
            xdmf_data_fn = pynibs.write_xdmf(data_fn, geo_fn, overwrite_xdmf=True)
            check_xml(xdmf_data_fn)


if __name__ == '__main__':
    unittest.main()
