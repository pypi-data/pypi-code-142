from . import iiifpapi3
errors = 0 
def assign(validationfunc,obj,key):
    try:
        value = getattr(obj,key)
        if value:
            try:
                validationfunc(value)
            except Exception as e:
                setattr(obj,key,"ERROR: "+str(e))
                errors += 1
    except AttributeError:
        pass

def validate_label(originalobj,obj):
    for i in originalobj.label:
        try:
            obj.add_label(i,obj.label[i])
        except Exception as e:
            obj.label[i] = obj.label[i] + "ERROR: "+str(e)

def validate_metadata(originalobj,obj):
    for i in originalobj.metadata:
        try:
            label = list(i['label'].items()) 
            value = list(i['value'].items()) 
            obj.add_metadata(label=label[0][0], value=value[0][0], language_l=label[0][1], language_v=value[0][1])
        except Exception as e:
            obj.metadata[i] = obj.metadata[i] + "ERROR: "+str(e)

def validate_behavior(obj):
    for bh in obj.behavior:
        try:
            obj.add_behavior(bh)
        except Exception as e:
            obj.behavior.append(bh + "ERROR: "+str(e))
            errors += 1

def validate_annotation(obj,parentobj):
    aAnnotation = iiifpapi3.Annotation()
    validate_behavior(obj,aAnnotation)
    validate_homepage(obj,aAnnotation)
    validate_label(obj,aAnnotation)
    validate_metadata(obj,aAnnotation)
    validate_partOf(obj,aAnnotation)
    validate_provider(obj,aAnnotation)
    validate_rendering(obj,aAnnotation)
    validate_requiredStatement(obj,aAnnotation)
    validate_seeAlso(obj,aAnnotation)
    validate_service(obj,aAnnotation)
    validate_summary(obj,aAnnotation)
    validate_thumbnail(obj,aAnnotation)
    assign(aAnnotation.set_id,obj,'id')
    assign(aAnnotation.set_motivation,obj,'motivation')
    assign(aAnnotation.set_requiredStatement,obj,'requiredStatement')
    assign(aAnnotation.set_rights,obj,'rights')
    assign(aAnnotation.set_target_specific_resource,obj,'target_specific_resource')
    assign(aAnnotation.set_type,obj,'type')
    parentobj.add_annotation(aAnnotation)


def validate_canvas_to_items(obj):
    pass

def validate_homepage(obj):
    ahompage = iiifpapi3.homepage()
    validate_label(obj,ahompage)
    assign(ahompage.set_format,obj,'format')
    assign(ahompage.set_id,obj,'id')
    assign(ahompage.set_language,obj,'language')
    assign(ahompage.set_type,obj,'type')

def validate_item(obj):
    pass

def validate_partOf(originalobj,obj):
    for i in originalobj.partOf:
        try:
            apartof = iiifpapi3.partOf()
            validate_label(i,apartof)
            assign(apartof.set_id,i,'id')
            assign(apartof.set_type,i,'type')
            obj.add_partOf(apartof)
        except Exception as e:
            obj.partOf.append(i + "ERROR: "+str(e))
            errors += 1
    

def validate_provider(obj):
    pass
def validate_range_to_structures(obj):
    pass
def validate_rendering(obj):
    pass
def validate_requiredStatement(obj):
    pass
def validate_seeAlso(obj):
    pass
def validate_service(obj):
    pass
def validate_services(obj):
    pass
def validate_structure(obj):
    pass
def validate_summary(obj):
    pass
def validate_thumbnail(obj):
    pass    

def validateManifest(obj):
    amanifest = iiifpapi3.Manifest()
    validate_annotation(obj,amanifest)
    validate_behavior(obj,amanifest)
    validate_canvas_to_items(obj,amanifest)
    validate_homepage(obj,amanifest)
    validate_item(obj,amanifest)
    validate_label(obj,amanifest)
    validate_metadata(obj,amanifest)
    validate_partOf(obj,amanifest)
    validate_provider(obj,amanifest)
    validate_range_to_structures(obj,amanifest)
    validate_rendering(obj,amanifest)
    validate_requiredStatement(obj,amanifest)
    validate_seeAlso(obj,amanifest)
    validate_service(obj,amanifest)
    validate_services(obj,amanifest)
    validate_structure(obj,amanifest)
    validate_summary(obj,amanifest)
    validate_thumbnail(obj,amanifest)
    assign(amanifest.set_id,obj,'id')
    #amanifest.set_type(obj.type)
    assign(amanifest.set_accompanyingCanvas,obj,'accompanyingCanvas')
    assign(amanifest.set_id,obj,'id')
    assign(amanifest.set_navDate,obj,'navDate')
    assign(amanifest.set_placeholderCanvas,obj,'placeholderCanvas')
    assign(amanifest.set_requiredStatement,obj,'requiredStatement')
    assign(amanifest.set_rights,obj,'rights')
    assign(amanifest.set_start,obj,'start')
    assign(amanifest.set_type,obj,'type')
    assign(amanifest.set_viewingDirection,obj,'viewingDirection')
    
    
    
    return amanifest
