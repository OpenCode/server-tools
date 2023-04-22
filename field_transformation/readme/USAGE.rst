User parameter `transformations_on` with value `read` or `write` to indicate when you want the data transformation to take place.
Define the transformations you need and any parameters:

* **capitalize**: `True`
* **expandtabs**: `True` or number of spaces
* **lower**: `True`
* **lstrip**: `True` or string with chars to remove
* **removeprefix:** String to remove
* **removesuffix**: String to remove
* **rstrip**: `True` or string with chars to remove
* **strip**: `True` or string with chars to remove
* **swapcase**: `True`
* **title**: `True`
* **upper**: `True`


.. code-block:: python

    class MyModel(models.Model):

        _name = 'my.model'

        # Result:
        #   name:
        #       "    jack joHN smiTh  "
        #       "Jack John Smith"

        name = fields.Char(
            transformations={
                "strip": True,
                "title": True,
            },
            transformations_on = "write",
        )

        # Result:
        #   email:
        #       "TEST@TEST.COM"
        #       "test@test.com"

        email = fields.Char(
            transformations={
                "lower": True,
            },
            transformations_on = "write",
        )

        # Result:
        #   lang_codes:
        #       " en\tUS "
        #       "en  US"

        lang_codes = fields.Char(
            transformations={
                "upper": True,
                "strip": True,
                "expandtabs": 2,
            },
            transformations_on = "write",
        )

        # Result:
        #   lang_codes:
        #       "IT12345678900"
        #       "12345678900"

        vat = fields.Char(
            transformations={
                "removeprefix": "IT",
            },
            transformations_on = "read",
        )
