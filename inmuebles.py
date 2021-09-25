class Inmueble:
    def __init__(self, codigo, direccion, telefono):
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono

    def Radicar(self):
        return self.codigo

    def Arrendar(self):
        return self.codigo

class Casa(Inmueble):
    def __init__(self, codigo, direccion, telefono, nroHabitaciones):
        Inmueble.__init__(self, codigo, direccion, telefono)
        self.nroHabitaciones = nroHabitaciones 

    def repararJardin(self):
        return 'Reparando el jardin'

class Oficina(Inmueble):
    def __init__(self, codigo, direccion, telefono, salaAsamblea):
        Inmueble.__init__(self, codigo, direccion, telefono)
        self.salaAsamblea = salaAsamblea

    def instalarInternet(self):
        return 'Instalando internet..'



office = Oficina("12412","12-asd","31796432","as")
print(office.codigo)
office.Arrendar()
casita = Casa("54","asd-122","3120023","3")
print(casita.direccion)
casita.repararJardin()
casita.Radicar()