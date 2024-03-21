from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos

def procesar_while(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    #print("procesar_while-----")
    expLog = resolver_expresion(instr.expLogica, ts)
    
    while expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        brk=procesar_instrucciones(instr.instrucciones,TablaLocal)
        if brk=="TB":
            break
        elif brk=="TC":
            continue
        ts.salida+=TablaLocal.salida
        expLog = resolver_expresion(instr.expLogica, ts)
        
        