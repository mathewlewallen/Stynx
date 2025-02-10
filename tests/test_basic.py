# tests/test_basic.py

import unittest
from stynx.parser import parse_source
from stynx.runtime import Runtime

class TestBasic(unittest.TestCase):
    def test_assignment_and_print(self):
        program = [
            "var x",
            "x = 10",
            "print(x)"
        ]
        ast_nodes = parse_source(program)
        rt = Runtime()
        
        # Capture stdout
        import io
        import sys
        backup_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            rt.run_statements(ast_nodes)
            output = sys.stdout.getvalue().strip()
        finally:
            sys.stdout = backup_stdout
        
        self.assertEqual(output, "10.0")

    def test_gradient(self):
        program = [
            "var a",
            "a = 2.0",
            "var b",
            "b = 3.0",
            "z = a * b",
            "grad(z, a)"
        ]
        ast_nodes = parse_source(program)
        rt = Runtime()
        
        import io
        import sys
        backup_stdout = sys.stdout
        try:
            sys.stdout = io.StringIO()
            rt.run_statements(ast_nodes)
            output = sys.stdout.getvalue().strip().splitlines()
        finally:
            sys.stdout = backup_stdout
        
        # The last line should look like "d(BinOpNode(...))/d(a) = 3.0"
        self.assertIn("= 3.0", output[-1])

if __name__ == '__main__':
    unittest.main()
