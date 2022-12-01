#!/usr/bin/env python3

import sys
from typing import Dict, List, Set, Tuple  # noqa F401
import libvirt
import unittest
import os


def get_libvirt_api_xml_path():
    import subprocess
    args = ["pkg-config", "--variable", "libvirt_api", "libvirt"]
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, _ = proc.communicate()
    if proc.returncode:
        sys.exit(proc.returncode)
    return stdout.splitlines()[0]

# Identify all functions and enums in public API
def identify_functions_enums(tree):
    enumvals = {}  # type: Dict[str, Dict[str, int]]
    second_pass = []  # type: List[str]
    wantenums = []  # type: List[str]
    wantfunctions = []  # type: List[str]

    wantfunctions = tree.xpath('/api/files/file/exports[@type="function"]/@symbol')

    for n in tree.xpath('/api/symbols/enum'):
        typ = n.attrib['type']
        name = n.attrib['name']
        val = n.attrib['value']

        if typ not in enumvals:
            enumvals[typ] = {}

        # If the value cannot be converted to int, it is reference to
        # another enum and needs to be sorted out later on
        try:
            val = int(val)
        except ValueError:
            second_pass.append(n)
            continue

        enumvals[typ][name] = int(val)

    for n in second_pass:
        typ = n.attrib['type']
        name = n.attrib['name']
        val = n.attrib['value']

        for v in enumvals.values():
            if val in v:
                val = int(v[val])
                break

        # Version 4.0.0 was broken as missing VIR_TYPED_PARAM enums
        # constants. This is harmless from POV of validating API
        # coverage so ignore this error.
        if (not isinstance(val, int) and
            not val.startswith("VIR_TYPED_PARAM_")):
            fail = True
            print("Cannot get a value of enum %s (originally %s)" % (val, name))
        enumvals[typ][name] = val

    for n in tree.xpath('/api/files/file/exports[@type="enum"]/@symbol'):
        for enumval in enumvals.values():
            if n in enumval:
                enumv = enumval
                break
        # Eliminate sentinels
        if n.endswith('_LAST') and enumv[n] == max(enumv.values()):
            continue
        wantenums.append(n)

    return wantfunctions, wantenums, enumvals


# Identify all classes and methods in the 'libvirt' python module
def identify_class_methods(wantenums, enumvals):
    gotenums = []  # type: List[str]
    gottypes = []  # type: List[str]
    gotfunctions = {"libvirt": []}  # type: Dict[str, List[str]]

    for name in dir(libvirt):
        if name.startswith('_'):
            continue
        thing = getattr(libvirt, name)
        # Special-case libvirtError to deal with python 2.4 difference
        # in Exception class type reporting.
        if isinstance(thing, int):
            gotenums.append(name)
        elif getattr(thing, "__module__", "") == "typing":
            continue
        elif type(thing) == type or name == "libvirtError":
            gottypes.append(name)
            gotfunctions[name] = []
        elif callable(thing):
            gotfunctions["libvirt"].append(name)

    for enum in wantenums:
        if enum not in gotenums:
            fail = True
            for typ, enumval in enumvals.items():
                if enum in enumval:
                    raise Exception("Missing exported enum %s of type %s" % (enum, typ))

    for klassname in gottypes:
        klassobj = getattr(libvirt, klassname)
        for name in dir(klassobj):
            if name.startswith('_'):
                continue
            if name == 'c_pointer':
                continue
            thing = getattr(klassobj, name)
            if callable(thing):
                gotfunctions[klassname].append(name)

    return gotfunctions, gottypes


# First cut at mapping of C APIs to python classes + methods
def basic_class_method_mapping(wantfunctions, gottypes):
    basicklassmap = {}  # type: Dict[str, Tuple[str, str, str]]

    for cname in wantfunctions:
        name = cname
        # Some virConnect APIs have stupid names
        if name[0:7] == "virNode" and name[0:13] != "virNodeDevice":
            name = "virConnect" + name[7:]
        if name[0:7] == "virConn" and name[0:10] != "virConnect":
            name = "virConnect" + name[7:]

        # The typed param APIs are only for internal use
        if name[0:14] == "virTypedParams":
            continue

        if name[0:23] == "virNetworkDHCPLeaseFree":
            continue

        if name[0:28] == "virDomainStatsRecordListFree":
            continue

        if name[0:19] == "virDomainFSInfoFree":
            continue

        if name[0:25] == "virDomainIOThreadInfoFree":
            continue

        if name[0:22] == "virDomainInterfaceFree":
            continue

        if name[0:21] == "virDomainListGetStats":
            name = "virConnectDomainListGetStats"

        # These aren't functions, they're callback signatures
        if name in ["virConnectAuthCallbackPtr", "virConnectCloseFunc",
                    "virStreamSinkFunc", "virStreamSourceFunc", "virStreamEventCallback",
                    "virEventHandleCallback", "virEventTimeoutCallback", "virFreeCallback",
                    "virStreamSinkHoleFunc", "virStreamSourceHoleFunc", "virStreamSourceSkipFunc"]:
            continue
        if name[0:21] == "virConnectDomainEvent" and name[-8:] == "Callback":
            continue
        if name[0:22] == "virConnectNetworkEvent" and name[-8:] == "Callback":
            continue
        if (name.startswith("virConnectStoragePoolEvent") and
            name.endswith("Callback")):
            continue
        if (name.startswith("virConnectNodeDeviceEvent") and
            name.endswith("Callback")):
            continue
        if (name.startswith("virConnectSecretEvent") and
            name.endswith("Callback")):
            continue

        # virEvent APIs go into main 'libvirt' namespace not any class
        if name[0:8] == "virEvent":
            if name[-4:] == "Func":
                continue
            basicklassmap[name] = ("libvirt", name, cname)
        else:
            found = False
            # To start with map APIs to classes based on the
            # naming prefix. Mistakes will be fixed in next
            # loop
            for klassname in gottypes:
                klen = len(klassname)
                if name[0:klen] == klassname:
                    found = True
                    if name not in basicklassmap:
                        basicklassmap[name] = (klassname, name[klen:], cname)
                    elif len(basicklassmap[name]) < klen:
                        basicklassmap[name] = (klassname, name[klen:], cname)

            # Anything which can't map to a class goes into the
            # global namespaces
            if not found:
                basicklassmap[name] = ("libvirt", name[3:], cname)

    return basicklassmap


# Deal with oh so many special cases in C -> python mapping
def fixup_class_method_mapping(basicklassmap):
    finalklassmap = {}  # type: Dict[str, Tuple[str, str, str]]

    for name, (klass, func, cname) in sorted(basicklassmap.items()):
        # The object lifecycle APIs are irrelevant since they're
        # used inside the object constructors/destructors.
        if func in ["Ref", "Free", "New", "GetConnect", "GetDomain", "GetNetwork"]:
            if klass == "virStream" and func == "New":
                klass = "virConnect"
                func = "NewStream"
            else:
                continue

        # All the error handling methods need special handling
        if klass == "libvirt":
            if func in ["CopyLastError", "DefaultErrorFunc",
                        "ErrorFunc", "FreeError",
                        "SaveLastError", "ResetError"]:
                continue
            elif func in ["GetLastError", "GetLastErrorMessage",
                          "GetLastErrorCode", "GetLastErrorDomain",
                          "ResetLastError", "Initialize"]:
                func = "vir" + func
            elif func == "SetErrorFunc":
                func = "RegisterErrorHandler"
        elif klass == "virConnect":
            if func in ["CopyLastError", "SetErrorFunc"]:
                continue
            elif func in ["GetLastError", "ResetLastError"]:
                func = "virConn" + func

        # Remove 'Get' prefix from most APIs, except those in virConnect
        # and virDomainSnapshot namespaces which stupidly used a different
        # convention which we now can't fix without breaking API
        if func[0:3] == "Get" and klass not in ["virConnect", "virDomainCheckpoint", "virDomainSnapshot", "libvirt"]:
            if func not in ["GetCPUStats", "GetTime"]:
                func = func[3:]

        # The object creation and lookup APIs all have to get re-mapped
        # into the parent class
        if func in ["CreateXML", "CreateLinux", "CreateXMLWithFiles",
                    "DefineXML", "CreateXMLFrom", "LookupByUUID",
                    "LookupByUUIDString", "LookupByVolume" "LookupByName",
                    "LookupByID", "LookupByName", "LookupByKey", "LookupByPath",
                    "LookupByMACString", "LookupByUsage", "LookupByVolume",
                    "LookupByTargetPath", "LookupSCSIHostByWWN", "LookupByPortDev",
                    "Restore", "RestoreFlags",
                    "SaveImageDefineXML", "SaveImageGetXMLDesc", "DefineXMLFlags",
                    "CreateXMLFlags"]:
            if klass != "virDomain":
                func = klass[3:] + func

            if klass in ["virDomainCheckpoint", "virDomainSnapshot"]:
                klass = "virDomain"
                func = func[6:]
            elif klass == "virStorageVol" and func in ["StorageVolCreateXMLFrom", "StorageVolCreateXML"]:
                klass = "virStoragePool"
                func = func[10:]
            elif klass == "virNetworkPort":
                klass = "virNetwork"
                func = func[7:]
            elif func == "StoragePoolLookupByVolume":
                klass = "virStorageVol"
            elif func == "StorageVolLookupByName":
                klass = "virStoragePool"
            else:
                klass = "virConnect"

        # The open methods get remapped to primary namespace
        if klass == "virConnect" and func in ["Open", "OpenAuth", "OpenReadOnly"]:
            klass = "libvirt"

        # These are inexplicably renamed in the python API
        if func == "ListDomains":
            func = "ListDomainsID"
        elif func == "ListAllNodeDevices":
            func = "ListAllDevices"
        elif func == "ListNodeDevices":
            func = "ListDevices"

        # The virInterfaceChangeXXXX APIs go into virConnect. Stupidly
        # they have lost their 'interface' prefix in names, but we can't
        # fix this name
        if func[0:6] == "Change":
            klass = "virConnect"

        # Need to special case the checkpoint and snapshot APIs
        if klass == "virDomainSnapshot" and func in ["Current", "ListNames", "Num"]:
            klass = "virDomain"
            func = "snapshot" + func

        # Names should start with lowercase letter...
        func = func[0:1].lower() + func[1:]
        if func[0:8] == "nWFilter":
            func = "nwfilter" + func[8:]
        if func[0:8] == "fSFreeze" or func[0:6] == "fSThaw" or func[0:6] == "fSInfo":
            func = "fs" + func[2:]
        if func[0:12] == "iOThreadInfo":
            func = "ioThreadInfo"

        if klass == "virNetwork":
            func = func.replace("dHCP", "DHCP")

        # ...except when they don't. More stupid naming
        # decisions we can't fix
        if func == "iD":
            func = "ID"
        if func == "uUID":
            func = "UUID"
        if func == "uUIDString":
            func = "UUIDString"
        if func == "oSType":
            func = "OSType"
        if func == "xMLDesc":
            func = "XMLDesc"
        if func == "mACString":
            func = "MACString"

        finalklassmap[name] = (klass, func, cname)

    return finalklassmap


# Validate that every C API is mapped to a python API
def validate_c_to_python_api_mappings(finalklassmap, gotfunctions):
    usedfunctions = set()  # type: Set[str]
    for name, (klass, func, cname) in sorted(finalklassmap.items()):
        if func in gotfunctions[klass]:
            usedfunctions.add("%s.%s" % (klass, func))
        else:
            raise Exception("%s -> %s.%s       (C API not mapped to python)" % (name, klass, func))
    return usedfunctions


# Validate that every python API has a corresponding C API
def validate_python_to_c_api_mappings(gotfunctions, usedfunctions):
    for klass in gotfunctions:
        if klass == "libvirtError":
            continue
        for func in sorted(gotfunctions[klass]):
            # These are pure python methods with no C APi
            if func in ["connect", "getConnect", "domain", "getDomain",
                        "virEventInvokeFreeCallback", "network",
                        "sparseRecvAll", "sparseSendAll"]:
                continue

            key = "%s.%s" % (klass, func)
            if key not in usedfunctions:
                raise Exception("%s.%s       (Python API not mapped to C)" % (klass, func))


# Validate that all the low level C APIs have binding
def validate_c_api_bindings_present(finalklassmap):
    for name, (klass, func, cname) in sorted(finalklassmap.items()):
        pyname = cname
        if pyname == "virSetErrorFunc":
            pyname = "virRegisterErrorHandler"
        elif pyname == "virConnectListDomains":
            pyname = "virConnectListDomainsID"

        # These exist in C and exist in python, but we've got
        # a pure-python impl so don't check them
        if name in ["virStreamRecvAll", "virStreamSendAll",
                    "virStreamSparseRecvAll", "virStreamSparseSendAll"]:
            continue

        try:
            thing = getattr(libvirt.libvirtmod, pyname)
        except AttributeError:
            raise Exception("libvirt.libvirtmod.%s      (C binding does not exist)" % pyname)

# Historically python lxml is incompatible with any other
# use of libxml2 in the same process. Merely importing
# 'lxml.etree' will result in libvirt's use of libxml2
# triggering a SEGV:
#
#    https://bugs.launchpad.net/lxml/+bug/1748019
#
# per the last comment though, it was somewhat improved by
#
#    https://github.com/lxml/lxml/commit/fa1d856cad369d0ac64323ddec14b02281491706
#
# so if we have version >= 4.5.2, we are safe to import
# lxml.etree for the purposes of unit tests at least
def broken_lxml():
    import lxml

    if not hasattr(lxml, "__version__"):
        return True

    digits = [int(d) for d in lxml.__version__.split(".")]

    # We have 3 digits in versions today, but be paranoid
    # for possible future changes.
    if len(digits) != 3:
        return False

    version = (digits[0] * 1000 * 1000) + (digits[1] * 1000) + digits[2]
    if version < 4005002:
        return True

    return False

api_test_flag = unittest.skipUnless(
    os.environ.get('LIBVIRT_API_COVERAGE', False),
    "API coverage test is only for upstream maintainers",
)

lxml_broken_flag = unittest.skipIf(
    broken_lxml(),
    "lxml version clashes with libxml usage from libvirt"
)

@api_test_flag
@lxml_broken_flag
class LibvirtAPICoverage(unittest.TestCase):
    def test_libvirt_api(self):
        xml = get_libvirt_api_xml_path()

        import lxml.etree
        with open(xml, "r") as fp:
            tree = lxml.etree.parse(fp)

        wantfunctions, wantenums, enumvals = identify_functions_enums(tree)
        gotfunctions, gottypes = identify_class_methods(wantenums, enumvals)
        basicklassmap = basic_class_method_mapping(wantfunctions, gottypes)
        finalklassmap = fixup_class_method_mapping(basicklassmap)
        usedfunctions = validate_c_to_python_api_mappings(finalklassmap, gotfunctions)
        validate_python_to_c_api_mappings(gotfunctions, usedfunctions)
        validate_c_api_bindings_present(finalklassmap)
