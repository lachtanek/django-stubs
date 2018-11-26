from typing import Type, Union, TypeVar, Any, Generic

from django.db import models
from django.db.models import Field

_T = TypeVar('_T', bound=models.Model)


class ForeignKey(Field, Generic[_T]):
    def __init__(self,
                 to: Union[Type[_T], str],
                 on_delete: Any,
                 related_name: str = ...,
                 **kwargs): ...
    def __get__(self, instance, owner) -> _T: ...


class OneToOneField(Field, Generic[_T]):
    def __init__(self,
                 to: Union[Type[_T], str],
                 on_delete: Any,
                 related_name: str = ...,
                 **kwargs): ...
    def __get__(self, instance, owner) -> _T: ...


class ManyToManyField(Field, Generic[_T]):
    def __init__(self,
                 to: Union[Type[_T], str],
                 on_delete: Any,
                 related_name: str = ...,
                 **kwargs): ...
    def __get__(self, instance, owner) -> _T: ...
