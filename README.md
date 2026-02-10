# Sumador y Restador Binario de 4 Bits

Este proyecto implementa un **sumador y un restador binario de 4 bits** en Python,
simulando el comportamiento de **circuitos de electrónica digital**.

La lógica del programa se construye **exclusivamente utilizando las compuertas
AND, OR y NOT**, respetando estrictamente la restricción académica del ejercicio.

---

##  Restricción principal

Durante la implementación **NO se utilizan**:
- Operadores aritméticos (`+`, `-`)
- XOR nativo
- Comparaciones (`==`, `<`, `>`)
- Operadores binarios propios de Python

La lógica del circuito usa únicamente:
- AND
- OR
- NOT

---

##  ¿Cómo funciona el programa?

###  Suma binaria
- La suma se realiza **bit a bit**, iniciando desde el bit menos significativo.
- Cada operación se lleva a cabo mediante un **Full Adder**.
- El **acarreo** se transfiere al siguiente bit, como en un circuito real.

###  Resta binaria
- La resta se implementa utilizando el **complemento a 2**.
- Se invierten los bits del segundo número (NOT).
- Se suma 1 al resultado.
- Finalmente, se suma este valor al primer número usando el mismo sumador de 4 bits.

---

##  Descripción general del código

El código está organizado de forma modular, representando bloques de un circuito digital:

- **Compuertas lógicas**: funciones AND, OR y NOT.
- **XOR lógico**: construido únicamente con compuertas básicas.
- **Half Adder**: suma dos bits sin considerar acarreo de entrada.
- **Full Adder**: suma dos bits teniendo en cuenta el acarreo.
- **Sumador de 4 bits**: encadena cuatro Full Adders.
- **Complemento a 2**: permite realizar la resta binaria.
- **Restador de 4 bits**: reutiliza el sumador para calcular A − B.
- **Tabla de verdad**: se muestra la tabla de verdad del Full Adder.

Los bits se representan de la siguiente manera:
- `False` → 0
- `True` → 1

---
##  Explicación de la tabla de verdad del sumador completo

La tabla de verdad representa el comportamiento de un **sumador completo (Full Adder)**, el cual es el bloque fundamental del sumador de 4 bits implementado en este programa.

El sumador completo recibe **tres entradas**:

- **A**: primer bit a sumar  
- **B**: segundo bit a sumar  
- **Cin**: acarreo de entrada (carry-in), proveniente del bit anterior  

Y produce **dos salidas**:

- **S**: bit de suma  
- **Cout**: acarreo de salida (carry-out), que pasa al siguiente bit  

---

###  ¿Por qué se obtiene cada salida?

| A | B | Cin | S | Cout | Explicación |
|---|---|-----|---|------|------------|
| 0 | 0 | 0 | 0 | 0 | No hay bits activos, la suma es 0 y no se genera acarreo |
| 0 | 0 | 1 | 1 | 0 | Solo hay acarreo de entrada, la suma es 1 |
| 0 | 1 | 0 | 1 | 0 | Un solo bit activo, la suma es 1 |
| 0 | 1 | 1 | 0 | 1 | 1 + 1 = 10, suma 0 y acarreo 1 |
| 1 | 0 | 0 | 1 | 0 | Un solo bit activo, la suma es 1 |
| 1 | 0 | 1 | 0 | 1 | 1 + 1 = 10, suma 0 y acarreo 1 |
| 1 | 1 | 0 | 0 | 1 | 1 + 1 = 10, suma 0 y acarreo 1 |
| 1 | 1 | 1 | 1 | 1 | 1 + 1 + 1 = 11, suma 1 y acarreo 1 |

---

###  Interpretación general

- La **suma (S)** es `1` cuando hay una **cantidad impar de unos** en las entradas.
- El **acarreo (Cout)** es `1` cuando **al menos dos entradas son 1**.
- Esta lógica se implementa en el código utilizando exclusivamente **AND, OR y NOT**.
- Al encadenar varios sumadores completos, el acarreo de salida de un bit se convierte en el acarreo de entrada del siguiente bit, permitiendo sumar números de varios bits.

Esta tabla demuestra que el circuito implementado cumple correctamente con las reglas de la suma binaria.










##  Cómo compilar / ejecutar el programa

> Python no se compila, se **ejecuta directamente**.

### Requisitos
- Tener **Python 3** instalado.

### Pasos para ejecutar

1. Abrir una terminal o consola.
2. Ubicarse en la carpeta donde se encuentra el archivo usando el comando `cd`.

Ejemplo en Windows:

```bash
cd Documents
cd ProyectoLogica

python sumador_restador_4bits.py
