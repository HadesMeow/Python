theBoard = {'A-0':' ', 'A-1':' ','A-2':' ','A-3':' ','A-4':' ',
            'B-0':' ','B-1':' ','B-2':' ','B-3':' ','B-4':' ',
            'C-0':' ','C-1':' ','C-2':' ','C-3':' ','C-4':' ',
            'D-0':' ','D-1':' ','D-2':' ','D-3':' ','D-4':' ',
            'E-0':' ','E-1':' ','E-2':' ','E-3':' ','E-4':' '
            }
def printBoard(board):
    print(' |0|1|2|3|4')
    print('-+-+-+-+-+-')
    print('A' + '|' + board['A-0'] + '|' + board['A-1'] + '|' + board['A-2'] + '|' + board['A-3'] + '|' + board['A-4'])
    print('-+-+-+-+-+-')
    print('B' + '|'  + board['B-0'] + '|' + board['B-1'] + '|' + board['B-2'] + '|' + board['B-3'] + '|' + board['B-4'])
    print('-+-+-+-+-+-')
    print('C' + '|'  + board['C-0'] + '|' + board['C-1'] + '|' + board['C-2'] + '|' + board['C-3'] + '|' + board['C-4'])
    print('-+-+-+-+-+-')
    print('D' + '|'  + board['D-0'] + '|' + board['D-1'] + '|' + board['D-2'] + '|' + board['D-3'] + '|' + board['D-4'])
    print('-+-+-+-+-+-')
    print('E' + '|'  + board['E-0'] + '|' + board['E-1'] + '|' + board['E-2'] + '|' + board['E-3'] + '|' + board['E-4'])

turn = 'X'
for i in range(25):
    printBoard(theBoard)
    print('Turn for ' + turn + ',Move on which space?')
    move = input()
    theBoard[move]= turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
printBoard(theBoard)
