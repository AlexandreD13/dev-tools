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
    group.add_argument("--cmykToRgb", type=str, help="Conversion from CMYK to RGB.")
    group.add_argument("--hexToRgb", type=str, help="Conversion from HEX to RGB.")
    group.add_argument("--hslToRgb", type=str, help="Conversion from HSL to RGB.")
    group.add_argument("--hsvToRgb", type=str, help="Conversion from HSV to RGB.")
    group.add_argument("--rgbToCmyk", type=str, help="Conversion from RGB to CMYK.")
    group.add_argument("--rgbToHex", type=str, help="Conversion from RGB to HEX.")
    group.add_argument("--rgbToHsl", type=str, help="Conversion from RGB to HSL.")
    group.add_argument("--rgbToHsv", type=str, help="Conversion from RGB to HSV.")

    parser.set_defaults(func=run)


def run(args):
    if args.cmykToRgb:
        getCmykToRGB(args.cmykToRgb)
    if args.hexToRgb:
        getHexToRgb(args.hexToRgb)
    if args.hslToRgb:
        getHslToRgb(args.hslToRgb)
    if args.hsvToRgb:
        getHsvToRgb(args.hsvToRgb)


def getCmykToRGB(cmykColor):
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

    c = float(cmykColor[match.regs[1][0]:match.regs[1][1]]) / 100
    m = float(cmykColor[match.regs[2][0]:match.regs[2][1]]) / 100
    y = float(cmykColor[match.regs[3][0]:match.regs[3][1]]) / 100
    k = float(cmykColor[match.regs[4][0]:match.regs[4][1]]) / 100

    r = round(255 * (1 - c) * (1 - k))
    g = round(255 * (1 - m) * (1 - k))
    b = round(255 * (1 - y) * (1 - k))

    print(
        f"\nConversion from CMYK to RGB:\n{Fore.BLUE}{Style.BRIGHT}{cmykColor} -> rgb({r}, {g}, {b}){Style.RESET_ALL}")


def getHexToRgb(hexColor):
    match = re.match(
        r"^#([0-9a-fA-F]{3}){1,2}$",
        hexColor.strip().lower()
    )

    if not match:
        raise ValueError("Invalid HEX format. Use '#FFFFFF' format.")

    r = int(hexColor[1:3], 16)
    g = int(hexColor[3:5], 16)
    b = int(hexColor[5:7], 16)

    print(f"\nConversion from HEX to RGB:\n{Fore.BLUE}{Style.BRIGHT}{hexColor} -> rgb({r}, {g}, {b}){Style.RESET_ALL}")


def getHslToRgb(hslColor):
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

    h = int(hslColor[match.regs[1][0]:match.regs[1][1]])
    s = float(hslColor[match.regs[2][0]:match.regs[2][1]]) / 100
    l = float(hslColor[match.regs[3][0]:match.regs[3][1]]) / 100

    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    r_prime, g_prime, b_prime = 0, 0, 0
    if 0 <= h < 60:
        r_prime, g_prime, b_prime = c, x, 0
    if 60 <= h < 120:
        r_prime, g_prime, b_prime = x, c, 0
    if 120 <= h < 180:
        r_prime, g_prime, b_prime = 0, c, x
    if 180 <= h < 240:
        r_prime, g_prime, b_prime = 0, x, c
    if 240 <= h < 300:
        r_prime, g_prime, b_prime = x, 0, c
    if 300 <= h < 360:
        r_prime, g_prime, b_prime = c, 0, x

    r = round((r_prime + m) * 255)
    g = round((g_prime + m) * 255)
    b = round((b_prime + m) * 255)

    print(f"\nConversion from HSL to RGB:\n{Fore.BLUE}{Style.BRIGHT}{hslColor} -> rgb({r}, {g}, {b}){Style.RESET_ALL}")


def getHsvToRgb(hsvColor):
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

    h = int(hsvColor[match.regs[1][0]:match.regs[1][1]])
    s = float(hsvColor[match.regs[2][0]:match.regs[2][1]]) / 100
    v = float(hsvColor[match.regs[3][0]:match.regs[3][1]]) / 100

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    r_prime, g_prime, b_prime = 0, 0, 0
    if 0 <= h < 60:
        r_prime, g_prime, b_prime = c, x, 0
    if 60 <= h < 120:
        r_prime, g_prime, b_prime = x, c, 0
    if 120 <= h < 180:
        r_prime, g_prime, b_prime = 0, c, x
    if 180 <= h < 240:
        r_prime, g_prime, b_prime = 0, x, c
    if 240 <= h < 300:
        r_prime, g_prime, b_prime = x, 0, c
    if 300 <= h < 360:
        r_prime, g_prime, b_prime = c, 0, x

    r = round((r_prime + m) * 255)
    g = round((g_prime + m) * 255)
    b = round((b_prime + m) * 255)

    print(f"\nConversion from HSV to RGB:\n{Fore.BLUE}{Style.BRIGHT}{hsvColor} -> rgb({r}, {g}, {b}){Style.RESET_ALL}")
