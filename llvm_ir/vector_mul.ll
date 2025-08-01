; ModuleID = 'vector_mul'
target triple = "x86_64-pc-linux-gnu"

; Define a struct type %memref representing a memref descriptor:
; { data pointer (i8*), aligned pointer (i8*), offset (i64), shape array ([1 x i64]), stride array ([1 x i64]) }
%memref = type { i8*, i8*, i64, [1 x i64], [1 x i64] }

; Define the vector_mul function, which takes a pointer to a memref descriptor as argument
define void @vector_mul(%memref* %arg) {
entry:
  ; Get pointer to the shape field: %arg->shape[0]
  %shape_ptr = getelementptr inbounds %memref, %memref* %arg, i32 0, i32 3, i32 0
  ; Load the size of the vector from shape
  %size = load i64, i64* %shape_ptr

  ; Get pointer to the aligned data pointer field: %arg->aligned
  %data_ptr = getelementptr inbounds %memref, %memref* %arg, i32 0, i32 1
  ; Load the actual aligned data pointer (i8*)
  %aligned_ptr = load i8*, i8** %data_ptr
  ; Cast the data pointer from byte pointer (i8*) to int pointer (i32*)
  %int_ptr = bitcast i8* %aligned_ptr to i32*

  ; Branch to loop label to start the loop
  br label %loop

loop:
  ; i is the loop induction variable: PHI node for the loop index
  ; Starts at 0 coming from entry, increments by 1 each iteration
  %i = phi i64 [ 0, %entry ], [ %i_next, %loop ]

  ; Compute pointer to element i: &int_ptr[i]
  %index_ptr = getelementptr i32, i32* %int_ptr, i64 %i
  ; Load the current value at element i
  %val = load i32, i32* %index_ptr
  ; Multiply the value by 2
  %double_val = mul i32 %val, 2
  ; Store the doubled value back to element i
  store i32 %double_val, i32* %index_ptr

  ; Increment loop index i by 1
  %i_next = add i64 %i, 1
  ; Check if i_next < size (loop condition)
  %cond = icmp slt i64 %i_next, %size
  ; Branch based on condition: if true continue loop, else go to done
  br i1 %cond, label %loop, label %done

done:
  ; Return void — end of function
  ret void
}
