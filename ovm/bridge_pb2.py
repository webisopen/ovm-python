# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1/ovm/bridge.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'api/v1/ovm/bridge.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/v1/ovm/bridge.proto\x12\x03ovm\"\x16\n\x04Task\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\r\n\x0bLoadRequest\"-\n\x0cLoadResponse\x12\x1d\n\x04task\x18\x01 \x01(\x0b\x32\t.ovm.TaskR\x04task\"&\n\nLogRequest\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\"\r\n\x0bLogResponse\"\'\n\rSubmitRequest\x12\x16\n\x06output\x18\x01 \x01(\tR\x06output\"\x10\n\x0eSubmitResponse2\x98\x01\n\x06\x42ridge\x12-\n\x04Load\x12\x10.ovm.LoadRequest\x1a\x11.ovm.LoadResponse\"\x00\x12*\n\x03Log\x12\x0f.ovm.LogRequest\x1a\x10.ovm.LogResponse\"\x00\x12\x33\n\x06Submit\x12\x12.ovm.SubmitRequest\x1a\x13.ovm.SubmitResponse\"\x00\x42Q\n\x07\x63om.ovmB\x0b\x42ridgeProtoP\x01Z\rgo/api/v1/ovm\xa2\x02\x03OXX\xaa\x02\x03Ovm\xca\x02\x03Ovm\xe2\x02\x0fOvm\\GPBMetadata\xea\x02\x03Ovmb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1.ovm.bridge_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\007com.ovmB\013BridgeProtoP\001Z\rgo/api/v1/ovm\242\002\003OXX\252\002\003Ovm\312\002\003Ovm\342\002\017Ovm\\GPBMetadata\352\002\003Ovm'
  _globals['_TASK']._serialized_start=32
  _globals['_TASK']._serialized_end=54
  _globals['_LOADREQUEST']._serialized_start=56
  _globals['_LOADREQUEST']._serialized_end=69
  _globals['_LOADRESPONSE']._serialized_start=71
  _globals['_LOADRESPONSE']._serialized_end=116
  _globals['_LOGREQUEST']._serialized_start=118
  _globals['_LOGREQUEST']._serialized_end=156
  _globals['_LOGRESPONSE']._serialized_start=158
  _globals['_LOGRESPONSE']._serialized_end=171
  _globals['_SUBMITREQUEST']._serialized_start=173
  _globals['_SUBMITREQUEST']._serialized_end=212
  _globals['_SUBMITRESPONSE']._serialized_start=214
  _globals['_SUBMITRESPONSE']._serialized_end=230
  _globals['_BRIDGE']._serialized_start=233
  _globals['_BRIDGE']._serialized_end=385
# @@protoc_insertion_point(module_scope)
