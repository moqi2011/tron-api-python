# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tron_api/grpc/core/contract/exchange_contract.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3tron_api/grpc/core/contract/exchange_contract.proto\x12\x08protocol\"\x9b\x01\n\x16\x45xchangeCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x16\n\x0e\x66irst_token_id\x18\x02 \x01(\x0c\x12\x1b\n\x13\x66irst_token_balance\x18\x03 \x01(\x03\x12\x17\n\x0fsecond_token_id\x18\x04 \x01(\x0c\x12\x1c\n\x14second_token_balance\x18\x05 \x01(\x03\"e\n\x16\x45xchangeInjectContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\x03\x12\x10\n\x08token_id\x18\x03 \x01(\x0c\x12\r\n\x05quant\x18\x04 \x01(\x03\"g\n\x18\x45xchangeWithdrawContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\x03\x12\x10\n\x08token_id\x18\x03 \x01(\x0c\x12\r\n\x05quant\x18\x04 \x01(\x03\"|\n\x1b\x45xchangeTransactionContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x65xchange_id\x18\x02 \x01(\x03\x12\x10\n\x08token_id\x18\x03 \x01(\x0c\x12\r\n\x05quant\x18\x04 \x01(\x03\x12\x10\n\x08\x65xpected\x18\x05 \x01(\x03\x42\x45\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron_api.grpc.core.contract.exchange_contract_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core'
  _globals['_EXCHANGECREATECONTRACT']._serialized_start=66
  _globals['_EXCHANGECREATECONTRACT']._serialized_end=221
  _globals['_EXCHANGEINJECTCONTRACT']._serialized_start=223
  _globals['_EXCHANGEINJECTCONTRACT']._serialized_end=324
  _globals['_EXCHANGEWITHDRAWCONTRACT']._serialized_start=326
  _globals['_EXCHANGEWITHDRAWCONTRACT']._serialized_end=429
  _globals['_EXCHANGETRANSACTIONCONTRACT']._serialized_start=431
  _globals['_EXCHANGETRANSACTIONCONTRACT']._serialized_end=555
# @@protoc_insertion_point(module_scope)
