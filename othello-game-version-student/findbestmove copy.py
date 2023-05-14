'''
    AI 2023
    แก้ code ได้เฉพาะใน file นี้เท่านั้น 
    จะเพิ่ม function ก็สามารถทำได้นะ แต่ชื่อ class กับชื่อ findBestMove method ห้ามแก้เด็ดขาด
    นอกนั้น ทำได้หมด จะเพิ่มตัวแปรก็ทำได้
    ห้ามใช้ library ที่ อจ ต้อง install เพิ่มเติมจากที่กำหนดให้
'''
import copy,random
from board import Board
from time import time
# use deepcopy to copy a list เนื่องจาก list ใน python ส่งค่าแบบ pass by reference
# ดังนั้นเราเลยต้องใช้ deepcopy function ใน copy เพื่อให้เป็นการส่งค่า pass by value แทน


MOVE_DIRS = [(-1, -1), (-1, 0), (-1, +1),
             (0, -1),           (0, +1),
             (+1, -1), (+1, 0), (+1, +1)]


# ห้ามแก้ชื่อ class
class ComputeOthello:
    
    # ห้ามแก้ __init__ method
    def __init__(self,board,num_tiles,n = 8):
        self.board = board
        self.num_tiles = num_tiles
        self.time_play = [0,0]
        self.n = n
        self.current_player = 0
        self.opponent = 1
        self.conner = False

    def make_move(self):
        if self.is_legal_move(self.move):
            self.board[self.move[0]][self.move[1]] = self.current_player + 1
            self.num_tiles[self.current_player] += 1
            self.flip_tiles()
    
    def flip_tiles(self):
        curr_tile = self.current_player + 1 
        for direction in MOVE_DIRS:
            if self.has_tile_to_flip(self.move, direction):
                i = 1
                while True:
                    row = self.move[0] + direction[0] * i
                    col = self.move[1] + direction[1] * i
                    if self.board[row][col] == curr_tile:
                        break
                    else:
                        self.board[row][col] = curr_tile
                        self.num_tiles[self.current_player] += 1
                        self.num_tiles[(self.current_player + 1) % 2] -= 1
                        i += 1

    def has_tile_to_flip(self, move, direction):
        i = 1
        if self.current_player in (0, 1) and \
           self.is_valid_coord(move[0], move[1]):
            curr_tile = self.current_player + 1
            while True:
                row = move[0] + direction[0] * i
                col = move[1] + direction[1] * i
                if not self.is_valid_coord(row, col) or \
                    self.board[row][col] == 0:
                    return False
                elif self.board[row][col] == curr_tile:
                    break
                else:
                    i += 1
        return i > 1

    def has_legal_move(self):
        for row in range(self.n):
            for col in range(self.n):
                move = (row, col)
                if self.is_legal_move(move):
                    return True
        return False
    
    def get_legal_moves(self):
        moves = []
        for row in range(self.n):
            for col in range(self.n):
                move = (row, col)
                if self.is_legal_move(move):
                    moves.append(move)
        
        if self.conner:
            connerset = [0,7]
            result = [sublist for sublist in moves if any(item in sublist for item in connerset)]
            if result:
                return result
        return moves

    def is_legal_move(self, move):
        if move != () and self.is_valid_coord(move[0], move[1]) \
           and self.board[move[0]][move[1]] == 0:
            for direction in MOVE_DIRS:
                if self.has_tile_to_flip(move, direction):
                    return True
        return False

    def is_valid_coord(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.n:
            return True
        return False


    # ทำ function นี้ให้สมบูรณ์
    # ห้ามแก้ชื่อ function และตัว arguments ที่เป็น input ของ function
    def findBestMove(self,board,current_player,opponent,num_tiles):
        self.board = board
        self.num_tiles = num_tiles
        self.current_player = current_player
        self.opponent = opponent
