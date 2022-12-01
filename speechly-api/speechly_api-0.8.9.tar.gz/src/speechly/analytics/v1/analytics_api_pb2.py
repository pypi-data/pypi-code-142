# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: speechly/analytics/v1/analytics_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from speechly.analytics.v1 import analytics_pb2 as speechly_dot_analytics_dot_v1_dot_analytics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='speechly/analytics/v1/analytics_api.proto',
  package='speechly.analytics.v1',
  syntax='proto3',
  serialized_options=b'\n\031com.speechly.analytics.v1B\021AnalyticsApiProtoP\001Z!speechly/analytics/v1;analyticsv1\242\002\003SAX\252\002\025Speechly.Analytics.V1\312\002\025Speechly\\Analytics\\V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)speechly/analytics/v1/analytics_api.proto\x12\x15speechly.analytics.v1\x1a%speechly/analytics/v1/analytics.proto\"\xcd\x02\n\x1aUtteranceStatisticsRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ys\x18\x02 \x01(\x05\x12\x46\n\x05scope\x18\x03 \x01(\x0e\x32\x37.speechly.analytics.v1.UtteranceStatisticsRequest.Scope\x12\x37\n\x0b\x61ggregation\x18\x04 \x01(\x0e\x32\".speechly.analytics.v1.Aggregation\x12\x12\n\nstart_date\x18\x05 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\"V\n\x05Scope\x12\x11\n\rSCOPE_INVALID\x10\x00\x12\x14\n\x10SCOPE_UTTERANCES\x10\x01\x12\x15\n\x11SCOPE_ANNOTATIONS\x10\x02\x12\r\n\tSCOPE_ALL\x10\x03\"\x98\x02\n\x1bUtteranceStatisticsResponse\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x02 \x01(\t\x12\x37\n\x0b\x61ggregation\x18\x03 \x01(\x0e\x32\".speechly.analytics.v1.Aggregation\x12?\n\x05items\x18\x04 \x03(\x0b\x32\x30.speechly.analytics.v1.UtteranceStatisticsPeriod\x12\x18\n\x10total_utterances\x18\x05 \x01(\x05\x12\x1e\n\x16total_duration_seconds\x18\x06 \x01(\x05\x12\x1f\n\x17total_annotated_seconds\x18\x07 \x01(\x05\"#\n\x11UtterancesRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\"J\n\x12UtterancesResponse\x12\x34\n\nutterances\x18\x01 \x03(\x0b\x32 .speechly.analytics.v1.Utterance\"\xb9\x01\n\x18RegisterUtteranceRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12 \n\x18utterance_length_seconds\x18\x03 \x01(\x05\x12\x1e\n\x16utterance_length_chars\x18\x04 \x01(\x05\x12\x38\n\x0c\x64\x65\x63oder_info\x18\x05 \x01(\x0b\x32\".speechly.analytics.v1.DecoderInfo\"\x1b\n\x19RegisterUtteranceResponse2\xe7\x02\n\x0c\x41nalyticsAPI\x12|\n\x13UtteranceStatistics\x12\x31.speechly.analytics.v1.UtteranceStatisticsRequest\x1a\x32.speechly.analytics.v1.UtteranceStatisticsResponse\x12\x61\n\nUtterances\x12(.speechly.analytics.v1.UtterancesRequest\x1a).speechly.analytics.v1.UtterancesResponse\x12v\n\x11RegisterUtterance\x12/.speechly.analytics.v1.RegisterUtteranceRequest\x1a\x30.speechly.analytics.v1.RegisterUtteranceResponseB\x89\x01\n\x19\x63om.speechly.analytics.v1B\x11\x41nalyticsApiProtoP\x01Z!speechly/analytics/v1;analyticsv1\xa2\x02\x03SAX\xaa\x02\x15Speechly.Analytics.V1\xca\x02\x15Speechly\\Analytics\\V1b\x06proto3'
  ,
  dependencies=[speechly_dot_analytics_dot_v1_dot_analytics__pb2.DESCRIPTOR,])



_UTTERANCESTATISTICSREQUEST_SCOPE = _descriptor.EnumDescriptor(
  name='Scope',
  full_name='speechly.analytics.v1.UtteranceStatisticsRequest.Scope',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCOPE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCOPE_UTTERANCES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCOPE_ANNOTATIONS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCOPE_ALL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=355,
  serialized_end=441,
)
_sym_db.RegisterEnumDescriptor(_UTTERANCESTATISTICSREQUEST_SCOPE)


_UTTERANCESTATISTICSREQUEST = _descriptor.Descriptor(
  name='UtteranceStatisticsRequest',
  full_name='speechly.analytics.v1.UtteranceStatisticsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='days', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.days', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scope', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.scope', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.aggregation', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.start_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.end_date', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='speechly.analytics.v1.UtteranceStatisticsRequest.project_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UTTERANCESTATISTICSREQUEST_SCOPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=441,
)


_UTTERANCESTATISTICSRESPONSE = _descriptor.Descriptor(
  name='UtteranceStatisticsResponse',
  full_name='speechly.analytics.v1.UtteranceStatisticsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_date', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.start_date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.end_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.aggregation', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_utterances', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.total_utterances', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_duration_seconds', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.total_duration_seconds', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_annotated_seconds', full_name='speechly.analytics.v1.UtteranceStatisticsResponse.total_annotated_seconds', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=724,
)


_UTTERANCESREQUEST = _descriptor.Descriptor(
  name='UtterancesRequest',
  full_name='speechly.analytics.v1.UtterancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='speechly.analytics.v1.UtterancesRequest.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=726,
  serialized_end=761,
)


_UTTERANCESRESPONSE = _descriptor.Descriptor(
  name='UtterancesResponse',
  full_name='speechly.analytics.v1.UtterancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='utterances', full_name='speechly.analytics.v1.UtterancesResponse.utterances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=837,
)


_REGISTERUTTERANCEREQUEST = _descriptor.Descriptor(
  name='RegisterUtteranceRequest',
  full_name='speechly.analytics.v1.RegisterUtteranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='speechly.analytics.v1.RegisterUtteranceRequest.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='speechly.analytics.v1.RegisterUtteranceRequest.device_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='utterance_length_seconds', full_name='speechly.analytics.v1.RegisterUtteranceRequest.utterance_length_seconds', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='utterance_length_chars', full_name='speechly.analytics.v1.RegisterUtteranceRequest.utterance_length_chars', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decoder_info', full_name='speechly.analytics.v1.RegisterUtteranceRequest.decoder_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=840,
  serialized_end=1025,
)


_REGISTERUTTERANCERESPONSE = _descriptor.Descriptor(
  name='RegisterUtteranceResponse',
  full_name='speechly.analytics.v1.RegisterUtteranceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1027,
  serialized_end=1054,
)

_UTTERANCESTATISTICSREQUEST.fields_by_name['scope'].enum_type = _UTTERANCESTATISTICSREQUEST_SCOPE
_UTTERANCESTATISTICSREQUEST.fields_by_name['aggregation'].enum_type = speechly_dot_analytics_dot_v1_dot_analytics__pb2._AGGREGATION
_UTTERANCESTATISTICSREQUEST_SCOPE.containing_type = _UTTERANCESTATISTICSREQUEST
_UTTERANCESTATISTICSRESPONSE.fields_by_name['aggregation'].enum_type = speechly_dot_analytics_dot_v1_dot_analytics__pb2._AGGREGATION
_UTTERANCESTATISTICSRESPONSE.fields_by_name['items'].message_type = speechly_dot_analytics_dot_v1_dot_analytics__pb2._UTTERANCESTATISTICSPERIOD
_UTTERANCESRESPONSE.fields_by_name['utterances'].message_type = speechly_dot_analytics_dot_v1_dot_analytics__pb2._UTTERANCE
_REGISTERUTTERANCEREQUEST.fields_by_name['decoder_info'].message_type = speechly_dot_analytics_dot_v1_dot_analytics__pb2._DECODERINFO
DESCRIPTOR.message_types_by_name['UtteranceStatisticsRequest'] = _UTTERANCESTATISTICSREQUEST
DESCRIPTOR.message_types_by_name['UtteranceStatisticsResponse'] = _UTTERANCESTATISTICSRESPONSE
DESCRIPTOR.message_types_by_name['UtterancesRequest'] = _UTTERANCESREQUEST
DESCRIPTOR.message_types_by_name['UtterancesResponse'] = _UTTERANCESRESPONSE
DESCRIPTOR.message_types_by_name['RegisterUtteranceRequest'] = _REGISTERUTTERANCEREQUEST
DESCRIPTOR.message_types_by_name['RegisterUtteranceResponse'] = _REGISTERUTTERANCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UtteranceStatisticsRequest = _reflection.GeneratedProtocolMessageType('UtteranceStatisticsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCESTATISTICSREQUEST,
  '__module__' : 'speechly.analytics.v1.analytics_api_pb2'
  # @@protoc_insertion_point(class_scope:speechly.analytics.v1.UtteranceStatisticsRequest)
  })
_sym_db.RegisterMessage(UtteranceStatisticsRequest)

UtteranceStatisticsResponse = _reflection.GeneratedProtocolMessageType('UtteranceStatisticsResponse', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCESTATISTICSRESPONSE,
  '__module__' : 'speechly.analytics.v1.analytics_api_pb2'
  # @@protoc_insertion_point(class_scope:speechly.analytics.v1.UtteranceStatisticsResponse)
  })
_sym_db.RegisterMessage(UtteranceStatisticsResponse)

UtterancesRequest = _reflection.GeneratedProtocolMessageType('UtterancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCESREQUEST,
  '__module__' : 'speechly.analytics.v1.analytics_api_pb2'
  # @@protoc_insertion_point(class_scope:speechly.analytics.v1.UtterancesRequest)
  })
_sym_db.RegisterMessage(UtterancesRequest)

UtterancesResponse = _reflection.GeneratedProtocolMessageType('UtterancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCESRESPONSE,
  '__module__' : 'speechly.analytics.v1.analytics_api_pb2'
  # @@protoc_insertion_point(class_scope:speechly.analytics.v1.UtterancesResponse)
  })
_sym_db.RegisterMessage(UtterancesResponse)

RegisterUtteranceRequest = _reflection.GeneratedProtocolMessageType('RegisterUtteranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERUTTERANCEREQUEST,
  '__module__' : 'speechly.analytics.v1.analytics_api_pb2'
  # @@protoc_insertion_point(class_scope:speechly.analytics.v1.RegisterUtteranceRequest)
  })
_sym_db.RegisterMessage(RegisterUtteranceRequest)

RegisterUtteranceResponse = _reflection.GeneratedProtocolMessageType('RegisterUtteranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERUTTERANCERESPONSE,
  '__module__' : 'speechly.analytics.v1.analytics_api_pb2'
  # @@protoc_insertion_point(class_scope:speechly.analytics.v1.RegisterUtteranceResponse)
  })
_sym_db.RegisterMessage(RegisterUtteranceResponse)


DESCRIPTOR._options = None

_ANALYTICSAPI = _descriptor.ServiceDescriptor(
  name='AnalyticsAPI',
  full_name='speechly.analytics.v1.AnalyticsAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1057,
  serialized_end=1416,
  methods=[
  _descriptor.MethodDescriptor(
    name='UtteranceStatistics',
    full_name='speechly.analytics.v1.AnalyticsAPI.UtteranceStatistics',
    index=0,
    containing_service=None,
    input_type=_UTTERANCESTATISTICSREQUEST,
    output_type=_UTTERANCESTATISTICSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Utterances',
    full_name='speechly.analytics.v1.AnalyticsAPI.Utterances',
    index=1,
    containing_service=None,
    input_type=_UTTERANCESREQUEST,
    output_type=_UTTERANCESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterUtterance',
    full_name='speechly.analytics.v1.AnalyticsAPI.RegisterUtterance',
    index=2,
    containing_service=None,
    input_type=_REGISTERUTTERANCEREQUEST,
    output_type=_REGISTERUTTERANCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYTICSAPI)

DESCRIPTOR.services_by_name['AnalyticsAPI'] = _ANALYTICSAPI

# @@protoc_insertion_point(module_scope)
