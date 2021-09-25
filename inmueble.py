class Inmueble:
    def __init__(self, codigo, direccion, telefono):
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono
    
    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def Radicar(self):
        return self.codigo

    def Arrendar(self, codigo):
        self.codigo = codigo


class Oficina(Inmueble):
    def __init__(self, codigo, direccion, telefono, salaAsamble):
        Inmueble.__init__(codigo, direccion, telefono)
        self.salaAsamble = salaAsamble

    def instalarInternet(self):
        print("Instalando internet...")

class Casa(Inmueble):
    eljarin = True
    def __init__(self, codigo, direccion, telefono, nroHabitaciones):
        Inmueble.__init__(codigo, direccion, telefono)
        self.nroHabitaciones = nroHabitaciones

    def getNroHabitaciones(self):
        return self.nroHabitaciones

    def setNroHabitaciones(self, nroHabitaciones):
        self.nroHabitaciones = nroHabitaciones

    def repararJardin(self):
        return "Reparando el Jardin"

    