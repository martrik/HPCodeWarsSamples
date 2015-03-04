def calculate_check_digit(code):
    odd_pos = code[0]+code[2]+code[4]+code[6]+code[8]+code[10]
    even_pos = int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])

    multiply_odd_by_three = int(odd_pos)*3
    add_even = multiply_odd_by_three + even_pos
    modulo_ten = add_even % 10

    return 10 - modulo_ten

inp = int(input())

for i in range(inp):
    upc = input()
    code = upc[0]+upc[2]+upc[4]+upc[6]+upc[8]+upc[10]+upc[12]+upc[14]+upc[16]+upc[18]+upc[20]
    check_code = calculate_check_digit(code)
    print(upc + " " + str(check_code))