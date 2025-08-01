from jit_engine.engine import run_jit_vector_mul

# project entry point. It calls to the function run_jit_vector_mul() within the jit_engine/engine.py file
# you have creative liberity on how you want to expand it but I would personally just try and get
# run_jit_vector_add() run_jit_vector_sub() etc... 
if __name__ == "__main__":
    run_jit_vector_mul()