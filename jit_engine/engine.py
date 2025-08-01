import llvmlite.binding as llvm
import ctypes
import numpy as np
from memory_layout.numpy_array_layout import numpy_to_memref, MemRefDescriptor

# Initialize the LLVM JIT infrastructure
def initialize_llvm():
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

# Create a JIT execution engine using the native target
def create_execution_engine():
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine

# Compile LLVM IR and add it to the execution engine
def compile_ir(engine, llvm_ir):
    mod = llvm.parse_assembly(llvm_ir) # Parse the LLVM IR string
    mod.verify() # Check for errors in the IR
    engine.add_module(mod) # Add the module to the JIT engine
    engine.finalize_object() 
    engine.run_static_constructors() # Run any static constructors
    return mod

# Call the compiled vector_mul function using ctypes
def run_vector_mul(engine, mod, memref):
    func_ptr = engine.get_function_address("vector_mul") # Call the compiled vector_mul function using ctypes
    cfunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(MemRefDescriptor))(func_ptr) # Create a C function wrapper
    cfunc(ctypes.byref(memref)) # Call the function with the memref

# Main function to execute the workflow
def run_jit_vector_mul():
    initialize_llvm()
    engine = create_execution_engine()

    # Read the LLVM IR from file
    with open("llvm_ir/vector_mul.ll") as f:
        llvm_ir = f.read()

    # Convert the array into a memref-compatible structure
    mod = compile_ir(engine, llvm_ir)

    # Create a NumPy array
    arr = np.array([1, 2, 3, 4], dtype=np.int32)
    print("Before:", arr)  # OG Values

    # Convert the array into a memref-compatible structure
    memref = numpy_to_memref(arr)
    run_vector_mul(engine, mod, memref)

    print("After:", arr)