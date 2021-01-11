'''
1. Implemente una base de datos que posea 4 tablas para almacenar datos provenientes de 
    * 7 sensores de temperatura, 
    * 3 sensores de apertura de una puerta de bodega, 
    * 4 sensores de nivel discreto de estanque de gasolina (“Bajo”, “Medio”, “Alto”), 
    * Códigos numéricos ingresados por un usuario que intenta abrir una puerta de acceso. 
2. Cada registro debe almacenar, nombre de sensores, fecha/hora-minuto-segundo del dato sensado.
3. Cree la sintaxis de las instrucciones en Django para poblar las tablas de la base de datos mencionada.
4. Llene las tablas con al menos 10 registros diferentes, cada una.
5. Muestre en templates Django los datos de las 4 tablas de sensores.

* Tabla sensor_temperatura
    * id
    * idsensor_temp: {'temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6', 'temp7'} 
    * fecha_temp
    * medicion_temp {15,250} en celsius
* Tabla puerta_bodega
    * id
    * idsensor_bodega: {'bod1', 'bod2', 'bod3'}
    * fecha_bodega
    * apertura_bodega {1,0}
* Tabla estanque_gasolina
    * id
    * idsensor_estanque: {'estanque1', 'estanque2', 'estanque3', 'estanque4'}
    * fecha_estanque
    * nivel_estanque {'Bajo','Medio','Alto'}
* Tabla apertura_puerta
    * id
    * id_puerta: {'temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6', 'temp7','bod1', 'bod2', 'bod3','estanque1', 'estanque2', 'estanque3', 'estanque4'}
    * id_usuario: random {1,5}
    * fecha_apertura
    * codigo_apertura random numerico de 6 caracteres
'''

# imports
import random
from string import digits

# Sensor temperatura
idsensor_temp=random.choice(['temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6', 'temp7'])
medicion_temp =random.randint(15,250)

# Puerta bodega
idsensor_bodega=random.choice(['bod1', 'bod2', 'bod3'])
apertura_bodega=random.choice([0,1])

# Estanque gasolina
idsensor_estanque=random.choice(['estanque1', 'estanque2', 'estanque3', 'estanque4'])
nivel_estanque=random.choice(['Bajo','Medio','Alto'])

# Apertura puerta
id_puerta=random.choice(['temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6', 'temp7','bod1',
                         'bod2', 'bod3','estanque1', 'estanque2', 'estanque3', 'estanque4'])
id_usuario=random.randint(1,5)

#codigo apertura random
secure_random = random.SystemRandom()
codigo_apertura="".join(secure_random.choice(digits) for i in range(6))
						 
						 
						 
						 
						 
						 
						 
						 
						 