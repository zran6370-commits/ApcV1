import re
import sys
import json

class ApcInterpreter:
    def __init__(self):
        self.variables = {}
        self.output = []

    def tokenize(self, code):
        # Sederhanakan tokenisasi untuk demonstrasi
        # Mendukung komentar, variabel $, let, echo, if, for, dll.
        # Hapus komentar
        code = re.sub(r'#.*|//.*', '', code)
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
        return code.strip().split('\n')

    def execute(self, code):
        lines = self.tokenize(code)
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Echo command (PHP/Shell style)
            if line.startswith('echo '):
                val = line[5:].strip().rstrip(';')
                self.output.append(self.evaluate_expression(val))
            
            # Variable assignment ($nama = "..." atau let nama = "...")
            elif '=' in line:
                parts = line.split('=', 1)
                var_part = parts[0].strip()
                val_part = parts[1].strip().rstrip(';')
                
                # Bersihkan prefix variabel
                var_name = var_part
                if var_name.startswith('$'):
                    var_name = var_name[1:]
                elif var_name.startswith('let '):
                    var_name = var_name[4:]
                
                self.variables[var_name] = self.evaluate_expression(val_part)

    def evaluate_expression(self, expr):
        expr = expr.strip()
        # String
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            return expr[1:-1]
        
        # Template literal (JavaScript style)
        if expr.startswith('`') and expr.endswith('`'):
            content = expr[1:-1]
            # Interpolasi ${...}
            matches = re.findall(r'\$\{(.*?)\}', content)
            for match in matches:
                val = self.evaluate_expression(match)
                content = content.replace(f'${{{match}}}', str(val))
            return content

        # Number
        try:
            if '.' in expr:
                return float(expr)
            return int(expr)
        except ValueError:
            pass

        # JSON / Object style
        if expr.startswith('{') and expr.endswith('}'):
            try:
                # Sederhanakan: coba parse sebagai JSON
                return json.loads(expr.replace("'", '"'))
            except:
                pass

        # Variable reference
        var_name = expr
        if var_name.startswith('$'):
            var_name = var_name[1:]
        
        if var_name in self.variables:
            return self.variables[var_name]
        
        return expr

    def get_output(self):
        return "\n".join(map(str, self.output))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
    else:
        # Contoh kode default
        code = """
        $nama = "Manus";
        let usia = 2;
        echo `Halo, nama saya ${$nama} dan saya berusia ${usia} tahun.`;
        $data = {"role": "AI Assistant", "status": "Active"};
        echo $data;
        """
    
    interpreter = ApcInterpreter()
    interpreter.execute(code)
    print(interpreter.get_output())
