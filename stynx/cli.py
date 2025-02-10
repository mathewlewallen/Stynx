# stynx/cli.py

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m stynx.cli <filename.sx>")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        content = f.read()
    lines = content.splitlines()

    ast_nodes = parse_source(lines)
    rt = Runtime()
    rt.run_statements(ast_nodes)

if __name__ == "__main__":
    main()
