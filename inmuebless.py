class Inmueble:
    def __init__(self,codigo,direccion,telefono):
        self.__codigo = codigo
        self.__direccion = direccion
        self.__telefono = telefono

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self,direccion):
        self.__direccion = direccion

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono = telefono

    def radicar(self, codigo):
        self.__codigo = codigo

    def arrendar(self,codigo):
        self.__codigo = codigo

class Oficina(Inmueble):
    internet = False
    def __init__(self, codigo, direccion, telefono, salaAsamblea):
        Inmueble.__init__(self, codigo, direccion, telefono)
        self.__salaAsamblea = salaAsamblea
    
    def instalarInternet(self):
        self.internet = True

    def estadoInternet(self):
        if(self.internet):
            return "Instalando internet.."
        else:
            return "Internet no instalado"

class Casa(Inmueble):
    repJardin = False
    def __init__(self, codigo, direccion, telefono, nroHabitaciones):
        Inmueble.__init__(self, codigo, direccion, telefono)
        self.__nroHabitaciones = nroHabitaciones  

    @property
    def nroHabitaciones(self):
        return self.__nroHabitaciones
    @nroHabitaciones.setter
    def nroHabitaciones(self, nroHabitaciones):
        self.__nroHabitaciones = nroHabitaciones

    def repararJardin(self):
        self.repJardin = True 

    def estadoDelJardin(self):
        if(self.repJardin):
            return "Jardin reparado"
        else:
            return "Jardin dañado..."

asd = Casa("12", "crra nro", "3013621", "2")
print(asd.codigo)
#asd.repararJardin()
print(asd.estadoDelJardin())
asd.arrendar("13")
print(asd.codigo)
