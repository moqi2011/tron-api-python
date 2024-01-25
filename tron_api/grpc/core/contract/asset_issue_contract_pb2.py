# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tron_api/grpc/core/contract/asset_issue_contract.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6tron_api/grpc/core/contract/asset_issue_contract.proto\x12\x08protocol\"\x90\x04\n\x12\x41ssetIssueContract\x12\n\n\x02id\x18) \x01(\t\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\x0c\x12\x0c\n\x04\x61\x62\x62r\x18\x03 \x01(\x0c\x12\x14\n\x0ctotal_supply\x18\x04 \x01(\x03\x12@\n\rfrozen_supply\x18\x05 \x03(\x0b\x32).protocol.AssetIssueContract.FrozenSupply\x12\x0f\n\x07trx_num\x18\x06 \x01(\x05\x12\x11\n\tprecision\x18\x07 \x01(\x05\x12\x0b\n\x03num\x18\x08 \x01(\x05\x12\x12\n\nstart_time\x18\t \x01(\x03\x12\x10\n\x08\x65nd_time\x18\n \x01(\x03\x12\r\n\x05order\x18\x0b \x01(\x03\x12\x12\n\nvote_score\x18\x10 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x14 \x01(\x0c\x12\x0b\n\x03url\x18\x15 \x01(\x0c\x12\x1c\n\x14\x66ree_asset_net_limit\x18\x16 \x01(\x03\x12#\n\x1bpublic_free_asset_net_limit\x18\x17 \x01(\x03\x12#\n\x1bpublic_free_asset_net_usage\x18\x18 \x01(\x03\x12#\n\x1bpublic_latest_free_net_time\x18\x19 \x01(\x03\x1a:\n\x0c\x46rozenSupply\x12\x15\n\rfrozen_amount\x18\x01 \x01(\x03\x12\x13\n\x0b\x66rozen_days\x18\x02 \x01(\x03\"f\n\x15TransferAssetContract\x12\x12\n\nasset_name\x18\x01 \x01(\x0c\x12\x15\n\rowner_address\x18\x02 \x01(\x0c\x12\x12\n\nto_address\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\".\n\x15UnfreezeAssetContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\"{\n\x13UpdateAssetContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\x0c\x12\x0b\n\x03url\x18\x03 \x01(\x0c\x12\x11\n\tnew_limit\x18\x04 \x01(\x03\x12\x18\n\x10new_public_limit\x18\x05 \x01(\x03\"n\n\x1dParticipateAssetIssueContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x12\n\nto_address\x18\x02 \x01(\x0c\x12\x12\n\nasset_name\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x42\x45\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron_api.grpc.core.contract.asset_issue_contract_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core'
  _globals['_ASSETISSUECONTRACT']._serialized_start=69
  _globals['_ASSETISSUECONTRACT']._serialized_end=597
  _globals['_ASSETISSUECONTRACT_FROZENSUPPLY']._serialized_start=539
  _globals['_ASSETISSUECONTRACT_FROZENSUPPLY']._serialized_end=597
  _globals['_TRANSFERASSETCONTRACT']._serialized_start=599
  _globals['_TRANSFERASSETCONTRACT']._serialized_end=701
  _globals['_UNFREEZEASSETCONTRACT']._serialized_start=703
  _globals['_UNFREEZEASSETCONTRACT']._serialized_end=749
  _globals['_UPDATEASSETCONTRACT']._serialized_start=751
  _globals['_UPDATEASSETCONTRACT']._serialized_end=874
  _globals['_PARTICIPATEASSETISSUECONTRACT']._serialized_start=876
  _globals['_PARTICIPATEASSETISSUECONTRACT']._serialized_end=986
# @@protoc_insertion_point(module_scope)