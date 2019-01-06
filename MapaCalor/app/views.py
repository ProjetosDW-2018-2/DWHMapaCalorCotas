from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.

def filtro_mapa(request, template_name='filtro_mapa.html'):
    if request.method == "POST":
        categoriaAdministrativa = request.POST.get("CategoriaAdministrativa")
        corRaca = request.POST.get("CorRaca")
        curso = request.POST.get("Curso")
        ies = request.POST.get("Ies")
        localOferta = request.POST.get("LocalOferta")
        modalidadeEnsino = request.POST.get("ModalidadeEnsino")
        organizacaoAcademica = request.POST.get("OrganizacaoAcademica")
        sexo = request.POST.get("Sexo")
        situacaoAluno = request.POST.get("SituacaoAluno")
        tempo = request.POST.get("Tempo")

        fatoCotas = FatoCotas.objects.all()[:100]

        if tempo is not None and tempo != "Todos":
            fatoCotas = fatoCotas.filter(fk_tempo=tempo)
        elif corRaca is not None and corRaca != "Todos":
            fatoCotas = fatoCotas.filter(fk_cor_raca=corRaca)
        elif categoriaAdministrativa is not None and categoriaAdministrativa != "Todos":
            fatoCotas = fatoCotas.filter(fk_categoria_administrativa=categoriaAdministrativa)
        elif organizacaoAcademica is not None and organizacaoAcademica != "Todos":
            fatoCotas = fatoCotas.filter(fk_organizacao_academica=organizacaoAcademica)
        elif ies is not None and ies != "Todos":
            fatoCotas = fatoCotas.filter(fk_ies=ies)
        elif localOferta is not None and localOferta != "Todos":
            fatoCotas = fatoCotas.filter(fk_local_oferta=localOferta)
        elif sexo is not None and sexo != "Todos":
            fatoCotas = fatoCotas.filter(fk_sexo=sexo)
        elif curso is not None and curso != "Todos":
            fatoCotas = fatoCotas.filter(fk_curso=curso)
        elif modalidadeEnsino is not None and modalidadeEnsino != "Todos":
            fatoCotas = fatoCotas.filter(fk_modalidade_ensino=modalidadeEnsino)
        elif situacaoAluno is not None and situacaoAluno != "Todos":
            fatoCotas = fatoCotas.filter(fk_situacao_aluno=situacaoAluno)

        fatCota = {'lista': fatoCotas}

        return render(request, template_name, fatCota)
    else:
        dimCategoriaAdministrativa = DimCategoriaAdministrativa.objects.all()
        dimCorRaca = DimCorRaca.objects.all()
        fatoCotasDimCurso = FatoCotas.objects.values_list("fk_curso", "fk_curso__descricao", named=True).distinct()
        fatoCotasDimIes = FatoCotas.objects.values_list("fk_ies", "fk_ies__no_ies", named=True).distinct()
        fatoCotasDimLocalOferta = FatoCotas.objects.values_list("fk_local_oferta", "fk_local_oferta__no_municipio", "fk_local_oferta__no_uf", named=True).distinct()
        dimModalidadeEnsino = DimModalidadeEnsino.objects.all()
        dimOrganizacaoAcademica = DimOrganizacaoAcademica.objects.all()
        dimSexo = DimSexo.objects.all()
        dimSituacaoAluno = DimSituacaoAluno.objects.all()
        fatoCotasDimTempo = FatoCotas.objects.values_list("fk_tempo", named=True).distinct()

        filtros = {'dimCategoriaAdministrativa': dimCategoriaAdministrativa, 'dimCorRaca': dimCorRaca,
                   "fatoCotasDimCurso": fatoCotasDimCurso, "fatoCotasDimIes": fatoCotasDimIes,
                   "fatoCotasDimLocalOferta": fatoCotasDimLocalOferta, "dimModalidadeEnsino": dimModalidadeEnsino,
                   "dimOrganizacaoAcademica": dimOrganizacaoAcademica, "dimSexo": dimSexo,
                   "dimSituacaoAluno": dimSituacaoAluno, "fatoCotasDimTempo": fatoCotasDimTempo}

        return render(request, template_name, filtros)
