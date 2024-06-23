# usando el import y el "as"
import modulo_saludar as m_saludar


saludo = m_saludar.saludar("limber")
print(saludo)

# haciendo uso del from y uso del "as"

from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_diferente

saludo = saludar_normal("limber")
saludo_raro = saludar_diferente("fer")

print(saludo)
print(saludo_raro)

