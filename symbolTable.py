class SymbolTable:
    def __init__(self):
        # Initialize an empty dictionary for the symbol table
        self.table = {}

    # Create or add a new entry to the symbol table
    def create(self, name, symbol_type, scope, value=None, datatype=None, returntype=None, paramtype=None):
        if name not in self.table:
            self.table[name] = {
                'type': symbol_type,
                'scope': scope,
                'value': value,
                'datatype': datatype,
                'returntype': returntype,
                'paramtype': paramtype
            }
            # print(f"Created: {name} -> {self.table[name]}")
        else:
            # print(f"Error: Symbol '{name}' already exists.")
            pass

    # Read or retrieve an entry from the symbol table
    def read(self, name):
        if name in self.table:
            return self.table[name]
        else:
            # print(f"Error: Symbol '{name}' not found.")
            return None

    # Update an existing entry in the symbol table
    def update(self, name, symbol_type=None, scope=None, value=None, datatype=None, returntype=None, paramtype=None):
        if name in self.table:
            if symbol_type is not None:
                self.table[name]['type'] = symbol_type
            if scope is not None:
                self.table[name]['scope'] = scope
            if value is not None:
                self.table[name]['value'] = value
            if datatype is not None:
                self.table[name]['datatype'] = datatype
            if returntype is not None:
                self.table[name]['returntype'] = returntype
            if paramtype is not None:
                self.table[name]['paramtype'] = paramtype
            # print(f"Updated: {name} -> {self.table[name]}")
        else:
            # print(f"Error: Symbol '{name}' not found.")
            pass

    # Delete an entry from the symbol table
    def delete(self, name):
        if name in self.table:
            del self.table[name]
            # print(f"Deleted: {name}")
        else:
            # print(f"Error: Symbol '{name}' not found.")
            pass

    # Optional: Print the entire symbol table for debugging
    def display(self):
        for name, attributes in self.table.items():
            print(f"{name}: {attributes}")
