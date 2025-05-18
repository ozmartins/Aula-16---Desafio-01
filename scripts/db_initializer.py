import json
import sqlite3

def create_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Raca (
            co_raca_cor integer PRIMARY KEY,
            no_raca_cor char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS Pais (
            co_pais integer PRIMARY KEY,
            no_pais char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS EtniaIndigena (
            co_etnia_indigena integer PRIMARY KEY,
            no_etnia_indigena char(1),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS TipoEstabelecimento (
            co_tipo_estabelecimento integer PRIMARY KEY,
            ds_tipo_estabelecimento char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS NaturezaEstabelecimento (
            co_natureza_estabelecimento integer PRIMARY KEY,
            ds_natureza_estabelecimento char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS DoseVacina (
            co_dose_vacina integer PRIMARY KEY,
            ds_dose_vacina char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS LocalAplicacao (
            co_local_aplicacao integer PRIMARY KEY,
            ds_local_aplicacao char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS ViaAdministracao (
            co_via_administracao integer PRIMARY KEY,
            ds_via_administracao char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS VacinaFabricante (
            co_vacina_fabricante integer PRIMARY KEY,
            ds_vacina_fabricante char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS SistemaOrigem (
            co_sistema_origem integer PRIMARY KEY,
            ds_sistema_origem char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS GrupoAtendimento (
            co_vacina_grupo_atendimento integer PRIMARY KEY,
            ds_vacina_grupo_atendimento char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS OrigemRegistro (
            co_origem_registro integer PRIMARY KEY,
            ds_origem_registro char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS EstrategiaVacinacao (
            co_estrategia_vacinacao integer PRIMARY KEY,
            ds_estrategia_vacinacao char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS CategoriaAtendimento (
            co_vacina_categoria_atendimento integer PRIMARY KEY,
            ds_vacina_categoria_atendimento char(100),
            fl_removido char(1)
        );

        CREATE TABLE IF NOT EXISTS UF (
            sg_uf char(2) PRIMARY KEY,
            no_uf char(100),
            co_pais integer,
            fl_removido char(1),
            FOREIGN KEY (co_pais) REFERENCES pais (co_pais)
        );

        CREATE TABLE IF NOT EXISTS Municipio (
            co_municipio integer PRIMARY KEY,
            no_municipio char(100),
            sg_uf char(2),
            fl_removido char(1),
            FOREIGN KEY (sg_uf) REFERENCES UF (sg_uf)
        );

        CREATE TABLE IF NOT EXISTS Paciente (
            co_paciente char(64) PRIMARY KEY,
            tp_sexo char(1),
            nu_cep integer,
            ds_nacionalidade char(1),
            nu_idade integer,
            co_condicao_maternal integer,
            co_raca_cor integer,
            co_municipio integer,
            co_etnia_indigena integer,
            fl_removido char(1),
            FOREIGN KEY (co_raca_cor) REFERENCES Raca (co_raca_cor),
            FOREIGN KEY (co_municipio) REFERENCES Municipio (co_municipio),	
            FOREIGN KEY (co_etnia_indigena) REFERENCES EtniaIndigena (co_etnia_indigena)
        );

        CREATE TABLE IF NOT EXISTS Estabelecimento (
            co_cnes_estabelecimento integer PRIMARY KEY,
            no_razao_social_estabelecimento char(100),
            no_fantasia_estalecimento char(100),
            co_municipio integer,
            co_natureza_estabelecimento integer,
            co_tipo_estabelecimento integer,
            fl_removido char(1),
            FOREIGN KEY (co_municipio) REFERENCES Municipio (co_municipio),
            FOREIGN KEY (co_tipo_estabelecimento) REFERENCES TipoEstabelecimento (co_tipo_estabelecimento),
            FOREIGN KEY (co_natureza_estabelecimento) REFERENCES NaturezaEstabelecimento (co_natureza_estabelecimento)
        );

        CREATE TABLE IF NOT EXISTS Vacina (
            co_vacina integer PRIMARY KEY,
            sg_vacina char(20),
            ds_vacina char(100),
            co_via_administracao integer,
            co_vacina_fabricante integer,
            fl_removido char(1),
            FOREIGN KEY (co_vacina_fabricante) REFERENCES VacinaFabricante (co_vacina_fabricante),
            FOREIGN KEY (co_via_administracao) REFERENCES ViaAdministracao (co_via_administracao)
        );

        CREATE TABLE IF NOT EXISTS Vacinacao (
            co_documento char(64) PRIMARY KEY,
            co_troca_documento integer,
            dt_vacina date,
            co_lote_vacina char(20),
            dt_entrada_rnds date,
            dt_deletado_rnds date,
            st_documento char(20),
            co_paciente char(64),
            co_vacina integer,
            co_dose_vacina integer,
            co_local_aplicacao integer,
            co_sistema_origem integer,
            co_origem_registro integer,
            co_estrategia_vacinacao integer,
            co_vacina_categoria_atendimento integer,
            co_vacina_grupo_atendimento integer,
            co_cnes_estabelecimento integer,
            fl_removido char(1),
            FOREIGN KEY (co_cnes_estabelecimento) REFERENCES Estabelecimento (co_cnes_estabelecimento),
            FOREIGN KEY (co_vacina_grupo_atendimento) REFERENCES GrupoAtendimento (co_vacina_grupo_atendimento),
            FOREIGN KEY (co_vacina_categoria_atendimento) REFERENCES CategoriaAtendimento (co_vacina_categoria_atendimento),
            FOREIGN KEY (co_estrategia_vacinacao) REFERENCES EstrategiaVacinacao (co_estrategia_vacinacao),
            FOREIGN KEY (co_origem_registro) REFERENCES OrigemRegistro (co_origem_registro),
            FOREIGN KEY (co_sistema_origem) REFERENCES SistemaOrigem (co_sistema_origem),
            FOREIGN KEY (co_local_aplicacao) REFERENCES LocalAplicacao (co_local_aplicacao),
            FOREIGN KEY (co_dose_vacina) REFERENCES DoseVacina (co_dose_vacina),
            FOREIGN KEY (co_vacina) REFERENCES Vacina (co_vacina),
            FOREIGN KEY (co_paciente) REFERENCES Paciente (co_paciente)
        );
    ''')
    cursor.close()

def open_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as read_file:
        return json.load(read_file)

def insert_categoria_atendimento(item, cursor):
    if item['co_vacina_categoria_atendimento'] != None:
            cursor.execute('''INSERT OR IGNORE INTO CategoriaAtendimento 
                        (co_vacina_categoria_atendimento, ds_vacina_categoria_atendimento, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_vacina_categoria_atendimento'], item['ds_vacina_categoria_atendimento'], 'N']))
            
def insert_dose_vacina(item, cursor):
    if item['co_dose_vacina'] != None:
        cursor.execute('''INSERT OR IGNORE INTO DoseVacina 
                        (co_dose_vacina, ds_dose_vacina, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_dose_vacina'], item['ds_dose_vacina'], 'N']))

def insert_Estabelecimento(item, cursor):
    if item['co_cnes_estabelecimento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Estabelecimento 
                        (co_cnes_estabelecimento, no_razao_social_estabelecimento, no_fantasia_estalecimento, co_municipio, co_natureza_estabelecimento, co_tipo_estabelecimento, fl_removido) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                        ([item['co_cnes_estabelecimento'], item['no_razao_social_estabelecimento'], item['no_fantasia_estalecimento'], item['co_municipio_estabelecimento'], item['co_natureza_estabelecimento'], item['co_tipo_estabelecimento'], 'N']))

def insert_EstrategiaVacinacao(item, cursor):
    if item['co_estrategia_vacinacao'] != None:
        cursor.execute('''INSERT OR IGNORE INTO EstrategiaVacinacao 
                        (co_estrategia_vacinacao, ds_estrategia_vacinacao, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_estrategia_vacinacao'], item['ds_estrategia_vacinacao'], 'N']))

def insert_EtniaIndigena(item, cursor):
    if item['co_etnia_indigena_paciente'] != None:
        cursor.execute('''INSERT OR IGNORE INTO EtniaIndigena 
                        (co_etnia_indigena, no_etnia_indigena, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_etnia_indigena_paciente'], item['no_etnia_indigena_paciente'], 'N']))

def insert_EtniaGrupoAtendimentoIndigena(item, cursor):
    if item['co_vacina_grupo_atendimento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO GrupoAtendimento
                        (co_vacina_grupo_atendimento, ds_vacina_grupo_atendimento, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_vacina_grupo_atendimento'], item['ds_vacina_grupo_atendimento'], 'N']))
            
def insert_LocalAplicacao(item, cursor):
    if item['co_local_aplicacao'] != None:
        cursor.execute('''INSERT OR IGNORE INTO LocalAplicacao 
                        (co_local_aplicacao, ds_local_aplicacao, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_local_aplicacao'], item['ds_local_aplicacao'], 'N']))
            
def insert_Municipio(item, cursor):
    if item['co_municipio_paciente'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Municipio 
                        (co_municipio, no_municipio, sg_uf, fl_removido) 
                        VALUES (?, ?, ?, ?)''', 
                        ([item['co_municipio_paciente'], item['no_municipio_paciente'], item['sg_uf_paciente'], 'N']))
        
    if item['co_municipio_estabelecimento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Municipio 
                        (co_municipio, no_municipio, sg_uf, fl_removido) 
                        VALUES (?, ?, ?, ?)''', 
                        ([item['co_municipio_estabelecimento'], item['no_municipio_estabelecimento'], item['sg_uf_estabelecimento'], 'N']))
            
def insert_NaturezaEstabelecimento(item, cursor):
    if item['co_natureza_estabelecimento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO NaturezaEstabelecimento 
                        (co_natureza_estabelecimento, ds_natureza_estabelecimento, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_natureza_estabelecimento'], item['ds_natureza_estabelecimento'], 'N']))
            
def insert_OrigemRegistro(item, cursor):
    if item['co_origem_registro'] != None:
        cursor.execute('''INSERT OR IGNORE INTO OrigemRegistro 
                        (co_origem_registro, ds_origem_registro, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_origem_registro'], item['ds_origem_registro'], 'N']))
            
def insert_Paciente(item, cursor):
    if item['co_paciente'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Paciente 
                        (co_paciente, tp_sexo, nu_cep, ds_nacionalidade, nu_idade, co_condicao_maternal, co_raca_cor, co_municipio, co_etnia_indigena, fl_removido)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                        ([item['co_paciente'], item['tp_sexo_paciente'], item['nu_cep_paciente'], item['ds_nacionalidade_paciente'], item['nu_idade_paciente'], item['co_condicao_maternal'], item['co_raca_cor_paciente'], item['co_municipio_paciente'], item['co_etnia_indigena_paciente'], 'N']))
            
def insert_Pais(item, cursor):
    if item['co_pais_paciente'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Pais 
                        (co_pais, no_pais, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_pais_paciente'], item['no_pais_paciente'], 'N']))
            
def insert_Raca(item, cursor):
    if item['co_raca_cor_paciente'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Raca 
                        (co_raca_cor, no_raca_cor, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_raca_cor_paciente'], item['no_raca_cor_paciente'], 'N']))
            
def insert_SistemaOrigem(item, cursor):
    if item['co_sistema_origem'] != None:
        cursor.execute('''INSERT OR IGNORE INTO SistemaOrigem 
                        (co_sistema_origem, ds_sistema_origem, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_sistema_origem'], item['ds_sistema_origem'], 'N']))
            
def insert_TipoEstabelecimento(item, cursor):
    if item['co_tipo_estabelecimento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO TipoEstabelecimento 
                        (co_tipo_estabelecimento, ds_tipo_estabelecimento, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_tipo_estabelecimento'], item['ds_tipo_estabelecimento'], 'N']))
            
def insert_UF(item, cursor):
    if item['sg_uf_paciente'] != None:
        cursor.execute('''INSERT OR IGNORE INTO UF 
                        (sg_uf, no_uf, co_pais, fl_removido) 
                        VALUES (?, ?, ?, ?)''', 
                        ([item['sg_uf_paciente'], item['no_uf_paciente'], item['co_pais_paciente'], 'N']))
    if item['sg_uf_estabelecimento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO UF 
                        (sg_uf, no_uf, co_pais, fl_removido) 
                        VALUES (?, ?, ?, ?)''', 
                        ([item['sg_uf_estabelecimento'], item['no_uf_estabelecimento'], item['co_pais_paciente'], 'N']))
            
def insert_Vacina(item, cursor):
    if item['co_vacina'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Vacina 
                        (co_vacina, sg_vacina, ds_vacina, co_via_administracao, co_vacina_fabricante, fl_removido) 
                        VALUES (?, ?, ?, ?, ?, ?)''', 
                        ([item['co_vacina'], item['sg_vacina'], item['ds_vacina'], item['co_via_administracao'], item['co_vacina_fabricante'], 'N']))

def insert_Vacinacao(item, cursor):
    if item['co_documento'] != None:
        cursor.execute('''INSERT OR IGNORE INTO Vacinacao 
                        (co_documento, co_troca_documento, dt_vacina, co_lote_vacina, dt_entrada_rnds, dt_deletado_rnds, st_documento, co_paciente, co_vacina, co_dose_vacina, co_local_aplicacao, co_sistema_origem, co_origem_registro, co_estrategia_vacinacao, co_vacina_categoria_atendimento, co_vacina_grupo_atendimento, co_cnes_estabelecimento, fl_removido) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                        ([item['co_documento'], item['co_troca_documento'], item['dt_vacina'], item['co_lote_vacina'], item['dt_entrada_rnds'], item['dt_deletado_rnds'], item['st_documento'], item['co_paciente'], item['co_vacina'], item['co_dose_vacina'], item['co_local_aplicacao'], item['co_sistema_origem'], item['co_origem_registro'], item['co_estrategia_vacinacao'], item['co_vacina_categoria_atendimento'], item['co_vacina_grupo_atendimento'], item['co_cnes_estabelecimento'], 'N']))

def insert_VacinaFabricante(item, cursor):
    if item['co_vacina_fabricante'] != None:
        cursor.execute('''INSERT OR IGNORE INTO VacinaFabricante 
                        (co_vacina_fabricante, ds_vacina_fabricante, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_vacina_fabricante'], item['ds_vacina_fabricante'], 'N']))

def insert_ViaAdministracao(item, cursor):
    if item['co_via_administracao'] != None:
        cursor.execute('''INSERT OR IGNORE INTO ViaAdministracao 
                        (co_via_administracao, ds_via_administracao, fl_removido) 
                        VALUES (?, ?, ?)''', 
                        ([item['co_via_administracao'], item['ds_via_administracao'], 'N']))
            
def insert_dataset_into_db(json_data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for item in json_data:
        insert_categoria_atendimento(item, cursor)
        insert_dose_vacina(item, cursor)
        insert_Estabelecimento(item, cursor)
        insert_EstrategiaVacinacao(item, cursor)
        insert_EtniaIndigena(item, cursor)
        insert_EtniaGrupoAtendimentoIndigena(item, cursor)
        insert_LocalAplicacao(item, cursor)
        insert_Municipio(item, cursor)
        insert_NaturezaEstabelecimento(item, cursor)
        insert_OrigemRegistro(item, cursor)
        insert_Paciente(item, cursor)
        insert_Pais(item, cursor)
        insert_Raca(item, cursor)
        insert_SistemaOrigem(item, cursor)
        insert_TipoEstabelecimento(item, cursor)
        insert_UF(item, cursor)
        insert_Vacina(item, cursor)
        insert_Vacinacao(item, cursor)
        insert_VacinaFabricante(item, cursor)
        insert_ViaAdministracao(item, cursor)
    conn.commit()
    conn.close()

def initialize_database():
    connection_string = 'Dados\\vacinacao.db'
    create_tables(connection_string)
    json_file = open_json_file('Dados\\vacinacao_jan_2025.json')    
    insert_dataset_into_db(json_file, connection_string)