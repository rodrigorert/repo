# Programa para contar palabras en un archivo de texto
# 1. Pedir al usuario la ruta de un archivo de texto. 
# 2. Leer el archivo
# 3. separar las palabras
# 4. contar las palabras
# 5. mostrar las 10 palabras mas frecuentes y su conteo

import re
from collections import Counter


class ContadorDePalabras:
    """
    Clase para contar palabras en archivos de texto.
    """
    
    def __init__(self):
        """
        Inicializa el contador compilando el patrón regex una vez
        para optimizar el rendimiento.
        """
        # Compilar el patrón regex una vez para reutilizarlo
        # Esto evita recompilar el patrón en cada llamada
        self._patron_palabra = re.compile(r"\w+", re.UNICODE)
    
    def leer_archivo(self, ruta):
        """
        Lee un archivo de texto y retorna su contenido.
        
        Args:
            ruta (str): Ruta del archivo a leer
            
        Returns:
            str: Contenido del archivo
            
        Raises:
            FileNotFoundError: Si el archivo no existe
            IOError: Si hay un error al leer el archivo
        """
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo especificado no existe: {ruta}")
        except IOError as e:
            raise IOError(f"Error al leer el archivo: {e}")
    
    def contar_palabras(self, texto):
        """
        Cuenta las palabras en una cadena de texto de forma optimizada.
        
        Optimizaciones aplicadas:
        - Usa un patrón regex precompilado
        - Usa finditer() en lugar de findall() para evitar crear listas grandes
        - Pasa directamente el generador a Counter para reducir uso de memoria
        
        Args:
            texto (str): Cadena de texto a analizar
            
        Returns:
            Counter: Contador con la frecuencia de cada palabra
        """
        # Usar finditer() en lugar de findall() para obtener un generador
        # Esto evita crear una lista completa en memoria
        # Convertir a minúsculas y buscar palabras directamente
        texto_lower = texto.lower()
        # finditer retorna un generador de objetos Match
        # Extraemos el grupo 0 (la palabra completa) de cada match
        palabras = (match.group(0) for match in self._patron_palabra.finditer(texto_lower))
        # Counter puede trabajar directamente con un generador
        return Counter(palabras)
    
    def contar_palabras_archivo(self, ruta):
        """
        Cuenta palabras en un archivo procesándolo línea por línea.
        Útil para archivos muy grandes que no caben en memoria.
        
        Optimizaciones aplicadas:
        - Procesa el archivo línea por línea sin cargar todo en memoria
        - Usa el patrón regex precompilado
        - Acumula resultados de forma eficiente
        
        Args:
            ruta (str): Ruta del archivo a procesar
            
        Returns:
            Counter: Contador con la frecuencia de cada palabra
            
        Raises:
            FileNotFoundError: Si el archivo no existe
            IOError: Si hay un error al leer el archivo
        """
        try:
            contador = Counter()
            with open(ruta, "r", encoding="utf-8") as f:
                # Procesar línea por línea para archivos grandes
                for linea in f:
                    texto_lower = linea.lower()
                    palabras = (match.group(0) for match in self._patron_palabra.finditer(texto_lower))
                    contador.update(palabras)
            return contador
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo especificado no existe: {ruta}")
        except IOError as e:
            raise IOError(f"Error al leer el archivo: {e}")


if __name__ == "__main__":
    contador = ContadorDePalabras()
    
    archivo = input("Introduce la ruta del archivo de texto: ")
    #archivo = D:\Documentos Trabajo y Estudio - Rodrigo Reyes\Cursos\Python_IA_Santander\contador_palabras\texto_de_prueba.txt

    try:
        texto = contador.leer_archivo(archivo)
    except (FileNotFoundError, IOError) as e:
        print(e)
        exit(1)

        
    # Contar palabras
    resultado = contador.contar_palabras(texto)
    total_palabras = sum(resultado.values())
    print(f"Total de palabras: {total_palabras}")

    mas_comunes = resultado.most_common(10)
    print("\nLas 10 palabras mas frecuentes:")
    for palabra, freq in mas_comunes:
        print(f"{palabra}: {freq}")

