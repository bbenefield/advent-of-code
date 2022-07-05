with open('2015/day2/day2input.txt', 'r') as fin:
    data = fin.readlines()

# Part A 
area: int = 0

for dim in data:
    dim_values: list[int] = [int(val) for val in dim.strip().split('x')]
    
    area += 2*dim_values[0]*dim_values[1] + 2*dim_values[1]*dim_values[2] + 2*dim_values[0]*dim_values[2]
    
    dim_values.sort()
    
    area += dim_values[0] * dim_values[1]
      
print(f'Total area: {area}')

# Part B

area: int = 0

for dim in data:
    dim_values: list[int] = [int(val) for val in dim.strip().split('x')]
    dim_values.sort()
    
    area += 2*dim_values[0] + 2*dim_values[1]
    area += dim_values[0] * dim_values[1] * dim_values[2]
    
print(f'Total area: {area}')