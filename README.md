# Stynx <img width="45" alt="schermafbeelding 2017-09-27 om 23 08 12" src="https://user-images.githubusercontent.com/7254997/30937972-c9632d04-a3d8-11e7-87f3-c44ce2b86d24.png">


This is a **proof-of-concept** AI-focused DSL that demonstrates:
- A simple grammar for tensor operations.
- A basic parser and AST.
- A runtime that executes tensor operations in Python.
- A **naive** automatic differentiation example for demonstration.

## Getting Started

1. **Clone** the repo:
   ```bash
   git clone https://github.com/mathewlewallen/stynx.git
   cd stynx
    ```

2. Install dependencies.
3. Run an example:
   ```bash
    python -m synx.cli examples/simple.sx
    ```
4. Try the gradient test:
   ```bash
    python -m stynx.cli examples/gradient_test.sx
    ```

## Roadmap

- [ ] Refine the parser and AST
- [ ] Enhance the automatic differentiation engine
- [ ] Add GPU/TPU integration and concurrency primitives
- [ ] Transition Python-based runtime to LLVM/MLIR backend
- [ ] Implement reference-counting memory model
- [ ] Add concurrency primitives (parallel_for)
- [ ] Expand autodiff to handle more complex neural nets
- [ ] Export to ONNX

## Contributing

PRs and issues welcome!
