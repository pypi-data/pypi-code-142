# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['escavador', 'escavador.resources', 'escavador.resources.helpers']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=3.0.0,<4.0.0',
 'asyncio>=3.4.3,<4.0.0',
 'cchardet>=2.1.7,<3.0.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'escavador',
    'version': '0.1.5',
    'description': 'A library to  interact with Escavador API',
    'long_description': '## SDK em python para utilizar a API do Escavador\n\n### Instalação\n    \nInstale utilizando o pip:\n```bash\npip install escavador\n```\n\n### Como Configurar\n\n- Crie no `.env` do seu projeto uma variável `ESCAVADOR_API_KEY` com seu token da API\n- ou\n- utilize a função `config()`\n```py\nimport escavador\nescavador.config("API_KEY")\n```\n\n- para obter seu token da API, acesse o [painel de tokens](https://api.escavador.com/tokens)\n\n### Exemplo de como utilizar\n[Buscando informações do processo no sistema do Tribunal](https://api.escavador.com/docs/#pesquisar-processo-no-site-do-tribunal-assncrono) (Assíncrono)\n```py\nfrom escavador import Processo, BuscaAssincrona\nimport time\n\nresultado_busca = Processo().informacoes_no_tribunal("0078700-86.2008.5.17.0009")  # Gera uma busca assíncrona\n\nwhile resultado_busca[\'resposta\'][\'status\'] == \'PENDENTE\':\n    # Aguarda para checar novamente\n    print("Está pendente")\n    time.sleep(20)\n\n    id_async = resultado_busca[\'resposta\'][\'id\']\n    resultado_busca = BuscaAssincrona().por_id(id_async)\n\n# Checa a saida do processso\nif resultado_busca[\'resposta\'][\'status\'] == \'ERRO\':\n    print("Deu erro, tentar novamente")\n    exit(0)\n\nif resultado_busca[\'resposta\'][\'status\'] == \'SUCESSO\':\n    busca_async = resultado_busca[\'resposta\']\n    for instancia in busca_async[\'resposta\'][\'instancias\']:\n        print(instancia[\'assunto\'])  # Imprime os assuntos das instâncias do processo\n```\n\n### Criando Monitoramentos\n```py\nfrom escavador import MonitoramentoTribunal, MonitoramentoDiario, TiposMonitoramentosTribunal, TiposMonitoramentosDiario,FrequenciaMonitoramentoTribunal\n\n# Monitoramento nos sisteams dos Tribunais\nmonitoramento_tribunal = MonitoramentoTribunal().criar(tipo_monitoramento=TiposMonitoramentosTribunal.UNICO,\n                                                                     valor="8809061-58.2022.8.10.3695",tribunal=\'TJSP\', \n                                                                     frequencia=FrequenciaMonitoramentoTribunal.SEMANAL)\n\n# Monitoramento em Diários Oficiais\nmonitoramento_diario = MonitoramentoDiario().criar(TiposMonitoramentosDiario.PROCESSO, processo_id=2, origens_ids=[2,4,6])\n```\n\n### Consultando os Tribunais e sistemas disponíveis\n```py\nfrom escavador import Tribunal\n\ntribunais_disponiveis = Tribunal().sistemas_disponiveis()\n```\n\n### Módulos Disponíveis e Referência da API\n\n| Módulo                | Link API                                                          |\n|-----------------------|-------------------------------------------------------------------|\n| Busca                 | https://api.escavador.com/docs/#busca                             |\n| Processo              | https://api.escavador.com/docs/#processos                         |\n| Callback              | https://api.escavador.com/docs/#callback                          |\n| DiarioOficial         | https://api.escavador.com/docs/#dirios-oficiais                   |\n| Instituicao           | https://api.escavador.com/docs/#instituies                        |\n| Legislacao            | https://api.escavador.com/docs/#legislao                          |\n| Jurisprudencia        | https://api.escavador.com/docs/#jurisprudncias                    |\n| MonitoramentoDiario   | https://api.escavador.com/docs/#monitoramento-de-dirios-oficiais  |\n| MonitoramentoTribunal | https://api.escavador.com/docs/#monitoramento-no-site-do-tribunal |\n| Movimentacao          | https://api.escavador.com/docs/#movimentaes                       |\n| Pessoa                | https://api.escavador.com/docs/#pessoas                           |\n| Tribunal              | https://api.escavador.com/docs/#tribunais                         |\n| Saldo                 | https://api.escavador.com/docs/#saldo-da-api                      | ',
    'author': 'Rafael',
    'author_email': 'rafaelcampos@escavador.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.escavador.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
