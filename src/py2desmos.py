# py2desmos: python objects to desmos latex converter module
import decimal

LPAREN = "\\left("
RPAREN = "\\right)"
LBRACK = "\\left["
RBRACK = "\\right]"
LBRACE = "\\left{"
RBRACE = "\\right}"

class DesmosObj:
    def __init__(self, value, varname=False):
        self.pyvalue = value
        self.value = self.convert(value, varname)

    def convert(self, obj, varname=False):
        match self.type_str(obj):
            case 'str':
                if varname:
                    return self.convert_varname(obj)
                else:
                    return obj
            case 'int' | 'float':
                return self.convert_number(obj)
            case 'tuple':
                return self.convert_tuple(obj)
            case 'list':
                return self.convert_list(obj)
            case 'DesmosObj': # Update if the class is renamed
                return obj.value
    
    def convert_varname(self, name):
        return f"{name[0]}_{{{name[1:]}}}"
    
    def convert_list(self, x):
        return self.convert_iterable(x, LBRACK, RBRACK)
    
    def convert_tuple(self, x):
        return self.convert_iterable(x, LPAREN, RPAREN)

    def convert_iterable(self, iterable, left, right):
        result = left
        for e in iterable:
            result += self.convert(e) + ","
        result = result[:-1] + right
        return result
    
    def convert_number(self, x):
        # i really wish it weren't so annoying to do this
        return format(x, f".{str(0-decimal.Decimal(str(x)).as_tuple().exponent)}f")
    
    def is_number(self, x):
        return type(x) in [int, float]
    
    def type_str(self, x):
        return type(x).__name__
    
    def __str__(self):
        return self.value
    
    def __add__(self, other):
        return DesmosObj(self.value + other.value)

if __name__ == "__main__":
    pass