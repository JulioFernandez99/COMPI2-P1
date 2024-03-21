from tabla.tablaSimbolos import TIPO_DATO, Simbolos


def guardar_funcion(instr, ts):
    funcion_id = instr.id

    #print("instrucciones***********",instr.instrucciones)
    #print("parametros***********",instr.parametros  )
    
    simbolo = Simbolos(funcion_id, TIPO_DATO.FUNCION,None, instrucciones=instr.instrucciones, parametros=instr.parametros)
    ts.agregar(simbolo)