# OLC 2 | PROYECTO 1  
## OLCScript

# 📋 Indice

- [Indice](#Indice)
- [Información](#Información)
- [Manual de usuario](#Manual-de-usuario)
    - [Archivos](#Archivos)
    - [Editar](#Editar)
    - [Consolas](#Consolas)
    - [Ejecutar](#Ejecutar)
- [Manual técnico](#Manual-técnico)
    - [Gramatica](#Gramatica)
    - [Herramientas utilizadas](#Herramientas-utilizadas)

# Información
OLCScript es un lenguaje de programación basado en el popular Typescript, conocido por su versatilidad al ser un lenguaje multiparadigma que ha ganado considerable popularidad gracias a su sintaxis moderna y diversas características distintivas. Este lenguaje no sólo hereda las ventajas de Typescript, sino que también incorpora funcionalidades avanzadas,como programación funcional, tipado estático, inferencia de tipos, entre otras. Estas características lo convierten en una herramienta moderna y eficiente, haciéndolo idóneo para su estudio y comprensión, especialmente en entornos de laboratorio.

<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/Principal.png" style="width:30rem"></a>
</div>

# Manual de usuario
El usuario cuenta con las herramientas para el análisis de código a traves de una área de código, donde se cuenta con consolas de salida, errores, y tambien reportes de errores, símbolos, funciones, y árbol CST.

## Archivos
Se cuenta con la opción de cargar archivos y guardar el archivo.

<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/Archivo.png" style="width:10rem"></a>
</div>

## Editar
Es la opción habilita la opción de escribir y/o modificar el texto en el área de código para su análisis.

<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/Editor.png" style="width:25rem"></a>
</div>

## Consolas
Se puede ver tanto la salida del código en consola,el listado de los errores y la tabla de simbolos.
<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/Consola.png" style="width:30rem"></a>
</div>
<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/Errores.png" style="width:30rem"></a>
</div>
<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/TablaSimbolos.png" style="width:30rem"></a>
</div>



## Ejecutar
Ejecuta el código escrito en el área de código.
<div align="center">
    <a href="" target="_blank"><img src="https://github.com/JulioFernandez99/COMPI2-P1/blob/main/Files/Consola.png" style="width:30rem"></a>
</div>

# Manual técnico

Para la realización de este proyecto se utilizó el lenguaje de programación Python, el cual nos permite realizar el análisis léxico, sintáctico y semántico del lenguaje OLCScript. Para la realización de la interfaz gráfica se utilizó TKinter.

## Gramatica

Gramatica utilizada con atlr4 para la realización del analizador sintáctico.

<details>
<summary>Gramtica</summary>
    
    init            : instrucciones

    instrucciones    : instrucciones instruccion
    
    instrucciones    : instruccion 
    
    instruccion      : imprimir PUNTOCOMA
                            | declaracion PUNTOCOMA
                            | asignacion PUNTOCOMA
                            | if_instr 
                            | if_else_instr 
                            | if_elseif_instr 
                            | if_elseif_else_instr
                            | for_instr
                            | while_instr
                            | switch_instr
                            | llamada_funcion_nativa PUNTOCOMA
                            | funcion_instr  
                            | call_funcion_instr PUNTOCOMA
                            | interface_instr
                            | delaracion_struct
                            | return_instr
                            | break_instr                        
                                 
    tipodeclaracion : LET
                | VAR
                | CONST
    
    lista_corchetes : lista_corchetes CORCHETEI CORCHETED 
                    | CORCHETEI CORCHETED CORCHETEI CORCHETED'''
     
    tipovar : NUMBER
                | FLOAT
                | STRING
                | BOOLEAN
                | CHAR
                | NUMBER CORCHETEI CORCHETED
                | FLOAT CORCHETEI CORCHETED
                | STRING CORCHETEI CORCHETED
                | BOOLEAN CORCHETEI CORCHETED
                | CHAR CORCHETEI CORCHETED
    
                | NUMBER lista_corchetes
                | FLOAT lista_corchetes
                | STRING lista_corchetes
                | BOOLEAN lista_corchetes
                | CHAR lista_corchetes
    
    listaExpresiones :  listaExpresiones COMA expresion
                        | expresion
                        
    arraylist : CORCHETEI listaExpresiones CORCHETED
        
    arraylist : CORCHETEI CORCHETED
    
    expresion : arraylist
    
    declaracion : tipodeclaracion ID DOSPUNTOS tipovar IGUAL expresion
    
    declaracion : tipodeclaracion ID IGUAL expresion
    
    declaracion : tipodeclaracion ID DOSPUNTOS tipovar
        
    asignacion : ID IGUAL expresion
    
    asignacion : ID CORCHETEI expresion CORCHETED IGUAL expresion
    
    asignacion : ID pos_matriz IGUAL expresion
    
    asignacion : ID AUMENTO expresion 
                      | ID DECREMENTO expresion  
    
    listaIf :  listaIf elseIF
                        | elseIF
     
    elseIF : ELSE if_instr
        
    if_instr           : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED
    
    if_else_instr      : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED ELSE LLAVEI instrucciones LLAVED
     
    if_elseif_instr   : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED listaIf
     
    if_elseif_else_instr   : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED listaIf ELSE LLAVEI instrucciones LLAVED
    
    actualizacion        : ID INCREMENTOFOR
    
    actualizacion        : ID DECREMENTOFOR     
    
    for_instr        : FOR PARENI declaracion PUNTOCOMA expresion PUNTOCOMA actualizacion PAREND LLAVEI instrucciones LLAVED
    
    for_instr        : FOR PARENI tipodeclaracion ID OF ID PAREND LLAVEI instrucciones LLAVED
    
    while_instr        : WHILE PARENI expresion PAREND LLAVEI instrucciones LLAVED
    
    listaCases : listaCases case
                        | case
    
    case : CASE expresion DOSPUNTOS instrucciones
        
    case : DEFAULT DOSPUNTOS instrucciones
    
    switch_instr        : SWITCH PARENI expresion PAREND LLAVEI listaCases LLAVED
    
    nativa_sin_parametros :     POP PARENI PAREND
                                      | JOIN PARENI PAREND
                                      | TSTRING PARENI PAREND
                                      | LC PARENI PAREND
                                      | UC PARENI PAREND
                                      | LENGTH
                                      
    llamada_funcion_nativa :    PUSH
                              | INDEXOF
    
    llamada_funcion_nativa :    expresion PUNTO nativa_sin_parametros
    
    llamada_funcion_nativa :    expresion PUNTO llamada_funcion_nativa PARENI listaExpresiones PAREND
    
    llamada_funcion_nativa :    TYPEOF expresion
    
    expresion : llamada_funcion_nativa
    
    expresion : TOINT PARENI expresion PAREND
    
    expresion : TOFLOAT PARENI expresion PAREND
        
    parametros_funcion : parametros_funcion COMA parametro_funcion
                        | parametro_funcion
    
    parametro_funcion : ID DOSPUNTOS tipovar
    
    parametro_funcion : ID DOSPUNTOS tipovar CORCHETEI  CORCHETED
    
    call_funcion_instr      : ID PARENI PAREND
        
    call_funcion_instr      : ID PARENI listaExpresiones PAREND
    
    funcion_instr      : FUNCTION ID PARENI parametros_funcion  PAREND LLAVEI instrucciones LLAVED
    
    
    funcion_instr      : FUNCTION ID PARENI PAREND LLAVEI instrucciones LLAVED
    
    interface_instr : INTERFACE ID LLAVEI interface_params PUNTOCOMA LLAVED
    
    interface_params : interface_params PUNTOCOMA ID DOSPUNTOS tipovar
                            | ID DOSPUNTOS tipovar
    
    delaracion_struct : expresion PUNTO expresion IGUAL expresion PUNTOCOMA
        
    expresion : expresion PUNTO expresion
        
    return_instr     : RETURN expresion PUNTOCOMA
                            | RETURN PUNTOCOMA
    
    break_instr     : BREAK PUNTOCOMA
    
    expresion : call_funcion_instr
    
    expresion : expresion MAS expresion
                      | expresion MENOS expresion
                      | expresion POR expresion
                      | expresion DIVIDIDO expresion
                      | expresion MOD expresion
        
    expresion : expresion MENORQ expresion
                      | expresion MAYORQ expresion
                      | expresion MAYORIGUALQ expresion
                      | expresion MENORIGUALQ expresion
                      | expresion IGUALIGUAL expresion
                      | expresion DIFERENTE expresion            
    
    expresion : expresion AND expresion
                      | expresion OR expresion
                      | NOT expresion
    
    expresion : PARENI expresion PAREND
    
    expresion    : ENTERO
        
    expresion    : DECIMAL
        
    expresion : FALSE
    
    expresion : TRUE
    
    expresion    : CADENA
    
    expresion    : CARACTER
    
    expresion    : ID
    
    expresion    : VACIO
    
    pos_matriz : pos_matriz CORCHETEI expresion CORCHETED
                        | CORCHETEI expresion CORCHETED CORCHETEI expresion CORCHETED
    
    expresion : ID pos_matriz
    
    expresion : ID CORCHETEI expresion CORCHETED
    
    expresion : MENOS expresion %prec UMENOS'
        t[0] = ExpresionNegativo(t[2])
        


</details>

## Herramientas utilizadas

- Python
- TKinter
- PLY
