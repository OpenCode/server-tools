# Copyright 2023 Apruzzese Francesco <cescoap@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields


fields.Char.transformations = {}
fields.Char.transformations_on = None


# /!\ Reuse the monkey-patching logic of official module
# community/odoo/addons/base_sparse_field
def monkey_patch(cls):
    """ Return a method decorator to monkey-patch the given class."""
    def decorate(func):
        name = func.__name__
        func.super = getattr(cls, name, None)
        setattr(cls, name, func)
        return func
    return decorate


@monkey_patch(fields.Char)
def convert_to_record(self, value, record):
    value = convert_to_record.super(self, value, record)
    if self.transformations_on == "read":
        value = self._transformation(value)
    return value


@monkey_patch(fields.Char)
def convert_to_read(self, value, record, use_name_get=True):
    value = convert_to_read.super(self, value, record, use_name_get)
    if self.transformations_on == "read":
        value = self._transformation(value)
    return value


@monkey_patch(fields.Char)
def convert_to_write(self, value, record):
    value = convert_to_write.super(self, value, record)
    if self.transformations_on == "write":
        value = self._transformation(value)
    return value


@monkey_patch(fields.Char)
def convert_to_column(self, value, record, values=None, validate=True):
    value = convert_to_column.super(self, value, record, values, validate)
    if self.transformations_on == "write":
        value = self._transformation(value)
    return value


@monkey_patch(fields.Char)
def convert_to_cache(self, value, record, validate=True):
    value = convert_to_cache.super(self, value, record, validate)
    if self.transformations_on == "write":
        value = self._transformation(value)
    return value


@monkey_patch(fields.Char)
def _transformation(self, value):
    if not value:
        return value
    for transformation, args in self.transformations.items():
        transformation_function_name = f"_transformation_{transformation}"
        if hasattr(self, transformation_function_name) and args:
            value = getattr(self, transformation_function_name)(value, args)
    return value


@monkey_patch(fields.Char)
def _transformation_capitalize(self, value, args):
    return value.capitalize() if value else value


@monkey_patch(fields.Char)
def _transformation_expandtabs(self, value, args):
    if not value:
        return value
    return value.expandtabs(args) if isinstance(args, int) else value.expandtabs()


@monkey_patch(fields.Char)
def _transformation_lower(self, value, args):
    return value.lower() if value else value


@monkey_patch(fields.Char)
def _transformation_lstrip(self, value, args):
    if not value:
        return value
    return value.lstrip(args) if isinstance(args, str) else value.lstrip()


@monkey_patch(fields.Char)
def _transformation_removeprefix(self, value, args):
    if not value or not args:
        return value
    return value.removeprefix(args)


@monkey_patch(fields.Char)
def _transformation_removesuffix(self, value, args):
    if not value or not args:
        return value
    return value.removesuffix(args)


@monkey_patch(fields.Char)
def _transformation_rstrip(self, value, args):
    if not value:
        return value
    return value.rstrip(args) if isinstance(args, str) else value.rstrip()


@monkey_patch(fields.Char)
def _transformation_strip(self, value, args):
    if not value:
        return value
    return value.strip(args) if isinstance(args, str) else value.strip()


@monkey_patch(fields.Char)
def _transformation_swapcase(self, value, args):
    return value.swapcase() if value else value


@monkey_patch(fields.Char)
def _transformation_title(self, value, args):
    return value.title() if value else value


@monkey_patch(fields.Char)
def _transformation_upper(self, value, args):
    return value.upper() if value else value
