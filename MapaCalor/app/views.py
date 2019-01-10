import sys
import os
import folium
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from folium.plugins import HeatMap
from django.shortcuts import render_to_response


# Create your views here.

def filtro_mapa(request, template_name='filtro_mapa.html'):
    if request.method == "POST":
        # sys.setrecursionlimit(100000)
        cotista = request.POST.get("TipoCota")
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

        todos = True

        fatoCotas = FatoCotas.objects.all().filter(fk_local_oferta__longitude__isnull=False,
                                                   fk_local_oferta__latitude__isnull=False)

        if tempo is not None and tempo != "Todos":
            fatoCotas = fatoCotas.filter(fk_tempo=tempo)

        if corRaca is not None and corRaca != "Todos":
            fatoCotas = fatoCotas.filter(fk_cor_raca=corRaca)
            todos = False

        if categoriaAdministrativa is not None and categoriaAdministrativa != "Todos":
            fatoCotas = fatoCotas.filter(fk_categoria_administrativa=categoriaAdministrativa)
            todos = False

        if organizacaoAcademica is not None and organizacaoAcademica != "Todos":
            fatoCotas = fatoCotas.filter(fk_organizacao_academica=organizacaoAcademica)
            todos = False

        if ies is not None and ies != "Todos":
            fatoCotas = fatoCotas.filter(fk_ies=ies)
            todos = False

        if localOferta is not None and localOferta != "Todos":
            fatoCotas = fatoCotas.filter(fk_local_oferta__no_uf=localOferta)
            todos = False

        if sexo is not None and sexo != "Todos":
            fatoCotas = fatoCotas.filter(fk_sexo=sexo)
            todos = False

        if curso is not None and curso != "Todos":
            fatoCotas = fatoCotas.filter(fk_curso__descricao=curso)
            todos = False

        if modalidadeEnsino is not None and modalidadeEnsino != "Todos":
            fatoCotas = fatoCotas.filter(fk_modalidade_ensino=modalidadeEnsino)
            todos = False

        if situacaoAluno is not None and situacaoAluno != "Todos":
            fatoCotas = fatoCotas.filter(fk_situacao_aluno=situacaoAluno)
            todos = False

        if cotista is not None and cotista != "Todos" and cotista == "Cotista":
            fatoCotas = fatoCotas.exclude(qtde_cotas=0)
            todos = False

        if cotista is not None and cotista != "Todos" and cotista == "NCotista":
            fatoCotas = fatoCotas.exclude(qtde_nao_cotas=0)
            todos = False

        if todos == True:
            fatoCotas = FatoCotas.objects.all().filter(fk_local_oferta__longitude__isnull=False,
                                                       fk_local_oferta__latitude__isnull=False)[:1000]

        locais = []

        mapa = folium.Map(location=[-8.0176527, -34.9443739], zoom_start=4)

        # locais = fatoCotas.values_list("fk_local_oferta__latitude", "fk_local_oferta__longitude")

        contadorRegistros = 0
        valorTotalCotistaOuNaoCotista = 0

        for linha in fatoCotas:
            if linha.fk_local_oferta.latitude is not None and linha.fk_local_oferta.longitude is not None:

                if cotista == "Cotista":
                    valorCotistaOuNaoCotista = linha.qtde_cotas
                elif cotista == "NCotista":
                    valorCotistaOuNaoCotista = linha.qtde_nao_cotas
                else:
                    valorCotistaOuNaoCotista = linha.qtde_nao_cotas + linha.qtde_cotas

                temp = [float(linha.fk_local_oferta.latitude), float(linha.fk_local_oferta.longitude),
                        valorCotistaOuNaoCotista]
                locais.append(temp)
                contadorRegistros = contadorRegistros + 1
                valorTotalCotistaOuNaoCotista = valorTotalCotistaOuNaoCotista + valorCotistaOuNaoCotista

        # HeatMap([[-8.0176527, -34.9443739]], radius=25).add_to(mapa)
        HeatMap(locais).add_to(mapa)

        mapa.save('mapa.html')

        fatCota = {'Post': True, 'Ma': mapa.get_root().render(), 'Contador': valorTotalCotistaOuNaoCotista}

        return render(request, template_name, fatCota)
        # return render_to_response('mapa.html')
    else:
        dimCategoriaAdministrativa = DimCategoriaAdministrativa.objects.all()
        dimCorRaca = DimCorRaca.objects.all()
        fatoCotasDimCurso = FatoCotas.objects.values_list("fk_curso__descricao", named=True).distinct()
        fatoCotasDimIes = FatoCotas.objects.values_list("fk_ies", "fk_ies__no_ies", named=True).distinct()
        fatoCotasDimLocalOferta = FatoCotas.objects.values_list("fk_local_oferta__no_uf", named=True).distinct()
        dimModalidadeEnsino = DimModalidadeEnsino.objects.all()
        dimOrganizacaoAcademica = DimOrganizacaoAcademica.objects.all()
        dimSexo = DimSexo.objects.all()
        dimSituacaoAluno = DimSituacaoAluno.objects.all()
        fatoCotasDimTempo = FatoCotas.objects.values_list("fk_tempo", named=True).distinct()

        filtros = {'dimCategoriaAdministrativa': dimCategoriaAdministrativa, 'dimCorRaca': dimCorRaca,
                   "fatoCotasDimCurso": fatoCotasDimCurso, "fatoCotasDimIes": fatoCotasDimIes,
                   "fatoCotasDimLocalOferta": fatoCotasDimLocalOferta, "dimModalidadeEnsino": dimModalidadeEnsino,
                   "dimOrganizacaoAcademica": dimOrganizacaoAcademica, "dimSexo": dimSexo,
                   "dimSituacaoAluno": dimSituacaoAluno, "fatoCotasDimTempo": fatoCotasDimTempo, "Post": False}

        return render(request, template_name, filtros)


def mapa(request, template_name='mapa.html'):
    return render(request, template_name)
