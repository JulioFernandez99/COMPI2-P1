






from instrucciones.instrucciones import Asignacion, Declaracion
from procesos.procesar_asignacion import procesar_asignacion
from procesos.procesar_declaracion import procesar_declaracion

from tabla.tablaSimbolos import TIPO_DATO, Simbolos, TablaSimbolos


def procesar_funcion(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    from procesos.procesar_instrucciones import procesar_instrucciones
    
    paramesRecive = instr.parametros   

    fun_ = ts.obtener(instr.id)
    instrucciones = fun_.instrucciones
    parametros = fun_.parametros
    
    # print("parametros",parametros)
    # print("paramesRecive",paramesRecive)
    # print("instrucciones",instrucciones)
    
    
    TablaLocal = TablaSimbolos(ts.simbolos.copy())
    
    if len(parametros) == len(paramesRecive):
        for i in range(len(paramesRecive)):
            val=resolver_expresion(paramesRecive[i], ts)
            simbolo = Simbolos(parametros[i].id, parametros[i].tipo,val)
            TablaLocal.agregar(simbolo)
            
    else:
        print("Error: la cantidad de parametros no coincide")
        ts.errores+="Error: la cantidad de parametros no coincide\n"
        return
    
    # if len(parametros) == len(paramesRecive):
    #     for i in range(len(paramesRecive)):
            
            
    #         val=resolver_expresion(paramesRecive[i], ts)
    #         print("val--------",val)
    #         simbolo = Simbolos(parametros[i].id, parametros[i].tipo,val)
    #         TablaLocal.agregar(simbolo)
    # else:
    #     print("Error: la cantidad de parametros no coincide")
    #     return
        
        
    procesar_instrucciones(instrucciones, TablaLocal)
    ts.salida+=TablaLocal.salida
    ts.errores+=TablaLocal.errores

    # #imprmir tabla local
    # print('Tabla de simbolos:')
    # for simbolo in TablaLocal.simbolos.values():
    #     print(simbolo.id, simbolo.tipo, simbolo.valor)
        
    # print("--------------------------------------------")
            
       
    
        

       