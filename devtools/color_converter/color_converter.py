from colorama import Fore, Style

import argparse
import re


def register(subparsers):
    parser = subparsers.add_parser(
        "color_converter",
        help="Convert between different color formats.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show the 'color_converter' tool usage guide."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--cmykRgb", type=str, metavar="COLOR", help="Conversion from CMYK to RGB. Format: cmyk(c, m, y, k)")
    group.add_argument("--hexRgb", metavar="COLOR", type=str, help="Conversion from HEX to RGB. Format: hex(#AABBCC)")
    group.add_argument("--hslRgb", metavar="COLOR", type=str, help="Conversion from HSL to RGB. Format: hsl(h, s, l)")
    group.add_argument("--hsvRgb", metavar="COLOR", type=str, help="Conversion from HSV to RGB. Format: hsv(h, s, v)")
    group.add_argument("--rgbCmyk", metavar="COLOR", type=str, help="Conversion from RGB to CMYK. Format: rgb(r, g, b)")
    group.add_argument("--rgbHex", metavar="COLOR", type=str, help="Conversion from RGB to HEX. Format: rgb(r, g, b)")
    group.add_argument("--rgbHsl", metavar="COLOR", type=str, help="Conversion from RGB to HSL. Format: rgb(r, g, b)")
    group.add_argument("--rgbHsv", metavar="COLOR", type=str, help="Conversion from RGB to HSV. Format: rgb(r, g, b)")

    parser.set_defaults(func=run)


def run(args):
    dispatch = {
        "cmykRgb": getCmykToRGB,
        "hexRgb":  getHexToRgb,
        "hslRgb":  getHslToRgb,
        "hsvRgb":  getHsvToRgb,
        "rgbCmyk": getRgbToCmyk,
        "rgbHex":  getRgbToHex,
        "rgbHsl":  getRgbToHsl,
        "rgbHsv":  getRgbToHsv,
    }

    for flag, func in dispatch.items():
        value = getattr(args, flag)
        if value is not None:
            func(value)
            break


def getCmykToRGB(cmykColor):
    match = validate_cmyk(cmykColor)

    cyan = float(cmykColor[match.regs[1][0]:match.regs[1][1]]) / 100
    magenta = float(cmykColor[match.regs[2][0]:match.regs[2][1]]) / 100
    yellow = float(cmykColor[match.regs[3][0]:match.regs[3][1]]) / 100
    black = float(cmykColor[match.regs[4][0]:match.regs[4][1]]) / 100

    red = round(255 * (1 - cyan) * (1 - black))
    green = round(255 * (1 - magenta) * (1 - black))
    blue = round(255 * (1 - yellow) * (1 - black))

    print(
        f"\nConversion from CMYK to RGB:\n{Fore.BLUE}{Style.BRIGHT}{cmykColor} -> rgb({red}, {green}, {blue}){Style.RESET_ALL}")


def getHexToRgb(hexColor):
    validate_hex(hexColor)

    red = int(hexColor[1:3], 16)
    green = int(hexColor[3:5], 16)
    blue = int(hexColor[5:7], 16)

    print(f"\nConversion from HEX to RGB:\n{Fore.BLUE}{Style.BRIGHT}{hexColor} -> rgb({red}, {green}, {blue}){Style.RESET_ALL}")


def getHslToRgb(hslColor):
    match = validate_hsl(hslColor)

    hue = int(hslColor[match.regs[1][0]:match.regs[1][1]])
    saturation = float(hslColor[match.regs[2][0]:match.regs[2][1]]) / 100
    lightness = float(hslColor[match.regs[3][0]:match.regs[3][1]]) / 100

    chroma = (1 - abs(2 * lightness - 1)) * saturation
    x = chroma * (1 - abs((hue / 60) % 2 - 1))
    match = lightness - chroma / 2

    red_prime, green_prime, blue_prime = 0, 0, 0
    if 0 <= hue < 60:
        red_prime, green_prime, blue_prime = chroma, x, 0
    if 60 <= hue < 120:
        red_prime, green_prime, blue_prime = x, chroma, 0
    if 120 <= hue < 180:
        red_prime, green_prime, blue_prime = 0, chroma, x
    if 180 <= hue < 240:
        red_prime, green_prime, blue_prime = 0, x, chroma
    if 240 <= hue < 300:
        red_prime, green_prime, blue_prime = x, 0, chroma
    if 300 <= hue < 360:
        red_prime, green_prime, blue_prime = chroma, 0, x

    red = round((red_prime + match) * 255)
    green = round((green_prime + match) * 255)
    blue = round((blue_prime + match) * 255)

    print(f"\nConversion from HSL to RGB:\n{Fore.BLUE}{Style.BRIGHT}{hslColor} -> rgb({red}, {green}, {blue}){Style.RESET_ALL}")


def getHsvToRgb(hsvColor):
    match = validate_hsv(hsvColor)

    hue = int(hsvColor[match.regs[1][0]:match.regs[1][1]])
    saturation = float(hsvColor[match.regs[2][0]:match.regs[2][1]]) / 100
    value = float(hsvColor[match.regs[3][0]:match.regs[3][1]]) / 100

    chroma = value * saturation
    x = chroma * (1 - abs((hue / 60) % 2 - 1))
    match = value - chroma

    red_prime, green_prime, blue_prime = 0, 0, 0
    if 0 <= hue < 60:
        red_prime, green_prime, blue_prime = chroma, x, 0
    if 60 <= hue < 120:
        red_prime, green_prime, blue_prime = x, chroma, 0
    if 120 <= hue < 180:
        red_prime, green_prime, blue_prime = 0, chroma, x
    if 180 <= hue < 240:
        red_prime, green_prime, blue_prime = 0, x, chroma
    if 240 <= hue < 300:
        red_prime, green_prime, blue_prime = x, 0, chroma
    if 300 <= hue < 360:
        red_prime, green_prime, blue_prime = chroma, 0, x

    red = round((red_prime + match) * 255)
    green = round((green_prime + match) * 255)
    blue = round((blue_prime + match) * 255)

    print(f"\nConversion from HSV to RGB:\n{Fore.BLUE}{Style.BRIGHT}{hsvColor} -> rgb({red}, {green}, {blue}){Style.RESET_ALL}")


def getRgbToCmyk(rgbColor):
    match = validate_rgb(rgbColor)
    red, green, blue = parseRGB(rgbColor, match)

    red_prime, green_prime, blue_prime = red / 255, green / 255, blue / 255

    black = 1 - max(red_prime, green_prime, blue_prime)
    cyan = (1 - red_prime - black) / (1 - black)
    magenta = (1 - green_prime - black) / (1 - black)
    yellow = (1 - blue_prime - black) / (1 - black)

    black = int(round(black, 2) * 100)
    cyan = int(round(cyan, 2) * 100)
    magenta = int(round(magenta, 2) * 100)
    yellow = int(round(yellow, 2) * 100)

    print(f"\nConversion from RGB to CMYK:\n{Fore.BLUE}{Style.BRIGHT}{rgbColor} -> cmyk({cyan}, {magenta}, {yellow}, {black}){Style.RESET_ALL}")


def getRgbToHex(rgbColor):
    match = validate_rgb(rgbColor)
    red, green, blue = parseRGB(rgbColor, match)

    red_hex = f"{red:02x}"
    green_hex = f"{green:02x}"
    blue_hex = f"{blue:02x}"

    print(
        f"\nConversion from RGB to HEX:\n{Fore.BLUE}{Style.BRIGHT}{rgbColor} -> hex(#{red_hex}{green_hex}{blue_hex}){Style.RESET_ALL}")


def getRgbToHsl(rgbColor):
    match = validate_rgb(rgbColor)
    red, green, blue = parseRGB(rgbColor, match)

    red_prime, green_prime, blue_prime = red / 255, green / 255, blue / 255

    c_max = max(red_prime, green_prime, blue_prime)
    c_min = min(red_prime, green_prime, blue_prime)
    delta = c_max - c_min

    lightness = (c_max + c_min) / 2

    if delta == 0:
        hue = 0
        saturation = 0
    else:
        if c_max == red_prime:
            hue = 60 * (((green_prime - blue_prime) / delta) % 6)
        if c_max == green_prime:
            hue = 60 * (((blue_prime - red_prime) / delta) + 2)
        if c_max == blue_prime:
            hue = 60 * (((red_prime - green_prime) / delta) + 4)

        saturation = delta / (1 - abs(2 * lightness - 1))

    hue = int(round(hue))
    saturation = int(round(saturation * 100))
    lightness = int(round(lightness * 100))

    print(
        f"\nConversion from RGB to HSL:\n{Fore.BLUE}{Style.BRIGHT}{rgbColor} -> hsl({hue}°, {saturation}%, {lightness}%){Style.RESET_ALL}")


def getRgbToHsv(rgbColor):
    match = validate_rgb(rgbColor)
    red, green, blue = parseRGB(rgbColor, match)

    red_prime, green_prime, blue_prime = red / 255, green / 255, blue / 255

    c_max = max(red_prime, green_prime, blue_prime)
    c_min = min(red_prime, green_prime, blue_prime)
    delta = c_max - c_min

    if delta == 0:
        hue = 0
    if c_max == red_prime:
        hue = 60 * (((green_prime - blue_prime) / delta) % 6)
    if c_max == green_prime:
        hue = 60 * (((blue_prime - red_prime) / delta) + 2)
    if c_max == blue_prime:
        hue = 60 * (((red_prime - green_prime) / delta) + 4)

    if c_max == 0:
        saturation = 0
    else:
        saturation = delta / c_max

    hue = int(round(hue))
    saturation = int(round(saturation * 100))
    value = int(round(c_max * 100))

    print(
        f"\nConversion from RGB to HSV:\n{Fore.BLUE}{Style.BRIGHT}{rgbColor} -> hsv({hue}°, {saturation}%, {value}%){Style.RESET_ALL}")


def validate_cmyk(cmykColor):
    match = re.match(
        r"cmyk\("
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*"
        r"\)",
        cmykColor.strip().lower()
    )

    if not match:
        raise ValueError("Invalid CMYK format. Use cmyk(c, m, y, k) between 0-100.")

    return match


def validate_hex(hexColor):
    match = re.match(
        r"^#([0-9a-fA-F]{3}){1,2}$",
        hexColor.strip().lower()
    )
    if not match:
        raise ValueError("Invalid HEX format. Use '#FFFFFF' format.")


def validate_hsl(hslColor):
    match = re.match(
        r"hsl\("
        r"\s*(360|[1-9]?\d)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*"
        r"\)",
        hslColor.strip().lower()
    )
    if not match:
        raise ValueError(
            "Invalid HSL format. Use hsl(h, s, l) with 'h' between 0-360, 's' between 0-100 and 'l' between 0-100.")
    return match


def validate_hsv(hsvColor):
    match = re.match(
        r"hsv\("
        r"\s*(360|[1-9]?\d)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*,"
        r"\s*(100(?:\.0+)?|[1-9]?\d(?:\.\d+)?|0(?:\.0+)?)\s*"
        r"\)",
        hsvColor.strip().lower()
    )
    if not match:
        raise ValueError(
            "Invalid HSV format. Use hsv(h, s, v) with 'h' between 0-360, 's' between 0-100 and 'v' between 0-100.")
    return match


def validate_rgb(rgbColor):
    match = re.match(
        r"rgb\("
        r"\s*(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\s*,"
        r"\s*(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\s*,"
        r"\s*(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\s*"
        r"\)",
        rgbColor.strip().lower()
    )

    if not match:
        raise ValueError(
            "Invalid RGB format. Use rgb(r, g, b) with 'r' between 0-255, 'g' between 0-255 and 'b' between 0-255.")

    return match


def parseRGB(rgbColor, match):
    red = int(rgbColor[match.regs[1][0]:match.regs[1][1]])
    green = int(rgbColor[match.regs[2][0]:match.regs[2][1]])
    blue = int(rgbColor[match.regs[3][0]:match.regs[3][1]])

    return red, green, blue
