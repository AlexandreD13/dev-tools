from enum import Enum

from devtools.fakie.FakerDataType import FakerDataType


class CustomDataTypes:
    """
    Description...

    """

    class Personal(Enum):
        """
        Section: Custom.providers

        """

        PHONE_NUMBER = FakerDataType(
            "phone_number",
            "Phone Number",
            "Generates a random phone number.",
            [
                "\"Example:\" (514)-345-2159"
            ]
        )