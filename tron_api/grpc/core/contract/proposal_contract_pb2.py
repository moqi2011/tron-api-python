# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tron_api/grpc/core/contract/proposal_contract.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3tron_api/grpc/core/contract/proposal_contract.proto\x12\x08protocol\"^\n\x17ProposalApproveContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x03\x12\x17\n\x0fis_add_approval\x18\x03 \x01(\x08\"\xa8\x01\n\x16ProposalCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x44\n\nparameters\x18\x02 \x03(\x0b\x32\x30.protocol.ProposalCreateContract.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"D\n\x16ProposalDeleteContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x03\x42\x45\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron_api.grpc.core.contract.proposal_contract_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core'
  _globals['_PROPOSALCREATECONTRACT_PARAMETERSENTRY']._options = None
  _globals['_PROPOSALCREATECONTRACT_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_PROPOSALAPPROVECONTRACT']._serialized_start=65
  _globals['_PROPOSALAPPROVECONTRACT']._serialized_end=159
  _globals['_PROPOSALCREATECONTRACT']._serialized_start=162
  _globals['_PROPOSALCREATECONTRACT']._serialized_end=330
  _globals['_PROPOSALCREATECONTRACT_PARAMETERSENTRY']._serialized_start=281
  _globals['_PROPOSALCREATECONTRACT_PARAMETERSENTRY']._serialized_end=330
  _globals['_PROPOSALDELETECONTRACT']._serialized_start=332
  _globals['_PROPOSALDELETECONTRACT']._serialized_end=400
# @@protoc_insertion_point(module_scope)
