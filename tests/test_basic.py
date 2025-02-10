import unittest
from stynx.parser import parse_source
from stynx.runtime import Runtime

class TestStynx(unittest.TestCase):
    def test_assignment_and_print(self):
        source = "var x\nx = 10\nprint(x)\n"
        ast = parse_source(source)
        runtime = Runtime()
        
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        runtime.run_statements(ast)
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "10")

    def test_gradient(self):
        source = "var a\na = 2.0\nvar b\nb = 3.0\nz = a * b\ngrad(z, a)\n"
        ast = parse_source(source)
        runtime = Runtime()
        
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        runtime.run_statements(ast)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().strip()
        self.assertIn("3.0", output)

if __name__ == '__main__':
    unittest.main()
