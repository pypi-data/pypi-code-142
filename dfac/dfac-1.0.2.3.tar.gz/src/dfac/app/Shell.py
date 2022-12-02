from dfac.app.Help import Help
from dfac.core.StringGenerator import StringGenerator
from dfac.core.ArrayGenerator import ArrayGenerator
from dfac.inout.Display import Display
from dfac.inout.FileGenerator import FileGenerator
from dfac.app.Error import Error

class Shell:

    def __init__(self) -> None:
        #match input to type
        # self.array_types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5, 'Integer':6,'Decimal':7, 'Symbolic':8}
        # self.xxstring_types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5}
        self.short_string_types={'n':'AlphaNumeric','a':'Alphabet','u':'Alphabet_Upper','l':'Alphabet_Lower','y':'AlphaSymbolic'}
        self.short_array_types={'n':'AlphaNumeric','a':'Alphabet','u':'Alphabet_Upper','l':'Alphabet_Lower','y':'AlphaSymbolic','i':'Integer','d':'Decimal','o':'Symbolic'}
        self.long_string_types={'alphanumeric':'AlphaNumeric','alphabet':'Alphabet','upper':'Alphabet_Upper','lower':'Alphabet_Lower','alphasymbolic':'AlphaSymbolic'}
        self.long_array_types={'alphanumeric':'AlphaNumeric','alphabet':'Alphabet','upper':'Alphabet_Upper','lower':'Alphabet_Lower','alphasymbolic':'AlphaSymbolic','integer':'Integer','decimal':'Decimal','symbolic':'Symbolic'}

        self.data_type=0
        self.value_type=0
        self.length=5
        self.array_low=1
        self.array_high=5
        self.printfile=False
        self.filename='output.txt'

    def parse(self, string):
        if '-h' in string or '--help' in string:
            Help().printHelp()

        self.check_for_errors(string)
        self.run()
        # print(self.filename)
    
    def run_string(self):
        so = StringGenerator(self.length,self.short_string_types[self.value_type])
        value=so.generate()
        if self.printfile==True:
            FileGenerator().print_out(value,self.filename)
        else:
            Display().print_out(so.generate())
    
    def run_array(self):
        if self.array_high - self.array_low<0:
            Error().print_error("High value less than low value")
            Help().noValue()
        ao= ArrayGenerator(self.length,self.short_array_types[self.value_type],self.array_low,self.array_high)
        value=ao.generate()
        if self.printfile==True:
            FileGenerator().print_out(str(value),self.filename)
        else:
            Display().print_out(ao.generate())
        

    def run(self):
        if self.data_type == 's':
            self.run_string()
        elif self.data_type == 'a':
            self.run_array()
        else:
            Help().noValue()

    def check_for_errors(self, string):
        if '-v' not in string and '--valuetype' not in string:
            Help().noValue()

        if '-t' not in string and '--datatype' not in string:
            Help().noValue()

        try:
            if '-t' in string:
                self.data_type=string[string.index('-t')+1]

            if '--datatype' in string:
                self.data_type=string[string.index('--datatype')+1]
            
            if '-v' in string:
                self.value_type=string[string.index('-v')+1]

            if '--valuetype' in string:
                self.value_type=string[string.index('--valuetype')+1]

            if '--file' in string:
                try:
                    self.filename=string[string.index('--file')+1]
                except:
                    pass

                self.printfile=True

            if '-x' in string:
                try:
                    self.filename=string[string.index('-x')+1]
                except:
                    pass

                self.printfile=True

            if '--length' in string:
                try:
                    self.length=int(string[string.index('--length')+1])
                except:
                    pass

            if '-0' in string:
                try:
                    self.length=int(string[string.index('-0')+1])
                except:
                    pass
            
            if '-L' in string:
                try:
                    self.array_low=int(string[string.index('-l')+1])
                except:
                    pass

            if '--low' in string:
                try:
                    self.array_low=int(string[string.index('--low')+1])
                except:
                    pass
            
            if '-H' in string:
                try:
                    self.array_high=int(string[string.index('-H')+1])
                except:
                    pass

            if '--high' in string:
                try:
                    self.array_high=int(string[string.index('--high')+1])
                except:
                    pass
            
        except:
            Help().noValue()
