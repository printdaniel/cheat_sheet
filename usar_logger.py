#########################################################
# ! Utilización de logger para debuggear
#########################################################

""" 
Logger es un módulo de registro de eventos en Python que se utiliza para recopilar 
información sobre los eventos que ocurren en una aplicación. Los registros 
son útiles para el análisis y la depuración de la aplicación, así como para 
mantener un registro de las actividades de la aplicación.
"""

import logging

"""
Configura el nivel de registro adecuado para el módulo logger. El nivel de 
registro indica el tipo de mensajes que se registran. Por ejemplo, si se 
establece el nivel de registro en DEBUG, se registrarán mensajes de depuración, 
información, advertencias y errores.
"""
logging.basicConfig(level=logging.DEBUG)
""" 
Crea un objeto logger utilizando el método getLogger() del módulo logging. 
Puedes pasar el nombre del objeto logger como argumento. El nombre es útil 
si deseas crear varios objetos logger en tu aplicación.
"""
logger = logging.getLogger('my_app')
""" 
Utiliza el objeto logger para registrar mensajes en tu aplicación utilizando 
los métodos de registro disponibles (debug(), info(), warning(), error() y 
critical()).
"""

logger.debug('Este es un mensaje de depuración')
logger.info('Este es un mensaje de información')
logger.warning('Este es un mensaje de advertencia')
logger.error('Este es un mensaje de error')
logger.critical('Este es un mensaje crítico')

"""Opcionalmente, puedes utilizar formateadores para personalizar la forma en 
que se registran los mensajes. Por ejemplo, puedes utilizar el formateador de 
registro predeterminado de la siguiente manera:

"""
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)



