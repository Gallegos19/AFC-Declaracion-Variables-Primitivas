

FINAL_STATES = {'q32'}

class Automata:
    def __init__(self):
        # self.code = code 
        self.variables = [] 
        self.position = 0  
        self.state = 'start'  # Inicializa el estado
        self.current_reference = ""  # Referencia actual
        self.referencias = []  # Lista para almacenar las referencias

    def is_letter(self, char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

    def transition(self, char):
        print(f"Estado: {self.state}, Carácter: {char}")
        if self.state == 'start':
            if char == 'b':
                self.state = 'q5'
                return True
            elif char == 'c':
                self.state = 'q4'
                return True
            elif char == 'd':
                self.state = 'q3'
                return True
            elif char == 'f':
                self.state = 'q2'
                return True
            elif char == 'i':
                self.state = 'q52'
                return True
            elif char == 'l':
                self.state = 'q7'
                return True
            elif char == 's':
                self.state = 'q6'
                return True
            
        # entrada bool
        elif self.state == 'q5':
            if char == 'o':
                self.state = "q21"
                return True

        elif self.state == 'q21':
            if char == 'o':
                self.state = "q22"
                return True

        elif self.state == 'q22':
            if char == 'l':
                self.state = "q53"
                return True

        elif self.state == 'q53':
            if char == ' ':
                self.state = "q54"
                return True
            
        elif self.state == 'q54':
            if char == ' ':
                return True
            elif self.is_letter(char) or char == '_' or char == '$':
                self.state = 'q55'
                return True
            
        elif self.state == 'q55':
            if self.is_letter(char) or char.isdigit() or char == '_':
                return True
            elif char == ' ':
                self.state = 'q33'
                return True
            elif char == '=':
                self.state = 'q34'
                return True
            
        elif self.state == 'q33':
            if char == ' ':
                return True
            elif char == '=':
                self.state = 'q34'
                return True
            
        elif self.state == 'q34':
            if char == 't':
                self.state = 'q35'
                return True
            elif char == ' ':
                self.state = 'q36'
                return True
            elif char == 'f':
                self.state = 'q37'
                return True

        elif self.state == 'q36':
            if char == 't':
                self.state = 'q35'
                return True    
            elif char == 'f':
                self.state = 'q37'
                return True    
            elif char == ' ':
                return True

        elif self.state == 'q35':
            if char == 'r':
                self.state = 'q38'
                return True

        elif self.state == 'q38':
            if char == 'u':
                self.state = 'q39'
                return True

        elif self.state == 'q37':
            if char == 'a':
                self.state = 'q41'
                return True

        elif self.state == 'q41':
            if char == 'l':
                self.state = 'q42'
                return True

        elif self.state == 'q42':
            if char == 's':
                self.state = 'q39'
                return True

        elif self.state == 'q39':
            if char == 'e':
                self.state = 'q40'
                return True

        elif self.state == 'q40':
            if char == ',':
                self.state = 'q54'
                return True
            elif char == ' ':
                return True
            elif char == ';':
                self.state = 'q32'
                return True
            
        # entrada char
        elif self.state == 'q4':
            if char == 'h':
                self.state = 'q18'
                return True

        elif self.state == 'q18':
            if char == 'a':
                self.state = 'q19'
                return True
        elif self.state == 'q19':
            if char == 'r':
                self.state = 'q10'
                return True

        elif self.state == 'q10':
            if char == ' ':
                self.state = 'q23'
                return True

        elif self.state == 'q23':
            if self.is_letter(char) or char == ' ':
                self.state = 'q43'
                return True
            
        elif self.state == 'q43':
            if char == ',':
                self.state = 'q23'
                return True
            elif self.is_letter(char) or char.isdigit() or char == '_':
                return True
            elif char == ' ':
                self.state = 'q44'
                return True
            elif char == '=':
                self.state = 'q56'
                return True

        elif self.state == 'q44':
            if char == '=':
                self.state = 'q56'
                return True
            elif char == ' ':
                return True

        elif self.state == 'q56':
            if char == ' ':
                self.state = 'q57'
                return True

        elif self.state == 'q57':
            if char == ' ':
                return True
            elif char == '\'':
                self.state = 'q58'
                return True
            

        elif self.state == 'q58':
            if self.is_letter(char) or char.isdigit():
                return True
            elif char == '\'':
                self.state = 'q40_1'
                return True
            

        elif self.state == 'q40_1':
            if char == ',':
                self.state = 'q23'
                return True
            elif char == ' ':
                return True
            elif char == ';':
                self.state = 'q32'
                return True
            
        #entrada double
        elif self.state == 'q3':
            if char == 'o':
                self.state = 'q14'
                return True
         
        elif self.state == 'q14':
            if char == 'u':
                self.state = 'q15'
                return True    
         
        elif self.state == 'q15':
            if char == 'b':
                self.state = 'q16'
                return True
        
        elif self.state == 'q16':
            if char == 'l':
                self.state = 'q17'
                return True     
        
        elif self.state == 'q17':
            if char == 'e':
                self.state = 'q45'
                return True   
           
        elif self.state == 'q45':
            if char == ' ':
                self.state = 'q47'
                return True   
        
        elif self.state == 'q47':
            if self.is_letter(char) or char.isdigit() or char == '$' or char == '_':
                self.state = 'q48'
                return True
            elif char == ' ':
                return True
            
        elif self.state == 'q48':
            if char == ',':
                self.state = 'q47'
                return True    
            elif char == ' ':
                self.state = 'q20'
                return True
            elif char == '=':
                self.state = 'q31'
                return True
            elif self.is_letter(char) or char.isdigit() or char == '_':
                return True
            
        elif self.state == 'q20':
            if char == '=':
                self.state = 'q31'
                return True   
            elif char == ' ':
                return True
        
        elif self.state == 'q31':
            if char.isdigit() or char == '-':
                self.state = 'q49'
                return True
            elif char == ' ':
                self.state == 'q46'
                return True
            
        elif self.state == 'q46':
            if char.isdigit() or char == '-':
                self.state = 'q49'
                return True    
            elif char == ' ':
                return True
        
        elif self.state == 'q49':
            if char == ',':
                self.state = 'q47'
                return True    
            elif char == '.':
                self.state = 'q50'
                return True
            elif char == ';':
                self.state = 'q32'
                return True
            elif char.isdigit():
                return True
            
        elif self.state == 'q50':
            if  char == ';':
                self.state = 'q32'
                return True    
            elif char.isdigit():
                return True
            elif char == ',':
                self.state = 'q47'
                return  True
            elif char == ' ':
                return True
            
        
        #entrada float
        elif self.state == 'q2':
            if char == 'l':
                self.state = 'q11'
                return True
        elif self.state == 'q11':
            if char == 'o':
                self.state = 'q12'
                return True
        
        elif self.state == 'q12':
            if char == 'a':
                self.state = 'q13'
                return True    
        
        elif self.state == 'q13':
            if char == 't':
                self.state = 'q45'
                return True
            
        #transicion fallida
        return False

    def reset(self):
        self.state = 'start'
        self.current_reference = ""

    # def store_reference(self, line_number, char_position):
    #     if self.current_reference and ';' in self.current_reference:
    #         self.referencias.append({
    #             "Declaracion": self.current_reference,
    #             "Linea": line_number,
    #             "Columna": char_position - len(self.current_reference) + 1
    #         })
    #     self.reset()

    # def find_references(self, text):
    #     self.referencias = []
    #     self.current_reference = ""
    #     self.state = 'start'
    #     lines = text.splitlines()
    #     for line_number, line in enumerate(lines, start=1):
    #         for char_position, char in enumerate(line, start=1):
    #             self.transition(char, line_number, char_position)

    #     self.store_reference(line_number, char_position)
    #     return self.referencias
    
    def is_valid(self, text):
        self.reset()
        self.text = text
        self.current_pos = 0  # Posición actual en la cadena

        for char in text:
            if not self.transition(char):
                return False
            self.current_pos += 1
        # Verificar si terminó en un estado de aceptación
        return self.state in FINAL_STATES


