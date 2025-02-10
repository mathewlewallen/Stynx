import sys
from stynx.parser import parse_code

def main():
    if len(sys.argv) < 2:
        print("Usage: stynx <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    try:
        with open(source_file, "r") as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
        sys.exit(1)
    
    try:
        ast = parse_code(source_code)
        print("Generated AST:")
        for node in ast:
            print(node)
    except Exception as e:
        print(f"Error during parsing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
