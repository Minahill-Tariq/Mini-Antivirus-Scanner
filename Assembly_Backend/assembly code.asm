INCLUDE Irvine32.inc
.data

line    BYTE "========================================",0
heading BYTE "     MINI ANTIVIRUS SCANNER             ",0
welcome BYTE "   WELCOME TO CYBER SECURITY PROJECT    ",0

userPrompt   BYTE "Enter Username: ",0
passPrompt   BYTE "Enter Password: ",0
loginSuccess BYTE "Login Successful!",0
loginFail    BYTE "Invalid Credentials! Try Again.",0
correctUser  BYTE "minahil",0
correctPass  BYTE "1234",0
userInput    BYTE 30 DUP(0)
passInput    BYTE 30 DUP(0)

menu1        BYTE "1. Quick Scan",0
menu2        BYTE "2. Full Scan",0
menu3        BYTE "3. Custom Scan (enter your own files)",0
menu4        BYTE "4. View Quarantine",0
menu5        BYTE "5. Add Files to Scanner",0
menu6        BYTE "6. Exit",0
choicePrompt BYTE "Enter Choice: ",0
choice       DWORD ?

file1 BYTE "safe.txt",0
file2 BYTE "virus.exe",0
file3 BYTE "project.doc",0
file4 BYTE "trojan.bat",0
file5 BYTE "notes.pdf",0
file6 BYTE "hacktool.exe",0
file7 BYTE "photo.jpg",0
file8 BYTE "malware.vbs",0

extraFile1 BYTE 50 DUP(0)
extraFile2 BYTE 50 DUP(0)
extraFile3 BYTE 50 DUP(0)
extraFile4 BYTE 50 DUP(0)
extraFile5 BYTE 50 DUP(0)

files DWORD OFFSET file1, OFFSET file2, OFFSET file3, OFFSET file4
      DWORD OFFSET file5, OFFSET file6, OFFSET file7, OFFSET file8
      DWORD OFFSET extraFile1, OFFSET extraFile2, OFFSET extraFile3
      DWORD OFFSET extraFile4, OFFSET extraFile5

fileCount  DWORD 8
maxFiles   DWORD 13

addHowMany  BYTE "How many files to add? (max 5): ",0
addPrompt   BYTE "Enter filename to add: ",0
addedMsg    BYTE "File added to scanner!",0
listFullMsg BYTE "File list is full! Cannot add more.",0
extraCount  DWORD 0

howManyPrompt BYTE "How many files to scan? (max 5): ",0
filePrompt    BYTE "Enter filename: ",0
customFile1   BYTE 50 DUP(0)
customFile2   BYTE 50 DUP(0)
customFile3   BYTE 50 DUP(0)
customFile4   BYTE 50 DUP(0)
customFile5   BYTE 50 DUP(0)

customFiles DWORD OFFSET customFile1, OFFSET customFile2
            DWORD OFFSET customFile3, OFFSET customFile4
            DWORD OFFSET customFile5

customCount DWORD 0

virusWord   BYTE "virus",0
hackWord    BYTE "hack",0
malwareWord BYTE "malware",0
trojanWord  BYTE "trojan",0

scanMsg         BYTE "Scanning Files...",0
safeMsg         BYTE "  --> SAFE FILE",0
threatMsg       BYTE "  --> THREAT DETECTED",0
reportTitle     BYTE "===== SCAN REPORT =====",0
filesScannedMsg BYTE "Files Scanned : ",0
threatFoundMsg  BYTE "Threats Found : ",0
safeFilesMsg    BYTE "Safe Files    : ",0
lowMsg          BYTE "Threat Level  : LOW",0
medMsg          BYTE "Threat Level  : MEDIUM",0
highMsg         BYTE "Threat Level  : HIGH",0
quarantineTitle BYTE "===== QUARANTINED FILES =====",0
noQuarantine    BYTE "(No files quarantined yet)",0

filesScanned DWORD 0
threatCount  DWORD 0
safeCount    DWORD 0


quarantine1  BYTE 50 DUP(0)
quarantine2  BYTE 50 DUP(0)
quarantine3  BYTE 50 DUP(0)
quarantine4  BYTE 50 DUP(0)
quarantine5  BYTE 50 DUP(0)
quarantine6  BYTE 50 DUP(0)
quarantine7  BYTE 50 DUP(0)
quarantine8  BYTE 50 DUP(0)
quarantine9  BYTE 50 DUP(0)
quarantine10 BYTE 50 DUP(0)
quarantine11 BYTE 50 DUP(0)
quarantine12 BYTE 50 DUP(0)
quarantine13 BYTE 50 DUP(0)
quarantine14 BYTE 50 DUP(0)
quarantine15 BYTE 50 DUP(0)
quarantine16 BYTE 50 DUP(0)
quarantine17 BYTE 50 DUP(0)
quarantine18 BYTE 50 DUP(0)
quarantine19 BYTE 50 DUP(0)
quarantine20 BYTE 50 DUP(0)

quarantineSlots DWORD OFFSET quarantine1,  OFFSET quarantine2
                DWORD OFFSET quarantine3,  OFFSET quarantine4
                DWORD OFFSET quarantine5,  OFFSET quarantine6
                DWORD OFFSET quarantine7,  OFFSET quarantine8
                DWORD OFFSET quarantine9,  OFFSET quarantine10
                DWORD OFFSET quarantine11, OFFSET quarantine12
                DWORD OFFSET quarantine13, OFFSET quarantine14
                DWORD OFFSET quarantine15, OFFSET quarantine16
                DWORD OFFSET quarantine17, OFFSET quarantine18
                DWORD OFFSET quarantine19, OFFSET quarantine20

quarantineCount DWORD 0
savedFileName   DWORD 0

.code

MyStrCompare PROC
CmpLoop:
    mov al, [esi]
    mov bl, [edi]
    cmp al, bl
    jne CmpNo
    cmp al, 0
    je  CmpYes
    inc esi
    inc edi
    jmp CmpLoop
CmpYes:
    mov eax, 1
    ret
CmpNo:
    mov eax, 0
    ret
MyStrCompare ENDP

ContainsWord PROC
CW_Outer:
    mov bl, [esi]
    cmp bl, 0
    je  CW_No
    mov ebx, esi
    mov ecx, edi
CW_Inner:
    mov al, [ecx]
    cmp al, 0
    je  CW_Yes
    mov ah, [ebx]
    cmp ah, 0
    je  CW_Next
    cmp al, ah
    jne CW_Next
    inc ebx
    inc ecx
    jmp CW_Inner
CW_Next:
    inc esi
    jmp CW_Outer
CW_Yes:
    mov eax, 1
    ret
CW_No:
    mov eax, 0
    ret
ContainsWord ENDP

MyCopy PROC
CP_Loop:
    mov al, [esi]
    mov [edi], al
    cmp al, 0
    je  CP_Done
    inc esi
    inc edi
    jmp CP_Loop
CP_Done:
    ret
MyCopy ENDP

main PROC

    call Clrscr

    mov eax, (0 * 16) + 11
    call SetTextColor
    mov edx, OFFSET line
    call WriteString
    call Crlf
    mov edx, OFFSET heading
    call WriteString
    call Crlf
    mov edx, OFFSET line
    call WriteString
    call Crlf
    mov edx, OFFSET welcome
    call WriteString
    call Crlf
    call Crlf

    mov eax, (0 * 16) + 15
    call SetTextColor

    call LoginSystem

MainMenu:
    call Crlf

    mov eax, (0 * 16) + 11
    call SetTextColor
    mov edx, OFFSET line
    call WriteString
    call Crlf

    mov eax, (0 * 16) + 15
    call SetTextColor
    mov edx, OFFSET menu1
    call WriteString
    call Crlf
    mov edx, OFFSET menu2
    call WriteString
    call Crlf
    mov edx, OFFSET menu3
    call WriteString
    call Crlf
    mov edx, OFFSET menu4
    call WriteString
    call Crlf
    mov edx, OFFSET menu5
    call WriteString
    call Crlf
    mov edx, OFFSET menu6
    call WriteString
    call Crlf

    mov eax, (0 * 16) + 11
    call SetTextColor
    mov edx, OFFSET line
    call WriteString
    call Crlf

    mov eax, (0 * 16) + 15
    call SetTextColor
    mov edx, OFFSET choicePrompt
    call WriteString
    call ReadInt
    mov choice, eax

    cmp choice, 1
    je  QuickScan
    cmp choice, 2
    je  FullScan
    cmp choice, 3
    je  CustomScan
    cmp choice, 4
    je  ViewQuarantine
    cmp choice, 5
    je  AddFiles
    cmp choice, 6
    je  ExitProgram
    jmp MainMenu

QuickScan:
    call ResetCounters
    call Crlf

    mov eax, (0 * 16) + 14
    call SetTextColor
    mov edx, OFFSET scanMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor

    mov ecx, 4
    mov esi, OFFSET files
QLoop:
    push ecx
    push esi
    mov ebx, [esi]
    mov edx, ebx
    call WriteString
    call Crlf
    mov edx, ebx
    call DetectThreat
    pop esi
    pop ecx
    add esi, 4
    loop QLoop

    call ShowReport
    jmp MainMenu

FullScan:
    call ResetCounters
    call Crlf

    mov eax, (0 * 16) + 14
    call SetTextColor
    mov edx, OFFSET scanMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor

    mov ecx, fileCount
    mov esi, OFFSET files
FLoop:
    push ecx
    push esi
    mov ebx, [esi]

    mov al, [ebx]
    cmp al, 0
    je  FSkip

    mov edx, ebx
    call WriteString
    call Crlf
    mov edx, ebx
    call DetectThreat
    jmp FNext

FSkip:
    dec filesScanned

FNext:
    pop esi
    pop ecx
    add esi, 4
    loop FLoop

    call ShowReport
    jmp MainMenu

CustomScan:
    call ResetCounters
    call Crlf

    mov eax, (0 * 16) + 15
    call SetTextColor
    mov edx, OFFSET howManyPrompt
    call WriteString
    call ReadInt
    mov customCount, eax

    cmp customCount, 5
    jle CountOK
    mov customCount, 5
CountOK:

    mov ecx, customCount
    mov esi, OFFSET customFiles
ReadLoop:
    push ecx
    push esi

    mov edi, [esi]
    push ecx
    mov ecx, 50
    mov al, 0
ClrBuf:
    mov [edi], al
    inc edi
    loop ClrBuf
    pop ecx

    mov edx, OFFSET filePrompt
    call WriteString
    mov edx, [esi]
    mov ecx, 49
    call ReadString

    pop esi
    pop ecx
    add esi, 4
    loop ReadLoop

    call Crlf
    mov eax, (0 * 16) + 14
    call SetTextColor
    mov edx, OFFSET scanMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor

    mov ecx, customCount
    mov esi, OFFSET customFiles
CScanLoop:
    push ecx
    push esi
    mov ebx, [esi]
    mov edx, ebx
    call WriteString
    call Crlf
    mov edx, ebx
    call DetectThreat
    pop esi
    pop ecx
    add esi, 4
    loop CScanLoop

    call ShowReport
    jmp MainMenu

AddFiles:
    call Crlf

    mov eax, extraCount
    cmp eax, 5
    jl  CanAdd

    mov eax, (0 * 16) + 4
    call SetTextColor
    mov edx, OFFSET listFullMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    jmp MainMenu

CanAdd:
    mov eax, (0 * 16) + 15
    call SetTextColor
    mov edx, OFFSET addHowMany
    call WriteString
    call ReadInt
    mov ebx, eax

    mov eax, 5
    sub eax, extraCount
    cmp ebx, eax
    jle AddCountOK
    mov ebx, eax
AddCountOK:

    mov ecx, ebx
    cmp ecx, 0
    je  MainMenu

    mov eax, extraCount
    mov edx, 50
    mul edx
    mov esi, OFFSET extraFile1
    add esi, eax

AddLoop:
    push ecx
    push esi

    mov edi, esi
    push ecx
    mov ecx, 50
    mov al, 0
ClrAdd:
    mov [edi], al
    inc edi
    loop ClrAdd
    pop ecx

    mov edx, OFFSET addPrompt
    call WriteString
    mov edx, esi
    mov ecx, 49
    call ReadString

    mov edx, esi
    call DetectThreat

    inc fileCount
    inc extraCount

    mov eax, (0 * 16) + 2
    call SetTextColor
    mov edx, OFFSET addedMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor

    pop esi
    pop ecx
    add esi, 50
    loop AddLoop

    jmp MainMenu

ViewQuarantine:
    call Crlf

    mov eax, (0 * 16) + 11
    call SetTextColor
    mov edx, OFFSET quarantineTitle
    call WriteString
    call Crlf

    mov eax, quarantineCount
    cmp eax, 0
    jne ShowQList

    mov eax, (0 * 16) + 14
    call SetTextColor
    mov edx, OFFSET noQuarantine
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    jmp MainMenu

ShowQList:
    mov ecx, quarantineCount
    mov esi, OFFSET quarantineSlots

QListLoop:
    push ecx
    push esi

    mov ebx, [esi]
    mov eax, (0 * 16) + 4
    call SetTextColor
    mov edx, ebx
    call WriteString
    call Crlf

    pop esi
    pop ecx
    add esi, 4
    loop QListLoop

    mov eax, (0 * 16) + 15
    call SetTextColor
    jmp MainMenu

ExitProgram:
    mov eax, (0 * 16) + 15
    call SetTextColor
    exit

main ENDP

LoginSystem PROC
TryAgain:
    mov ecx, 30
    mov edi, OFFSET userInput
    xor al, al
ClrU:
    mov [edi], al
    inc edi
    loop ClrU

    mov ecx, 30
    mov edi, OFFSET passInput
    xor al, al
ClrP:
    mov [edi], al
    inc edi
    loop ClrP

    mov eax, (0 * 16) + 15
    call SetTextColor
    mov edx, OFFSET userPrompt
    call WriteString
    mov edx, OFFSET userInput
    mov ecx, 29
    call ReadString

    mov edx, OFFSET passPrompt
    call WriteString
    mov edx, OFFSET passInput
    mov ecx, 29
    call ReadString

    mov esi, OFFSET userInput
    mov edi, OFFSET correctUser
    call MyStrCompare
    cmp eax, 1
    jne BadLogin

    mov esi, OFFSET passInput
    mov edi, OFFSET correctPass
    call MyStrCompare
    cmp eax, 1
    jne BadLogin

    mov eax, (0 * 16) + 2
    call SetTextColor
    mov edx, OFFSET loginSuccess
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    ret

BadLogin:
    mov eax, (0 * 16) + 4
    call SetTextColor
    mov edx, OFFSET loginFail
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    jmp TryAgain

LoginSystem ENDP

DetectThreat PROC
    inc filesScanned
    mov savedFileName, edx

    mov esi, edx
    mov edi, OFFSET virusWord
    call ContainsWord
    cmp eax, 1
    je  Found

    mov esi, savedFileName
    mov edi, OFFSET trojanWord
    call ContainsWord
    cmp eax, 1
    je  Found

    mov esi, savedFileName
    mov edi, OFFSET malwareWord
    call ContainsWord
    cmp eax, 1
    je  Found

    mov esi, savedFileName
    mov edi, OFFSET hackWord
    call ContainsWord
    cmp eax, 1
    je  Found

    inc safeCount
    mov eax, (0 * 16) + 2
    call SetTextColor
    mov edx, OFFSET safeMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    ret

Found:
    inc threatCount
    mov eax, (0 * 16) + 4
    call SetTextColor
    mov edx, OFFSET threatMsg
    call WriteString
    call Crlf

    mov eax, quarantineCount
    cmp eax, 20
    jge ShowLevel

    mov eax, quarantineCount
    mov ebx, 4
    mul ebx
    mov edi, OFFSET quarantineSlots
    add edi, eax
    mov edi, [edi]

    mov esi, savedFileName
    call MyCopy

    inc quarantineCount

ShowLevel:
    mov eax, (0 * 16) + 14
    call SetTextColor

    cmp threatCount, 1
    je  Lv1
    cmp threatCount, 2
    je  Lv2
    jmp Lv3

Lv1:
    mov edx, OFFSET lowMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    ret

Lv2:
    mov edx, OFFSET medMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    ret

Lv3:
    mov eax, (0 * 16) + 4
    call SetTextColor
    mov edx, OFFSET highMsg
    call WriteString
    call Crlf
    mov eax, (0 * 16) + 15
    call SetTextColor
    ret

DetectThreat ENDP

ShowReport PROC
    call Crlf

    mov eax, (0 * 16) + 11
    call SetTextColor
    mov edx, OFFSET reportTitle
    call WriteString
    call Crlf

    mov eax, (0 * 16) + 15
    call SetTextColor
    mov edx, OFFSET filesScannedMsg
    call WriteString
    mov eax, filesScanned
    call WriteDec
    call Crlf

    mov eax, (0 * 16) + 4
    call SetTextColor
    mov edx, OFFSET threatFoundMsg
    call WriteString
    mov eax, threatCount
    call WriteDec
    call Crlf

    mov eax, (0 * 16) + 2
    call SetTextColor
    mov edx, OFFSET safeFilesMsg
    call WriteString
    mov eax, safeCount
    call WriteDec
    call Crlf

    mov eax, (0 * 16) + 15
    call SetTextColor
    ret
ShowReport ENDP

ResetCounters PROC
    mov filesScanned, 0
    mov threatCount,  0
    mov safeCount,    0
    ret
ResetCounters ENDP

END main
