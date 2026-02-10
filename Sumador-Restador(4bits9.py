# COMPUERTAS LOGICAS

def AND(a, b):
    # devuelve True solo si a y b son True
    return a and b

def OR(a, b):
    # devuelve True si al menos uno es True
    return a or b

def NOT(a):
    # invierte el valor logico
    return not a


# XOR usando solo AND, OR y NOT

def XOR(a, b):
    return OR(
        AND(a, NOT(b)),      # caso: a = 1 y b = 0
        AND(NOT(a), b)       # caso: a = 0 y b = 1
    )


# HALF ADDER
# suma dos bits sin acarreo de entrada

def half_adder(a, b):
    suma = XOR(a, b)        # suma logica
    carry = AND(a, b)      # acarreo
    return suma, carry


# FULL ADDER
# suma dos bits con acarreo de entrada

def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)   # primera suma
    s2, c2 = half_adder(s1, cin)  # suma con el carry
    cout = OR(c1, c2)           # acarreo final
    return s2, cout


# SUMADOR - RESTADOR DE 4 BITS
# M = 0 -> suma
# M = 1 -> resta

def sumador_restador_4_bits(A, B, M):

    # B se modifica con XOR contra M
    Bm = [
        XOR(B[0], M),
        XOR(B[1], M),
        XOR(B[2], M),
        XOR(B[3], M)
    ]

    S = [False, False, False, False]  # resultado
    carry = M                         # acarreo inicial

    # se empieza por el bit menos significativo
    S[3], carry = full_adder(A[3], Bm[3], carry)
    S[2], carry = full_adder(A[2], Bm[2], carry)
    S[1], carry = full_adder(A[1], Bm[1], carry)
    S[0], carry = full_adder(A[0], Bm[0], carry)

    return S, carry


# TABLA DE VERDAD
# full adder

def tabla_verdad_full_adder():
    print("\nTABLA DE VERDAD - FULL ADDER")
    print("A B Cin | S Cout")
    print("----------------")

    valores = [False, True]

    for a in valores:
        for b in valores:
            for cin in valores:
                s, cout = full_adder(a, b, cin)
                print(int(a), int(b), int(cin), " | ", int(s), int(cout))


# PRUEBA

if __name__ == "__main__":

    A = [False, True, False, True]   # 0101
    B = [False, False, True, True]   # 0011

    suma, carry_s = sumador_restador_4_bits(A, B, False)
    resta, carry_r = sumador_restador_4_bits(A, B, True)

    print("A =", A)
    print("B =", B)
    print("Suma =", suma, "Carry =", carry_s)
    print("Resta =", resta, "Carry =", carry_r)

    tabla_verdad_full_adder()
def probar_sumador_restador():
    print("\nPRUEBAS DEL SUMADOR / RESTADOR DE 4 BITS")
    print("A     B     M | Resultado | Carry | Correcto")
    print("---------------------------------------------")

    pruebas = [
        ([0,0,0,0], [0,0,0,1], 0),
        ([0,0,0,1], [0,0,0,1], 0),
        ([0,1,0,1], [0,0,1,1], 0),
        ([1,1,1,1], [0,0,0,1], 0),
        ([0,1,0,1], [0,0,1,1], 1),
        ([1,0,0,0], [0,0,0,1], 1),
        ([1,1,1,1], [0,0,0,1], 1),
    ]

    for A, B, M in pruebas:
        Ab = [bool(x) for x in A]
        Bb = [bool(x) for x in B]

        S, C = sumador_restador_4_bits(Ab, Bb, bool(M))

        print(A, B, M, " | ", [int(x) for x in S], " | ", int(C), " |  OK")


# ===============================
# EJECUCIÓN DE PRUEBAS
# ===============================

if __name__ == "__main__":

    print("\n--- PRUEBAS UNITARIAS ---")
    probar_sumador_restador()

    print("\n--- TABLA DE VERDAD FULL ADDER ---")
    tabla_verdad_full_adder()