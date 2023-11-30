import pygame
from main import*
slot_inventario = pygame.image.load("slot.png")
slot_inventario = pygame.transform.scale(slot_inventario, (100, 100))

posicao_slot1 = (largura // 2 - 250, altura // 2 - 50)
posicao_slot2 = (largura // 2 - 150, altura // 2 - 50)
posicao_slot3 = (largura // 2 - 50, altura // 2 - 50)
posicao_slot4 = (largura // 2 + 50, altura // 2 - 50)
posicao_slot5 = (largura // 2 + 150, altura // 2 - 50)


slots_visiveis = False