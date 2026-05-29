from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hello(_message.Message):
    __slots__ = ("name", "text")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    text: str
    def __init__(self, name: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class MultiHelloResponse(_message.Message):
    __slots__ = ("title", "greetings")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GREETINGS_FIELD_NUMBER: _ClassVar[int]
    title: str
    greetings: _containers.RepeatedCompositeFieldContainer[Hello]
    def __init__(self, title: _Optional[str] = ..., greetings: _Optional[_Iterable[_Union[Hello, _Mapping]]] = ...) -> None: ...
