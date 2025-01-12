# py2desmos: python objects to desmos latex converter module
import decimal

LPAREN = "\\left("
RPAREN = "\\right)"
LBRACK = "\\left["
RBRACK = "\\right]"
LBRACE = "\\left{"
RBRACE = "\\right}"

def convert(obj):
    match type(obj).__name__:
        case 'str':
            return obj
        case 'int' | 'float':
            return convert_number(obj)
        case 'tuple':
            return convert_tuple(obj)
        case 'list':
            return convert_list(obj)

def convert_varname(name):
    return f"{name[0]}_{{{name[1:]}}}" if len(name) > 1 else name

def convert_list(x):
    return convert_iterable(x, LBRACK, RBRACK)

def convert_tuple(x):
    return convert_iterable(x, LPAREN, RPAREN)

def convert_iterable(iterable, left, right):
    result = left
    for e in iterable:
        result += convert(e) + ","
    result = result[:-1] + right
    return result

def fraction(n, d):
    return f"\\frac{{{convert(n)}}}{{{convert(d)}}}"

def parentheses(x):
    return LPAREN + convert(x) + RPAREN

def brackets(x):
    return LBRACK + convert(x) + RBRACK

def braces(x):
    return LBRACE + convert(x) + RBRACE

def convert_number(x):
    # i really wish it weren't so annoying to do this
    return format(x, f".{str(0-decimal.Decimal(str(x)).as_tuple().exponent)}f")

if __name__ == "__main__":
    pass
