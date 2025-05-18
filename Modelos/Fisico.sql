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