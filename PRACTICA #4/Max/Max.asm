// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/Max.asm

// Computes M[2] = max(M[0], M[1])  where M stands for RAM

   @0
   D=M              
   @1
   D=D-M            
   @OUTPUT_FIRST
   D;JGT            
   @1
   D=M              
   @OUTPUT_D
   0;JMP           
(OUTPUT_FIRST)
   @0             
   D=M             
(OUTPUT_D)
   @2
   M=D              
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP          
