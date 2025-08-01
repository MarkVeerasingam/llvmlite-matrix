# Matrix llvmlite Project

This project is designed to help you write LLVM IR and use **llvmlite** as a JIT engine.

It serves as a first step towards hardware acceleration by working directly with low-level memory references based on the NumPy array structure.  
(Inspired by Stephen Diehl’s post on MLIR memory: [https://www.stephendiehl.com/posts/mlir_memory/](https://www.stephendiehl.com/posts/mlir_memory/))

Please Read.

---

## Goals

- Get hands-on experience with Python and LLVM IR.
- Create new LLVM files such as:
  - `vector_add.ll`
  - `vector_sub.ll`
  - `vector_div.ll`
- Update your engine.py in accordance 
- If you progress well, extend your work to handle 2D and 3D arrays (matrices and tensors).

---

## Why this project?

This is intended as an independent and exploratory project that can serve as poster material for EuroLLVM submissions or inspire early research topics such as:

- Compiler construction
- Hardware acceleration
- Designing your own programming language

It’s a great way to step into LLVM, tensors, and matrix computations, and could form the basis of an FYP

This will be a huge step up from the LLVM we were writing but I have no doubt you guys are up to the challenge :) 

---

## Further thoughts

This project is flexible enough for you to extend individually on the side, reinforcing the importance of thinking about your FYP or research topic early. You can develop this alongside your main internship work.

You'll soon find that LLVM for tensor and matrix operations can get complicated and a pain in the ass. If so, I highly recommend looking into **MLIR** - which inspired this project - for more elegant and scalable solutions:  
- [https://www.stephendiehl.com/posts/mlir_introduction/](https://www.stephendiehl.com/posts/mlir_introduction/)

- [https://www.stephendiehl.com/posts/mlir_memory/](https://www.stephendiehl.com/posts/mlir_memory/)

Feel free to explore MLIR if interested, but for now, this project should keep you well engaged while I’m away.

If won't be of major help for you, for this project but if you do go down that route, it is something I personally have done before
- [https://github.com/MarkVeerasingam/matrices-mlir/tree/main](https://github.com/MarkVeerasingam/matrices-mlir/tree/main)
