import os
from dataclasses import dataclass, field
from typing import List, Callable

@dataclass
class Config:
    # Extensiones de archivos a incluir (ejemplo: ['.py', '.md'])
    include_extensions: List[str] = field(default_factory=lambda: ['.py', '.md'])
    # Nombres y extensiones a ignorar
    ignore_names: List[str] = field(default_factory=lambda: ['__pycache__', '.git'])
    ignore_extensions: List[str] = field(default_factory=lambda: ['.log', '.tmp'])
    # Funciones predicate para seleccionar archivos y directorios
    def file_predicate(self, filename: str) -> bool:
        # Selecciona archivos que tengan una extensión permitida y no estén en la lista de ignorados
        ext = os.path.splitext(filename)[1]
        if filename in self.ignore_names:
            return False
        if ext in self.ignore_extensions:
            return False
        return ext in self.include_extensions

    def dir_predicate(self, dirname: str) -> bool:
        # Ignora los directorios en la lista ignore_names
        return dirname not in self.ignore_names

def generate_tree(
    root_path: str,
    config: Config,
    prefix: str = ''
) -> str:
    """
    Genera una representación en Markdown del árbol de directorios.
    """
    markdown_lines = []

    def recurse(current_path: str, current_prefix: str):
        try:
            entries = sorted(os.listdir(current_path))
        except PermissionError:
            return

        # Filtrar directorios y archivos
        entries_dirs = [e for e in entries if os.path.isdir(os.path.join(current_path, e)) and config.dir_predicate(e)]
        entries_files = [e for e in entries if os.path.isfile(os.path.join(current_path, e)) and config.file_predicate(e)]

        for index, dir_name in enumerate(entries_dirs):
            connector = '├── ' if index < len(entries_dirs) - 1 or entries_files else '└── '
            line = f"{current_prefix}{connector}{dir_name}"
            markdown_lines.append(line)
            # Si no es la última, usar | para continuar
            extension_prefix = '│   ' if index < len(entries_dirs) - 1 or entries_files else '    '
            recurse(os.path.join(current_path, dir_name), current_prefix + extension_prefix)

        for index, file_name in enumerate(entries_files):
            connector = '├── ' if index < len(entries_files) - 1 else '└── '
            line = f"{current_prefix}{connector}{file_name}"
            markdown_lines.append(line)

    # Encabezado
    # markdown_lines.append(f"# Árbol de la carpeta: {root_path}")
    recurse(root_path, '')
    return '\n'.join(markdown_lines)

# config = Config(
    #     include_extensions=['.py', '.md', '.txt'],  # Extensiones a incluir
    #     ignore_names=['__pycache__', '.git', '.vscode','migrations','admin.py','apps.py','endpoints.py','factory.py','models.py','serializers.py','urls.py','utils.py'],  # Nombres a ignorar
    #     ignore_extensions=['.log', '.tmp']  # Extensiones a ignorar
    # )

# carpeta_raiz = 'D:\\TRABAJO\\Crinnotech\\Proyecto Gran Azul\\multicorelink\\affiliates'  # Reemplaza con la ruta que deseas analizar

if __name__ == "__main__":
    # Configuración
    config = Config(
        include_extensions=['.py', '.md', '.txt','.html'],  # Extensiones a incluir
        ignore_names=['__pycache__', '.git', '.vscode','migrations',],  # Nombres a ignorar
        ignore_extensions=['.log', '.tmp']  # Extensiones a ignorar
    )
    

    # Carpeta raíz a analizar
    carpeta_raiz = 'D:\\TRABAJO\\Crinnotech\\Proyecto Gran Azul\\multicorelink\\templates\\commercials\\affiliates'  # Reemplaza con la ruta que deseas analizar

    # Generar y guardar el árbol en un archivo Markdown
    arbol_markdown = generate_tree(carpeta_raiz, config)
    with open('arbol_carpeta.md', 'w', encoding='utf-8') as f:
        f.write('```\n')
        f.write(arbol_markdown)
        f.write('\n```')

    print("Archivo 'arbol_carpeta.md' generado con éxito.")
