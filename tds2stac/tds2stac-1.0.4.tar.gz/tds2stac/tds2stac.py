import requests
from shapely import geometry
import os
from lxml import etree
from urllib import parse as urlparse
from urllib.parse import quote_plus
from tds2stac import constants, funcs
from dateutil.parser import parse
import pytz
from tqdm import tqdm
import pystac
from datetime import datetime
from pystac.extensions.datacube import DatacubeExtension, Variable, HorizontalSpatialDimension, TemporalDimension, DimensionType


class Converter(object):
    def __init__(self, main_url, stac = None, stac_dir = None, stac_id = None, stac_description = None):

        self.scanned = []
        self.catalog = dict()
        self.catalog_names =[]
        self.catalog_id = []
        self.data_num = 0
        self.branch_num = 0



        url_cat = funcs.html2xml(main_url)
        convert_xml_o = funcs.replacement_func(url_cat)
        xml = funcs.get_xml(url_cat)

        print("Start Scanning datasets of %s" % url_cat)
        Scanning = list(self.dataset_status(url_cat,xml)) 

        self.catalog[convert_xml_o] = pystac.Catalog(id = convert_xml_o, description = url_cat)
        self.catalog_id.append(self.catalog[convert_xml_o].id)
        #print(self.catalog_id)
        self.catalog_all = pystac.Catalog(id = "all", description = "all")
        self.catalog_all.add_child(self.catalog[convert_xml_o])


        print(str(self.data_num), "data are going to be set as items")
        print(str(self.branch_num), "data are going to be set as items")
        self.scanned = []

        self.data_num1 = 0
        self.branch_num1 = 0
        if stac is not None:
            self.catalog_main = pystac.Catalog(id = stac_id, description = stac_description)

            urls = list(self.dataset_url_finder(url_cat,xml)) 

            self.catalog[convert_xml_o].normalize_hrefs(os.path.join(stac_dir, 'stac'))

            self.catalog[convert_xml_o].save(catalog_type=pystac.CatalogType.SELF_CONTAINED)


    def dataset_url_finder(self, url, xml_content):


        if url in self.scanned:
            print("Already Scanned %s " % url)
            return
        self.scanned.append(url)

        convert_xml = funcs.replacement_func(url)
        
        for el in list(self.catalog_all.get_children()):
            self.catalog_id.append(el.id)
        if convert_xml not in self.catalog_id:
            self.catalog[convert_xml] = pystac.Catalog(id = convert_xml, description = url)
        self.catalog_all.add_child(self.catalog[convert_xml])
        self.catalog_names.append(convert_xml)

        url = funcs.html2xml(url)

        try:
            tree = etree.XML(xml_content)
        except BaseException:
            return


        branches_main = []
        for br in tree.findall('.//{%s}catalogRef' % constants.unidata):
            branches_main.append(funcs.references_urls(url, br.get("{%s}href" % constants.w3)))
            convert_xml_x = funcs.replacement_func(funcs.references_urls(url, br.get("{%s}href" % constants.w3)))

            self.catalog[convert_xml_x] = pystac.Catalog(id = convert_xml_x, description = url)
            self.catalog_all.add_child(self.catalog[convert_xml_x])
            self.catalog[convert_xml].add_child(self.catalog[convert_xml_x])          


        data_main = []
        for e in branches_main:
            try:
                url_stat = requests.get(e, None, verify=False)
                content = url_stat.text.encode('utf-8')
            except BaseException:
                continue
            data_main.append(content)

        if branches_main == []:
            self.data_num1 = self.data_num1 + len(tree.findall('.//{%s}dataset[@urlPath]' % constants.unidata))
        else:
            self.branch_num1 = self.branch_num1 + len(tree.findall('.//{%s}catalogRef' % constants.unidata))            


        for i, d in enumerate(data_main):
            #print(i)
            for dataset in self.dataset_url_finder(branches_main[i], d):
                yield dataset


        print("Start processing: ",url)        
        print(self.branch_num1,"/", self.branch_num, "STAC catalogs are created")
        print(self.data_num1,"/", self.data_num, "STAC items are connected to the related catalog")        
        for elem in tqdm(tree.findall('.//{%s}dataset[@urlPath]' % constants.unidata),colour="red"):
            gid = elem.get('ID')
            self.services    = []
            self.id          = None
            self.name        = None
            self.catalog_url = None
            self.date_   = None
            variables={}
            dimensions={}
            var = []
            dim = []            
            keyword = []
            aName = []
            descriptor = []
            dimensionName = []
            resolution = []
          
            const_list = ["time","lat","latitude","lon","longitude","long","time_bnds"]
            data_format = ["float", "double", "int"]
            r = requests.get(str(url)+"?dataset="+str(gid), None, verify=False)
            try:
                tree_x = etree.XML(r.text.encode('utf-8'))
            except etree.XMLSyntaxError:
                continue
            else:
                try:
                    dataset = tree_x.find("{%s}dataset" % constants.unidata)
                    self.id = dataset.get("ID")
                    self.name = dataset.get("name")
                    metadata = dataset.find("{%s}metadata" % constants.unidata)
                    self.catalog_url = url.split("?")[0]

                    date_ = dataset.find('.//{%s}date[@type="modified"]' % constants.unidata)
                    if date_ is not None:
                        try:
                            dt = date_.text
                            comp_dt = parse(date_.text)
                            comp_dt = comp_dt.replace(tzinfo=pytz.utc)
                            self.date_ = dt

                        except ValueError:
                            continue
                    # Services
                    service_tag = dataset.find("{%s}serviceName" % constants.unidata)
                    if service_tag is None:
                        if metadata is not None:
                            service_tag = metadata.find("{%s}serviceName" % constants.unidata)

                    if service_tag is None:
                        # Use services found in the file. FMRC aggs do this.
                        services = tree_x.findall(".//{%s}service[@serviceType='Compound']" % constants.unidata)
                    else:
                        # Use specific named services
                        services = tree_x.findall(".//{%s}service[@name='%s']" % (constants.unidata, service_tag.text))

                    for service in services:
                        if service.get("serviceType") == "Compound":
                            for s in service.findall("{%s}service" % constants.unidata):
                                service_url = funcs.references_urls(url, s.get('base')) + dataset.get("urlPath")
                                if s.get("suffix") is not None:
                                    service_url += s.get("suffix")
                                if s.get('name') in ["iso", "ncml", "uddc"]:
                                    service_url += "?dataset=%s&&catalog=%s" % (self.id, quote_plus(self.catalog_url))                                
                                if 'iso' in service_url:
                                    root = etree.parse(service_url).getroot()
                                    
                                    for watt in root.iter():
                                        if watt.tag == "{%s}westBoundLongitude" % constants.iso_gmd:
                                            
                                            for wa in watt:
                                                westBoundLongitude = wa.text
                                        if watt.tag == "{%s}eastBoundLongitude" % constants.iso_gmd:
                                            
                                            for wa in watt:
                                                eastBoundLongitude = wa.text
                                        if watt.tag == "{%s}southBoundLatitude" % constants.iso_gmd:
                                            
                                            for wa in watt:
                                                southBoundLatitude = wa.text
                                        if watt.tag == "{%s}northBoundLatitude" % constants.iso_gmd:                                        
                                            for wa in watt:
                                                northBoundLatitude = wa.text
                                        # if watt.tag == "{%s}title" % constants.iso_gmd:                                        
                                        #     for wa in watt:
                                        #         title_ = wa.text
                                        if watt.tag == "{%s}keyword" % constants.iso_gmd:                                        
                                            for wa in watt:
                                                if wa.text in const_list:
                                                    keyword.append(wa.text)                                                 
                                        if watt.tag == "{%s}aName" % constants.iso_gco:                                        
                                            for wa in watt:
                                                if wa.text not in data_format:
                                                    aName.append(wa.text)   
                                        if watt.tag == "{%s}descriptor" % constants.iso_gmd:                                        
                                            for wa in watt:
                                                descriptor.append(wa.text) 
                                        if watt.tag == "{%s}dimensionName" % constants.iso_gmd:
                                            for wa in watt:
                                                dimensionName.append(wa.text)                                                 
                                        # if watt.tag == "{%s}Measure" % constants.iso_gco: 
                                        #     for wa in watt:
                                        #         Measure.append(wa.text)
                                        if watt.tag == "{%s}resolution" % constants.iso_gmd: 
                                            for wa in watt:
                                                resolution.append(wa.text)  
   
                                        if watt.tag == "{%s}beginPosition" % constants.iso_gml:
                                            beginPosition = watt.text

                                        if watt.tag == "{%s}endPosition" % constants.iso_gml: 
                                            endPosition = watt.text 
                    boundingBox = [westBoundLongitude,southBoundLatitude,eastBoundLongitude,northBoundLatitude]
                    bbox_x = list(map(float, boundingBox))
                    footprint = geometry.Polygon([
                                [bbox_x[0], bbox_x[1]],
                                [bbox_x[0], bbox_x[3]],
                                [bbox_x[2], bbox_x[3]],
                                [bbox_x[2], bbox_x[1]]
                            ])
                    
                    item = pystac.Item(id=elem.get('ID'),
                    geometry=geometry.mapping(footprint),
                    bbox=bbox_x,
                    datetime=comp_dt,
                    properties={ })   
                    # Adding web services as assets into items                                         
                    for service in services:
                        if service.get("serviceType") == "Compound":
                            for s in service.findall("{%s}service" % constants.unidata):
                                service_url = funcs.references_urls(url, s.get('base')) + dataset.get("urlPath")
                                if s.get("suffix") is not None:
                                    service_url += s.get("suffix")
                                if s.get('name') in ["iso", "ncml", "uddc"]:
                                    service_url += "?dataset=%s&&catalog=%s" % (self.id, quote_plus(self.catalog_url))
                                if s.get("name") in ["odap"]:
                                    service_url += ".html"
                                # Determinatio of Media Type                                    
                                if s.get('name') in ["iso", "ncml", "wms", "wcs"]:
                                    media_type_ = pystac.MediaType.XML
                                elif s.get('name') in ["http"]:
                                    media_type_ = "application/netcdf"
                                elif s.get('name') in ["dap4", "odap", "uddc"]:
                                    media_type_ = pystac.MediaType.HTML
                                else:
                                    media_type_ = pystac.MediaType.TEXT


                                item.add_asset(
                                    key=s.get("name"), 
                                    asset=pystac.Asset(
                                        href=service_url,
                                        # title=without_slash,
                                        media_type=media_type_
                                    )
                                )

                    cube = DatacubeExtension.ext(item, add_if_missing=True)


                    for i,v in enumerate(aName):
                        var.append(Variable(
                            dict(
                                type="data",
                                description=descriptor[i],
                                dimensions=keyword,
                            )
                        ))

                    for i,v in enumerate(aName):
                        if aName[i] not in const_list:
                            variables[v] = var[i]
                        
                    for i,v in enumerate(dimensionName):
                        if dimensionName[i] == "row":
                            extend_ = [westBoundLongitude,eastBoundLongitude]
                            type_ = DimensionType.SPATIAL.value
                            description_ = "longitude"
                            axis_ = "x"
                        elif dimensionName[i] == "column":
                            extend_ = [southBoundLatitude,northBoundLatitude]
                            type_ = DimensionType.SPATIAL.value
                            description_ = "latitude"
                            axis_ = "y"
                        else:
                            extend_ = [beginPosition,endPosition]
                            type_ = DimensionType.TEMPORAL.value
                            description_ = "time"
                            axis_ = "time"


                        dim.append(HorizontalSpatialDimension(
                            properties=dict(
                                axis=axis_,
                                extent=extend_,
                                description=description_,
                                reference_system="epsg:4326",
                                type=type_,
                            )
                        ))
                    for i,v in enumerate(dimensionName):
                        dimensions[v] = dim[i]                         

                    cube.apply(dimensions=dimensions, variables=variables)

                    convert_xml_m = funcs.replacement_func(url)
                    self.catalog[convert_xml_m].add_item(item)
                except BaseException as e:
                    continue

            yield str(url)+"?dataset="+str(gid)

    def dataset_status(self, url, xml_content):

        if url in self.scanned:
            print("Already Scanned %s " % url)
            return
        self.scanned.append(url)

        url = funcs.html2xml(url)

        try:
            tree = etree.XML(xml_content)
        except BaseException:
            return

        branches = []

        for br in (tree.findall('.//{%s}catalogRef' % constants.unidata)):
            branches.append(funcs.references_urls(url, br.get("{%s}href" % constants.w3)))
            
        data = []
        for e in branches:
            try:
                url_stat = requests.get(e, None, verify=False)
                content = url_stat.text.encode('utf-8')
            except BaseException:
                print("INFO: Skipping %s (error parsing the XML)" % url)            
            data.append(content)

            
        if branches == []:
            print("|_______",url, "|  Number of data: ",len(tree.findall('.//{%s}dataset[@urlPath]' % constants.unidata)))
            self.data_num = self.data_num +len(tree.findall('.//{%s}dataset[@urlPath]' % constants.unidata))
        else:
            print("|__",url, "|  Number of branches: ",len(tree.findall('.//{%s}catalogRef' % constants.unidata)))
            self.branch_num = self.branch_num + len(tree.findall('.//{%s}catalogRef' % constants.unidata))

        for i, d in enumerate(data):

            for dataset in self.dataset_status(branches[i], d):
                yield dataset


        for elem in tree.findall('.//{%s}dataset[@urlPath]' % constants.unidata):
            gid = elem.get('ID')
            yield str(url)+"?dataset="+str(gid)



