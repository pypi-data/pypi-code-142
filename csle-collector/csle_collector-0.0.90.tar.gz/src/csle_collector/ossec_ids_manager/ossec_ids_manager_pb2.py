# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ossec_ids_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17ossec_ids_manager.proto\"@\n\x14GetOSSECIdsAlertsMsg\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\x12\x15\n\rlog_file_path\x18\x02 \x01(\t\"\x18\n\x16StopOSSECIdsMonitorMsg\"\x11\n\x0fStopOSSECIdsMsg\"\x12\n\x10StartOSSECIdsMsg\"u\n\x17StartOSSECIdsMonitorMsg\x12\x10\n\x08kafka_ip\x18\x01 \x01(\t\x12\x12\n\nkafka_port\x18\x02 \x01(\x05\x12\x15\n\rlog_file_path\x18\x03 \x01(\t\x12\x1d\n\x15time_step_len_seconds\x18\x04 \x01(\x05\"\x1d\n\x1bGetOSSECIdsMonitorStatusMsg\"H\n\x12OSSECIdsMonitorDTO\x12\x17\n\x0fmonitor_running\x18\x01 \x01(\x08\x12\x19\n\x11ossec_ids_running\x18\x02 \x01(\x08\"\x80\x07\n\x0eOSSECIdsLogDTO\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x1e\n\x16\x61ttempted_admin_alerts\x18\x03 \x01(\x05\x12\x14\n\x0ctotal_alerts\x18\x04 \x01(\x05\x12\x16\n\x0ewarning_alerts\x18\x05 \x01(\x05\x12\x15\n\rsevere_alerts\x18\x06 \x01(\x05\x12 \n\x18\x61lerts_weighted_by_level\x18\x07 \x01(\x05\x12\x16\n\x0elevel_0_alerts\x18\x08 \x01(\x05\x12\x16\n\x0elevel_1_alerts\x18\t \x01(\x05\x12\x16\n\x0elevel_2_alerts\x18\n \x01(\x05\x12\x16\n\x0elevel_3_alerts\x18\x0b \x01(\x05\x12\x16\n\x0elevel_4_alerts\x18\x0c \x01(\x05\x12\x16\n\x0elevel_5_alerts\x18\r \x01(\x05\x12\x16\n\x0elevel_6_alerts\x18\x0e \x01(\x05\x12\x16\n\x0elevel_7_alerts\x18\x0f \x01(\x05\x12\x16\n\x0elevel_8_alerts\x18\x10 \x01(\x05\x12\x16\n\x0elevel_9_alerts\x18\x11 \x01(\x05\x12\x17\n\x0flevel_10_alerts\x18\x12 \x01(\x05\x12\x17\n\x0flevel_11_alerts\x18\x13 \x01(\x05\x12\x17\n\x0flevel_12_alerts\x18\x14 \x01(\x05\x12\x17\n\x0flevel_13_alerts\x18\x15 \x01(\x05\x12\x17\n\x0flevel_14_alerts\x18\x16 \x01(\x05\x12\x17\n\x0flevel_15_alerts\x18\x17 \x01(\x05\x12\x1c\n\x14invalid_login_alerts\x18\x18 \x01(\x05\x12%\n\x1d\x61uthentication_success_alerts\x18\x19 \x01(\x05\x12$\n\x1c\x61uthentication_failed_alerts\x18\x1a \x01(\x05\x12!\n\x19\x63onnection_attempt_alerts\x18\x1b \x01(\x05\x12\x16\n\x0e\x61ttacks_alerts\x18\x1c \x01(\x05\x12\x16\n\x0e\x61\x64\x64user_alerts\x18\x1d \x01(\x05\x12\x13\n\x0bsshd_alerts\x18\x1e \x01(\x05\x12\x12\n\nids_alerts\x18\x1f \x01(\x05\x12\x17\n\x0f\x66irewall_alerts\x18  \x01(\x05\x12\x14\n\x0csquid_alerts\x18! \x01(\x05\x12\x15\n\rapache_alerts\x18\" \x01(\x05\x12\x15\n\rsyslog_alerts\x18# \x01(\x05\x32\xa5\x03\n\x0fOSSECIdsManager\x12=\n\x11getOSSECIdsAlerts\x12\x15.GetOSSECIdsAlertsMsg\x1a\x0f.OSSECIdsLogDTO\"\x00\x12\x45\n\x13stopOSSECIdsMonitor\x12\x17.StopOSSECIdsMonitorMsg\x1a\x13.OSSECIdsMonitorDTO\"\x00\x12G\n\x14startOSSECIdsMonitor\x12\x18.StartOSSECIdsMonitorMsg\x1a\x13.OSSECIdsMonitorDTO\"\x00\x12\x37\n\x0cstopOSSECIds\x12\x10.StopOSSECIdsMsg\x1a\x13.OSSECIdsMonitorDTO\"\x00\x12\x39\n\rstartOSSECIds\x12\x11.StartOSSECIdsMsg\x1a\x13.OSSECIdsMonitorDTO\"\x00\x12O\n\x18getOSSECIdsMonitorStatus\x12\x1c.GetOSSECIdsMonitorStatusMsg\x1a\x13.OSSECIdsMonitorDTO\"\x00\x62\x06proto3')



_GETOSSECIDSALERTSMSG = DESCRIPTOR.message_types_by_name['GetOSSECIdsAlertsMsg']
_STOPOSSECIDSMONITORMSG = DESCRIPTOR.message_types_by_name['StopOSSECIdsMonitorMsg']
_STOPOSSECIDSMSG = DESCRIPTOR.message_types_by_name['StopOSSECIdsMsg']
_STARTOSSECIDSMSG = DESCRIPTOR.message_types_by_name['StartOSSECIdsMsg']
_STARTOSSECIDSMONITORMSG = DESCRIPTOR.message_types_by_name['StartOSSECIdsMonitorMsg']
_GETOSSECIDSMONITORSTATUSMSG = DESCRIPTOR.message_types_by_name['GetOSSECIdsMonitorStatusMsg']
_OSSECIDSMONITORDTO = DESCRIPTOR.message_types_by_name['OSSECIdsMonitorDTO']
_OSSECIDSLOGDTO = DESCRIPTOR.message_types_by_name['OSSECIdsLogDTO']
GetOSSECIdsAlertsMsg = _reflection.GeneratedProtocolMessageType('GetOSSECIdsAlertsMsg', (_message.Message,), {
  'DESCRIPTOR' : _GETOSSECIDSALERTSMSG,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:GetOSSECIdsAlertsMsg)
  })
_sym_db.RegisterMessage(GetOSSECIdsAlertsMsg)

StopOSSECIdsMonitorMsg = _reflection.GeneratedProtocolMessageType('StopOSSECIdsMonitorMsg', (_message.Message,), {
  'DESCRIPTOR' : _STOPOSSECIDSMONITORMSG,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:StopOSSECIdsMonitorMsg)
  })
_sym_db.RegisterMessage(StopOSSECIdsMonitorMsg)

StopOSSECIdsMsg = _reflection.GeneratedProtocolMessageType('StopOSSECIdsMsg', (_message.Message,), {
  'DESCRIPTOR' : _STOPOSSECIDSMSG,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:StopOSSECIdsMsg)
  })
_sym_db.RegisterMessage(StopOSSECIdsMsg)

StartOSSECIdsMsg = _reflection.GeneratedProtocolMessageType('StartOSSECIdsMsg', (_message.Message,), {
  'DESCRIPTOR' : _STARTOSSECIDSMSG,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:StartOSSECIdsMsg)
  })
_sym_db.RegisterMessage(StartOSSECIdsMsg)

StartOSSECIdsMonitorMsg = _reflection.GeneratedProtocolMessageType('StartOSSECIdsMonitorMsg', (_message.Message,), {
  'DESCRIPTOR' : _STARTOSSECIDSMONITORMSG,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:StartOSSECIdsMonitorMsg)
  })
_sym_db.RegisterMessage(StartOSSECIdsMonitorMsg)

GetOSSECIdsMonitorStatusMsg = _reflection.GeneratedProtocolMessageType('GetOSSECIdsMonitorStatusMsg', (_message.Message,), {
  'DESCRIPTOR' : _GETOSSECIDSMONITORSTATUSMSG,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:GetOSSECIdsMonitorStatusMsg)
  })
_sym_db.RegisterMessage(GetOSSECIdsMonitorStatusMsg)

OSSECIdsMonitorDTO = _reflection.GeneratedProtocolMessageType('OSSECIdsMonitorDTO', (_message.Message,), {
  'DESCRIPTOR' : _OSSECIDSMONITORDTO,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:OSSECIdsMonitorDTO)
  })
_sym_db.RegisterMessage(OSSECIdsMonitorDTO)

OSSECIdsLogDTO = _reflection.GeneratedProtocolMessageType('OSSECIdsLogDTO', (_message.Message,), {
  'DESCRIPTOR' : _OSSECIDSLOGDTO,
  '__module__' : 'ossec_ids_manager_pb2'
  # @@protoc_insertion_point(class_scope:OSSECIdsLogDTO)
  })
_sym_db.RegisterMessage(OSSECIdsLogDTO)

_OSSECIDSMANAGER = DESCRIPTOR.services_by_name['OSSECIdsManager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETOSSECIDSALERTSMSG._serialized_start=27
  _GETOSSECIDSALERTSMSG._serialized_end=91
  _STOPOSSECIDSMONITORMSG._serialized_start=93
  _STOPOSSECIDSMONITORMSG._serialized_end=117
  _STOPOSSECIDSMSG._serialized_start=119
  _STOPOSSECIDSMSG._serialized_end=136
  _STARTOSSECIDSMSG._serialized_start=138
  _STARTOSSECIDSMSG._serialized_end=156
  _STARTOSSECIDSMONITORMSG._serialized_start=158
  _STARTOSSECIDSMONITORMSG._serialized_end=275
  _GETOSSECIDSMONITORSTATUSMSG._serialized_start=277
  _GETOSSECIDSMONITORSTATUSMSG._serialized_end=306
  _OSSECIDSMONITORDTO._serialized_start=308
  _OSSECIDSMONITORDTO._serialized_end=380
  _OSSECIDSLOGDTO._serialized_start=383
  _OSSECIDSLOGDTO._serialized_end=1279
  _OSSECIDSMANAGER._serialized_start=1282
  _OSSECIDSMANAGER._serialized_end=1703
# @@protoc_insertion_point(module_scope)
