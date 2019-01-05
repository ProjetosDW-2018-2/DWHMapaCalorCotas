# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DimCategoriaAdministrativa(models.Model):
    id_categoria_administrativa = models.AutoField(db_column='ID_CATEGORIA_ADMINISTRATIVA', primary_key=True)  # Field name made lowercase.
    co_categoria_administrativa = models.IntegerField(db_column='CO_CATEGORIA_ADMINISTRATIVA', blank=True, null=True)  # Field name made lowercase.
    no_categoria_administrativa = models.CharField(db_column='NO_CATEGORIA_ADMINISTRATIVA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_categoria_administrativa'


class DimCorRaca(models.Model):
    id_cor_raca = models.IntegerField(db_column='ID_COR_RACA', primary_key=True)  # Field name made lowercase.
    co_cor_raca = models.IntegerField(db_column='CO_COR_RACA', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_cor_raca'


class DimCurso(models.Model):
    id_curso = models.AutoField(db_column='ID_CURSO', primary_key=True)  # Field name made lowercase.
    co_curso = models.IntegerField(db_column='CO_CURSO', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_curso'


class DimIes(models.Model):
    id_ies = models.AutoField(db_column='ID_IES', primary_key=True)  # Field name made lowercase.
    co_ies = models.IntegerField(db_column='CO_IES', blank=True, null=True)  # Field name made lowercase.
    no_ies = models.CharField(db_column='NO_IES', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sg_ies = models.CharField(db_column='SG_IES', max_length=45, blank=True, null=True)  # Field name made lowercase.
    in_capital = models.IntegerField(db_column='IN_CAPITAL', blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_ies'


class DimLocalOferta(models.Model):
    id_local_oferta = models.AutoField(db_column='ID_LOCAL_OFERTA', primary_key=True)  # Field name made lowercase.
    co_local_oferta = models.IntegerField(db_column='CO_LOCAL_OFERTA', blank=True, null=True)  # Field name made lowercase.
    no_uf = models.CharField(db_column='NO_UF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    no_municipio = models.CharField(db_column='NO_MUNICIPIO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='LONGITUDE', max_length=108, blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='LATITUDE', max_length=108, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_local_oferta'


class DimModalidadeEnsino(models.Model):
    id_modalidade_ensino = models.AutoField(db_column='ID_MODALIDADE_ENSINO', primary_key=True)  # Field name made lowercase.
    co_modalidade_ensino = models.IntegerField(db_column='CO_MODALIDADE_ENSINO', blank=True, null=True)  # Field name made lowercase.
    no_modalidade_ensino = models.CharField(db_column='NO_MODALIDADE_ENSINO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_modalidade_ensino'


class DimOrganizacaoAcademica(models.Model):
    id_organizacao_academica = models.AutoField(db_column='ID_ORGANIZACAO_ACADEMICA', primary_key=True)  # Field name made lowercase.
    co_organizacao_academica = models.IntegerField(db_column='CO_ORGANIZACAO_ACADEMICA', blank=True, null=True)  # Field name made lowercase.
    no_organizacao_academica = models.CharField(db_column='NO_ORGANIZACAO_ACADEMICA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_organizacao_academica'


class DimSexo(models.Model):
    id_sexo = models.AutoField(db_column='ID_SEXO', primary_key=True)  # Field name made lowercase.
    co_sexo = models.IntegerField(db_column='CO_SEXO', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_sexo'


class DimSituacaoAluno(models.Model):
    id_situacao_aluno = models.AutoField(db_column='ID_SITUACAO_ALUNO', primary_key=True)  # Field name made lowercase.
    co_situacao_aluno = models.IntegerField(db_column='CO_SITUACAO_ALUNO', blank=True, null=True)  # Field name made lowercase.
    no_situacao_aluno = models.CharField(db_column='NO_SITUACAO_ALUNO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dim_situacao_aluno'


class DimTempo(models.Model):
    id_tempo = models.IntegerField(db_column='ID_TEMPO', primary_key=True)  # Field name made lowercase.
    data_id = models.DateTimeField()
    dia_ehdiautil = models.IntegerField(blank=True, null=True)
    dia_numeronasemana = models.IntegerField(blank=True, null=True)
    dia_numeronomes = models.IntegerField(blank=True, null=True)
    dia_numeronoano = models.IntegerField(blank=True, null=True)
    semana_id = models.IntegerField(blank=True, null=True)
    semana_nome = models.CharField(max_length=255, blank=True, null=True)
    semana_texto = models.CharField(max_length=255, blank=True, null=True)
    semana_numeronoano = models.IntegerField(blank=True, null=True)
    mes_id = models.IntegerField(blank=True, null=True)
    mes_nome = models.CharField(max_length=255, blank=True, null=True)
    mes_texto = models.CharField(max_length=255, blank=True, null=True)
    mes_numeronoano = models.CharField(max_length=255, blank=True, null=True)
    trimestre_id = models.IntegerField(blank=True, null=True)
    trimestre_nome = models.CharField(max_length=255, blank=True, null=True)
    trimestre_texto = models.CharField(max_length=255, blank=True, null=True)
    trimestre_numeronoano = models.IntegerField(blank=True, null=True)
    semestre_id = models.IntegerField(blank=True, null=True)
    semestre_nome = models.CharField(max_length=255, blank=True, null=True)
    semestre_texto = models.CharField(max_length=255, blank=True, null=True)
    semestre_numeronoano = models.IntegerField(blank=True, null=True)
    ano_id = models.IntegerField(blank=True, null=True)
    ano_nome = models.CharField(max_length=255, blank=True, null=True)
    ano_texto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_tempo'


class FatoCotas(models.Model):
    qtde_cotas = models.IntegerField(db_column='QTDE_COTAS')  # Field name made lowercase.
    qtde_nao_cotas = models.IntegerField(db_column='QTDE_NAO_COTAS')  # Field name made lowercase.
    perc_cotas = models.IntegerField(db_column='PERC_COTAS')  # Field name made lowercase.
    perc_nao_cotas = models.IntegerField(db_column='PERC_NAO_COTAS')  # Field name made lowercase.
    fk_tempo = models.ForeignKey(DimTempo, models.DO_NOTHING, db_column='FK_TEMPO', primary_key=True)  # Field name made lowercase.
    fk_cor_raca = models.ForeignKey(DimCorRaca, models.DO_NOTHING, db_column='FK_COR_RACA')  # Field name made lowercase.
    fk_categoria_administrativa = models.ForeignKey(DimCategoriaAdministrativa, models.DO_NOTHING, db_column='FK_CATEGORIA_ADMINISTRATIVA')  # Field name made lowercase.
    fk_organizacao_academica = models.ForeignKey(DimOrganizacaoAcademica, models.DO_NOTHING, db_column='FK_ORGANIZACAO_ACADEMICA')  # Field name made lowercase.
    fk_ies = models.ForeignKey(DimIes, models.DO_NOTHING, db_column='FK_IES')  # Field name made lowercase.
    fk_local_oferta = models.ForeignKey(DimLocalOferta, models.DO_NOTHING, db_column='FK_LOCAL_OFERTA')  # Field name made lowercase.
    fk_sexo = models.ForeignKey(DimSexo, models.DO_NOTHING, db_column='FK_SEXO')  # Field name made lowercase.
    fk_curso = models.ForeignKey(DimCurso, models.DO_NOTHING, db_column='FK_CURSO')  # Field name made lowercase.
    fk_modalidade_ensino = models.ForeignKey(DimModalidadeEnsino, models.DO_NOTHING, db_column='FK_MODALIDADE_ENSINO')  # Field name made lowercase.
    fk_situacao_aluno = models.ForeignKey(DimSituacaoAluno, models.DO_NOTHING, db_column='FK_SITUACAO_ALUNO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fato_cotas'
        unique_together = (('fk_tempo', 'fk_categoria_administrativa', 'fk_organizacao_academica', 'fk_cor_raca', 'fk_ies', 'fk_local_oferta', 'fk_sexo', 'fk_curso', 'fk_modalidade_ensino', 'fk_situacao_aluno'),)
