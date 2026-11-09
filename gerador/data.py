# Conteúdo do guia da Turquia, fiel ao roteiro revisado enviado pela Luciane
# (Roteiro_Turquia_Layout_Bulgaria_1.docx). Cada item: t = horário, n = nome,
# p = parágrafos, m = busca no Google Maps, l = [(rótulo, url)], k = "move" para deslocamentos.

from urllib.parse import quote_plus

def maps(q):
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(q)

def route(points, mode):
    o, d, w = points[0], points[-1], points[1:-1]
    u = ("https://www.google.com/maps/dir/?api=1&origin=" + quote_plus(o)
         + "&destination=" + quote_plus(d))
    if w:
        u += "&waypoints=" + quote_plus("|".join(w))
    return u + "&travelmode=" + mode

TITLE = "Turquia"
SUBTITLE = "Roteiro histórico e arqueológico"
DATES = "28 de dezembro de 2026 a 4 de janeiro de 2027"
GROUP = "6 pessoas · Istambul e costa do Egeu"

INTRO = [
    "28 de dezembro de 2026 a 4 de janeiro de 2027. Quatro dias em Istambul e quatro na costa do Egeu, de van, com volta por Izmir.",
    "Todos os horários abaixo são locais da Turquia. Distâncias e tempos de deslocamento são estimativas de planejamento, não medições de navegação em tempo real. A base considerada em Istambul é Sultanahmet; o endereço do hotel, o trânsito, as filas e as pausas podem alterar os percursos. Reconfirmar os horários das atrações perto da viagem.",
]

DAYS = [
 dict(id="dia1", n=1, wd="Segunda", date="28/12", long="28 de dezembro", place="Roma → Istambul",
  title="Chegada, hotel e jantar", short="Chegada",
  route=route(["Istanbul Airport", "Sultanahmet, Istanbul"], "driving"),
  intro=[],
  items=[
   dict(t="17h", n="Pouso em Istambul", m="Istanbul Airport IST", p=[
    "Considerando que 17h seja o horário de chegada indicado na passagem, já se trata do horário turco. Não acrescentar novamente as duas horas de diferença em relação a Roma. Reservar cerca de 1h–1h30 para desembarque, imigração e retirada das malas."]),
   dict(t="18h–19h30/20h30", n="Transfer e chegada ao hotel", m="Sultanahmet, Istanbul", p=[
    "Para seis pessoas com bagagem, reservar van. IST → Sultanahmet: aproximadamente 45–50 km, com 1h–1h30 de carro; SAW → Sultanahmet: aproximadamente 45–55 km, com 1h15–2h, conforme trânsito e rota. A chegada ao hotel tende a ficar entre 19h e 20h30. Usar 19h30 como referência, com flexibilidade."]),
   dict(t="20h–21h30", n="Jantar perto do hotel", m="restaurantes Sultanahmet Istanbul", p=[
    "Depois do check-in, jantar em Sultanahmet, preferencialmente a 5–10 minutos a pé do hotel. Se o transfer atrasar, jantar mais tarde ou no próprio hotel. Noite de descanso, sem visitas nem deslocamento para Gálata."]),
  ]),
 dict(id="dia2", n=2, wd="Terça", date="29/12", long="29 de dezembro", place="Istambul",
  title="Sultanahmet, arqueologia e Torre de Gálata", short="Sultanahmet e Gálata",
  route=route(["Hagia Sophia, Istanbul", "Blue Mosque, Istanbul", "Basilica Cistern, Istanbul",
               "Istanbul Archaeological Museums", "Galata Tower, Istanbul", "Istiklal Avenue, Istanbul"], "walking"),
  intro=["Percurso: Santa Sofia → Mesquita Azul → Cisterna da Basílica → almoço → Museus Arqueológicos → Gálata → Galip Dede e İstiklal. Os museus ficam antes da travessia do Corno de Ouro. Topkapı permanece na quarta-feira, pois fecha às terças."],
  walk="Caminhada estimada do dia: 5–7 km incluindo parte dos percursos internos e as lojas, usando o T1 na travessia. Fazer todo o trecho museus → torre a pé acrescentaria esforço: são aproximadamente 2,5–3 km, com subida ao final.",
  items=[
   dict(t="9h–10h15", n="Santa Sofia", m="Hagia Sophia, Istanbul", p=[
    "Chegar por volta das 8h45 para segurança e fila. A visita turística percorre as galerias; reservar 1h15 no interior, ajustando a saída se houver espera. Verificar o ingresso e as condições de acesso antes da viagem.",
    "Observe a grande cúpula, os revestimentos de mármore e os mosaicos acessíveis nas galerias. O mais interessante é perceber as camadas do edifício: a igreja imperial de Justiniano, sua transformação em mesquita e as intervenções que continuam a modificar a experiência de visita."]),
   dict(k="move", p=["Até a Mesquita Azul: cerca de 400–600 m, 10–15 minutos a pé, conforme os portões de acesso."]),
   dict(t="10h30–11h10", n="Mesquita Azul", m="Blue Mosque Sultan Ahmed Mosque, Istanbul", p=[
    "Visita ao interior e ao pátio, observando os azulejos, a iluminação e o espaço de oração. Levar lenço para o cabelo e calçado fácil de tirar. O acesso turístico é interrompido durante as orações; ajustar a visita à sinalização do dia."]),
   dict(k="move", p=["Até a cisterna: cerca de 500–700 m, 10–15 minutos a pé."]),
   dict(t="11h25–12h20", n="Cisterna da Basílica", m="Basilica Cistern, Istanbul", l=[("Site oficial", "https://yerebatan.com")], p=[
    "A visita leva cerca de cinquenta minutos, incluindo o percurso entre as colunas e as duas cabeças de Medusa. Interessa observar a reutilização de elementos antigos na infraestrutura da cidade bizantina; as razões exatas da disposição das Medusas ainda são discutidas."]),
   dict(t="12h30–13h30", n="Almoço na região da Rua Yerebatan", m="restaurantes Yerebatan Caddesi Alemdar Istanbul", p=[
    "Almoço com calma perto da cisterna. Escolher um restaurante no eixo Yerebatan–Alemdar para continuar em direção aos museus. Deslocamento para o restaurante: aproximadamente 100–300 m, 3–5 minutos a pé."]),
   dict(k="move", p=["Restaurante → Museus Arqueológicos: aproximadamente 700–900 m, 15 minutos a pé, com subida na chegada."]),
   dict(t="13h45–16h15", n="Museus Arqueológicos de Istambul", m="Istanbul Archaeological Museums",
    l=[("Turkish Museums", "https://www.turkishmuseums.com/museum/detail/2066-istanbul-arkeoloji-muzeleri/2066/4")], p=[
    "Reservar 2h30. Começar pelos sarcófagos da necrópole real de Sidon: o chamado Sarcófago de Alexandre, o das Mulheres Enlutadas e o de Tabnit. Depois, percorrer as demais coleções no seu ritmo. Confirmar quais alas estarão acessíveis, especialmente o Museu do Antigo Oriente e o Pavilhão Azulejado."]),
   dict(t="16h15–17h", n="Deslocamento para Gálata", k="move", m="Karaköy tram station, Istanbul", p=[
    "Caminhar até a parada Gülhane, tomar o bonde T1 no sentido Kabataş e descer em Karaköy. De lá, subir a pé até a torre: aproximadamente 600–800 m, 15–20 minutos em ladeira. Reservar 40–45 minutos para o conjunto, incluindo espera. Para poupar a subida, usar transporte até uma rua acessível próxima à torre; o tempo dependerá do trânsito. Não há visita à Estação Sirkeci."]),
   dict(t="17h–18h", n="Torre de Gálata", m="Galata Tower, Istanbul", l=[("Site oficial", "https://galatakulesi.gov.tr/ziyaret")], p=[
    "Subir à torre para observar o Corno de Ouro, a península histórica e o Bósforo na transição para a noite. O bloco inclui uma margem inicial de fila; se a espera aumentar, reduzir o passeio seguinte. A vista depende do clima. O horário atualmente divulgado permite visita noturna, mas deve ser reconfirmado para 29/12."]),
   dict(t="18h15–19h15", n="Café, Galip Dede e Rua İstiklal", m="Galip Dede Caddesi, Istanbul", p=[
    "Subir pela Galip Dede Caddesi em direção a Tünel e ao início da İstiklal: aproximadamente 500–700 m, 10–15 minutos, sem contar paradas. Tempo para café e lojas; a caminhada pode chegar a 1–1,5 km conforme o trecho de İstiklal escolhido. As compras previstas na chegada passam para este momento."]),
   dict(t="19h30–20h30", n="Jantar em Beyoğlu", m="restaurantes Tünel Beyoğlu Istanbul", p=[
    "Jantar na região de Tünel/İstiklal, perto de onde o passeio terminar. Depois, voltar ao hotel em Sultanahmet: aproximadamente 5–7 km de carro, 20–45 minutos conforme trânsito. Para seis pessoas, combinar van ou dois táxis."]),
  ]),
 dict(id="dia3", n=3, wd="Quarta", date="30/12", long="30 de dezembro", place="Istambul",
  title="Topkapı, Sinan e a cidade dos comerciantes", short="Topkapı e bazares",
  route=route(["Topkapi Palace, Istanbul", "Hagia Irene, Istanbul", "Grand Bazaar Nuruosmaniye Gate, Istanbul",
               "Süleymaniye Mosque, Istanbul", "Spice Bazaar, Istanbul", "Hamdi Restaurant Eminönü"], "walking"),
  intro=["Percurso: Topkapı e Santa Irene → almoço em Sultanahmet → Grande Bazar → Süleymaniye → Bazar das Especiarias → jantar no Hamdi. O caminho avança para oeste e depois desce para Eminönü."],
  walk="Caminhada estimada: 7–9 km no dia, incluindo Topkapı e o interior dos bazares. O trecho urbano entre o complexo do palácio e Eminönü soma aproximadamente 3,5–4 km; a circulação dentro das atrações varia bastante.",
  items=[
   dict(t="8h40", n="Chegada ao Palácio Topkapı", m="Topkapi Palace, Istanbul",
    l=[("Milli Saraylar", "https://www.millisaraylar.gov.tr/Lokasyon/2/Topkapi-Sarayi?culture=en")], p=[
    "Chegue antes da abertura, às 9h, com ingresso que inclua o Harém e Santa Irene. O Topkapı foi residência dos sultões e centro do governo otomano por quase quatro séculos."]),
   dict(t="9h–12h30", n="Topkapı com Harém", m="Topkapi Palace Harem, Istanbul", p=[
    "Comece pelo Harém e siga pelas salas do governo, pelo Tesouro, pelas Relíquias Sagradas e pelos pátios e terraços. Vale dar atenção à organização do poder dentro do palácio: quem podia atravessar cada portão, como funcionavam as audiências e como a vida da família imperial se relacionava com a sucessão dinástica. Nas Relíquias Sagradas, observe a ligação entre autoridade política e legitimidade religiosa."]),
   dict(t="12h30", n="Santa Irene", m="Hagia Irene, Istanbul", p=[
    "No primeiro pátio do complexo, uma igreja bizantina muito diferente da Santa Sofia. Na abside, a grande cruz sobre fundo dourado merece atenção pela relação com o período iconoclasta, quando o uso de imagens religiosas foi intensamente disputado."]),
   dict(t="13h–14h", n="Almoço em Sultanahmet", m="restaurantes Divanyolu Caddesi Istanbul", p=[
    "Sair pelo portão imperial e almoçar no eixo da Divanyolu. Prever cerca de 10 minutos a pé desde Santa Irene, conforme o restaurante, e uma pausa de aproximadamente 50 minutos."]),
   dict(t="14h–14h30", n="Caminhada até o Grande Bazar", k="move", m="Column of Constantine Çemberlitaş, Istanbul", p=[
    "Seguir pela Divanyolu até a entrada de Nuruosmaniye. Conforme o restaurante, são aproximadamente 1–1,3 km, 20–30 minutos. A via acompanha parte do antigo eixo cerimonial de Constantinopla e passa pela Coluna de Constantino."]),
   dict(t="14h30–15h30", n="Grande Bazar", m="Grand Bazaar Nuruosmaniye Gate, Istanbul", p=[
    "Percorrer as galerias, escolhendo lojas de cerâmica, tecidos, joias ou antiguidades. Sair pelo lado de Beyazıt para seguir à Süleymaniye. O tempo dentro do bazar inclui compras e orientação entre as galerias."]),
   dict(k="move", p=["Beyazıt → Süleymaniye: aproximadamente 800 m–1 km, 15–20 minutos a pé."]),
   dict(t="15h50–16h40", n="Mesquita Süleymaniye", m="Süleymaniye Mosque, Istanbul", p=[
    "Começar pelo pátio e pelo terraço com vista para o Corno de Ouro; visitar o interior assim que o acesso turístico estiver liberado após a oração. Observar as proporções e a luz na arquitetura de Sinan. Os túmulos ficam sujeitos ao horário de acesso e ao tempo disponível. O horário exato das orações deve ser conferido no dia."]),
   dict(t="16h40–17h", n="Descida para Eminönü", k="move", p=[
    "Seguir pelas ruas comerciais até o Bazar das Especiarias: aproximadamente 900 m–1,1 km, 20 minutos a pé, predominantemente em descida. Com piso molhado, caminhar com cuidado e prever alguns minutos extras."]),
   dict(t="17h–18h45", n="Bazar das Especiarias e ruas de Eminönü", m="Spice Bazaar, Istanbul", p=[
    "Tempo para compras, ruas comerciais e uma pausa para café. Confirmar o fechamento do bazar para a data; se houver atraso na mesquita, usar parte deste bloco para absorvê-lo."]),
   dict(t="19h–20h15", n="Jantar no Hamdi de Eminönü", m="Hamdi Restaurant Eminönü, Istanbul", p=[
    "Reservar a unidade ao lado do bazar e pedir mesa com vista. Caminhada de aproximadamente 100–200 m, 3–5 minutos. Se já houver reserva às 19h30, mantê-la e prolongar a pausa para café. Retorno a Sultanahmet: cerca de 2–3 km; reservar 15–30 minutos com transporte, conforme trânsito ou espera do T1."]),
  ]),
 dict(id="dia4", n=4, wd="Quinta", date="31/12", long="31 de dezembro", place="Istambul",
  title="Chora, Balat, Fener, Dolmabahçe e o Bósforo", short="Chora e Bósforo",
  route=route(["Chora Church Kariye Mosque, Istanbul", "Tekfur Palace, Istanbul", "Bulgarian St. Stephen Church, Istanbul",
               "Ecumenical Patriarchate of Constantinople", "Dolmabahçe Palace, Istanbul"], "driving"),
  intro=["A manhã fica na Constantinopla cristã e a tarde no Bósforo, com volta ao hotel às 18h, a tempo do réveillon. Beylerbey é visto do barco: é um palácio do século XIX do mesmo estilo de Dolmabahçe."],
  items=[
   dict(t="8h30", n="Táxi até Chora", k="move", m="Chora Church Kariye Mosque, Istanbul", p=[
    "Comece pelo ponto mais afastado do roteiro: Chora, hoje Kariye Camii, na região de Edirnekapı."]),
   dict(t="9h–10h15", n="Chora", m="Chora Church Kariye Mosque, Istanbul", p=[
    "Observe os mosaicos e afrescos acessíveis, especialmente os ciclos da vida de Maria e de Cristo e a Anástasis, com Cristo retirando Adão e Eva dos túmulos. Vale relacionar as imagens às narrativas religiosas, inclusive às tradições apócrifas que influenciaram a representação da infância de Maria, como o Proto-Evangelho de Tiago. Alguns mosaicos da área de culto ficam cobertos. Chora fecha para turistas às sextas; o dia 31 é quinta."]),
   dict(t="10h15–11h30", n="Descida a pé por Balat", m="Balat, Istanbul", p=[
    "Desça em direção ao Corno de Ouro, passando pelo exterior de Tekfur Sarayı e das muralhas. Explore as ruas históricas, com casas coloridas, pequenos comércios e cafés, atentando para as marcas da história judaica e cristã do bairro. Termine na Igreja Búlgara de Santo Estêvão, a Igreja de Ferro, de estrutura metálica pré-fabricada; entre se estiver aberta."]),
   dict(t="11h45", n="Patriarcado Ecumênico e Igreja de São Jorge", m="Ecumenical Patriarchate of Constantinople, Fener",
    l=[("Patriarcado", "https://ec-patr.org")], p=[
    "A continuidade viva do cristianismo ortodoxo na antiga Constantinopla. Visite a Igreja de São Jorge conforme o acesso do dia, respeitando eventuais celebrações."]),
   dict(t="12h15", n="Almoço em Fener", m="restaurantes Fener Istanbul", p=[]),
   dict(t="13h15", n="Táxi até Dolmabahçe", k="move", m="Dolmabahçe Palace, Istanbul", p=[]),
   dict(t="14h–16h", n="Palácio Dolmabahçe", m="Dolmabahçe Palace, Istanbul",
    l=[("Ingressos (Milli Saraylar)", "https://www.millisaraylar.gov.tr")], p=[
    "O palácio do século XIX para onde a corte se mudou ao deixar o Topkapı. A visita tem duas partes, o Selamlık e o Harém, e pede pelo menos duas horas. Compre o ingresso no site oficial (millisaraylar.gov.tr); ele não entra no Museum Pass. A bilheteria fecha às 17h."]),
   dict(t="16h15–17h30", n="Barco privado pelo Bósforo", m="Beşiktaş pier, Istanbul", p=[
    "Um barco privado para o grupo sai de Beşiktaş, ao lado do palácio, sobe o Bósforo passando por Beylerbey, Ortaköy e a Fortaleza de Rumeli, e volta com o pôr do sol, desembarcando em Karaköy. É a hora em que o estreito mostra melhor como a cidade se organiza entre duas margens e dois continentes."]),
   dict(t="18h", n="Volta ao hotel e réveillon", p=[
    "Evite a İstiklal e Taksim depois das 17h, por causa da lotação e dos bloqueios. Os fogos principais são vistos do Bósforo, em Ortaköy. O jantar de réveillon precisa estar reservado: quase todos os restaurantes têm menu fechado e lotam."]),
  ]),
 dict(id="dia5", n=5, wd="Sexta", date="1/1", long="1 de janeiro", place="Istambul → Troia → Assos",
  title="Troia", short="Troia",
  route=route(["Sultanahmet, Istanbul", "Troy Museum, Tevfikiye", "Troy Ancient City", "Behramkale, Assos"], "driving"),
  intro=["O 1º de janeiro é feriado civil, e a saída de Istambul costuma estar vazia. Confirme antes que Troia abre nesse dia."],
  items=[
   dict(t="9h", n="Saída de Istambul de van", k="move", m="1915 Çanakkale Bridge", p=[
    "Cerca de 300 km pela ponte Çanakkale 1915, com pedágios na rodovia e na ponte. Com uma parada, são de 4h a 4h30 de estrada."]),
   dict(t="13h30", n="Chegada em Troia e almoço rápido", m="Tevfikiye, Çanakkale", p=[]),
   dict(t="14h", n="Museu de Troia", m="Troy Museum, Tevfikiye", p=[
    "O museu fica a cerca de 1 km da entrada do sítio. Reserve uma hora e quinze minutos."]),
   dict(t="15h20", n="Sítio arqueológico de Troia", m="Troy Ancient City archaeological site", p=[
    "Percorra o sítio com a luz baixa da tarde, até o fechamento."]),
   dict(t="17h", n="Saída para Assos", k="move", m="Temple of Athena, Behramkale Assos", p=[
    "São 65 km, cerca de 1 hora; a chegada será no escuro. Confirme o hotel com antecedência: muitos hotéis do porto de Assos fecham no inverno. Se ainda houver luz, o Templo de Atena, no alto da vila de Behramkale, tem vista para a ilha de Lesbos."]),
  ]),
 dict(id="dia6", n=6, wd="Sábado", date="2/1", long="2 de janeiro", place="Assos → Pérgamo → Selçuk",
  title="Pérgamo", short="Pérgamo",
  route=route(["Behramkale, Assos", "Pergamon Acropolis, Bergama", "Red Basilica, Bergama", "Asclepieion of Pergamon", "Bergama Archaeological Museum", "Selçuk, İzmir"], "driving"),
  intro=["Pérgamo reúne arquitetura monumental, religião antiga e um grande santuário de cura. A cidade atual chama-se Bergama, e as visitas se distribuem por quatro lugares. Saindo às 8h, dá para ver tudo antes de os sítios fecharem, por volta das 17h."],
  items=[
   dict(t="8h", n="Saída de Assos", k="move", p=["Cerca de 2h30 pela costa, via Edremit e Ayvalık."]),
   dict(t="10h30–12h45", n="A Acrópole", m="Pergamon Acropolis, Bergama", p=[
    "A cidade antiga no alto da colina, com templos, palácios e espaços públicos em terraços. Os destaques são o teatro helenístico, com arquibancadas muito íngremes e uma vista impressionante; o Templo de Trajano, com parte das colunas de mármore reerguidas; os vestígios do santuário de Atena e da biblioteca, importante centro de conhecimento da Antiguidade; e as fundações do Grande Altar de Pérgamo, o Altar de Zeus, cuja reconstrução e relevos estão em Berlim.",
    "Suba de teleférico se estiver funcionando; ele para com vento forte, e nesse caso a van sobe até o estacionamento do alto. No inverno venta muito lá em cima: casaco corta-vento e gorro."]),
   dict(t="13h", n="Almoço em Bergama", m="restaurantes Bergama", p=[]),
   dict(t="14h", n="Basílica Vermelha (Kızıl Avlu)", m="Red Basilica Kızıl Avlu, Bergama", p=[
    "Um enorme edifício romano de tijolos vermelhos, originalmente um templo dedicado a divindades egípcias, conhecido como templo de Serápis. Depois, parte do conjunto foi transformada em igreja cristã, uma mudança de uso muito ligada ao seu interesse pelas transformações das religiões. Reserve uns quarenta minutos."]),
   dict(t="14h45–16h15", n="O Asclepieion", m="Asclepieion of Pergamon, Bergama", p=[
    "O santuário de Asclépio, deus da cura, que recebia pessoas em busca de tratamento. Entre os vestígios estão a via de acesso, os pórticos, um teatro e estruturas ligadas aos tratamentos. O interesse está em ver como culto religioso e práticas de cura conviviam no mundo antigo."]),
   dict(t="16h20", n="Museu Arqueológico de Bergama", m="Bergama Archaeological Museum", p=[
    "Reúne peças das escavações da acrópole, do Asclepieion e de outros sítios da região. Entre se ainda aceitar visitantes; é o primeiro item a sair se o dia atrasar."]),
   dict(t="17h", n="Saída para Selçuk", k="move", m="Selçuk, İzmir", p=["Cerca de 190 km, com pedágios; chegada por volta das 19h15."]),
  ]),
 dict(id="dia7", n=7, wd="Domingo", date="3/1", long="3 de janeiro", place="Selçuk",
  title="Éfeso", short="Éfeso",
  route=route(["Selçuk, İzmir", "House of the Virgin Mary, Selçuk", "Ephesus Upper Gate", "Ephesus Lower Gate",
               "Basilica of St. John, Selçuk", "Ephesus Archaeological Museum, Selçuk", "Şirince"], "driving"),
  intro=["Manter quatro horas para Éfeso e 1h30 para o museu. Usar a van entre os pontos mais afastados; a visita termina em Şirince, sem parada no Templo de Ártemis."],
  items=[
   dict(t="7h30–8h", n="Selçuk → Casa da Virgem Maria", k="move", p=[
    "Saída do hotel. Aproximadamente 8–10 km de estrada em subida, 20–30 minutos. Confirmar a abertura às 8h no inverno; se o acesso começar mais tarde, ajustar este primeiro bloco com o motorista e o guia."]),
   dict(t="8h–8h40", n="Casa da Virgem Maria", m="House of the Virgin Mary Meryem Ana Evi, Selçuk", p=[
    "Visita de cerca de quarenta minutos. A tradição liga o local a Maria e ao apóstolo João; distinguir essa tradição religiosa da comprovação histórica do edifício."]),
   dict(k="move", p=["Casa da Virgem Maria → portão superior de Éfeso: aproximadamente 5–7 km, 10–15 minutos de van; o restante da margem até as 9h fica para ingresso e entrada."]),
   dict(t="9h–13h", n="Éfeso", m="Ephesus Upper Gate, Selçuk", p=[
    "Dentro do sítio, a sequência é: a Ágora do Estado, o Odeon e o Prytaneion, a parte administrativa e política da cidade; a Rua dos Curetes, descendo entre fontes, monumentos e o Templo de Adriano; as Casas nos Terraços (Yamaç Evler), pelos mosaicos, pinturas e interiores das residências, com ingresso adicional e escadas; a Biblioteca de Celso, a fachada mais conhecida de Éfeso; a Ágora comercial, o Grande Teatro e a Via do Porto; e, por fim, a Igreja de Maria, associada ao Concílio de Éfeso de 431.",
    "Um guia particular com foco em arqueologia e história das religiões rende muito aqui. Há aviso de obras entre a Biblioteca de Celso e o teatro, e o percurso pode precisar de ajustes."]),
   dict(k="move", p=["Percurso interno: aproximadamente 3–4 km, incluindo desvios para as Casas nos Terraços e a Igreja de Maria. A van deixa o grupo no portão superior e busca no inferior. Portão inferior → centro de Selçuk: cerca de 3–4 km, 10–15 minutos de carro."]),
   dict(t="13h20–14h20", n="Almoço em Selçuk", m="restaurantes Selçuk İzmir", p=[
    "Uma hora de almoço no centro, já contando a saída do sítio e o encontro com a van no bloco anterior. Após a refeição, seguir para a Basílica de São João: aproximadamente 500 m–1 km, 10–15 minutos a pé, com subida, ou um trajeto curto de van."]),
   dict(t="14h30–15h20", n="Basílica de São João", m="Basilica of St. John, Selçuk", p=[
    "Na colina de Ayasuluk estão as ruínas da grande basílica do século VI, construída sob Justiniano sobre o local tradicionalmente identificado como o túmulo do apóstolo João. Mostra a transformação da região em centro de peregrinação cristã. Ao lado fica a Mesquita de İsa Bey, do século XIV. Reservar cerca de cinquenta minutos para a basílica; a mesquita próxima depende do tempo e do acesso."]),
   dict(k="move", p=["Basílica → Museu Arqueológico de Éfeso: aproximadamente 600–800 m, 10–15 minutos a pé, em descida. A margem até 15h40 permite ingresso e uma breve pausa."]),
   dict(t="15h40–17h10", n="Museu Arqueológico de Éfeso", m="Ephesus Archaeological Museum, Selçuk",
    l=[("Ministério da Cultura", "https://muze.gov.tr/muze-detay?distid=efm&sectionid=efm01")], p=[
    "No centro de Selçuk, guarda os achados das escavações. As peças mais conhecidas são as duas estátuas de Ártemis de Éfeso, fundamentais para conhecer a representação da deusa cultuada na cidade. É diferente do Ephesus Experience Museum, dentro do sítio, que é uma experiência audiovisual."]),
   dict(t="17h15–17h40", n="Selçuk → Şirince", k="move", p=[
    "Aproximadamente 8 km, 20–25 minutos de van, por estrada sinuosa. A chegada será ao entardecer ou já escurecendo, conforme a luz e o horário efetivo de saída; não contar com um passeio longo à luz do dia."]),
   dict(t="17h40–19h30", n="Passeio breve e jantar em Şirince", m="Şirince, Selçuk", p=[
    "Caminhada curta pela vila e jantar por volta das 18h. Şirince é conhecida pelas casas tradicionais e pelos vinhos de frutas. Reservar restaurante aberto no inverno; a oferta de lojas pode ser reduzida à noite."]),
   dict(t="19h30–20h", n="Retorno ao hotel em Selçuk", k="move", p=[
    "Cerca de 8 km, 20–25 minutos de van."]),
  ],
  walk="Caminhada estimada do dia: 5–7 km, considerando Éfeso, basílica, museu e um trecho curto em Şirince."),
 dict(id="dia8", n=8, wd="Segunda", date="4/1", long="4 de janeiro", place="Selçuk → Izmir",
  title="Voos de volta", short="Volta por Izmir",
  route=route(["Selçuk, İzmir", "Izmir Adnan Menderes Airport"], "driving"),
  intro=[],
  items=[
   dict(t="Manhã", n="Selçuk → Aeroporto de Izmir (ADB)", k="move", m="Izmir Adnan Menderes Airport", p=[
    "De Selçuk ao aeroporto de Izmir (ADB) é cerca de 1 hora de van, e a van fica em Izmir. Voar de Izmir sai mais barato e evita voltar a Istambul."]),
   dict(n="Cotações saindo de Izmir", p=[
    "Madri, R$ 747 por pessoa (R$ 1.494 para duas); Barcelona, R$ 943; Genebra, R$ 1.648; Stuttgart, R$ 1.649; Sofia, R$ 1.315 por pessoa (R$ 2.630 para duas). Total de R$ 8.364, contra R$ 10.869 saindo de Istambul, uma economia de R$ 2.505."]),
   dict(n="Antes de embarcar", p=[
    "Confira se as conexões em Istambul têm pelo menos 1h30 e se a bagagem vai despachada até o destino final. Pergunte à locadora a taxa de devolução da van em Izmir. Se os voos forem à tarde, a manhã pode ter Şirince ou o que tiver ficado de fora no dia 3."]),
  ]),
]

RESERVAR = [
 ("28/12", "Transfer do aeroporto de Istambul em 28/12.", "dia1"),
 ("29–30/12", "Ingressos de Santa Sofia, Cisterna da Basílica e Topkapı com Harém.", "dia2"),
 ("29–30/12", "Torre de Gálata em 29/12, por volta das 17h, e jantar no Hamdi em 30/12, às 19h (ou manter 19h30 se já reservado).", "dia2"),
 ("31/12", "Ingressos de Dolmabahçe (Selamlık e Harém) para 31/12, às 14h.", "dia4"),
 ("31/12", "Barco privado em 31/12, das 16h15 às 17h30, de Beşiktaş a Karaköy.", "dia4"),
 ("31/12", "Jantar de réveillon.", "dia4"),
 ("1–4/1", "Van de 1 a 4/1: com motorista ou não, e taxa de devolução em Izmir.", "dia5"),
 ("1/1", "Hotel em Assos aberto em janeiro.", "dia5"),
 ("29/12 · 31/12 · 3/1", "Guias para Santa Sofia e Chora, e para Éfeso.", "dia2"),
 ("4/1", "Voos de 4/1 saindo de Izmir.", "dia8"),
]
CONFIRMAR = [
 ("29/12", "Horário de inverno dos Museus Arqueológicos e situação do Museu do Antigo Oriente.", "dia2"),
 ("29/12", "Horários, ingresso e condições de visita à Torre de Gálata em 29/12.", "dia2"),
 ("1/1", "Troia aberta em 1/1.", "dia5"),
 ("2/1", "Teleférico de Pérgamo funcionando.", "dia6"),
 ("3/1", "Obras em Éfeso.", "dia7"),
 ("3/1", "Abertura da Casa da Virgem Maria às 8h, horário de inverno do Museu de Éfeso e restaurante em Şirince para 3/1.", "dia7"),
 ("—", "Museum Pass Türkiye: o que cobre e o preço atual.", None),
]
LEMBRETES = "Em Istambul faz de 5 a 12 °C, e no Egeu de 7 a 14 °C, com chuva frequente. Levem calçado impermeável com sola de borracha, capa de chuva e roupas em camadas. Nas mesquitas, lenço para o cabelo e calçado fácil de tirar. Os horários das orações mudam um pouco a cada dia; confira num app como o Namaz Vakti."

FONTES_NOTA = "Consulta em 9 de novembro de 2026. Os horários futuros podem mudar. As distâncias deste roteiro são aproximações por localização e percurso, com margens de planejamento."
FONTES = [
 ("Torre de Gálata", "página oficial de visita", "https://galatakulesi.gov.tr/ziyaret"),
 ("Topkapı", "Milli Saraylar, fechamento às terças", "https://www.millisaraylar.gov.tr/Lokasyon/2/Topkapi-Sarayi?culture=en"),
 ("Museus Arqueológicos de Istambul", "Turkish Museums", "https://www.turkishmuseums.com/museum/detail/2066-istanbul-arkeoloji-muzeleri/2066/4"),
 ("Museu de Éfeso", "Ministério da Cultura, horário consultado 8h30–17h30", "https://muze.gov.tr/muze-detay?distid=efm&sectionid=efm01"),
]
