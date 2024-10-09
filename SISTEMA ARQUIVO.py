import sys
from PyQt5 import QtWidgets, QtGui

# Definindo constantes
MEMORY_SIZE = 32

# Estruturas de dados
class Block:
    def __init__(self):
        self.data = ''  # Um caractere que representa parte do arquivo
        self.next_block = -1  # Ponteiro para o próximo bloco (-1 indica o final)

class File:
    def __init__(self, name, size, start_block):
        self.name = name
        self.size = size
        self.start_block = start_block

class FileSystem:
    def __init__(self):
        self.memory = [Block() for _ in range(MEMORY_SIZE)]
        self.file_table = []

    def find_free_blocks(self, size):
        free_count = 0
        for i in range(MEMORY_SIZE):
            if self.memory[i].data == '':
                free_count += 1
                if free_count == size:
                    return i - size + 1  # Retorna o índice do primeiro bloco livre
            else:
                free_count = 0  # Resetar contagem se encontrar um bloco usado
        return -1  # Não encontrou blocos livres

    def create_file(self, filename, content):
        if len(self.file_table) >= MEMORY_SIZE:
            return "Erro: Memória insuficiente para criar novos arquivos."

        if len(content) > MEMORY_SIZE:
            return "Erro: O conteúdo do arquivo é maior que a memória disponível."

        for f in self.file_table:
            if f.name == filename:
                return f"Erro: Arquivo '{filename}' já existe."

        start_block = self.find_free_blocks(len(content))
        if start_block == -1:
            return "Erro: Memória insuficiente."

        for i in range(len(content)):
            self.memory[start_block + i].data = content[i]
            self.memory[start_block + i].next_block = start_block + i + 1 if i < len(content) - 1 else -1

        self.file_table.append(File(filename, len(content), start_block))
        return f"Arquivo '{filename}' criado com sucesso."

    def read_file(self, filename):
        for f in self.file_table:
            if f.name == filename:
                block_index = f.start_block
                content = ""
                while block_index != -1:
                    content += self.memory[block_index].data
                    block_index = self.memory[block_index].next_block
                return f"Conteúdo do arquivo '{filename}': {content}"
        return f"Erro: Arquivo '{filename}' não encontrado."

    def delete_file(self, filename):
        for i, f in enumerate(self.file_table):
            if f.name == filename:
                block_index = f.start_block
                while block_index != -1:
                    next_block = self.memory[block_index].next_block
                    self.memory[block_index].data = ''  # Liberar o bloco
                    self.memory[block_index].next_block = -1
                    block_index = next_block

                del self.file_table[i]  # Remove o arquivo da tabela
                return f"Arquivo '{filename}' excluído com sucesso."
        return f"Erro: Arquivo '{filename}' não encontrado."

    def print_disk_state(self):
        disk_state = []
        for i, block in enumerate(self.memory):
            disk_state.append(f"Bloco {i}: '{block.data}', Próximo: {block.next_block}")
        return "\n".join(disk_state)

# Interface Gráfica
class FileSystemApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.file_system = FileSystem()

    def initUI(self):
        self.setWindowTitle("Simulador de Sistema de Arquivos")

        layout = QtWidgets.QVBoxLayout()

        self.create_button = QtWidgets.QPushButton("Criar Arquivo")
        self.create_button.clicked.connect(self.create_file)
        layout.addWidget(self.create_button)

        self.read_button = QtWidgets.QPushButton("Ler Arquivo")
        self.read_button.clicked.connect(self.read_file)
        layout.addWidget(self.read_button)

        self.delete_button = QtWidgets.QPushButton("Excluir Arquivo")
        self.delete_button.clicked.connect(self.delete_file)
        layout.addWidget(self.delete_button)

        self.state_button = QtWidgets.QPushButton("Estado do Disco")
        self.state_button.clicked.connect(self.show_disk_state)
        layout.addWidget(self.state_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def create_file(self):
        filename, ok = QtWidgets.QInputDialog.getText(self, "Criar Arquivo", "Nome do arquivo:")
        if ok:
            content, ok = QtWidgets.QInputDialog.getText(self, "Criar Arquivo", "Conteúdo do arquivo:")
            if ok:
                message = self.file_system.create_file(filename, content)
                QtWidgets.QMessageBox.information(self, "Resultado", message)

    def read_file(self):
        filename, ok = QtWidgets.QInputDialog.getText(self, "Ler Arquivo", "Nome do arquivo:")
        if ok:
            message = self.file_system.read_file(filename)
            QtWidgets.QMessageBox.information(self, "Resultado", message)

    def delete_file(self):
        filename, ok = QtWidgets.QInputDialog.getText(self, "Excluir Arquivo", "Nome do arquivo:")
        if ok:
            message = self.file_system.delete_file(filename)
            QtWidgets.QMessageBox.information(self, "Resultado", message)

    def show_disk_state(self):
        disk_state = self.file_system.print_disk_state()
        QtWidgets.QMessageBox.information(self, "Estado do Disco", disk_state)

# Executando a aplicação
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = FileSystemApp()
    sys.exit(app.exec_())