import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from Automata2 import Automata

class VariableAnalyzerApp:
    def __init__(self, root):
        self.validator = Automata()
        self.root = root
        self.root.title("MultiLangVarDetector")

        self.root.configure(bg='#f0f4f8')  
        self.style = ttk.Style()
        
        self.style.configure('TButton', font=('Arial', 12), background='#89c9e8', foreground='#ffffff')
        self.style.map('TButton', background=[('active', '#89c9e8')])  

        self.create_widgets()
       
    def create_widgets(self):
        """Crear los elementos de la interfaz gráfica con colores y estilo mejorado."""
        title_label = ttk.Label(self.root, text="Analizador de Variables", style='TLabel')
        title_label.pack(pady=10)

        self.select_button = ttk.Button(self.root, text="Seleccionar archivo", command=self.select_file)
        self.select_button.pack(pady=10)

        self.report_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=20, font=('Consolas', 10))
        self.report_text.pack(pady=10)

        # Botón para descargar el reporte
        self.download_button = ttk.Button(self.root, text="Descargar reporte", command=self.download_report)
        self.download_button.pack(pady=10)

    def select_file(self):
        """Seleccionar un archivo C++ y procesar su contenido."""
        file_path = filedialog.askopenfilename(filetypes=[("Archivos C++", "*.cpp")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()

            self.validate(content)

    def validate(self, declarations):
        results = []
        # Separar el contenido en líneas y quitar espacios en blanco
        lines = declarations.splitlines()
        cleaned_lines = [line.strip() for line in lines]  # Quitar espacios en blanco de cada línea
        print(cleaned_lines)
        
        for index, declaration in enumerate(cleaned_lines, start=1):
            if self.validator.is_valid(declaration):
                print(f"Fila {index}: declaración válida: {declaration}")
                results.append([index, declaration, "declaración aceptada"])
            else:
                print(f"Fila {index}: declaración no válida: {declaration}")
                results.append([index, declaration, "declaración inválida"])
        
        self.display_results(results)

    def display_results(self, references):
        """Mostrar los resultados en el área de texto."""
        self.report_text.delete(1.0, tk.END)
        if references:
            for ref in references:
                index = ref[0]         # Primer elemento: índice de línea
                declaration = ref[1]   # Segundo elemento: declaración
                status = ref[2]        # Tercer elemento: estado
                self.report_text.insert(tk.END, f"{declaration} (Fila: {index}, Estado: {status})\n")
        else:
            self.report_text.insert(tk.END, "No se encontraron referencias.")

    def download_report(self):
        """Guardar el contenido del reporte en un archivo de texto."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.report_text.get(1.0, tk.END))  # Escribir todo el contenido del scrolledtext
                messagebox.showinfo("Éxito", "Reporte guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VariableAnalyzerApp(root)
    root.mainloop()
