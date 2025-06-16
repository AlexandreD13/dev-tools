from enum import Enum

from devtools.fakie.FakerDataType import FakerDataType


class FakerDataTypes:
    """
    Description...

    """

    # class Base(Enum):
    #     """
    #     Section: Faker.providers
    #
    #     """
    #
    #     BOTHIFY = FakerDataType(
    #         "bothify",
    #         "Generate a string with each placeholder in 'text' replaced according to the "
    #         "following rules:",
    #         [
    #             "Number signs ('#') are replaced with a random digit (0 to 9).",
    #             "Question marks ('?') are replaced with a random 'letter'.",
    #             "'Example:' Product Number: ????-########"
    #         ]
    #     )

    #     HEXIFY = FakerDataType(
    #         "hexify",
    #         "Generate a string with each circumflex ('^') in text replaced with a random "
    #         "hexadecimal character.",
    #         [
    #             "'Example:' MAC Address: ^^:^^:^^:^^:^^:^^"
    #         ]
    #     )

    #     LEXIFY = FakerDataType(
    #         "lexify",
    #         "Generate a string with each question mark ('?') in text replaced with a "
    #         "random 'letter'.",
    #         [
    #             "'Example:' Random Identifier: ??????????"
    #         ]
    #     )

    #     NUMERIFY = FakerDataType(
    #         "numerify",
    #         "Generate a string with each placeholder in text replaced according to the "
    #         "following rules:",
    #         [
    #             "Number signs ('#') are replaced with a random digit (0 to 9).",
    #             "Percent signs ('%') are replaced with a random non-zero digit (1 to 9).",
    #             "Dollar signs ('$') are replaced with a random digit above two (2 to 9).",
    #             "Exclamation marks ('!') are replaced with a random digit or an empty string.",
    #             "At symbols ('@') are replaced with a random non-zero digit or an empty string.",
    #             "'Example:' Intel Core i%-%%##K vs AMD Ryzen % %%##X"
    #
    #         ]
    #     )

    class Address(Enum):
        """
        Section: Faker.providers.address

        """

        ADDRESS = FakerDataType(
            "address",
            "Address",
            "Generates a complete random address, including the building number, street, "
            "city, state abbreviation, and postal code.",
            [
                "'Example:' 48764 Howard Forge Apt. 421\nVanessaside, VT 79393"
            ]
        )

        CITY = FakerDataType(
            "city",
            "City",
            "Generates a random city name. The generated names can be realistic but are "
            "typically fictional, combining common city name structures or suffixes.",
            [
                "'Example:' Sashabury"
            ]
        )

        COUNTRY = FakerDataType(
            "country",
            "Country",
            "Generates a random country name.",
            [
                "'Example:' Canada"
            ]
        )

        COUNTRY_CODE = FakerDataType(
            "country_code",
            "Country Code",
            "Generates a random country code.",
            [
                "'Example:' CA"
            ]
        )

        POSTCODE = FakerDataType(
            "postcode",
            "Postcode",
            "Generates a random postal code, formatted according to the locale of the "
            "Faker instance. In the U.S. it would generate a five-digit ZIP code.",
            [
                "'Example:' 50995"
            ]
        )

        STREET_ADDRESS = FakerDataType(
            "street_address",
            "Street Address",
            "Generates a random street address that includes the building number and the "
            "street name. The address may also contain details like apartment or suite "
            "numbers.",
            [
                "'Example:' 487 Hull Village Suite 759"
            ]
        )

        STREET_NAME = FakerDataType(
            "street_name",
            "Street Name",
            "Generates a random street name, which may include names of people, "
            "geographic features, or traditional street naming conventions like "
            "'Main' or 'Elm'.",
            [
                "'Example:' Sullivan Avenue"
            ]
        )

    class Automotive(Enum):
        """
        Section: Faker.providers.automotive

        """

        LICENSE_PLATE = FakerDataType(
            "license_plate",
            "License Plate",
            "Generates a random automotive license plate number. The format may vary "
            "depending on the locale, typically combining letters and numbers in "
            "different patterns. The output mimics real-world license plates, which may "
            "include separators such as dashes or spaces.",
            [
                "'Example:' 487-YNB"
            ]
        )

        VIN = FakerDataType(
            "vin",
            "VIN",
            "Generates a random 'Vehicle Identification Number' ('VIN'), a unique "
            "alphanumeric code used to identify individual motor vehicles. The generated "
            "'VIN' follows the standardized format and length typically used in the "
            "automotive industry.",
            [
                "'Example:' RT3GZYSKXXNDZ9J97"
            ]
        )

    class Color(Enum):
        """
        Section: Faker.providers.color

        """

        COLOR_HSL = FakerDataType(
            "color_hsl",
            "Color HSL",
            "Generates a random 'HSL' ('Hue', 'Saturation', 'Lightness') color "
            "represented as a tuple of three integers. The color values are in the "
            "range '0-255'.",
            [
                "'Example:' [197, 57, 32]"
            ]
        )

        COLOR_HSV = FakerDataType(
            "color_hsv",
            "Color HSV",
            "Generates a random 'HSV' ('Hue', 'Saturation', 'Value') color represented as "
            "a tuple of three integers. The color values are in the range '0-255'.",
            [
                "'Example:' [197, 57, 32]"
            ]
        )

        COLOR_NAME = FakerDataType(
            "color_name",
            "Color Name",
            "Generates a human-readable color name from a predefined set of color names. "
            "Similar to 'Html Named Colors'.",
            [
                "'Example:' OliveDrab"
            ]
        )

        COLOR_RGB = FakerDataType(
            "color_rgb",
            "Color RGB",
            "Generates a random 'RGB' ('Red', 'Green', 'Blue') color represented as a "
            "tuple of three integers. The color values are in the range '0-255'.",
            [
                "'Example:' [197, 57, 32]"
            ]
        )

        COLOR_HEX = FakerDataType(
            "hex_color",
            "Color HEX",
            "Generates a random color formatted as a hexadecimal triplet, used commonly "
            "in web development and graphic design. The output is a string representing "
            "the color in '#RRGGBB' format.",
            [
                "'Example:' #d82c08"
            ]
        )

    class Company(Enum):
        """
        Section: Faker.providers.company

        """

        COMPANY_CATCH_PHRASE = FakerDataType(
            "catch_phrase",
            "Catch Phrase",
            "Generates a random business catchphrase or slogan that mimics the kind of "
            "jargon-filled statements often used in corporate marketing or branding.",
            [
                "'Example:' Pre-emptive impactful toolset"
            ]
        )

        COMPANY_NAME = FakerDataType(
            "company",
            "Company Name",
            "Generates a random company name, typically formatted as a "
            "combination of surnames, business abbreviations (e.g., LLC, PLC), or "
            "fictional corporate structures.",
            [
                "'Example:' Chang-Fisher"
            ]
        )

    class CreditCard(Enum):
        """
        Section: Faker.providers.credit_card

        """

        CREDIT_CARD_EXPIRE = FakerDataType(
            "credit_card_expire",
            "Credit Card Expiry Date",
            "Generates a random credit card expiration date between now and the "
            "next 10 years.",
            [
                "'Example:' 04/33"
            ]
        )

        CREDIT_CARD_FULL = FakerDataType(
            "credit_card_full",
            "Credit Card Full Description",
            "Generates a full set of random credit card details, including the provider, "
            "cardholder name, card number, expiration date, and security code.",
            [
                "'Example:' Discover\nKatherine Fisher\n6587647593824218 12/30\nCVC: 489\n"
            ]
        )

        CREDIT_CARD_NUMBER = FakerDataType(
            "credit_card_number",
            "Credit Card Number",
            "Generates a valid random credit card number.",
            [
                "'Example:' 6504876475938248"
            ]
        )

        CREDIT_CARD_PROVIDER = FakerDataType(
            "credit_card_provider",
            "Credit Card Provider",
            "Generates the name of a random credit card provider.",
            [
                "'Example:' Visa"
            ]
        )

        CREDIT_CARD_SECURITY_CODE = FakerDataType(
            "credit_card_security_code",
            "Credit Card Security Code",
            "Generates a random credit card security code ('CVC'/'CVV'). The length and "
            "format of the code may depend on the card_type.",
            [
                "'Example:' 604"
            ]
        )

    class Currency(Enum):
        """
        Section: Faker.providers.currency
        """

        CRYPTOCURRENCY = FakerDataType(
            "cryptocurrency",
            "Cryptocurrency",
            "Generates a random cryptocurrency represented as a tuple of its code and name.",
            [
                "'Example:' [BTC, Bitcoin]"
            ]
        )

        CRYPTOCURRENCY_CODE = FakerDataType(
            "cryptocurrency_code",
            "Cryptocurrency Code",
            "Generates a random cryptocurrency code, which is typically a three or four-letter "
            "abbreviation.",
            [
                "'Example:' BTC"
            ]
        )

        CRYPTOCURRENCY_NAME = FakerDataType(
            "cryptocurrency_name",
            "Cryptocurrency Name",
            "Generates a random cryptocurrency name, providing the full name associated with "
            "a code.",
            [
                "'Example:' Bitcoin"
            ]
        )

        CURRENCY = FakerDataType(
            "currency",
            "Currency",
            "Generates a random currency as a tuple with the ISO code and the currency's full "
            "name.",
            [
                "'Example:' [USD, United States dollar]"
            ]
        )

        CURRENCY_CODE = FakerDataType(
            "currency_code",
            "Currency Code",
            "Generates a random currency code, typically a three-letter ISO code.",
            [
                "'Example:' USD"
            ]
        )

        CURRENCY_NAME = FakerDataType(
            "currency_name",
            "Currency Name",
            "Generates a random currency name, representing the full name of a country’s currency.",
            [
                "'Example:' United States dollar"
            ]
        )

        CURRENCY_SYMBOL = FakerDataType(
            "currency_symbol",
            "Currency Symbol",
            "Generates a random currency symbol. Optionally accepts a currency code to return "
            "its specific symbol.",
            [
                "'Example:' $"
            ]
        )

        PRICETAG = FakerDataType(
            "pricetag",
            "Pricetag",
            "Generates a random price tag, including a currency symbol and a random monetary "
            "value with two decimal points.",
            [
                "'Example:' $1,234.56"
            ]
        )

    class DateTime(Enum):
        """
        Section: Faker.providers.date_time

        """

        DATE = FakerDataType(
            "date",
            "Date",
            "Generates a random date as a string in 'YYYY-MM-DD' format. By default, generates "
            "dates between January 1, 1970, and today.",
            [
                "'Example:' 2016-04-26"
            ]
        )

        DATE_OF_BIRTH = FakerDataType(
            "date",
            "Date of Birth",
            "Generates a random date of birth, represented as a date object, within a specified "
            "age range. Defaults to between 0 and 115 years old.",
            [
                "'Example:' 1980-05-17"
            ]
        )

        DATE_TIME = FakerDataType(
            "date_time",
            "Datetime",
            "Generates a random datetime object between January 1, 1970, and the current date "
            "and time, with optional timezone support.",
            [
                "'Example:' Thu, 05 Sep 1991 05:26:59 GMT"
            ]
        )

        DATE_TIME_AD = FakerDataType(
            "date_time_ad",
            "Datetime AD",
            "Generates a random datetime in the Anno Domini (AD) era between January 1, year 1, "
            "and today, with optional timezone support.",
            [
                "'Example:' Tue, 05 Mar 0216 17:00:52 GMT"
            ]
        )

        DAY_OF_WEEK = FakerDataType(
            "day_of_week",
            "Day of the Week",
            "Generates a random day of the week, such as 'Monday' or 'Wednesday'.",
            [
                "'Example:' Monday"
            ]
        )

        FUTURE_DATE = FakerDataType(
            "future_date",
            "Future Date",
            "Generates a random future date as a string in 'YYYY-MM-DD' format.",
            [
                "'Example:' Thu, 15 May 2025 00:00:00 GMT"
            ]
        )

        FUTURE_DATETIME = FakerDataType(
            "future_datetime",
            "Future Datetime",
            "Generates a random future date and time as a datetime object, with optional timezone "
            "support.",
            [
                "'Example:' Sun, 18 May 2025 23:35:53 GMT"
            ]
        )

        MONTH_NAME = FakerDataType(
            "month_name",
            "Month Name",
            "Generates a random month name, such as 'January' or 'October'.",
            [
                "'Example:' July"
            ]
        )

        TIME = FakerDataType(
            "time",
            "Time",
            "Generates a random time as a string in 'HH:MM:SS' format, defaulting to 24-hour format.",
            [
                "'Example:' 18:45:00"
            ]
        )

        YEAR = FakerDataType(
            "year",
            "Year",
            "Generates a random year as a string, typically between 1970 and the current year.",
            [
                "'Example:' 1993"
            ]
        )

    # class Emoji(Enum):
    #     """
    #     Section: Faker.providers.emoji
    #
    #     """
    #
    #     EMOJI = FakerDataType(
    #         "emoji",
    #         "Generates a random emoji.",
    #         [
    #             "'Example:' "
    #         ]
    #     )

    class File(Enum):
        """
        Section: Faker.providers.file

        This enum contains types related to file data generation, including file extensions,
        file names, file paths, MIME types, Unix devices, and partitions. Each type provides
        utilities for generating realistic file-related data.
        """

        FILE_EXTENSION = FakerDataType(
            "file_extension",
            "File Extension",
            "Generates a random file extension from categories like 'audio', 'image', 'office', "
            "'text', or 'video'.",
            [
                "'Example:' txt"
            ]
        )

        FILE_NAME = FakerDataType(
            "file_name",
            "File Name",
            "Generates a random file name with an optional specified category or extension. If "
            "no extension is specified, it defaults to a random valid extension based on the "
            "category.",
            [
                "'Example:' photo.jpg"
            ]
        )

        FILE_PATH = FakerDataType(
            "file_path",
            "File Path",
            "Generates a random file path, with customizable directory depth, file system type "
            "('linux' or 'windows'), and category. By default, the path is absolute.",
            [
                "'Example:' /involve/piece.jpeg"
            ]
        )

        MIME_TYPE = FakerDataType(
            "mime_type",
            "MIME Type",
            "Generates a random MIME type, with options across categories like 'application', "
            "'audio', 'image', 'text', or 'video'.",
            [
                "'Example:' video/x-ms-wmv"
            ]
        )

        UNIX_DEVICE = FakerDataType(
            "unix_device",
            "Unix Device",
            "Generates a random Unix device file name, with optional prefix such as 'sd', 'vd', "
            "or 'xvd'.",
            [
                "'Example:' /dev/vdx"
            ]
        )

        UNIX_PARTITION = FakerDataType(
            "unix_partition",
            "Unix Partition",
            "Generates a random Unix partition name. It utilizes unix_device() under the hood "
            "and can specify a prefix like 'sd' or 'xvd'.",
            [
                "'Example:' /dev/xvdb9"
            ]
        )

    class Geo(Enum):
        """
        Section: Faker.providers.geo

        Provides methods to generate geographic data, including coordinates, latitudes, longitudes,
        and specific locations on land with timezone information.
        """

        COORDINATE = FakerDataType(
            "coordinate",
            "Coordinate",
            "Generates a random geographic coordinate, optionally centered around a specified "
            "point with a defined radius.",
            [
                "'Example:' -126.064879"
            ]
        )

        LATITUDE = FakerDataType(
            "latitude",
            "Latitude",
            "Generates a random latitude, ranging from -90 to 90 degrees.",
            [
                "'Example:' 76.9564165"
            ]
        )

        LATLNG = FakerDataType(
            "latlng",
            "Latitude - Longitude",
            "Generates a random pair of latitude and longitude coordinates as a tuple.",
            [
                "'Example:' [54.4551245, 93.656652]"
            ]
        )

        LOCAL_LATLNG = FakerDataType(
            "local_latlng",
            "Local Latitude - Longitude",
            "Generates a known location on land within a specified country (default is 'US'). "
            "Returns coordinates, place name, country code, and timezone.",
            [
                "'Example:' [45.53929, -122.38731, Troutdale, US, America/Los_Angeles]"
            ]
        )

        LOCATION_ON_LAND = FakerDataType(
            "location_on_land",
            "Location on Land",
            "Generates a random location that is guaranteed to be on land, including coordinates, "
            "place name, country code, and timezone. Optionally returns only coordinates.",
            [
                "'Example:' [31.82539, 72.54064, Sillanwali, PK, Asia/Karachi]"
            ]
        )

        LONGITUDE = FakerDataType(
            "longitude",
            "Longitude",
            "Generates a random longitude, ranging from -180 to 180 degrees.",
            [
                "'Example:' -11.058062"
            ]
        )

    class Internet(Enum):
        """
        Section: Faker.providers.internet
        Contains methods for generating common internet-related values like emails, domains,
        IP addresses, and other network-related identifiers.
        """

        EMAIL = FakerDataType(
            "email",
            "Email Address",
            "Generates a random email address in a standard format (username@domain). Commonly "
            "used for creating mock email addresses in tests.",
            [
                "'Example:' alice.smith@example.com"
            ]
        )

        DOMAIN_NAME = FakerDataType(
            "domain_name",
            "Domain Name",
            "Generates a random domain name with a typical structure (name.extension), often "
            "used for testing domain-based services.",
            [
                "'Example:' mycompany.com"
            ]
        )

        HOSTNAME = FakerDataType(
            "hostname",
            "Hostname",
            "Produces a random hostname, which can include a specified number of subdomain "
            "levels. Useful for simulating devices or server addresses.",
            [
                "'Example:' server-01.mycompany.com"
            ]
        )

        HTTP_METHOD = FakerDataType(
            "http_method",
            "HTTP Method",
            "Generates a random HTTP method (GET, POST, PUT, etc.), used to simulate HTTP "
            "requests in API testing.",
            [
                "'Example:' POST"
            ]
        )

        HTTP_STATUS_CODE = FakerDataType(
            "http_status_code",
            "HTTP Status Code",
            "Returns a random HTTP status code (200, 404, etc.), useful for testing response "
            "handling.",
            [
                "'Example:' 404"
            ]
        )

        IPV4 = FakerDataType(
            "ipv4",
            "IPv4",
            "Generates a random IPv4 address in standard dot-decimal notation, commonly used "
            "in network simulations.",
            [
                "'Example:' 182.150.227.232"
            ]
        )

        IPV6 = FakerDataType(
            "ipv6",
            "IPv6",
            "Produces a random IPv6 address in colon-separated hexadecimal format, for testing "
            "IPv6 configurations.",
            [
                "'Example:' 7e4f:99a:9ba1:9e24:7bf3:6124:169b:4197"
            ]
        )

        MAC_ADDRESS = FakerDataType(
            "mac_address",
            "MAC Address",
            "Returns a random MAC address in hexadecimal notation, used to identify network "
            "interfaces.",
            [
                "'Example:' 6c:0b:2c:b4:8f:2d"
            ]
        )

        PORT_NUMBER = FakerDataType(
            "port_number",
            "PORT Number",
            "Generates a random network port number (0-65535) for simulating service endpoints.",
            [
                "'Example:' 8080"
            ]
        )

        SLUG = FakerDataType(
            "slug",
            "Slug",
            "Produces a URL-friendly slug (typically lowercase with hyphens), often used for "
            "generating URLs or page identifiers.",
            [
                "'Example:' my-cool-blog-post"
            ]
        )

        URI = FakerDataType(
            "uri",
            "URI",
            "Generates a random URI path, used to simulate resource endpoints in testing.",
            [
                "'Example:' https://www.lowe.net/postshomepage.jsp"
            ]
        )

        URL = FakerDataType(
            "url",
            "URL",
            "Returns a complete random URL (scheme, domain, and path), useful for testing "
            "link generation or HTTP requests.",
            [
                "'Example:' https://www.clark-thomas.com/"
            ]
        )

        USER_NAME = FakerDataType(
            "user_name",
            "Username",
            "Generates a random username in various formats, often used for simulating login credentials.",
            [
                "'Example:' alice_smith123"
            ]
        )

    class Job(Enum):
        """
        Section: Faker.providers.job

        """

        JOB_TITLE = FakerDataType(
            "job",
            "Job Title",
            "Generates a random job title.",
            [
                "'Example:' Chartered public finance accountant"
            ]
        )

    class Lorem(Enum):
        """
        Section: Faker.providers.lorem

        """

        TEXT = FakerDataType(
            "text",
            "Random Text",
            "Generates random text.",
            [
                "'Example:' Choice note father consider. Onto hour vote blue rather factor.\nAgain reach American. Offer idea case hold total friend present reach."
            ]
        )

        PARAGRAPH = FakerDataType(
            "paragraph",
            "Random Paragraph",
            "Generates a random paragraph.",
            [
                "'Example:' Property class result force measure. Majority business smile power rate citizen response."
            ]
        )

        PARAGRAPHS = FakerDataType(
            "paragraphs",
            "Random Multiple Paragraphs",
            "Generates random paragraphs.",
            [
                "'Example:' [Mission determine her effort so television none. Themselves drive west low nearly certain company., Ball child often key various available single. Investment decision its., Interesting exist our step ball. Media could value prevent lawyer it.]"
            ]
        )

        SENTENCE = FakerDataType(
            "sentence",
            "Random Sentence",
            "Generates a random sentence.",
            [
                "'Example:' Clear create form difficult."
            ]
        )

        SENTENCES = FakerDataType(
            "sentences",
            "Random Multiple Sentences",
            "Generates random sentences.",
            [
                "'Example:' [Seek green idea happy herself fly., Forward mother cup have week too who., Recent what seat country mean democratic.]"
            ]
        )

        TEXTS = FakerDataType(
            "texts",
            "Random Multiple Texts",
            "Generates random texts.",
            [
                "'Example:' [Them attorney each pattern huge third film. Nearly with teacher tell kitchen professional., Camera traditional special tough.\nFederal six similar head against agency. Be up see environment particularly guess before., Participant early sister generation support drop. Student quite recently rule sell position people rise.\nOpportunity easy product. Likely conference will floor. Safe situation threat budget.]"
            ]
        )

        WORD = FakerDataType(
            "word",
            "Random Word",
            "Generates a random word.",
            [
                "'Example:' total"
            ]
        )

        WORDS = FakerDataType(
            "words",
            "Random Multiple Words",
            "Generates random words.",
            [
                "'Example:' [future, smile, soon]"
            ]
        )

    class Misc(Enum):
        """
        Section: Faker.providers.misc

        """

        BINARY = FakerDataType(
            "binary",
            "Binary",
            "Generates a random binary value.",
            [
                "'Example:' "
            ]
        )

        BOOLEAN = FakerDataType(
            "boolean",
            "Boolean",
            "Generates a random boolean value.",
            [
                "'Example:' "
            ]
        )

        CSV = FakerDataType(
            "csv",
            "CSV String",
            "Generates a random CSV string.",
            [
                "'Example:' "
            ]
        )

        FIXED_WIDTH = FakerDataType(
            "fixed_width",
            "Fixed Width String",
            "Generates a random fixed width string.",
            [
                "'Example:' "
            ]
        )

        IMAGE = FakerDataType(
            "image",
            "Random Image",
            "Generates a random image.",
            [
                "'Example:' "
            ]
        )

        JSON = FakerDataType(
            "json",
            "JSON String",
            "Generates a random JSON string.",
            [
                "'Example:' "
            ]
        )

        JSON_BYTES = FakerDataType(
            "json_bytes",
            "JSON Bytes",
            "Generates random JSON bytes.",
            [
                "'Example:' "
            ]
        )

        MD5 = FakerDataType(
            "md5",
            "Md5 Hash",
            "Generates a random MD5 hash.",
            [
                "'Example:' "
            ]
        )

        PASSWORD = FakerDataType(
            "password",
            "Random Password",
            "Generates a random password.",
            [
                "'Example:' "
            ]
        )

        SHA1 = FakerDataType(
            "sha1",
            "Sha1 Hash",
            "Generates a random SHA1 hash.",
            [
                "'Example:' "
            ]
        )

        SHA256 = FakerDataType(
            "sha256",
            "Sha256 Hash",
            "Generates a random SHA256 hash.",
            [
                "'Example:' "
            ]
        )

        UUID4 = FakerDataType(
            "uuid4",
            "Random UUID4",
            "Generates a random UUID4.",
            [
                "'Example:' "
            ]
        )

        XML = FakerDataType(
            "xml",
            "XML String",
            "Generates a random XML string.",
            [
                "'Example:' "
            ]
        )

    class Person(Enum):
        """
        Section: Faker.providers.person

        """

        FIRST_NAME = FakerDataType(
            "first_name",
            "First Name",
            "Generates a random first name.",
            [
                "'Example:' "
            ]
        )

        LAST_NAME = FakerDataType(
            "last_name",
            "Last Name",
            "Generates a random last name.",
            [
                "'Example:' "
            ]
        )

        FIRST_NAME_FEMALE = FakerDataType(
            "first_name_female",
            "Female First Name",
            "Generates a random female first name.",
            [
                "'Example:' "
            ]
        )

        FIRST_NAME_MALE = FakerDataType(
            "first_name_male",
            "Male First Name",
            "Generates a random male first name.",
            [
                "'Example:' "
            ]
        )

        LANGUAGE_NAME = FakerDataType(
            "language_name",
            "Language Name",
            "Generates a random language name.",
            [
                "'Example:' "
            ]
        )

        LAST_NAME_FEMALE = FakerDataType(
            "last_name_female",
            "Female Last Name",
            "Generates a random female last name.",
            [
                "'Example:' "
            ]
        )

        LAST_NAME_MALE = FakerDataType(
            "last_name_male",
            "Male Last Name",
            "Generates a random male last name.",
            [
                "'Example:' "
            ]
        )

        NAME = FakerDataType(
            "name",
            "Full Name",
            "Generates a random full name.",
            [
                "'Example:' "
            ]
        )

        NAME_FEMALE = FakerDataType(
            "name_female",
            "Female Full Name",
            "Generates a random female full name.",
            [
                "'Example:' "
            ]
        )

        NAME_MALE = FakerDataType(
            "name_male",
            "Male Full Name",
            "Generates a random male full name.",
            [
                "'Example:' "
            ]
        )

        PREFIX = FakerDataType(
            "prefix",
            "Name Prefix",
            "Generates a random name prefix.",
            [
                "'Example:' "
            ]
        )

        PREFIX_FEMALE = FakerDataType(
            "prefix_female",
            "Female Name Prefix",
            "Generates a random female name prefix.",
            [
                "'Example:' "
            ]
        )

        PREFIX_MALE = FakerDataType(
            "prefix_male",
            "Male Name Prefix",
            "Generates a random male name prefix.",
            [
                "'Example:' "
            ]
        )

        SUFFIX = FakerDataType(
            "suffix",
            "Name Suffix",
            "Generates a random name suffix.",
            [
                "'Example:' "
            ]
        )

        SUFFIX_FEMALE = FakerDataType(
            "suffix_female",
            "Female Name Suffix",
            "Generates a random female name suffix.",
            [
                "'Example:' "
            ]
        )

        SUFFIX_MALE = FakerDataType(
            "suffix_male",
            "Male Name Suffix",
            "Generates a random male name suffix.",
            [
                "'Example:' "
            ]
        )

    class Profile(Enum):
        """
        Section: Faker.providers.profile

        """

        PROFILE = FakerDataType(
            "profile",
            "Random Profile",
            "Generates a random profile.",
            [
                "'Example:' "
            ]
        )

        SIMPLE_PROFILE = FakerDataType(
            "simple_profile",
            "Random Simplified Profile",
            "Generates a simple random profile.",
            [
                "'Example:' "
            ]
        )

    class UserAgent(Enum):
        """
        Section: Faker.providers.user_agent

        """

        ANDROID_PLATFORM_TOKEN = FakerDataType(
            "android_platform_token",
            "Android Platform Token",
            "Generates a random user agent for Android devices.",
            [
                "'Example:' "
            ]
        )

        CHROME = FakerDataType(
            "chrome",
            "Chrome User Agent",
            "Generates a random user agent for Chrome browser.",
            [
                "'Example:' "
            ]
        )

        FIREFOX = FakerDataType(
            "firefox",
            "Firefox User Agent",
            "Generates a random user agent for Firefox browser.",
            [
                "'Example:' "
            ]
        )

        INTERNET_EXPLORER = FakerDataType(
            "internet_explorer",
            "Explorer User Agent",
            "Generates a random user agent for Internet Explorer.",
            [
                "'Example:' "
            ]
        )

        IOS_PLATFORM_TOKEN = FakerDataType(
            "ios_platform_token",
            "iOS Platform Token",
            "Generates a random user agent for iOS devices.",
            [
                "'Example:' "
            ]
        )

        LINUX_PLATFORM_TOKEN = FakerDataType(
            "linux_platform_token",
            "Linux PLatform Token",
            "Generates a random user agent for Linux platforms.",
            [
                "'Example:' "
            ]
        )

        MAC_PLATFORM_TOKEN = FakerDataType(
            "mac_platform_token",
            "Mac Platform Token",
            "Generates a random user agent for Mac platforms.",
            [
                "'Example:' "
            ]
        )

        OPERA = FakerDataType(
            "opera",
            "Opera User Agent",
            "Generates a random user agent for Opera browser.",
            [
                "'Example:' "
            ]
        )

        SAFARI = FakerDataType(
            "safari",
            "Safari User Agent",
            "Generates a random user agent for Safari browser.",
            [
                "'Example:' "
            ]
        )

        USER_AGENT = FakerDataType(
            "user_agent",
            "User Agent",
            "Generates a random user agent string.",
            [
                "'Example:' "
            ]
        )

        WINDOWS_PLATFORM_TOKEN = FakerDataType(
            "windows_platform_token",
            "Windows Platform Token",
            "Generates a random user agent for Windows platforms.",
            [
                "'Example:' "
            ]
        )