


from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos


def procesar_if_elif_else(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    expLog = resolver_expresion(instr.expLogica, ts)
    TablaLocal = None
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        procesar_instrucciones(instr.instrIfVerdadero,TablaLocal)
        ts.salida+=TablaLocal.salida
    else:
        for data in instr.instrIfFalso:
            expLog = resolver_expresion(data.expLogica, ts)
            if expLog:
                TablaLocal = TablaSimbolos(ts.simbolos.copy()) 
                procesar_instrucciones(data.instrucciones,TablaLocal)
                ts.salida+=TablaLocal.salida
                return
            
        TablaLocal = TablaSimbolos(ts.simbolos.copy()) 
        procesar_instrucciones(instr.instrIfElse,TablaLocal)
        ts.salida+=TablaLocal.salida
        ts.errores+=TablaLocal.errores
        