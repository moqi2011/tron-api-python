# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tron_api/grpc/core/contract/smart_contract.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tron_api.grpc.core import Tron_pb2 as tron__api_dot_grpc_dot_core_dot_Tron__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0tron_api/grpc/core/contract/smart_contract.proto\x12\x08protocol\x1a\x1dtron_api/grpc/core/Tron.proto\"\xac\x07\n\rSmartContract\x12\x16\n\x0eorigin_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\x12(\n\x03\x61\x62i\x18\x03 \x01(\x0b\x32\x1b.protocol.SmartContract.ABI\x12\x10\n\x08\x62ytecode\x18\x04 \x01(\x0c\x12\x12\n\ncall_value\x18\x05 \x01(\x03\x12%\n\x1d\x63onsume_user_resource_percent\x18\x06 \x01(\x03\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x1b\n\x13origin_energy_limit\x18\x08 \x01(\x03\x12\x11\n\tcode_hash\x18\t \x01(\x0c\x12\x10\n\x08trx_hash\x18\n \x01(\x0c\x12\x0f\n\x07version\x18\x0b \x01(\x05\x1a\x90\x05\n\x03\x41\x42I\x12\x31\n\x06\x65ntrys\x18\x01 \x03(\x0b\x32!.protocol.SmartContract.ABI.Entry\x1a\xd5\x04\n\x05\x45ntry\x12\x11\n\tanonymous\x18\x01 \x01(\x08\x12\x10\n\x08\x63onstant\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x37\n\x06inputs\x18\x04 \x03(\x0b\x32\'.protocol.SmartContract.ABI.Entry.Param\x12\x38\n\x07outputs\x18\x05 \x03(\x0b\x32\'.protocol.SmartContract.ABI.Entry.Param\x12\x39\n\x04type\x18\x06 \x01(\x0e\x32+.protocol.SmartContract.ABI.Entry.EntryType\x12\x0f\n\x07payable\x18\x07 \x01(\x08\x12N\n\x0fstateMutability\x18\x08 \x01(\x0e\x32\x35.protocol.SmartContract.ABI.Entry.StateMutabilityType\x1a\x34\n\x05Param\x12\x0f\n\x07indexed\x18\x01 \x01(\x08\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"q\n\tEntryType\x12\x14\n\x10UnknownEntryType\x10\x00\x12\x0f\n\x0b\x43onstructor\x10\x01\x12\x0c\n\x08\x46unction\x10\x02\x12\t\n\x05\x45vent\x10\x03\x12\x0c\n\x08\x46\x61llback\x10\x04\x12\x0b\n\x07Receive\x10\x05\x12\t\n\x05\x45rror\x10\x06\"a\n\x13StateMutabilityType\x12\x19\n\x15UnknownMutabilityType\x10\x00\x12\x08\n\x04Pure\x10\x01\x12\x08\n\x04View\x10\x02\x12\x0e\n\nNonpayable\x10\x03\x12\x0b\n\x07Payable\x10\x04\"R\n\rContractState\x12\x14\n\x0c\x65nergy_usage\x18\x01 \x01(\x03\x12\x15\n\renergy_factor\x18\x02 \x01(\x03\x12\x14\n\x0cupdate_cycle\x18\x03 \x01(\x03\"\x87\x01\n\x13\x43reateSmartContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12-\n\x0cnew_contract\x18\x02 \x01(\x0b\x32\x17.protocol.SmartContract\x12\x18\n\x10\x63\x61ll_token_value\x18\x03 \x01(\x03\x12\x10\n\x08token_id\x18\x04 \x01(\x03\"\x95\x01\n\x14TriggerSmartContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\x12\x12\n\ncall_value\x18\x03 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x18\n\x10\x63\x61ll_token_value\x18\x05 \x01(\x03\x12\x10\n\x08token_id\x18\x06 \x01(\x03\"C\n\x10\x43learABIContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\"o\n\x15UpdateSettingContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\x12%\n\x1d\x63onsume_user_resource_percent\x18\x03 \x01(\x03\"i\n\x19UpdateEnergyLimitContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\x12\x1b\n\x13origin_energy_limit\x18\x03 \x01(\x03\"\x91\x01\n\x18SmartContractDataWrapper\x12/\n\x0esmart_contract\x18\x01 \x01(\x0b\x32\x17.protocol.SmartContract\x12\x13\n\x0bruntimecode\x18\x02 \x01(\x0c\x12/\n\x0e\x63ontract_state\x18\x03 \x01(\x0b\x32\x17.protocol.ContractStateBE\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron_api.grpc.core.contract.smart_contract_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core'
  _globals['_SMARTCONTRACT']._serialized_start=94
  _globals['_SMARTCONTRACT']._serialized_end=1034
  _globals['_SMARTCONTRACT_ABI']._serialized_start=378
  _globals['_SMARTCONTRACT_ABI']._serialized_end=1034
  _globals['_SMARTCONTRACT_ABI_ENTRY']._serialized_start=437
  _globals['_SMARTCONTRACT_ABI_ENTRY']._serialized_end=1034
  _globals['_SMARTCONTRACT_ABI_ENTRY_PARAM']._serialized_start=768
  _globals['_SMARTCONTRACT_ABI_ENTRY_PARAM']._serialized_end=820
  _globals['_SMARTCONTRACT_ABI_ENTRY_ENTRYTYPE']._serialized_start=822
  _globals['_SMARTCONTRACT_ABI_ENTRY_ENTRYTYPE']._serialized_end=935
  _globals['_SMARTCONTRACT_ABI_ENTRY_STATEMUTABILITYTYPE']._serialized_start=937
  _globals['_SMARTCONTRACT_ABI_ENTRY_STATEMUTABILITYTYPE']._serialized_end=1034
  _globals['_CONTRACTSTATE']._serialized_start=1036
  _globals['_CONTRACTSTATE']._serialized_end=1118
  _globals['_CREATESMARTCONTRACT']._serialized_start=1121
  _globals['_CREATESMARTCONTRACT']._serialized_end=1256
  _globals['_TRIGGERSMARTCONTRACT']._serialized_start=1259
  _globals['_TRIGGERSMARTCONTRACT']._serialized_end=1408
  _globals['_CLEARABICONTRACT']._serialized_start=1410
  _globals['_CLEARABICONTRACT']._serialized_end=1477
  _globals['_UPDATESETTINGCONTRACT']._serialized_start=1479
  _globals['_UPDATESETTINGCONTRACT']._serialized_end=1590
  _globals['_UPDATEENERGYLIMITCONTRACT']._serialized_start=1592
  _globals['_UPDATEENERGYLIMITCONTRACT']._serialized_end=1697
  _globals['_SMARTCONTRACTDATAWRAPPER']._serialized_start=1700
  _globals['_SMARTCONTRACTDATAWRAPPER']._serialized_end=1845
# @@protoc_insertion_point(module_scope)