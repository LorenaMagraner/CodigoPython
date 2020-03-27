

class Animal:

    organos = []

    def __init__(self, organos_):

        self.organos = organos_


class Mamifero(Animal):
    # variables globales
    pelo = True
    patas = 0
    tiempo_gestacion = 0

    def __init__(self, pelo_, patas_, tiempo_gestacion_):

        Animal.__init__(self, organos_=['ojos', 'estomago', 'corazon'])

        self.pelo = pelo_
        self.patas = patas_
        self.tiempo_gestacion = tiempo_gestacion_


class Perro(Mamifero):

    nombre = ''
    cola = True
    castracion = False
    raza = None

    def __init__(self, nombre_, cola_, castracion_, raza_):
        """
        constructor de la clase Perro. Es la funcion que se ejecuta al crear un objeto Perro
        :param cola_: variable booleana
        :param castracion_: variable booleana
        :param raza_: None, aunque cuando cree el objeto (pancho = Perro (col.....) raza sera "Jack_Russel"
        """

        # inicializar a la clase padre
        Mamifero.__init__(self, pelo_=True, patas_=4, tiempo_gestacion_=2)

        # inicializar las variables de la clase
        self.nombre = nombre_
        self.cola = cola_
        self.castracion = castracion_
        self.raza = raza_

    def ladrar(self):
        print('Guau!')

    def __str__(self):

        val = '\nSoy ' + self.nombre
        val += '\ncola: ' + str(self.cola)
        val += '\ncastracion: ' + str(self.castracion)
        val += '\nraza: ' + str(self.raza)
        val += '\npelo: ' + str(self.pelo)
        val += '\npatas: ' + str(self.patas)
        val += '\ntiempo gestacion: ' + str(self.tiempo_gestacion)
        val += '\norganos: ' + str(self.organos)

        return val

    def guardar(self):
        text_file = open(self.nombre + ".txt", "w")
        text_file.write(self.__str__())
        text_file.close()


########################################################################################################################
########################################################################################################################
########################################################################################################################
# ESTO YA NOS SON LAS CLASEEEES
# ESTO ES UN TROZO DE CODIGO PARA PROBAR LAS CLASESS!!!!!!!!!
########################################################################################################################
if __name__ == '__main__':

    pancho = Perro(nombre_='Pancho', cola_=True, castracion_=False, raza_='Jack_Russel')
    pancho.ladrar()
    pancho.guardar()
    print(pancho)

    nieve = Perro(nombre_='Nieve', cola_=True, castracion_=False, raza_='Labrador')
    nieve.ladrar()
    nieve.guardar()
    print(nieve)