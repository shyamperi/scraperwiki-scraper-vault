# encoding: utf-8

# Mitula premium ads dataminer

require 'open-uri'
require 'nokogiri'
require 'net/http'
require 'ostruct'
require 'mechanize'

queries=[
'contabilista',
'contas+a+pagar',
'contas+a+receber',
'atuário',
'finanças+de+bens',
'assistente+de+contabilista',
'auditor',
'bancário',
'banqueiro',
'contador',
'analista+de+orçamento',
'analista+do+negócio',
'programador+web+.net',
'programador+access',
'controlador+de+tráfego+aéreo',
'animador',
'programador+asp',
'técnico+audiovisual',
'autocad',
'analista+de+sistemas+de+negócio',
'programador+c++',
'chief+technology+officer',
'cobol',
'cognos',
'coldfusion',
'programador+de+computador',
'Graduado+de+informática',
'gestor+de+conteúdo',
'testador+de+contrato',
'analista+de+negócio+de+crm',
'vendas+de+crm',
'programador+css',
'analista+de+dados',
'arquiteto+de+dados',
'administrador+de+banco+de+dados',
'supervisor+de+centro+de+processamento+de+dados',
'data+mining',
'programador+data+warehouse',
'dba',
'delphi',
'engenheiro+de+suporte+ao+cliente',
'líder+de+equipe+de+programação',
'dreamweaver',
'programador+de+drupal',
'supervisor+de+e+commerce',
'editor',
'e+learning',
'sistemas+embebidos',
'epos',
'programador+flash',
'fortran',
'foxpro',
'programador+freelance',
'programador+de+jogos',
'testador+de+jogos',
'gis+data',
'graduado+de+programação+de+software',
'gráfico/web+designer',
'html+5',
'programador+de+html',
'técnico+de+informática',
'informática',
'arquiteto+de+informação',
'supervisor+de+seguraça+da+informação',
'analista+de+inteligência',
'estagiário',
'venda+de+publicidade',
'supervisor+de+vendas+de+publicidade',
'gerente+de+pós+venda',
'vendas+de+agricultura',
'supervisor+de+vendas+de+área',
'vendas+automóveis',
'vendas+de+banheiros',
'vendas+de+beleza',
'gerente+de+desenvolvimento+do+negócio',
'açougueiro',
'venda+de+carros',
'diretor+comercial',
'supervisor+comercial',
'executivo+apoio+a+clientes',
'assistente+de+vendas+de+magazine',
'vendas+porta+a+porta',
'vendas+eletrônica',
'vendas+de+Patrimônio',
'vendas+de+erp',
'produção+de+eventos',
'vendas+de+moda',
'executivo+de+vendas+externas',
'supervisor+de+vendas+externas',
'televendas+francesas',
'vendas+de+mobiliário',
'supervisor+de+vendas',
'vendas+de+hotel',
'vendas+de+hvac',
'assessor+de+vendas+inbound',
'vendas+industriais',
'vendas+de+seguros',
'vendas+de+investimentos',
'executivo+de+vendas+de+TI',
'design+de+vendas+de+cozinha',
'imobiliário',
'vendas+de+seguros+de+vida',
'vendas+de+iluminação',
'media+buyer',
'media+sales',
'vendas+de+equipamento+médico',
'representante+de+vendas+médicas',
'supervisor+de+merchandising',
'vendas+de+celular',
'vendas+de+hipoteca',
'apoio+ao+cliente+bilíngüe',
'assessor+de+call+centre',
'supervisor+de+call+centre',
'líder+de+equipe+de+call+centre',
'atendente',
'supervisor+de+relações+com+o+cliente',
'executivo+de+serviço+ao+cliente',
'supervisor+de+serviço+ao+cliente',
'supervisor+de+atendimento+ao+cliente',
'executivo+de+serviço+ao+cliente',
'supervisor+de+serviço+ao+cliente',
'apoio+ao+cliente',
'guest+relations',
'supervisor+de+serviço+ao+cliente',
'atendimento+de+chamadas+inbound+',
'outbound+call+centre',
'operador+de+call+centre+meio+período',
'engenheiro+aeronáutico',
'manufatura+aeroepacial',
'engenheiro+de+ar+condicionado',
'engenharia+de+aeronáutica',
'engenheiro+de+alarmes',
'engenheiro+de+arquitetura',
'técnico+de+assemblagem',
'assistente+de+engenheiro',
'engenheiro+de+automação',
'design+automóvel',
'engenheiro+de+aeronáutica',
'engenheiro+de+caldeiras',
'engenheiro+de+cablagem',
'mecânico+de+carros',
'engenheiro+mecânico+registrado',
'engenheiro+químico',
'operador+de+processo+químico',
'engeheiro+civil',
'cnc+setter',
'engenheiro+de+componentes',
'engenheiro+de+sistemas+e+controle',
'processamento+de+dados',
'engenharia+de+defesa',
'lavador+de+pratos',
'engenheiro+de+drenagem',
'engenheiro+de+perfuração',
'engenheiro+elétrico',
'técnico+elétrico',
'engenheiro+eletromecânico',
'eletrônica+e+instrumentação',
'engenharia+ambiental',
'proteção+ambiental',
'técnico+de+campo',
'engenheiro+de+alarme+de+incêndio',
'engenheiro+de+segurança+ao+incêncio',
'engeheiro+de+gás',
'engenheiro+de+gerador',
'geólogo',
'graduado+de+engenharia+elétrica',
'engenharia+de+hnc',
'supervisor+de+relações+trabalhistas',
'especialista+em+lei+do+trabalho',
'graduado+em+RH',
'headhunter',
'administrador+de+RH',
'assistente+de+RH',
'diretor+de+RH',
'supervisor+de+RH',
'cuidado+animal',
'cardiologista',
'farmacêutico',
'enfermeiro+em+saúde+infantil',
'Podólogo',
'quiropraxista',
'assistente+clinico',
'psicologia+clinica',
'cientista+clinico',
'enfermeiro+comunitário',
'enfermeiro+de+cirurgia+cosmética',
'auxiliar+odontológico',
'higienista+dental',
'enfermeiro+odontologista',
'dentista',
'enfermeiro+especialista+em+diabetes',
'nutricionista',
'médico',
'cirurgião',
'psicologista+educacional',
'médico',
'médico+substituto',
'cabeleireiro',
'assistente+de+saúde',
'assistente+de+saúde',
'enfermeiro+visitador',
'cuidado+em+domicílio',
'médico+de+hospital',
'supervisor+de+hospital',
'assistente+de+laboratório',
'trabalhador',
'Fonoaudiólogo+de+línguas',
'massagista',
'Babá',
'administração+médica',
'diretor+médico',
'laboratório+médico',
'arquivos+médicos',
'enfermeiro+em+saúde+mental',
'obstetra',
'neurologia',
'médico+do+SUS',
'supervisor+SUS',
'padeiro',
'supervisor+de+banquete',
'barmaid',
'supervisor+de+bar',
'barman',
'supervisor+de+',
'caterer',
'assistente+de+catering',
'chef+de+cozinha',
'chef+de+partida',
'bar+de+coquetel',
'café',
'commis+chef',
'cozinheiro(a)',
'trabalhador+de+cruzeiro',
'sub-chef+de+partida',
'planejamento+de+eventos',
'planejador+de+eventos',
'instrutor+de+educação+fisica',
'supervisor+de+higiene+alimentar',
'preparação+de+alimentos',
'atendimento+a+hóspedes',
'instrutor+de+academia',
'mercados+de+capitais',
'cfa',
'supervisor+de+hse',
'apoio+a+clientes+sênior',
'consultor+de+TI',
'finanças+para+ONGs',
'contabilista+registrado',
'suporte+TI',
'chef+principal',
'supervisor+de+contas+nacionais',
'engenheiro+hvac',
'cobrador',
'secretária',
'cuidado+noturno',
'medicina+nuclear',
'conservador+de+arte',
'banca+comercial',
'finanças+comerciais',
'gerente+de+itil',
'estagiário+de+TI',
'trader+de+commodities',
'gerente+de+compliance',
'contabilidade+de+contratos',
'enfermeiro(a)',
'banca+corporativa',
'finanças+corporativas',
'gerente+de+finanças+corporativas',
'gerente+de+vendas+nacionais',
'contabilidade+de+custo',
'cpa',
'analista+de+crédito',
'controlador+de+crédito',
'recrutador+de+TI',
'supervisor+de+vendas+de+TI',
'hidrologia',
'Anfitrião',
'conformidade+de+aduana',
'cobrador',
'trader+de+derivatives',
'novas+vendas+de+casa',
'especialista+de+TI',
'diretor+financeiro',
'supervisor+de+controle+de+documentos',
'economista',
'suporte+a+sistemas+de+TI',
'engenheiro+de+inspeções',
'chef+de+hotel',
'treinamento+de+TI',
'analista+de+patrimônio',
'investigador+de+patrimônio+',
'engenheiro+de+instalações',
'recepcionista+para+hotel',
'designer+de+interior',
'limpeza+de+hotel',
'programador+j2ee',
'arquiteto+java',
'programador+java',
'nutricionista',
'gerente+de+hotel',
'programador+java',
'programador+javascript',
'graduado+de+finanças+estagiário',
'estagiário+de+finanças',
'auditor+iso+9001',
'porteiro+de+hotel',
'contabilidade+financeira',
'assessor+financeiro',
'analista+financeiro',
'controlador+financeiro',
'assistende+de+caixa+de+supermercado',
'programador+júnior',
'Saúde+ocupacional',
'Terapeuta+ocupacional',
'diretor+financeiro',
'planejador+financeiro',
'oficial+de+recursos+humanos',
'enfermeiro+de+oncologia',
'oftalmologia',
'administrador+de+linux',
'programador+linux',
'engenheiro+de+elevadores',
'técnico+de+óptica',
'gerence+financeiro',
'analista+de+renda+fixa',
'vendas+ortopédicas',
'optometrista',
'supervisor+de+manutenção',
'prevenção+a+fraude',
'vendas+de+embalagens',
'recepção',
'contabilista+de+fundos',
'recepção+de+hotel',
'fuzileiro',
'gerente+de+fundos',
'marketing+de+fundos',
'Razão',
'contabilidade+governamental',
'graduado+em+contabilidade',
'graduado+em+finanças',
'mcse',
'supervisor+financeiro',
'finanças+de+saúde',
'programador+de+aplicativos+para+celular',
'designer+de+iu+para+celular',
'ms+access',
'gerente+de+hedge+fund',
'vendas+farmacêuticas',
'pré+vendas',
'homeopata',
'assessor+financeiro+independente',
'oftalmologia',
'vendas+de+impressão',
'engenheiro+mecânico',
'mysql',
'comercial+de+seguros',
'corretor+de+seguros',
'enfermeiro+pediátrico',
'gerente+de+reivindicações+de+seguro',
'ajustador+de+sinistro',
'subscritor+de+seguro',
'assistente+de+cozinha',
'genrente+de+cozinha',
'ajudante+de+cozinha',
'paramédico',
'administrador+de+rede',
'engenheiro+de+rede',
'interim+finance',
'genrente+de+centro+de+lazer',
'chef+de+cozinha',
'comercial+de+produto',
'auditor+interno',
'live+in+chef',
'enfermeiro+meio+período',
'investigador+médico',
'secretário+médico',
'gerente+de+folha+de+pagamentos',
'assesor+pessoal',
'vendas+de+publicações',
'soldador+MIG',
'programador+objective+c',
'imposto+internacional',
'museu',
'gerente+de+comunidade+online',
'online+copywriting',
'analista+de+investimentos',
'consultor+de+recrutamento',
'banqueiro+de+investimento',
'relações+com+investidores',
'contabilista+junior',
'gerente+de+contas+chave',
'gerente+de+contas+regionais',
'mineiro',
'boate',
'oracle+dba',
'programador+oracle',
'supervisor+de+projecto+oracle',
'supervisor+de+conformidades+legais',
'oficial+de+crédito',
'programador+perl',
'farmacêutico',
'programador+php',
'programador+python',
'porteiro',
'gerente+de+relacionamento',
'media+finance',
'assesor+de+hipoteca',
'corretor+de+hipoteca',
'contabilista+recém+formado',
'barman+meio+período',
'part+qualified+accountant',
'contabilista+meio+período',
'fisioterapeuta',
'chef+de+cozinha+meio+período',
'executivo+de+venda+a+varejo',
'podologista',
'engenheiro+de+minas',
'recrutador',
'programador+ruby',
'supervisor+de+venda+a+varejo',
'sap+abap',
'esporte+a+motor',
'sap+bw',
'sap+crm',
'enfermeiro+de+prisídio',
'arquiteto+naval',
'engenheiro+naval',
'supervisor+de+implementação+sap',
'sap+sd',
'analista+sap',
'engenheiro+de+satélites',
'enfermeiro+pessoal',
'enfermeiro+psiquiátrico',
'psiquiatra',
'psicólogo',
'técnico+em+radiologia',
'radiologista',
'engenharia+nuclear',
'otimização+de+motor+de+busca',
'engenharia+offshore',
'assistente+de+vendas',
'enfermeiro+de+escola',
'assistente+de+folha+de+pagamentos',
'folha+de+pagamentos',
'contabilista+de+pensões',
'chefe+de+pastelaria',
'banqueiro+pessoal',
'oficial+de+planejamento',
'banca+privada',
'Patrimônio+liquido+privado',
'gestão+de+patrimônio+privado',
'contabilista+de+produção',
'diretor+de+vendas',
'ultra-sonografista',
'contabilista+de+projectos',
'finanças+imobiliárias',
'Fonoaudiólogo',
'finanças+do+setor+público',
'secretário+de+compras+de+razão',
'analista+quantitativo',
'chef+pessoal',
'finanças+quantitativas',
'web+designer+sênior',
'psicologia+do+esporte',
'massagem+esportiva',
'nutrição+esportiva',
'engenheiro+óptico',
'chefe+de+cozinha+de+pub',
'secretário+de+vendas+de+razão',
'comercial',
'programador+shell',
'siebel',
'social+media',
'programador+software',
'publicado',
'engenheiro+de+software',
'supervisor+de+vendas+de+software',
'engenheito+de+testes+de+software',
'supervisor+de+rh+sênior',
'arquiteto+de+soluçóes',
'cirurgião',
'programador+sql',
'sybase',
'gerente+de+reservas',
'administrador+de+sistemas',
'arquiteto+técnico',
'settlements+manager',
'engenheiro+de+petróleo',
'corretor',
'finanças+estruturadas',
'uat',
'contabilista+de+impostos',
'assessor+de+impostos',
'apoio+comercial',
'gerente+de+restaurante',
'supervisor+de+imposto',
'desiner+de+iu',
'administrador+unix',
'designer+de+interface+de+usuário',
'especialística+de+imposto',
'tesoureiro',
'analista+de+tesouro',
'gerente+de+pessoal',
'engenheiro+fabril',
'vbscript',
'contabilista+de+fundos',
'desenvolvedor+de+visual+basic',
'underwriter',
'trabalhador+de+fábrica',
'especialista+de+suporte+de+vendas',
'web+analytics',
'web+designer',
'engenheria+de+caminho+de+ferro',
'engenheiro+de+refrigeração',
'xhtml',
'desenvolvedor+de+xml',
'trainer+de+sales',
'silver+service',
'sommelier',
'sous+chef',
'gestor+de+esporte',
'empregado+de+mesa',
'empregada+de+mesa',
'coordenador+de+casamentos',
'planejador+de+casamentos',
'engenheiro+de+reservatório',
'veterinário',
'wine+bar',
'xslt',
'vendas+solares',
'vendas+de+esporte',
'vp+de+finanças',
'gestão+de+patrimônio',
'executivo+de+televendas',
'gestor+de+televendas',
'engenheiro+elêtrico+sênior',
'supervisor+de+vendas+de+território',
'supervisor+de+enfermaria',
'executivo+de+vendas+estagiário',
'tratamento+de+esgotos',
'six+sigma',
'engenharia+de+som',
'engenharia+aeroespacial',
'engenheiro+de+sistemas',
'engenheiro+de+turbinas',
'engenheiro+de+validação',
'tratamento+de+águas',
'inspeção+de+soldagem',
'zend',
'piloto+de+linha+aérea',
'motorista+de+ambulância',
'motorista+de+ônibus',
'motorista',
'motorista+de+ônibus',
'motorista/entregador+de+van+',
'expedição',
'motorista',
'operador+de+empilhadeira',
'transporte',
'coordenador+de+logística',
'caminhão',
'entregador',
'logísticas+offshore',
'entregador+de+encomendas',
'entregador+de+pizza',
'expedição',
'cadeia+logística',
'taxista',
'tratorista',
'maquinista+/+condutor+de+trem',
'motorista+de+caminhão',
'maquinista+/+condutor+de+metrô',
'motorista+de+van',
'supervisor+de+armazém',
'agência+de+publicidade',
'consultor+publicitário',
'copywriter+publicitário',
'recrutamento+de+vendas+publicitárias',
'gerente+de+marketing+afiliado',
'carga+aérea',
'blogger',
'jornalista+de+negócios',
'gerente+de+transporte+de+negócios',
'gerente+de+aluguel+de+carros+',
'supervisor+de+carga',
'gerente+de+conferências',
'motorista+de+van+de+entregas',
'operador+de+grua',
'digital',
'executivo+de+conta+digital',
'gerente+de+conteúdo+digital',
'copywriter+digital',
'gerente+de+marketing+direto',
'gerente+de+distribuição+logística',
'rp+de+moda',
'google+analytics',
'controlador+de+importação+e+exportação',
'google+analytics',
'controlador+de+importação+e+exportação',
'jornalista',
'marketer+junior',
'administrador+de+logística',
'analista+de+logística',
'assistente+de+logística',
'supervisor+de+logística',
'supervisor+de+operações+logistícas',
'supervisor+de+cadeia+de+logística',
'armazém+de+logística',
'gerente+de+armazém+de+logística',
'investigação+de+mercado',
'gerente+de+comunicação+marketing',
'gerente+de+eventos+de+marketing',
'publicidade+dos+mídia',
'gerente+de+mídia',
'técnico+de+automóveis',
'entregador+de+van',
'entrega+de+jornais',
'supervisor+de+turno+da+noite',
'gerente+de+conteúdo+online',
'especialista+em+online+marketing',
'operador+de+armazém+meio+período',
'armazém+permanente',
'executivo+de+contas+de+rp',
'executivo+de+rp',
'estágio+de+rp',
'gerente+de+rp',
'oficial+de+rp',
'executivo+de+investigação',
'expeditor+de+frete+marítimo',
'motorista+por+conta+própria',
'gerente+de+logistíca+sênior',
'seo+copywriter',
'gerente+de+seo',
'marketing+social',
'gerente+de+social+media',
'auxiliar+de+armazém+temporário',
'planejador+de+transporte',
'gerente+de+transporte',
'mecânico+técnico+de+automóvel',
'administrador+de+armazém',
'motorista+de+armazém',
'armazém+turno+noite',
'armazém+turno+noite',
'operador+armazém',
'embaladoria+de+armazém',
'assistente+de+publicitário',
'estágio+de+publicidade',
'executivo+publicitário',
'executivo+de+afiliados',
'programa+de+afiliados',
'copywriting',
'digital+media',
'graduado+em+marketing',
'cmo',
'chief+marketing+officer',
'publicidade+online',
'rp+online',
'diretor+de+rp',
'gestor+de+conta+de+rp',
'supervisor+de+rp',
'assessoria+de+imprensa',
'internet+marketing',
'supervisor+de+seo',
'diretor+de+seo',
'supervisor+de+marca',
'gerente+de+marca',
'rp+financeiro',
'rp+meio+período',
'rp',
'publicidade',
'gerente+publicitário',
'marketing+digital',
'marketing+online',
'gerente+de+marketing',
'carteiro',
'condução',
'bagageiro',
'executivo+de+marketing+digital',
'estagiário+de+marketing',
'entregador+de+jornais',
'homem+da+companhia+de+mudanças',
'executivo+de+seo',
'controlador+de+estoque',
'motorista+de+van',
'embalador+de+armazém',
'executivo+de+conta+publicitária',
'motorista+entregador',
'investigador+de+mercado',
'gerente+de+marketing+online',
'embalador',
'gerente+de+ppc',
'Rio+Branco',
'Maceió',
'Macapá',
'Manaus',
'Salvador',
'Fortaleza',
'Brasilía',
'Vitória',
'Goiânia',
'São+Luís',
'Cuiabá',
'Campo+Grande',
'Belo+Horizonte',
'Belém',
'João+Pessoa',
'Curitiba',
'Recife',
'Teresina',
'Natal',
'Porto+Alegre',
'Rio+de+Janeiro',
'Porto+Velho',
'Boa+Vista',
'Florianópolis',
'São+Paulo',
'Aracaju',
'Palmas',
'Tocantins',
'Sergipe',
'Santa+Catarina',
'Roraima',
'Rondônia',
'Rio+Grande+do+Sul',
'Rio+Grande+do+Norte',
'Piauí',
'Pernambuco',
'Paraná',
'Pará',
'Minas+Gerais',
'Mato+Grosso+do+Sul',
'Mato+Grosso',
'Maranhão',
'Goiás',
'Espírito+Santo',
'Distrito+Federal',
'Ceará',
'Bahia',
'Amazonas',
'Amapá',
'Alagoas',
'Acre',
'Engenharia,+São+Paulo',
'Engenharia,+Rio+de+Janeiro',
'Engenharia,+Fortaleza',
'Engenharia,+Curitiba',
'Finanças,+Rio+de+Janeiro',
'Finanças,+Brasília',
'Finanças,+São+Paulo',
'Finanças,+Porto+Alegre',
'TI,+Vitória',
'TI,+Goiânia',
'TI,+Brasília',
'TI,+São+Paulo',
'Marketing,+Rio+de+Janeiro',
'Marketing,+São+Paulo',
'Marketing,+Brasília',
'Marketing,+Salvador',
'Enfermagem,+Belo+Horizonte',
'Enfermagem,+Curitiba',
'Enfermagem,+Manaus',
'Enfermagem,+São+Paulo'
]
counts = Hash.new(0)
j=0
while j<queries.count
  queryurl='http://dcc.ufrj.br/~diogobor/browse.php?u=http://empregos.mitula.com.br/empregos/'+queries[j]
 # puts queryurl
  doc = Nokogiri::HTML(open(URI::encode(queryurl)))
doc.search("div[@class='listing sponsored']").each do |node|
  #puts node
    cells=node.search("small") 
   # puts cells.text
    name=cells.text.gsub!(/.*?(?=em )/, "") 
   # puts name
    name.slice! "em "  
   # puts name
    data={
         advertiser: name,
         occurrences: counts[name] += 1
    }
          ScraperWiki::save_sqlite(['advertiser'], data)
    end
j=j+1
end