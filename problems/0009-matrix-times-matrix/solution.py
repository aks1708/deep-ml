def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              a_rows, a_cols = len(a), len(a[0])
              b_rows, b_cols = len(b), len(b[0])
              if a_cols != b_rows:
                return -1
              else:
                c = [[0]*b_cols for i in range(a_rows)]
                for i in range(a_rows):
                  for j in range(b_cols):
                    total = 0
                    for k in range(a_cols):
                      total += a[i][k] * b[k][j]
                    
                    c[i][j] = total
              
              return c
                
