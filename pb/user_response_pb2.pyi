import pb.user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseMeta(_message.Message):
    __slots__ = ("page", "total", "pageSize")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    total: int
    pageSize: int
    def __init__(self, page: _Optional[int] = ..., total: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("users", "meta")
    USERS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    meta: ResponseMeta
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., meta: _Optional[_Union[ResponseMeta, _Mapping]] = ...) -> None: ...
