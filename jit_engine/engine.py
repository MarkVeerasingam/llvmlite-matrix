import llvmlite.binding as llvm
import ctypes
import numpy as np
from memory_layout.numpy_array_layout import numpy_to_memref, MemRefDescriptor

def initialize_llvm():
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

def create_execution_engine():
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine

def compile_ir(engine, llvm_ir):
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod

def run_vector_mul(engine, mod, memref):
    func_ptr = engine.get_function_address("vector_mul")
    cfunc = ctypes.CFUNCTYPE(None, ctypes.POINTER(MemRefDescriptor))(func_ptr)
    cfunc(ctypes.byref(memref))

def run_jit_vector_mul():
    initialize_llvm()
    engine = create_execution_engine()

    with open("llvm_ir/vector_mul.ll") as f:
        llvm_ir = f.read()

    mod = compile_ir(engine, llvm_ir)

    arr = np.array([1, 2, 3, 4], dtype=np.int32)
    print("Before:", arr)

    memref = numpy_to_memref(arr)
    run_vector_mul(engine, mod, memref)

    print("After:", arr)