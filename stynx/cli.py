import sys
from .parser import parse_source
from .runtime import Runtime

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m stynx.cli <source_file>")
        sys.exit(1)
    source_file = sys.argv[1]
    try:
        with open(source_file, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
        sys.exit(1)
    try:
        ast = parse_source(source_code)
    except Exception as e:
        print(f"Parsing error: {e}")
        sys.exit(1)
    runtime = Runtime()
    runtime.run_statements(ast)

if __name__ == '__main__':
    main()
