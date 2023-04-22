from odoo.tests import common


LOREM_IPSUM = "Lorem ipsum DOLOR sit\tamet, consectetur adipiscing elit. 1000!@"


class TestFieldTransportation(common.TransactionCase):

    def test_transformation(self):
        record = self.env['field.transformation.test'].create({
            "no_change": LOREM_IPSUM,
            "upper_on_write": LOREM_IPSUM,
            "lower_on_read": LOREM_IPSUM,
            "capitalize_on_read": LOREM_IPSUM,
        })
        self.assertEqual(record.no_change, LOREM_IPSUM)
        self.assertEqual(
            record.upper_on_write,
            "LOREM IPSUM DOLOR SIT\tAMET, CONSECTETUR ADIPISCING ELIT. 1000!@"
        )
        self.assertEqual(
            record.lower_on_read,
            "lorem ipsum dolor sit\tamet, consectetur adipiscing elit. 1000!@"
        )
        self.assertEqual(
            record.capitalize_on_read,
            "Lorem ipsum dolor sit\tamet, consectetur adipiscing elit. 1000!@"
        )
