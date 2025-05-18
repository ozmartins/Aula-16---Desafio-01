import sqlite3

def select(table, conditions=''):
    conn = sqlite3.connect('Dados\\vacinacao.db')
    cursor = conn.cursor() 
    cursor.execute(f'select * from {table} where fl_removido = \'N\' {conditions}')
    racas = cursor.fetchall()
    conn.close()
    return racas

def insert(table, data):
    conn = sqlite3.connect('Dados\\vacinacao.db')
    cursor = conn.cursor() 
    fields = ''
    values = ''
    for item in data:
        fields += item + ','
        if (item == 'fl_removido'):
            values += '\'N\','
        elif isinstance(data[item], str):
            values += f'\'{data[item]}\','
        else:
            values += f'{str(data[item])},'
    cursor.execute(f'insert into {table} ({fields[:-1]}) values ({values[:-1]})')
    conn.commit()
    conn.close()

def update(table, data, conditions):
    conn = sqlite3.connect('Dados\\vacinacao.db')
    cursor = conn.cursor() 
    fields_and_values = ''    
    for item in data:        
        if isinstance(data[item], str):
            fields_and_values += f'{item}=\'{data[item]}\','
        else:
            fields_and_values += f'{item}={data[item]},'
    cursor.execute(f'update {table} set {fields_and_values[:-1]} where fl_removido = \'N\' {conditions}')
    conn.commit()
    conn.close()

def delete(table, conditions):
    conn = sqlite3.connect('Dados\\vacinacao.db')
    cursor = conn.cursor()     
    cursor.execute(f'update {table} set fl_removido = \'S\' where fl_removido = \'N\' {conditions}')
    conn.commit()
    conn.close()