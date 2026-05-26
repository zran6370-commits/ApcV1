import re
import sys
import json
import math
import os
import platform
import datetime

class ApcInterpreter:
    def __init__(self):
        self.variables = {
            'PLATFORM': platform.system(),
            'VERSION': '0.2.0',
            'AUTHOR': 'Manus AI'
        }
        self.output = []
        
        # Daftar fungsi bawaan
        self.builtins = {
            'print': print,
            'echo': self._echo,
            'len': len,
            'str_upper': lambda s: str(s).upper(),
            'str_lower': lambda s: str(s).lower(),
            'math_sqrt': math.sqrt,
            'math_pow': math.pow,
            'math_abs': abs,
            'now': lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'json_encode': lambda d: json.dumps(d),
            'json_decode': lambda s: json.loads(s),
            'get_env': lambda k: os.getenv(k, ""),
            'exit': sys.exit
        }

    def _echo(self, *args):
        text = " ".join(map(str, args))
        self.output.append(text)
        print(text)

    def tokenize(self, code):
        # Hapus komentar
        code = re.sub(r'#.*|//.*', '', code)
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        # Pisahkan berdasarkan baris, abaikan baris kosong
        return [line.strip() for line in code.split('\n') if line.strip()]

    def execute(self, code):
        lines = self.tokenize(code)
        for line in lines:
            try:
                self.execute_line(line)
            except Exception as e:
                print(f"Error pada baris '{line}': {e}")

    def execute_line(self, line):
        line = line.strip().rstrip(';')
        
        # Echo command
        if line.startswith('echo '):
            val_expr = line[5:].strip()
            self._echo(self.evaluate_expression(val_expr))
            return

        # Assignment: $var = expr atau let var = expr
        if '=' in line and not line.startswith('if') and not line.startswith('for'):
            parts = line.split('=', 1)
            var_part = parts[0].strip()
            val_part = parts[1].strip()
            
            var_name = var_part
            if var_name.startswith('$'):
                var_name = var_name[1:]
            elif var_name.startswith('let '):
                var_name = var_name[4:]
            
            self.variables[var_name] = self.evaluate_expression(val_part)
            return

        # Function call langsung (misal: print("hello"))
        if '(' in line and line.endswith(')'):
            self.evaluate_expression(line)

    def evaluate_expression(self, expr):
        expr = expr.strip()
        
        # String Literals
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            return expr[1:-1]
        
        # Template Literals `...`
        if expr.startswith('`') and expr.endswith('`'):
            content = expr[1:-1]
            matches = re.findall(r'\$\{(.*?)\}', content)
            for match in matches:
                val = self.evaluate_expression(match)
                content = content.replace(f'${{{match}}}', str(val))
            return content

        # Numbers
        try:
            if '.' in expr: return float(expr)
            return int(expr)
        except ValueError: pass

        # JSON/Object Literals
        if expr.startswith('{') and expr.endswith('}'):
            try: return json.loads(expr.replace("'", '"'))
            except: pass
            
        # Function Calls: func_name(args)
        func_match = re.match(r'^(\w+)\((.*)\)$', expr)
        if func_match:
            func_name = func_match.group(1)
            args_str = func_match.group(2)
            # Sederhanakan parsing argumen (hanya mendukung satu argumen atau dipisah koma tanpa koma di dalam string)
            args = []
            if args_str:
                args = [self.evaluate_expression(a.strip()) for a in args_str.split(',')]
            
            if func_name in self.builtins:
                return self.builtins[func_name](*args)
            else:
                raise Exception(f"Fungsi '{func_name}' tidak ditemukan")

        # Variable Reference
        var_name = expr
        if var_name.startswith('$'):
            var_name = var_name[1:]
        
        if var_name in self.variables:
            val = self.variables[var_name]
            # Handle object property access: $obj.prop
            return val
            
        # Simple Arithmetic (sangat terbatas)
        if '+' in expr:
            parts = expr.split('+')
            return self.evaluate_expression(parts[0]) + self.evaluate_expression(parts[1])

        return expr

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            print(f"File tidak ditemukan: {file_path}")
            return
        with open(file_path, 'r') as f:
            code = f.read()
    else:
        print("Apc Language Interpreter v0.2.0")
        print("Penggunaan: python apc_interpreter.py <file.apc>")
        return
    
    interpreter = ApcInterpreter()
    interpreter.execute(code)

if __name__ == "__main__":
    main()
