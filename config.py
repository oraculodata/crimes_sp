bq = {
    'key_path': 'transparenciassp-conta-servico.json',
    'dataset': 'transparenciassp.transparenciassp_data',
}

ssp = {
    'portal': 'http://www.ssp.sp.gov.br/transparenciassp/',
    'selector': '#cphBody_ExportarBOLink',
    'crime': 'ROUBO DE CELULAR',
    'ano': '2022',
    'mes': 'Novembro',
}

"""
Os valores aceitos no dicionário -ssp- em 'crime' são: ROUBO DE CELULAR, FURTO DE CELULAR, ROUBO DE VEÍCULO E FURTO DE VEÍCULO.

Em 'ano', para ROUBO e FURTO DE CELULAR no Portal de Seguranća Pública do Estado de São Paulo, disponibiliza o histórico de 2010 até 2023.

Já para ROUBO DE VEÍCULO E FURTO DE VEÍCULO está disponível de 2003 até 2023.

E o mês mais atual para ambos crimes é Fevereiro de 2023 (Isso no momento em que estou digitando este comentário).

"""