



def procesar_llamada_funcion(instr, ts):
    from procesos.procesar_funcion import procesar_funcion
    #print("Procesar llamada a funcion************")
    
    procesar_funcion(instr, ts)
    fun_ = ts.obtener(instr.id)
    retorno = fun_.retorno
    #print("Retorno de la funcion: ", retorno)
    return retorno