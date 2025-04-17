from colorama import Fore, Style

import argparse
import difflib

explanations = {
    100: "Continue: The server has received the request headers and the client should proceed to send the request body.",
    101: "Switching Protocols: The requester has asked the server to switch protocols and the server has agreed to do so.",
    102: "Processing (WebDAV): The server has received and is processing the request, but no response is available yet.",
    103: "Early Hints: Primarily intended to be used with the Link header to allow the user agent to start preloading resources while the server prepares a response.",

    200: "OK: The request has succeeded.",
    201: "Created: The request has been fulfilled, resulting in the creation of a new resource.",
    202: "Accepted: The request has been received but not yet acted upon.",
    203: "Non-Authoritative Information: The server successfully processed the request, but is returning information that may be from another source.",
    204: "No Content: The server successfully processed the request and is not returning any content.",
    205: "Reset Content: The server successfully processed the request and asks the client to reset its document view.",
    206: "Partial Content: The server is delivering only part of the resource due to a range header sent by the client.",
    207: "Multi-Status (WebDAV): The message body that follows is by default an XML message and can contain a number of separate response codes.",
    208: "Already Reported (WebDAV): The members of a DAV binding have already been enumerated in a previous reply to this request and are not being included again.",
    226: "IM Used: The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.",

    300: "Multiple Choices: There are multiple options for the resource that the client may follow.",
    301: "Moved Permanently: This and all future requests should be directed to the given URI.",
    302: "Found: The URI of the requested resource has been changed temporarily.",
    303: "See Other: The response can be found under another URI using a GET method.",
    304: "Not Modified: Indicates that the resource has not been modified since the version specified by the request headers.",
    305: "Use Proxy: The requested resource is available only through a proxy, the address for which is provided in the response.",
    306: "(Unused): This status code is no longer used, but is reserved for future use.",
    307: "Temporary Redirect: The request should be repeated with another URI, but future requests should still use the original URI.",
    308: "Permanent Redirect: The request and all future requests should be repeated using another URI.",

    400: "Bad Request: The server could not understand the request due to invalid syntax.",
    401: "Unauthorized: The client must authenticate itself to get the requested response.",
    402: "Payment Required: Reserved for future use.",
    403: "Forbidden: The client does not have access rights to the content.",
    404: "Not Found: The server cannot find the requested resource.",
    405: "Method Not Allowed: The request method is known by the server but has been disabled and cannot be used.",
    406: "Not Acceptable: The server cannot produce a response matching the list of acceptable values defined in the request's headers.",
    407: "Proxy Authentication Required: The client must first authenticate itself with the proxy.",
    408: "Request Timeout: The server would like to shut down this unused connection.",
    409: "Conflict: The request conflicts with the current state of the server.",
    410: "Gone: The requested resource is no longer available and will not be available again.",
    411: "Length Required: The server refuses to accept the request without a defined Content-Length header.",
    412: "Precondition Failed: A condition provided in the request header fields evaluated to false.",
    413: "Payload Too Large: The request entity is larger than limits defined by the server.",
    414: "URI Too Long: The URI requested by the client is longer than the server is willing to interpret.",
    415: "Unsupported Media Type: The media format of the requested data is not supported by the server.",
    416: "Range Not Satisfiable: The range specified by the Range header cannot be fulfilled.",
    417: "Expectation Failed: The expectation given in the request's Expect header could not be met.",
    418: "I'm a teapot: The server refuses to brew coffee because it is, permanently, a teapot.",
    421: "Misdirected Request: The request was directed at a server that is not able to produce a response.",
    422: "Unprocessable Entity (WebDAV): The request was well-formed but was unable to be followed due to semantic errors.",
    423: "Locked (WebDAV): The resource that is being accessed is locked.",
    424: "Failed Dependency (WebDAV): The request failed because it depended on another request and that request failed.",
    425: "Too Early: Indicates that the server is unwilling to risk processing a request that might be replayed.",
    426: "Upgrade Required: The server refuses to perform the request using the current protocol but might be willing to after the client upgrades.",
    428: "Precondition Required: The origin server requires the request to be conditional.",
    429: "Too Many Requests: The user has sent too many requests in a given amount of time (rate limiting).",
    431: "Request Header Fields Too Large: The server is unwilling to process the request because its header fields are too large.",
    451: "Unavailable For Legal Reasons: The client requests a resource that is unavailable for legal reasons.",

    500: "Internal Server Error: The server has encountered a situation it doesn't know how to handle.",
    501: "Not Implemented: The server does not support the functionality required to fulfill the request.",
    502: "Bad Gateway: The server, while acting as a gateway or proxy, received an invalid response from the upstream server.",
    503: "Service Unavailable: The server is not ready to handle the request, e.g., is overloaded or down for maintenance.",
    504: "Gateway Timeout: The server is acting as a gateway and cannot get a response in time.",
    505: "HTTP Version Not Supported: The HTTP version used in the request is not supported by the server.",
    506: "Variant Also Negotiates: The server has an internal configuration error where the chosen variant resource is configured to engage in transparent content negotiation itself.",
    507: "Insufficient Storage (WebDAV): The server is unable to store the representation needed to complete the request.",
    508: "Loop Detected (WebDAV): The server detected an infinite loop while processing a request with Depth: infinity.",
    510: "Not Extended: Further extensions to the request are required for the server to fulfill it.",
    511: "Network Authentication Required: The client needs to authenticate to gain network access.",
}


def register(subparsers):
    parser = subparsers.add_parser(
        "http_status",
        help="Defines all HTTP status code.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show the 'http_status' tool usage guide."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("code", nargs="?", type=int, help="Get definition of a specific HTTP status code.")
    group.add_argument("--category", help="Show all HTTP status codes in a category: 1xx, 2xx, etc...")
    group.add_argument("--all", action="store_true", help="Show all available HTTP status codes.")

    parser.set_defaults(func=run)


def run(args):
    if args.all:
        print(f"\nAll HTTP Status Codes:\n")
        for code in sorted(explanations):
            print(f"{code} -> {Fore.BLUE}{Style.BRIGHT}{explanations[code]}{Style.RESET_ALL}")
        return

    if args.category:
        prefix = args.category.lower().strip().replace("x", "")
        print(f"\nHTTP Status Codes in {prefix}xx Category:\n")
        found = False
        for code in sorted(explanations):
            if str(code).startswith(prefix):
                print(f"{code} -> {Fore.BLUE}{Style.BRIGHT}{explanations[code]}{Style.RESET_ALL}")
                found = True
        if not found:
            print(f"{Fore.RED}{Style.DIM}No status codes found for category '{args.category}'.{Style.RESET_ALL}")
        return

    if args.code is not None:
        code = args.code
        if code in explanations:
            message = explanations[code]
        else:
            close_matches = difflib.get_close_matches(str(code), map(str, explanations.keys()), n=3, cutoff=0.6)
            close_matches.sort(reverse=False)
            suggestion = f" Did you mean: {', '.join(close_matches)} ?" if close_matches else ""
            message = f"{Fore.RED}{Style.DIM}Status code not recognized.{suggestion}{Style.RESET_ALL}"

        print(f"\nHTTP {code}\n{Fore.BLUE}{Style.BRIGHT}{message}{Style.RESET_ALL}")
        return

    print(f"{Fore.RED}Please specify either a status code, a category (--category), or use --all.{Style.RESET_ALL}")
