// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// Entry point of the program
@main
0;JMP

// Infinite loop to listen for keyboard input and update the screen accordingly
(main)
  // Listen for keyboard input
  @KBD
  D=M

  // Check if any key is pressed
  @key_pressed
  D;JEQ   // If no key is pressed, jump to clear_screen

  // If a key is pressed, blacken the screen
  @SCREEN
  D=A
  @black_screen
  0;JMP   // Jump to blacken the screen

// Clear the screen
(clear_screen)
  @SCREEN
  D=A
  @clear_loop
  0;JMP   // Jump to clear_loop

// Blacken the screen
(black_screen)
  @SCREEN
  D=A
  @black_loop
  0;JMP   // Jump to black_loop

// Loop to clear the screen
(clear_loop)
  // Write "white" (0) to screen memory
  M=0

  // Move to next screen location
  @SCREEN
  M=M+1

  // Check if the end of the screen memory is reached
  @END_SCREEN
  D=M
  @clear_loop
  D;JLT   // If not, continue clearing the screen

  // If the end of the screen memory is reached, jump back to main loop
  @main
  0;JMP

(END_SCREEN)

// Loop to blacken the screen
(black_loop)
  // Write "black" (1) to screen memory
  M=-1

  // Move to next screen location
  @SCREEN
  M=M+1

  // Check if the end of the screen memory is reached
  @END_SCREEN
  D=M
  @black_loop
  D;JLT   // If not, continue blackening the screen

  // If the end of the screen memory is reached, jump back to main loop
  @main
  0;JMP

(END_SCREEN)
