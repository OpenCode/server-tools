# Copyright 2023 Apruzzese Francesco <cescoap@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FieldTransformationTest(models.Model):

    _name = 'field.transformation.test'
    _description = "Utility to test base module"

    no_change = fields.Char()

    upper_on_write = fields.Char(
        transformations={"upper": True},
        transformations_on = "write",
    )

    lower_on_read = fields.Char(
        transformations={"lower": True},
        transformations_on = "read",
    )

    capitalize_on_read = fields.Char(
        transformations={"capitalize": True},
        transformations_on = "read",
    )
