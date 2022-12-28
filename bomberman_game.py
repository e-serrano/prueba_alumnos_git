import random

class bomberman:
  def initial_board(self, rows, columns, chr):
    self.rows=rows
    self.columns=columns
    self.chr=chr
    result=[[self.chr for item in range(self.columns)] for i in range(self.rows)]
    return result

  def locate_mines(self, rows, columns, mines):
    self.rows=rows
    self.columns=columns
    self.mines=mines
    table=self.initial_board(self.rows,self.columns,0)
    for i in range(self.mines):
      col_random=random.randint(0,self.columns-1)
      row_random=random.randint(0,self.rows-1)
      if table[row_random][col_random]!='B':
        table[row_random][col_random]='B'
      else:
        col_random=random.randint(0,self.columns-1)
        row_random=random.randint(0,self.rows-1)
        table[row_random][col_random]='B'
    return table

  def numbers(self, rows, columns, mines):
    self.rows=rows
    self.columns=columns
    self.mines=mines
    table=self.locate_mines(self.rows,self.columns,self.mines)

    r_mine=[table.index(i) for i in table if 'B' in i]
    col_mine=[[index for (index, item) in enumerate(table[i]) if item == 'B'] for i in r_mine]
    col_mine=[int("".join(map(str, i))) if len(i)==1 else i for i in col_mine]

    positions=dict(zip(r_mine,col_mine))

    for r_final in positions.keys():
      x=positions[r_final]
      if type(x) is list:
        for i in x:
          c_final = i
          #condicional para marcar filas superiores e inferiores de minas
          if r_final != self.rows-1 and table[r_final+1][c_final]!='B':
            table[r_final+1][c_final]+=1          
          if r_final != 0 and table[r_final-1][c_final]!='B':
            table[r_final-1][c_final]+=1

          #condicional para marcar columnas derecha e izquierda de minas
          if c_final != self.columns-1 and table[r_final][c_final+1]!='B':
            table[r_final][c_final+1]+=1          
          if c_final != 0 and table[r_final][c_final-1]!='B':
            table[r_final][c_final-1]+=1

          #condicionales para esquinas de bombas
          if (r_final != self.rows-1 and c_final != self.columns-1) and table[r_final+1][c_final+1] != 'B':
            table[r_final+1][c_final+1] += 1
          if (r_final != 0 and c_final != self.columns-1) and table[r_final-1][c_final+1] != 'B':
            table[r_final-1][c_final+1] += 1
          if (r_final != self.rows-1 and c_final != 0) and table[r_final+1][c_final-1] != 'B':
            table[r_final+1][c_final-1] += 1
          if (r_final != 0 and c_final != 0) and table[r_final-1][c_final-1] != 'B':
            table[r_final-1][c_final-1] += 1

      else:
        c_final = x
        #condicional para marcar filas superiores e inferiores de minas
        if r_final != self.rows-1 and table[r_final+1][c_final]!='B':
          table[r_final+1][c_final]+=1          
        if r_final != 0 and table[r_final-1][c_final]!='B':
          table[r_final-1][c_final]+=1

        #condicional para marcar columnas derecha e izquierda de minas
        if c_final != self.columns-1 and table[r_final][c_final+1]!='B':
          table[r_final][c_final+1]+=1
        if c_final != 0 and table[r_final][c_final-1]!='B':
          table[r_final][c_final-1]+=1

        #condicionales para esquinas de bombas
        if (r_final != self.rows-1 and c_final != self.columns-1) and table[r_final+1][c_final+1] != 'B':
          table[r_final+1][c_final+1] += 1
        if (r_final != 0 and c_final != self.columns-1) and table[r_final-1][c_final+1] != 'B':
          table[r_final-1][c_final+1] += 1
        if (r_final != self.rows-1 and c_final != 0) and table[r_final+1][c_final-1] != 'B':
          table[r_final+1][c_final-1] += 1
        if (r_final != 0 and c_final != 0) and table[r_final-1][c_final-1] != 'B':
          table[r_final-1][c_final-1] += 1
    
    return table
  

  def play (self,rows,columns,mines):
    self.rows=rows
    self.columns=columns
    self.mines=mines
    table_empty=self.initial_board(self.rows,self.columns,' ')
    table_mines=self.numbers(self.rows,self.columns,self.mines)
    result=0
    while result != 'B':
      x,y=map(int,input('Enter row and column to check (r,c format): ').split(','))
      result=table_mines[x][y]
      table_empty[x][y]=table_mines[x][y]
      if result == 'B':
        print(table_empty)
        print('Game Over')
      else:
        print(table_empty)

bomberman().play(5,5,5)