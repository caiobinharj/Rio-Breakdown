import pygame
import sys

#rodar
pygame.init()

#informações principais
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Rio Breakdown")


#fases: prisao (1), refeitorio (2), cozinha (3), quadra (4), estacionamento (5), lixão (6), pátio (7) e lago (8)
fase_atual = 1

#itens
pedecabra_visivel = True
pedecabra = pygame.image.load("items/pedecabra.png")
pedecabra = pygame.transform.scale(pedecabra, (50, 50))
posicao_pedecabra = (750, 350)

botas_visivel = True
botas = pygame.image.load("items/botasmagicas.png")
botas = pygame.transform.scale(botas, (50, 50))
posicao_botas = (150, 200)

panela_visivel = True
panela = pygame.image.load("items/panela.png")
panela = pygame.transform.scale(panela, (50, 50))
posicao_panela = (110, 80)

peixe_visivel = True
peixe = pygame.image.load("items/peixao.png")
peixe = pygame.transform.scale(peixe, (50, 50))
posicao_peixe = (700, 500)

apito_visivel = True
apito = pygame.image.load("items/apito.png")
apito = pygame.transform.scale(apito, (50, 50))
posicao_apito = (365, 105)

pirotecnia_visivel = True
pirotecnia = pygame.image.load("items/pirotecnia.png")
pirotecnia = pygame.transform.scale(pirotecnia, (24, 30))
posicao_pirotecnia = (25, 500)

geocinese_visivel = True
geocinese = pygame.image.load("items/geocinese.png")
geocinese = pygame.transform.scale(geocinese, (24, 30))
posicao_geocinese = (300, 100)

tormenta_visivel = True
tormenta = pygame.image.load("items/tormenta.png")
tormenta = pygame.transform.scale(tormenta, (24, 30))
posicao_tormenta = (588, 555)

vortex_visivel = True
vortex = pygame.image.load("items/vortex.png")
vortex = pygame.transform.scale(vortex, (24, 30))
posicao_vortex = (522, 60)


#littlemor
imagem = pygame.image.load("littlemor.png")
novo_largura = imagem.get_width() * 2
nova_altura = imagem.get_height() * 2
littlemor = pygame.transform.scale(imagem, (novo_largura, nova_altura))

#movimento
tamanho_bloco = 12.5
posicao_x, posicao_y = 400, 50
velocidade = 2
incremento = tamanho_bloco
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

#Blate
blate = pygame.image.load("blate.png")
blate = pygame.transform.scale(blate, (novo_largura, nova_altura))
blate_revertido = pygame.transform.flip(blate, False, False)
posicao_blate = (80, 30)
dialogo_aberto_blate = False
texto_blate1 = ("Coe irmao, to exausto. Tá na hora da Lili cantar. ")
texto_blate2 = ("Tu vem também né?.")

#Lu Bu
lubu = pygame.image.load("lubu.png")
lubu = pygame.transform.scale(lubu, (novo_largura, nova_altura))
lubu_revertido = pygame.transform.flip(lubu, True, False)
posicao_lubu = (400, 450)
dialogo_aberto_lubu = False
texto_lubu1 = ("Já te passei a visão, se adianta enquanto pode")
texto_lubu2 = ("Bagulho vai ficar de verdade.")

#Lady laura
lady = pygame.image.load("ladylaura.png")
lady = pygame.transform.scale(lady, (novo_largura, nova_altura))
lady_revertido = pygame.transform.flip(lady, True, False)
posicao_lady = (675, 40)
dialogo_aberto_lady = False
texto_lady1 = ("Oie gatinho! O que te traz dessa vez?")
texto_lady2 = ("Já tá querendo mais uma?")

#Coquinha
coq = pygame.image.load("coquinha.png")
coq = pygame.transform.scale(coq, (novo_largura, nova_altura))
coq_revertido = pygame.transform.flip(coq, False, False)
posicao_coq = (80, 475)
dialogo_aberto_coq = False
texto_coq1 = ("Sei que você tá querendo fugir. Leve-me para")
texto_coq2 = ("para longe do Lu Bu, ele não larga do meu pé!")

#Sábio
sab = pygame.image.load("sabio.png")
sab = pygame.transform.scale(sab, (novo_largura, nova_altura))
sab_revertido = pygame.transform.flip(sab, True, False)
posicao_sab = (650, 475)
dialogo_aberto_sab = False
texto_sab1 = ("Brother, bizu: busca umas carta por aí ta ligado,")
texto_sab2 = ("tu consegue mlk bom.")

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

            if evento.key == pygame.K_SPACE and fase_atual==5:
                pedecabra_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==6:
                botas_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==3:
                panela_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==8:
                peixe_visivel = False
                vortex_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==7:
                apito_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==2:
                pirotecnia_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==1:
                geocinese_visivel = False
            if evento.key == pygame.K_SPACE and fase_atual==4:
                tormenta_visivel = False


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
    if fase_atual == 1 and proxima_posicao_x <= 0:
        print("Transição para Fase 2!")
        fase_atual = 2
        proxima_posicao_x = 700

    if fase_atual == 2:

        if proxima_posicao_x >= largura - novo_largura:
            print("Transição para Fase 1!")
            fase_atual = 1
            proxima_posicao_x = 50

        elif proxima_posicao_y <= 0:
            fase_atual=3
            proxima_posicao_y = 525

        elif proxima_posicao_y >= altura - nova_altura:
            fase_atual = 6
            proxima_posicao_y = 50


    if fase_atual == 3:

        if proxima_posicao_y >= altura - nova_altura:
            print("Transição para Fase 3 (extremo inferior)!")
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


    camera.center = retangulo_personagem.center

    if fase_atual ==1:
        background = pygame.image.load("prisao.png")
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


    # colisoes
    if (
            0 <= proxima_posicao_x < largura - novo_largura
            and 0 <= proxima_posicao_y < altura - nova_altura
            and proxima_posicao_x % tamanho_bloco == 0
            and proxima_posicao_y % tamanho_bloco == 0
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


    if fase_atual == 2:
        background = pygame.image.load("refeitorio.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual==3:
        background = pygame.image.load("cozinha.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual==4:
        background = pygame.image.load("quadra.png")
        background = pygame.transform.scale(background, (largura, altura))


    if fase_atual == 5:
        background = pygame.image.load("estacionamento.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 6:
        background = pygame.image.load("quadra.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 7:
        background = pygame.image.load("patio.png")
        background = pygame.transform.scale(background, (largura, altura))

    if fase_atual == 8:
        background = pygame.image.load("lago.png")
        background = pygame.transform.scale(background, (largura, altura))



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

    if fase_atual==3:
        if panela_visivel:
            tela.blit(panela, posicao_panela)
    elif fase_atual==5:
        if pedecabra_visivel:
            tela.blit(pedecabra, posicao_pedecabra)
    elif fase_atual==6:
        if botas_visivel:
            tela.blit(botas, posicao_botas)
    elif fase_atual==8:
        if peixe_visivel:
            tela.blit(peixe, posicao_peixe)
        if vortex_visivel:
            tela.blit(vortex, posicao_vortex)

    elif fase_atual==7:
        if apito_visivel:
            tela.blit(apito, posicao_apito)
    elif fase_atual==2:
        if pirotecnia_visivel:
            tela.blit(pirotecnia, posicao_pirotecnia)
    elif fase_atual==4:
        if tormenta_visivel:
            tela.blit(tormenta, posicao_tormenta)



    elif fase_atual==1:

        if geocinese_visivel:
            tela.blit(geocinese, posicao_geocinese)


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


    pygame.display.update()

pygame.quit()
sys.exit()
