
# Aqui se define el tipo de instrucciones que se van a recibir

class Instruccion:
    '''Clase abs de instrucciones'''


class Imprimir(Instruccion):

    def __init__(self,  cad) :
        self.cad = cad

class Declaracion(Instruccion):
    def __init__(self, id, exp,tipovar,tipodec):
        self.id = id
        self.exp = exp
        self.tipovar = tipovar
        self.tipodec = tipodec
        
class Asignacion(Instruccion):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
        
class AsignacionPosicionArray(Instruccion):
    def __init__(self, id, posicion, exp):
        self.id = id
        self.exp = exp
        self.posicion = posicion
        
class AsignacionOperador(Instruccion):
    def __init__(self, id, exp, operador):
        self.id = id
        self.exp = exp
        self.operador = operador

class If(Instruccion):
    def __init__(self, expLogica, instrucciones = []):
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        
class IfElse(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = []):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso
        
class Elif(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = []):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso

class Elif_ELSE(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = [],instrIfElse = []):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso
        self.instrIfElse = instrIfElse
        
class ACTUALIZACIONFOR(Instruccion):
    def __init__(self, id, operador):
        self.id = id
        self.operador = operador

class For(Instruccion):
    def __init__(self,declaracion, expLogica, actualizacion, instrucciones = []):
        self.declaracion = declaracion
        self.expLogica = expLogica
        self.actualizacion = actualizacion
        self.instrucciones = instrucciones
        
class ForOf(Instruccion):
    def __init__(self, idDeclaracion,idDeclarada, instrucciones = []):
        self.idDeclaracion = idDeclaracion
        self.idDeclarada = idDeclarada
        self.instrucciones = instrucciones
        
class While(Instruccion):
    def __init__(self, expLogica, instrucciones = []):
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        

class Case(Instruccion):
    def __init__(self, exp, instrucciones=[] ):
        self.expLogica = exp
        self.instrucciones = instrucciones
        
        
class Switch(Instruccion):
    def __init__(self, expLogica, casos = []):
        self.expLogica = expLogica
        self.casos = casos
        
class LlamadaNativaSinParamtros(Instruccion):
    def __init__(self, id, funcion):
        self.id = id
        self.funcion = funcion
        
class LlamadaNativaConParamtros(Instruccion):
    def __init__(self, id, funcion, parametro):
        self.id = id
        self.funcion = funcion
        self.parametro = parametro

class Parseo(Instruccion):
    def __init__(self, tipo,expresion):
        self.tipo = tipo
        self.exp = expresion
        
class LlamadaNativaTypeOf(Instruccion):
    def __init__(self,expresion):
        self.exp = expresion
        
class Function(Instruccion):
    def __init__(self, id, parametros = [], instrucciones = [],exp = None):
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.exp = exp

class CallFunction(Instruccion):
    def __init__(self, id, parametros = []):
        self.id = id
        self.parametros = parametros

class Parametro(Instruccion):
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        
class Interface(Instruccion):
    def __init__(self, id, props = []):
        self.id = id
        self.props = props
        
