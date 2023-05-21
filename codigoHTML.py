import re

def escape_html(text):
    map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;',
        'á': '&aacute;',
        'é': '&eacute;',
        'í': '&iacute;',
        'ó': '&oacute;',
        'ú': '&uacute;',
        'ñ': '&ntilde;'
    }
    return re.sub(r'[&<>"\'áéíóúñ]', lambda m: map[m.group()], text)

texto = """
CEGED tiene como misión promover y ejecutar la investigación, capacitación y superación en el desarrollo, uso y manejo de sistema de conocimientos y de información agrario y rural con el objetivo de desarrollar programas y actividades de investigación, asesoramiento, capacitación, estudio y diseminación, tendientes al avance del conocimiento y de la información agraria y rural con para así promover procesos de desarrollo local sustentables.
"""
texto_html = escape_html(texto)
print(texto_html)