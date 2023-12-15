import pygame
import sys

#rodar
pygame.init()

#musica
try:
    pygame.mixer.init()
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()
except pygame.error as e:
    print("erro do pygame:", e)



#informações principais
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rio Breakdown")



#fases: prisao (1), refeitorio (2), cozinha (3), quadra (4), estacionamento (5), lixão (6), pátio (7), lago (8), biblioteca(9),
# cemiterio(10), alojamento(11) e tela vitoria(12)
fase_atual = 1

fechadura = False

#itens
pedecabra_visivel = True
pedecabra = pygame.image.load("items/baseballbat.png")
pedecabra = pygame.transform.scale(pedecabra, (50, 50))
posicao_pedecabra = (700, 350)
colisao_pedecabra = False

botas_visivel = True
botas = pygame.image.load("items/sandalias.png")
botas = pygame.transform.scale(botas, (40, 40))
posicao_botas = (365, 105)
colisao_botas = False

saida_visivel = True
saida = pygame.image.load("items/saida.png")
saida = pygame.transform.scale(saida, (50, 50))
posicao_saida = (450, 325)
colisao_saida = False


panela_visivel = True
panela = pygame.image.load("items/panela.png")
panela = pygame.transform.scale(panela, (50, 50))
posicao_panela = (110, 80)
colisao_panela = False

pa_visivel = True
pa = pygame.image.load("items/pa.png")
pa = pygame.transform.scale(pa, (50, 50))
posicao_pa = (710, 80)
colisao_pa = False


peixe_visivel = True
peixe = pygame.image.load("items/peixao.png")
peixe = pygame.transform.scale(peixe, (50, 50))
posicao_peixe = (700, 100)
colisao_peixe = False


apito_visivel = True
apito = pygame.image.load("items/apito.png")
apito = pygame.transform.scale(apito, (40, 40))
posicao_apito = (373, 275)
colisao_apito = False

medkit_visivel = True
medkit = pygame.image.load("items/medkit.png")
medkit = pygame.transform.scale(medkit, (30, 30))
posicao_medkit = (75, 130)
colisao_medkit = False

leque_visivel = True
leque = pygame.image.load("items/leque.png")
leque = pygame.transform.scale(leque, (40, 40))
posicao_leque = (700, 500)
colisao_leque = False

pirotecnia = pygame.image.load("items/pirotecnia.png")
pirotecnia = pygame.transform.scale(pirotecnia, (24, 30))
pirotecnia_nao_coletada = True

chave = pygame.image.load("items/chave.png")
chave = pygame.transform.scale(chave, (50, 50))
chave_nao_coletada = True

geocinese = pygame.image.load("items/geocinese.png")
geocinese = pygame.transform.scale(geocinese, (24, 30))
geocinese_nao_coletada = True

tormenta = pygame.image.load("items/tormenta.png")
tormenta = pygame.transform.scale(tormenta, (24, 30))
tormenta_nao_coletada = True


vortex = pygame.image.load("items/vortex.png")
vortex = pygame.transform.scale(vortex, (24, 30))
vortex_nao_coletada = True

#colisoes do mapa
col1cozinha = False
col2cozinha = False
col_est = False
col_liv1 = False
col_liv2 = False
col_liv3 = False
col_liv4 = False
col_lixao = False
colmesa1 = False
colmesa2 = False
colbanheiro = False
colbanheiro2 = False
colcela1 = False
colcela2 = False
colcela3 = False
colcela4 = False
colcela5 = False
colcela6 = False
colcela7 = False
colcela8 = False
colcela9 = False
colcela10 = False
colcela11 = False
colcem1 = False
colcem2 = False



#littlemor
imagem = pygame.image.load("sprt_personagens/littlemor.png")
novo_largura = imagem.get_width() * 2
nova_altura = imagem.get_height() * 2
littlemor = pygame.transform.scale(imagem, (novo_largura, nova_altura))

#movimento
tamanho_bloco = 5
posicao_x, posicao_y = 400, 50
velocidade = 5
incremento = velocidade
movendo_para_direita = False

#camera
camera = pygame.Rect(0, 0, largura, altura)

#Caixa de texto
caixa_texto = pygame.image.load("textbox.png")
caixa_texto = pygame.transform.scale(caixa_texto, (largura, 200))
posicao_caixa_texto = (0, altura - 150)
caixa_texto.fill((255, 255, 255))
fonte = pygame.font.Font(None, 36)
cor_texto = (0, 0, 0)


#Policiais e Cachorros
policial = pygame.image.load("sprt_personagens/policial.png")
policial = pygame.transform.scale(policial, (novo_largura, nova_altura))
policial_revertido = pygame.transform.flip(policial, False, False)
policial1, policial2, policial4, policial5, policial6, policial7, policial8, policial9 = policial, policial, policial, policial, policial, policial, policial, policial
policial1_posicaox = 80
policial1_posicaoy = 250
policial2_posicaox = 400
policial2_posicaoy = 430
policial4_posicaox = 200
policial4_posicaoy = 200
policial5_posicaox = 100
policial5_posicaoy = 350
policial6_posicaox = 200
policial6_posicaoy = 500
policial7_posicaox = 200
policial7_posicaoy = 200
policial8_posicaox = 650
policial8_posicaoy = 250
policial9_posicaox = 200
policial9_posicaoy = 500
colisao_policial1 = False
colisao_policial2 = False
colisao_policial4 = False
colisao_policial5 = False
colisao_policial6 = False
colisao_policial7 = False
colisao_policial8 = False
colisao_policial9 = False
vel_policial = 1

cao = pygame.image.load("sprt_personagens/cao.png")
cao = pygame.transform.scale(cao, (novo_largura, nova_altura))
cao_revertido = pygame.transform.flip(cao, False, False)
cao1, cao2, cao3, cao4, cao5, cao6 = cao, cao, cao, cao, cao, cao
cao1_posicaox = 225
cao1_posicaoy = 400
cao2_posicaox = 400
cao2_posicaoy = 150
cao3_posicaox = 575
cao3_posicaoy = 100
cao4_posicaox = 225
cao4_posicaoy = 100
cao5_posicaox = 400
cao5_posicaoy = 250
cao6_posicaox = 575
cao6_posicaoy = 400
colisao_cao1 = False
colisao_cao2 = False
colisao_cao3 = False
colisao_cao4 = False
colisao_cao5 = False
colisao_cao6 = False
vel_cao = 1.2

slots = []


#Blate
blate = pygame.image.load("sprt_personagens/blate.png")
blate = pygame.transform.scale(blate, (novo_largura, nova_altura))
blate_revertido = pygame.transform.flip(blate, True, False)
posicao_blate = (150, 100)
dialogo_aberto_blate = False
texto_blate1 = ("Blate: Tem uma saída da cadeia seguindo à esquerda, traz")
texto_blate2 = ("pra mim quatro cartões escondidos que te passo a chave.")

#Lu Bu
lubu = pygame.image.load("sprt_personagens/lubu.png")
lubu = pygame.transform.scale(lubu, (novo_largura, nova_altura))
lubu_revertido = pygame.transform.flip(lubu, True, False)
posicao_lubu = (400, 425)
dialogo_aberto_lubu = False
texto_lubu1 = ("Lu Bu: QUERO MATAR O COQUINHA! Traz um Taco e uma pá")
texto_lubu2 = ("para eu enterrar aquele meliante corrupto.")

#Lady laura
lady = pygame.image.load("sprt_personagens/ladylaura.png")
lady = pygame.transform.scale(lady, (novo_largura, nova_altura))
lady_revertido = pygame.transform.flip(lady, True, False)
posicao_lady = (650, 80)
dialogo_aberto_lady = False
texto_lady1 = ("Lady Laura: Olá meu bem! Traga-me minhas sandálias e meu")
texto_lady2 = ("leque para que você receba algo muito especial.")

#Coquinha
coq = pygame.image.load("sprt_personagens/coquinha.png")
coq = pygame.transform.scale(coq, (novo_largura, nova_altura))
coq_revertido = pygame.transform.flip(coq, True, False)
posicao_coq = (150, 425)
dialogo_aberto_coq = False
texto_coq1 = ("Coquinha: Lu bu roubou meu lanche! Mó fome! Traz peixe e")
texto_coq2 = ("panela que eu te passo uma carta especial para sua fuga!")

#Sábio
sab = pygame.image.load("sprt_personagens/sabio.png")
sab = pygame.transform.scale(sab, (novo_largura, nova_altura))
sab_revertido = pygame.transform.flip(sab, True, False)
posicao_sab = (650, 435)
dialogo_aberto_sab = False
texto_sab1 = ("Sábio Luan: Coe meu nobrer, to passando mal papo reto, traz")
texto_sab2 = ("um kit médico que te passo um presente daora meu padrin.")

#slots
slot_inventario = pygame.image.load("slot.png")
slot_inventario = pygame.transform.scale(slot_inventario, (100, 100))

posicao_slot1 = (largura // 2 - 250, 0)
posicao_slot2 = (largura // 2 - 150, 0)
posicao_slot3 = (largura // 2 - 50, 0)
posicao_slot4 = (largura // 2 + 50, 0)
posicao_slot5 = (largura // 2 + 150, 0)
posicao_slot6 = (largura // 2 - 250, altura-100)
posicao_slot7 = (largura // 2 - 150, altura-100)
posicao_slot8 = (largura // 2 - 50, altura-100 )
posicao_slot9 = (largura // 2 + 50, altura-100 )
posicao_slot10 = (largura // 2 + 150, altura-100 )

posicao_item_slot = [(largura//2 - 220, 30),(largura//2 - 120, 30),(largura//2 - 20, 30),(largura//2 + 80, 30), (largura//2 + 180, 30), (largura//2 - 220, altura - 75),(largura//2  - 120, altura-75),(largura//2  - 20, altura -75),(largura//2  +80, altura-75),(largura//2  +180, altura-75)]
cards_to_win = []

slots_visiveis = False





#Laço jogo
executando = True
while executando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                slots_visiveis = not slots_visiveis  # Alternar a visibilidade dos slots

            if evento.key == pygame.K_SPACE and colisao_pedecabra and pedecabra_visivel:
                pedecabra_visivel = False
                slots.append(pedecabra)

            if evento.key == pygame.K_SPACE and colisao_botas and botas_visivel:
                botas_visivel = False
                slots.append(botas)

            if evento.key == pygame.K_SPACE and colisao_saida and saida_visivel:
                fase_atual = 12

            if evento.key == pygame.K_SPACE and colisao_panela and panela_visivel:
                panela_visivel = False
                slots.append(panela)

            if evento.key == pygame.K_SPACE and colisao_pa and pa_visivel:
                pa_visivel = False
                slots.append(pa)

            if evento.key == pygame.K_SPACE and colisao_peixe and peixe_visivel:
                peixe_visivel = False
                slots.append(peixe)


            if evento.key == pygame.K_SPACE and colisao_apito and apito_visivel:
                apito_visivel = False
                slots.append(apito)

            if evento.key == pygame.K_SPACE and colisao_medkit and medkit_visivel:
                medkit_visivel = False
                slots.append(medkit)

            if evento.key == pygame.K_SPACE and colisao_leque and leque_visivel:
                leque_visivel = False
                slots.append(leque)



            if panela in slots and peixe in slots:
                texto_coq1 = ("Coquinha: muito obrigado chefe, toma aqui tua carta")
                texto_coq2 = ("do vórtex, prossiga")
                if colisao_coq and vortex_nao_coletada:
                    texto_coq1 = ("Coquinha: me leva contigo, lá fora seremos ricos, te passo")
                    texto_coq2 = ("um carguinho na câmara fácil fácil")
                    slots.append(vortex)
                    vortex_nao_coletada = False
                    slots.remove(peixe)
                    slots.remove(panela)

            if medkit in slots:
                texto_sab1 = ("Sábio Luan: MEU DEUS MEU NOBRE OBRIGADO! Me sinto bem")
                texto_sab2 = ("melhor agora meno tamo junto meno papo reto memo meno ")
                if colisao_sab and geocinese_nao_coletada:
                    texto_sab1 = ("Sábio Luan: Agora me sinto melhor chefe. Quando tiver as")
                    texto_sab2 = ("quatro cartas, vá para o alojamento à esquerda do refeitório")
                    slots.append(geocinese)
                    geocinese_nao_coletada = False
                    slots.remove(medkit)

            if pedecabra in slots and pa in slots:
                texto_lubu1 = ("Lu Bu: vou amassar ele KKKKKKKKKKKKK")
                texto_lubu2 = ("toma tua carta aqui e mete o pé")
                if colisao_lubu and pirotecnia_nao_coletada:
                    texto_lubu1 = ("Lu Bu: que que tu quer agora teu mlk? rala rala rala")
                    texto_lubu2 = ("peito neguin feioso.")
                    slots.append(pirotecnia)
                    pirotecnia_nao_coletada = False
                    slots.remove(pedecabra)
                    slots.remove(pa)

            if botas in slots and leque in slots:
                texto_lady1 = ("Lady Laura: Agora sim amore! Finalmente linda pra")
                texto_lady2 = ("te dar! A carta né? Pensou o que?")
                if colisao_lady and tormenta_nao_coletada:
                    texto_lady1 = ("Lady Laura: Oi bb! Você vai me levar daqui contigo?")
                    texto_lady2 = ("Vamos nos casar e construir uma família? ")
                    slots.append(tormenta)
                    tormenta_nao_coletada = False
                    slots.remove(botas)
                    slots.remove(leque)

            if apito in slots:
                vel_cao = 0.25

    teclas = pygame.key.get_pressed()

    proxima_posicao_x = posicao_x
    proxima_posicao_y = posicao_y

    if teclas[pygame.K_LEFT]:
        proxima_posicao_x = posicao_x - incremento
        movendo_para_direita = False
    if teclas[pygame.K_RIGHT]:
        proxima_posicao_x = posicao_x + incremento
        movendo_para_direita = True
    if teclas[pygame.K_UP]:
        proxima_posicao_y = posicao_y - incremento
    if teclas[pygame.K_DOWN]:
        proxima_posicao_y = posicao_y + incremento



    retangulo_personagem = pygame.Rect(proxima_posicao_x, proxima_posicao_y, novo_largura, nova_altura)

    # Verificar transição entre fases
    if fase_atual == 1:

        if proxima_posicao_x <= 0:
            fase_atual = 2
            proxima_posicao_x = 700

        elif proxima_posicao_x >= largura - novo_largura:
            fase_atual = 9
            proxima_posicao_x = 50

    if fase_atual == 2:

        if proxima_posicao_x >= largura - novo_largura:
            fase_atual = 1
            proxima_posicao_x = 50

        elif proxima_posicao_y <= 0:
            fase_atual=3
            proxima_posicao_y = 525

        elif proxima_posicao_y >= altura - nova_altura:
            fase_atual = 6
            proxima_posicao_y = 50

        if proxima_posicao_x <= 0 and fechadura:
            fase_atual = 11
            proxima_posicao_x = 700

    if fase_atual == 3:

        if proxima_posicao_y >= altura - nova_altura:
            fase_atual = 2
            proxima_posicao_y = 50

        elif proxima_posicao_x >= largura - novo_largura:
            fase_atual = 4
            proxima_posicao_x = 50

    if fase_atual == 4:

        if proxima_posicao_x <= 0:
            fase_atual = 3
            proxima_posicao_x = 700

        elif proxima_posicao_x >= largura - novo_largura:
            fase_atual = 5
            proxima_posicao_x = 50

    if fase_atual == 5:

        if proxima_posicao_y >= altura - nova_altura:
            fase_atual = 9
            proxima_posicao_y = 50

        if proxima_posicao_x <= 0:
            fase_atual = 4
            proxima_posicao_x = 700

    if fase_atual == 6:

        if proxima_posicao_y <= 0:
            fase_atual=2
            proxima_posicao_y = 525

        elif proxima_posicao_x >= largura - novo_largura:
            fase_atual = 7
            proxima_posicao_x = 50

    if fase_atual == 7:

        if proxima_posicao_x <= 0:
            fase_atual = 6
            proxima_posicao_x = 700

        elif proxima_posicao_x >= largura - novo_largura:
            fase_atual = 8
            proxima_posicao_x = 50

    if fase_atual == 8:

        if proxima_posicao_x <= 0:
            fase_atual = 7
            proxima_posicao_x = 700

    if fase_atual == 9:

        if proxima_posicao_x <= 0:
            fase_atual = 1
            proxima_posicao_x = 700

        elif proxima_posicao_y <= 0:
            fase_atual=5
            proxima_posicao_y = 525

        elif proxima_posicao_x >= largura - novo_largura:
            fase_atual = 10
            proxima_posicao_x = 50

    if fase_atual == 10:

        if proxima_posicao_x <= 0:
            fase_atual = 9
            proxima_posicao_x = 700



    camera.center = retangulo_personagem.center


    retangulo_cao1 = pygame.Rect(cao1_posicaox, cao1_posicaoy, 50, 50)
    retangulo_policial1 = pygame.Rect(policial1_posicaox, policial1_posicaoy, 50, 50)
    if fase_atual==2:
        colisao_policial1 = retangulo_personagem.colliderect(retangulo_policial1)
        colisao_cao1 = retangulo_personagem.colliderect(retangulo_cao1)

        if policial1_posicaox < proxima_posicao_x:
            policial1_posicaox += vel_policial
        elif policial1_posicaox > proxima_posicao_x:
            policial1_posicaox -= vel_policial

        if policial1_posicaoy < proxima_posicao_y:
            policial1_posicaoy += vel_policial
        elif policial1_posicaoy > proxima_posicao_y:
            policial1_posicaoy -= vel_policial

        if cao1_posicaox < proxima_posicao_x:
            cao1_posicaox += vel_cao
        elif cao1_posicaox > proxima_posicao_x:
            cao1_posicaox -= vel_cao

        if cao1_posicaoy < proxima_posicao_y:
            cao1_posicaoy += vel_cao
        elif cao1_posicaoy > proxima_posicao_y:
            cao1_posicaoy -= vel_cao

    retcol2cozinha = pygame.Rect(1, 70, 800, 1)
    retangulo_policial7 = pygame.Rect(policial7_posicaox, policial7_posicaoy, 50, 50)
    retangulo_panela = pygame.Rect(posicao_panela[0], posicao_panela[1], 30, 30)
    if fase_atual == 3:
        retcol1cozinha = pygame.Rect(90, 100, 1, 600)
        col1cozinha = retangulo_personagem.colliderect(retcol1cozinha)
        col2cozinha = retangulo_personagem.colliderect(retcol2cozinha)
        colisao_policial7 = retangulo_personagem.colliderect(retangulo_policial7)
        colisao_panela = retangulo_personagem.colliderect((retangulo_panela))

        if policial7_posicaox < proxima_posicao_x:
            policial7_posicaox += vel_policial
        elif policial7_posicaox > proxima_posicao_x:
            policial7_posicaox -= vel_policial

        if policial7_posicaoy < proxima_posicao_y:
            policial7_posicaoy += vel_policial
        elif policial7_posicaoy > proxima_posicao_y:
            policial7_posicaoy -= vel_policial

    retangulo_cao2 = pygame.Rect(cao2_posicaox, cao2_posicaoy, 50, 50)
    retangulo_policial2 = pygame.Rect(policial2_posicaox, policial2_posicaoy, 50, 50)
    if fase_atual == 4:
        retangulo_apito = pygame.Rect(posicao_apito[0], posicao_apito[1], 20, 20)
        colisao_apito = retangulo_personagem.colliderect((retangulo_apito))
        colisao_policial2 = retangulo_personagem.colliderect(retangulo_policial2)
        colisao_cao2 = retangulo_personagem.colliderect(retangulo_cao2)

        if policial2_posicaox < proxima_posicao_x:
            policial2_posicaox += vel_policial
        elif policial2_posicaox > proxima_posicao_x:
            policial2_posicaox -= vel_policial

        if policial2_posicaoy < proxima_posicao_y:
            policial2_posicaoy += vel_policial
        elif policial2_posicaoy > proxima_posicao_y:
            policial2_posicaoy -= vel_policial

        if cao2_posicaox < proxima_posicao_x:
            cao2_posicaox += vel_cao
        elif cao2_posicaox > proxima_posicao_x:
            cao2_posicaox -= vel_cao

        if cao2_posicaoy < proxima_posicao_y:
            cao2_posicaoy += vel_cao
        elif cao2_posicaoy > proxima_posicao_y:
            cao2_posicaoy -= vel_cao

    retangulo_policial4 = pygame.Rect(policial4_posicaox, policial4_posicaoy, 50, 50)
    retangulo_policial5 = pygame.Rect(policial5_posicaox, policial5_posicaoy, 50, 50)
    retangulo_policial6 = pygame.Rect(policial6_posicaox, policial6_posicaoy, 50, 50)
    if fase_atual == 11:
        colisao_policial4 = retangulo_personagem.colliderect(retangulo_policial4)
        colisao_policial5 = retangulo_personagem.colliderect(retangulo_policial5)
        colisao_policial6 = retangulo_personagem.colliderect(retangulo_policial6)


        if policial4_posicaox < proxima_posicao_x:
            policial4_posicaox += vel_policial
        elif policial4_posicaox > proxima_posicao_x:
            policial4_posicaox -= vel_policial

        if policial4_posicaoy < proxima_posicao_y:
            policial4_posicaoy += vel_policial
        elif policial4_posicaoy > proxima_posicao_y:
            policial4_posicaoy -= vel_policial

        if policial5_posicaox < proxima_posicao_x:
            policial5_posicaox += vel_policial
        elif policial5_posicaox > proxima_posicao_x:
            policial5_posicaox -= vel_policial

        if policial5_posicaoy < proxima_posicao_y:
            policial5_posicaoy += vel_policial
        elif policial5_posicaoy > proxima_posicao_y:
            policial5_posicaoy -= vel_policial

        if policial6_posicaox < proxima_posicao_x:
            policial6_posicaox += vel_policial
        elif policial6_posicaox > proxima_posicao_x:
            policial6_posicaox -= vel_policial

        if policial6_posicaoy < proxima_posicao_y:
            policial6_posicaoy += vel_policial
        elif policial6_posicaoy > proxima_posicao_y:
            policial6_posicaoy -= vel_policial

    retangulo_pa = pygame.Rect(posicao_pa[0], posicao_pa[1], 30, 30)
    retangulo_cao4 = pygame.Rect(cao4_posicaox, cao4_posicaoy, 50, 50)
    retangulo_cao5 = pygame.Rect(cao5_posicaox, cao5_posicaoy, 50, 50)
    retangulo_cao6 = pygame.Rect(cao6_posicaox, cao6_posicaoy, 50, 50)
    if fase_atual == 10:
        retangulo_leque = pygame.Rect(posicao_leque[0], posicao_leque[1], 20, 20)
        colisao_leque = retangulo_personagem.colliderect((retangulo_leque))
        colisao_pa = retangulo_personagem.colliderect((retangulo_pa))
        colisao_cao4 = retangulo_personagem.colliderect(retangulo_cao4)
        colisao_cao5 = retangulo_personagem.colliderect(retangulo_cao5)
        colisao_cao6 = retangulo_personagem.colliderect(retangulo_cao6)
        retcem1 = pygame.Rect(20, 0, 1, 200)
        colcem1 = retangulo_personagem.colliderect(retcem1)
        retcem2 = pygame.Rect(20, 350, 1, 250)
        colcem2 = retangulo_personagem.colliderect(retcem2)

        if cao4_posicaox < proxima_posicao_x:
            cao4_posicaox += vel_cao
        elif cao4_posicaox > proxima_posicao_x:
            cao4_posicaox -= vel_cao

        if cao4_posicaoy < proxima_posicao_y:
            cao4_posicaoy += vel_cao
        elif cao4_posicaoy > proxima_posicao_y:
            cao4_posicaoy -= vel_cao

        if cao5_posicaox < proxima_posicao_x:
            cao5_posicaox += vel_cao
        elif cao5_posicaox > proxima_posicao_x:
            cao5_posicaox -= vel_cao

        if cao5_posicaoy < proxima_posicao_y:
            cao5_posicaoy += vel_cao
        elif cao5_posicaoy > proxima_posicao_y:
            cao5_posicaoy -= vel_cao

        if cao6_posicaox < proxima_posicao_x:
            cao6_posicaox += vel_cao
        elif cao6_posicaox > proxima_posicao_x:
            cao6_posicaox -= vel_cao

        if cao6_posicaoy < proxima_posicao_y:
            cao6_posicaoy += vel_cao
        elif cao6_posicaoy > proxima_posicao_y:
            cao6_posicaoy -= vel_cao

    retangulo_policial8 = pygame.Rect(policial8_posicaox, policial8_posicaoy, 50, 50)
    retangulo_pedecabra = pygame.Rect(posicao_pedecabra[0], posicao_pedecabra[1], 30, 30)
    if fase_atual == 5:
        retest = pygame.Rect(200, 585, 600, 1)
        col_est = retangulo_personagem.colliderect(retest)
        colisao_policial8 = retangulo_personagem.colliderect(retangulo_policial8)
        colisao_pedecabra = retangulo_personagem.colliderect((retangulo_pedecabra))

        if policial8_posicaox < proxima_posicao_x:
            policial8_posicaox += vel_policial
        elif policial8_posicaox > proxima_posicao_x:
            policial8_posicaox -= vel_policial

        if policial8_posicaoy < proxima_posicao_y:
            policial8_posicaoy += vel_policial
        elif policial8_posicaoy > proxima_posicao_y:
            policial8_posicaoy -= vel_policial

    retangulo_policial9 = pygame.Rect(policial9_posicaox, policial9_posicaoy, 50, 50)
    if fase_atual == 6:
        retlixao = pygame.Rect(100, 200, 100, 600)
        col_lixao = retangulo_personagem.colliderect(retlixao)
        colisao_policial9 = retangulo_personagem.colliderect(retangulo_policial9)
        retangulo_medkit = pygame.Rect(posicao_medkit[0], posicao_medkit[1], 20, 20)
        colisao_medkit = retangulo_personagem.colliderect((retangulo_medkit))

        if policial9_posicaox < proxima_posicao_x:
            policial9_posicaox += vel_policial
        elif policial9_posicaox > proxima_posicao_x:
            policial9_posicaox -= vel_policial

        if policial9_posicaoy < proxima_posicao_y:
            policial9_posicaoy += vel_policial
        elif policial9_posicaoy > proxima_posicao_y:
            policial9_posicaoy -= vel_policial

    retangulo_saida = pygame.Rect(posicao_saida[0], posicao_saida[1], 30, 30)
    if fase_atual == 11:
        colisao_saida = retangulo_personagem.colliderect((retangulo_saida))

    retangulo_cao3 = pygame.Rect(cao3_posicaox, cao3_posicaoy, 50, 50)
    if fase_atual == 7:
        retmesa1 = pygame.Rect(130, 310, 75, 200)
        colmesa1 = retangulo_personagem.colliderect(retmesa1)
        retmesa2 = pygame.Rect(506, 310, 75, 200)
        colmesa2 = retangulo_personagem.colliderect(retmesa2)
        retbanheiro = pygame.Rect(105, 170, 330, 5)
        colbanheiro = retangulo_personagem.colliderect(retbanheiro)
        retbanheiro2 = pygame.Rect(435, 0, 5, 150)
        colbanheiro2 = retangulo_personagem.colliderect(retbanheiro2)

        retangulo_botas = pygame.Rect(posicao_apito[0], posicao_botas[1], 30, 30)
        colisao_botas = retangulo_personagem.colliderect((retangulo_botas))
        colisao_cao3 = retangulo_personagem.colliderect(retangulo_cao3)



        if cao3_posicaox < proxima_posicao_x:
            cao3_posicaox += vel_cao
        elif cao3_posicaox > proxima_posicao_x:
            cao3_posicaox -= vel_cao

        if cao3_posicaoy < proxima_posicao_y:
            cao3_posicaoy += vel_cao
        elif cao3_posicaoy > proxima_posicao_y:
            cao3_posicaoy -= vel_cao

    if fase_atual == 9:
        retliv1 = pygame.Rect(200, 100, 500, 100)
        col_liv1 = retangulo_personagem.colliderect(retliv1)
        retliv2 = pygame.Rect(115, 530, 550, 5)
        col_liv2 = retangulo_personagem.colliderect(retliv2)
        retliv3 = pygame.Rect(20, 0, 1, 200)
        col_liv3 = retangulo_personagem.colliderect(retliv3)
        retliv4 = pygame.Rect(20, 350, 1, 250)
        col_liv4 = retangulo_personagem.colliderect(retliv4)

    if colisao_policial2 or colisao_policial1 or colisao_cao1 or colisao_cao2 or colisao_cao3 or colisao_policial4 or colisao_policial5 or colisao_policial6 or colisao_cao4 or colisao_cao5 or colisao_cao6 or colisao_policial7 or colisao_policial8 or colisao_policial9:
        fase_atual = 13

    retangulo_peixe = pygame.Rect(posicao_peixe[0], posicao_peixe[1], 30, 30)
    if fase_atual == 8:
        colisao_peixe = retangulo_personagem.colliderect(retangulo_peixe)


    if fase_atual ==1:

        retcela1 = pygame.Rect(50, 180, 28, 1)
        colcela1 = retangulo_personagem.colliderect(retcela1)

        retcela2 = pygame.Rect(180, 180, 155, 1)
        colcela2 = retangulo_personagem.colliderect(retcela2)

        retcela3 = pygame.Rect(440, 180, 172, 1)
        colcela3 = retangulo_personagem.colliderect(retcela3)

        retcela4 = pygame.Rect(710, 180, 28, 1)
        colcela4 = retangulo_personagem.colliderect(retcela4)

        retcela5 = pygame.Rect(50, 410, 28, 1)
        colcela5 = retangulo_personagem.colliderect(retcela5)

        retcela6 = pygame.Rect(180, 410, 155, 1)
        colcela6 = retangulo_personagem.colliderect(retcela6)

        retcela7 = pygame.Rect(440, 410, 172, 1)
        colcela7 = retangulo_personagem.colliderect(retcela7)

        retcela8 = pygame.Rect(710, 410, 28, 1)
        colcela8 = retangulo_personagem.colliderect(retcela8)

        retcela9 = pygame.Rect(250, 00, 1, 180)
        colcela9 = retangulo_personagem.colliderect(retcela9)

        retcela10 = pygame.Rect(530, 00, 1, 180)
        colcela10 = retangulo_personagem.colliderect(retcela10)

        retcela11 = pygame.Rect(280, 30, 30, 45)
        colcela11 = retangulo_personagem.colliderect(retcela11)






        background = pygame.image.load("fases/prisao.png")
        background = pygame.transform.scale(background, (largura, altura))

        retangulo_blate = pygame.Rect(posicao_blate[0], posicao_blate[1], 50, 50)
        colisao_blate = retangulo_personagem.colliderect(retangulo_blate)
        distancia_entre_personagem_e_blate = abs(posicao_x - posicao_blate[0])

        retangulo_lubu = pygame.Rect(posicao_lubu[0], posicao_lubu[1], 50, 50)
        colisao_lubu = retangulo_personagem.colliderect(retangulo_lubu)
        distancia_entre_personagem_e_lubu = abs(posicao_x - posicao_lubu[0])

        retangulo_lady = pygame.Rect(posicao_lady[0], posicao_lady[1], 50, 50)
        colisao_lady = retangulo_personagem.colliderect(retangulo_lady)
        distancia_entre_personagem_e_lady = abs(posicao_x - posicao_lady[0])

        retangulo_coq = pygame.Rect(posicao_coq[0], posicao_coq[1], 50, 50)
        colisao_coq = retangulo_personagem.colliderect(retangulo_coq)
        distancia_entre_personagem_e_coq = abs(posicao_x - posicao_coq[0])

        retangulo_sab = pygame.Rect(posicao_sab[0], posicao_sab[1], 50, 50)
        colisao_sab = retangulo_personagem.colliderect(retangulo_sab)
        distancia_entre_personagem_e_sab = abs(posicao_x - posicao_sab[0])





    if fase_atual == 2:
        background = pygame.image.load("fases/refeitorio.png")
        background = pygame.transform.scale(background, (largura, altura))


    if fase_atual==3:
        background = pygame.image.load("fases/cozinha.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual==4:
        background = pygame.image.load("fases/quadra.png")
        background = pygame.transform.scale(background, (largura, altura))


    if fase_atual == 5:
        background = pygame.image.load("fases/estacionamento.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 6:
        background = pygame.image.load("fases/lixao.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 7:
        background = pygame.image.load("fases/patio.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 8:
        background = pygame.image.load("fases/lago.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 9:
        background = pygame.image.load("fases/biblioteca.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 10:
        background = pygame.image.load("fases/cemiterio.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 11:
        background = pygame.image.load("fases/alojamento.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual ==12:
        background=pygame.image.load("fases/tela_vitoria.png")
        background=pygame.transform.scale(background, (largura,altura))

    if fase_atual == 13:
        background=pygame.image.load("fases/gameover.png")
        background=pygame.transform.scale(background, (largura, altura))




    # colisoes
    if (
            0 <= proxima_posicao_x < largura - novo_largura
            and 0 <= proxima_posicao_y < altura - nova_altura
            and proxima_posicao_x % tamanho_bloco == 0
            and proxima_posicao_y % tamanho_bloco == 0
            and not colcela1
            and not colcela2
            and not colcela3
            and not colcela4
            and not colcela5
            and not colcela6
            and not colcela7
            and not colcela8
            and not colcela9
            and not colcela10
            and not colcela11
            and not col_lixao
            and not col1cozinha
            and not colbanheiro
            and not colbanheiro2
            and not colmesa1
            and not colmesa2
            and not col_est
            and not colcem1
            and not colcem2
            and not col2cozinha
            and not col_liv1
            and not col_liv2
            and not col_liv3
            and not col_liv4
            and not colisao_medkit
            and not colisao_leque
            and not colisao_peixe
            and not colisao_panela
            and not colisao_pa
            and not colisao_pedecabra
            and not colisao_apito
            and not colisao_botas
            and not colisao_saida
            and not colisao_policial2
            and not colisao_policial1
            and not colisao_policial4
            and not colisao_policial5
            and not colisao_policial6
            and not colisao_policial7
            and not colisao_policial8
            and not colisao_policial9
            and not colisao_cao1
            and not colisao_cao2
            and not colisao_cao3
            and not colisao_cao4
            and not colisao_cao5
            and not colisao_cao6
    ):

        if distancia_entre_personagem_e_blate < 100:  # Define a distância de proximidade
            dialogo_aberto_blate = True
        else:
            dialogo_aberto_blate = False
        if not colisao_blate and not colisao_lubu and not colisao_lady and not colisao_coq and not colisao_sab:
            posicao_x = proxima_posicao_x
            posicao_y = proxima_posicao_y

        if distancia_entre_personagem_e_lubu < 100:  # Define a distância de proximidade
            dialogo_aberto_lubu = True
        else:
            dialogo_aberto_lubu = False
        if not colisao_blate and not colisao_lubu and not colisao_lady and not colisao_coq and not colisao_sab:
            posicao_x = proxima_posicao_x
            posicao_y = proxima_posicao_y

        if distancia_entre_personagem_e_lady < 100:  # Define a distância de proximidade
            dialogo_aberto_lady = True
        else:
            dialogo_aberto_lady = False
        if not colisao_blate and not colisao_lubu and not colisao_lady and not colisao_coq and not colisao_sab:
            posicao_x = proxima_posicao_x
            posicao_y = proxima_posicao_y

        if distancia_entre_personagem_e_coq < 100:  # Define a distância de proximidade
            dialogo_aberto_coq = True
        else:
            dialogo_aberto_coq = False
        if not colisao_blate and not colisao_lubu and not colisao_lady and not colisao_coq and not colisao_sab:
            posicao_x = proxima_posicao_x
            posicao_y = proxima_posicao_y

        if distancia_entre_personagem_e_sab < 100:  # Define a distância de proximidade
            dialogo_aberto_sab = True
        else:
            dialogo_aberto_sab = False
        if not colisao_blate and not colisao_lubu and not colisao_lady and not colisao_coq and not colisao_sab:
            posicao_x = proxima_posicao_x
            posicao_y = proxima_posicao_y





    tela.blit(background, (0, 0))

    render_x = posicao_x - camera.x
    render_y = posicao_y - camera.y

    if movendo_para_direita:
        tela.blit(pygame.transform.flip(littlemor, True, False), (posicao_x, posicao_y))
    else:
        tela.blit(littlemor, (posicao_x, posicao_y))

    if slots_visiveis:
        tela.blit(slot_inventario, posicao_slot1)
        tela.blit(slot_inventario, posicao_slot2)
        tela.blit(slot_inventario, posicao_slot3)
        tela.blit(slot_inventario, posicao_slot4)
        tela.blit(slot_inventario, posicao_slot5)
        tela.blit(slot_inventario, posicao_slot6)
        tela.blit(slot_inventario, posicao_slot7)
        tela.blit(slot_inventario, posicao_slot8)
        tela.blit(slot_inventario, posicao_slot9)
        tela.blit(slot_inventario, posicao_slot10)

        for i, value in enumerate(slots):
            tela.blit(value, posicao_item_slot[i])



    if fase_atual==3:
        tela.blit(policial7, (policial7_posicaox, policial7_posicaoy))
        if panela_visivel:
            tela.blit(panela, posicao_panela)

    elif fase_atual==5:
        tela.blit(policial8, (policial8_posicaox, policial8_posicaoy))
        if pedecabra_visivel:
            tela.blit(pedecabra, posicao_pedecabra)

    elif fase_atual==6:
        tela.blit(policial9, (policial9_posicaox, policial9_posicaoy))
        if medkit_visivel:
            tela.blit(medkit, posicao_medkit)


    elif fase_atual==10:
        if leque_visivel:
            tela.blit(leque, posicao_leque)
        if pa_visivel:
            tela.blit(pa, posicao_pa)
        tela.blit(cao4, (cao4_posicaox, cao4_posicaoy))
        tela.blit(cao5, (cao5_posicaox, cao5_posicaoy))
        tela.blit(cao6, (cao6_posicaox, cao6_posicaoy))

    elif fase_atual==11:
        if saida_visivel:
            tela.blit(saida, posicao_saida)
        tela.blit(policial4, (policial4_posicaox, policial4_posicaoy))
        tela.blit(policial5, (policial5_posicaox, policial5_posicaoy))
        tela.blit(policial6, (policial6_posicaox, policial6_posicaoy))

    elif fase_atual==8:
        if peixe_visivel:
            tela.blit(peixe, posicao_peixe)


    elif fase_atual==7:
        tela.blit(cao3, (cao3_posicaox, cao3_posicaoy))
        if botas_visivel:
            tela.blit(botas, posicao_botas)


    elif fase_atual==2:
        tela.blit(policial1, (policial1_posicaox, policial1_posicaoy))
        tela.blit(cao1, (cao1_posicaox, cao1_posicaoy))



    elif fase_atual==4:
        if apito_visivel:
            tela.blit(apito, posicao_apito)
        tela.blit(policial2, (policial2_posicaox, policial2_posicaoy))
        tela.blit(cao2, (cao2_posicaox, cao2_posicaoy))



    elif fase_atual==1:




        tela.blit(blate_revertido, posicao_blate)
        tela.blit(lubu_revertido, posicao_lubu)
        tela.blit(lady_revertido, posicao_lady)
        tela.blit(coq_revertido, posicao_coq)
        tela.blit(sab_revertido, posicao_sab)

        if colisao_blate and dialogo_aberto_blate:
            tela.blit(caixa_texto, posicao_caixa_texto)
            texto_superficie1 = fonte.render(texto_blate1, True, cor_texto)
            tela.blit(texto_superficie1, (50, altura - 135))
            texto_superficie2 = fonte.render(texto_blate2, True, cor_texto)
            tela.blit(texto_superficie2, (50, altura - 105))

        if colisao_lubu and dialogo_aberto_lubu:
            tela.blit(caixa_texto, posicao_caixa_texto)
            texto_superficie3 = fonte.render(texto_lubu1, True, cor_texto)
            tela.blit(texto_superficie3, (50, altura - 135))
            texto_superficie4 = fonte.render(texto_lubu2, True, cor_texto)
            tela.blit(texto_superficie4, (50, altura - 105))

        if colisao_lady and dialogo_aberto_lady:
            tela.blit(caixa_texto, posicao_caixa_texto)
            texto_superficie5 = fonte.render(texto_lady1, True, cor_texto)
            tela.blit(texto_superficie5, (50, altura - 135))
            texto_superficie6 = fonte.render(texto_lady2, True, cor_texto)
            tela.blit(texto_superficie6, (50, altura - 105))

        if colisao_coq and dialogo_aberto_coq:
            tela.blit(caixa_texto, posicao_caixa_texto)
            texto_superficie7 = fonte.render(texto_coq1, True, cor_texto)
            tela.blit(texto_superficie7, (50, altura - 135))
            texto_superficie8 = fonte.render(texto_coq2, True, cor_texto)
            tela.blit(texto_superficie8, (50, altura - 105))

        if colisao_sab and dialogo_aberto_sab:
            tela.blit(caixa_texto, posicao_caixa_texto)
            texto_superficie9 = fonte.render(texto_sab1, True, cor_texto)
            tela.blit(texto_superficie9, (50, altura - 135))
            texto_superficie10 = fonte.render(texto_sab2, True, cor_texto)
            tela.blit(texto_superficie10, (50, altura - 105))

    if tormenta in slots and pirotecnia in slots and vortex in slots and geocinese in slots:
        texto_sab1 = "Sábio Luan: Meu nobrer, parabéns! Agora o alojamento está"
        texto_sab2 = "desbloqueado! É à esquerda do refeitório, fuja!"

        texto_blate1 = "Blate: Já tá tudo certo! Vá para a esquerda duas vezes e"
        texto_blate2 = "use a chave que te dei para chegar no alojamento"
        if colisao_blate and chave_nao_coletada:
            slots.append(chave)
            chave_nao_coletada = False
            slots.remove(pirotecnia)
            slots.remove(vortex)
            slots.remove(geocinese)
            slots.remove(tormenta)
            fechadura = True

    pygame.display.update()

pygame.quit()
sys.exit()
