# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        # REGRA 1 - Se você ou seu oponente tiver duas marcações em sequência, marque o quadrado restante.

        for il in range(0, 3):
            if self.matriz[il][0] == self.matriz[il][1] and self.matriz[il][0] == Tabuleiro.JOGADOR_0 and self.matriz[il][2] == Tabuleiro.DESCONHECIDO:
                return (il, 2)
            
            if self.matriz[il][1] == self.matriz[il][2] and self.matriz[il][1] == Tabuleiro.JOGADOR_0 and self.matriz[il][0] == Tabuleiro.DESCONHECIDO:
                return (il, 0)
            
            if self.matriz[il][0] == self.matriz[il][2] and self.matriz[il][0] == Tabuleiro.JOGADOR_0 and self.matriz[il][1] == Tabuleiro.DESCONHECIDO:
                return (il, 1)

            if self.matriz[il][0] == self.matriz[il][1] and self.matriz[il][0] == Tabuleiro.JOGADOR_X and self.matriz[il][2] == Tabuleiro.DESCONHECIDO:
                return (il, 2)
            
            if self.matriz[il][1] == self.matriz[il][2] and self.matriz[il][1] == Tabuleiro.JOGADOR_X and self.matriz[il][0] == Tabuleiro.DESCONHECIDO:
                return (il, 0)

            if self.matriz[il][0] == self.matriz[il][2] and self.matriz[il][0] == Tabuleiro.JOGADOR_X and self.matriz[il][1] == Tabuleiro.DESCONHECIDO:
                return (il, 1)
                
        for ic in range(0, 3):

            if self.matriz[0][ic] == self.matriz[1][ic] and self.matriz[0][ic] == Tabuleiro.JOGADOR_0 and self.matriz[2][ic] == Tabuleiro.DESCONHECIDO:
                return (2, ic)

            if self.matriz[1][ic] == self.matriz[2][ic] and self.matriz[1][ic] == Tabuleiro.JOGADOR_0 and self.matriz[0][ic] == Tabuleiro.DESCONHECIDO:
                return (0, ic)

            if self.matriz[0][ic] == self.matriz[2][ic] and self.matriz[0][ic] == Tabuleiro.JOGADOR_0 and self.matriz[1][ic] == Tabuleiro.DESCONHECIDO:
                return (1, ic)


            if self.matriz[0][ic] == self.matriz[1][ic] and self.matriz[0][ic] == Tabuleiro.JOGADOR_X and self.matriz[2][ic] == Tabuleiro.DESCONHECIDO:
                return (il, 2)

            if self.matriz[1][ic] == self.matriz[2][ic] and self.matriz[1][ic] == Tabuleiro.JOGADOR_X and self.matriz[0][ic] == Tabuleiro.DESCONHECIDO:
                return (0, ic)

            if self.matriz[0][ic] == self.matriz[2][ic] and self.matriz[0][ic] == Tabuleiro.JOGADOR_X and self.matriz[1][ic] == Tabuleiro.DESCONHECIDO:
                return (1, ic)
            
            
        if self.matriz[0][0] == self.matriz[1][1] and self.matriz[0][0] == Tabuleiro.JOGADOR_0 and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)

        if self.matriz[1][1] == self.matriz[2][2] and self.matriz[1][1] == Tabuleiro.JOGADOR_0 and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)

        if self.matriz[0][0] == self.matriz[2][2] and self.matriz[0][0] == Tabuleiro.JOGADOR_0 and self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        if self.matriz[0][0] == self.matriz[1][1] and self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)

        if self.matriz[1][1] == self.matriz[2][2] and self.matriz[1][1] == Tabuleiro.JOGADOR_X and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)

        if self.matriz[0][0] == self.matriz[2][2] and self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # REGRA 2 - Se houver uma jogada que crie duas sequências de duas marcações, use-a

        for il in range(0, 3):

            if self.matriz[il][0] == Tabuleiro.JOGADOR_0 and self.matriz[il][1] == Tabuleiro.DESCONHECIDO:
                return (il, 1)

            if self.matriz[il][2] == Tabuleiro.JOGADOR_0 and self.matriz[il][1] == Tabuleiro.DESCONHECIDO:
                return (il, 1)

            if self.matriz[il][1] == Tabuleiro.JOGADOR_0 and self.matriz[il][0] == Tabuleiro.DESCONHECIDO and self.matriz[il][2] == Tabuleiro.DESCONHECIDO:
                return (il, 0)

        for ic in range(0, 3):

            if self.matriz[0][ic] == Tabuleiro.JOGADOR_0 and self.matriz[1][ic] == Tabuleiro.DESCONHECIDO:
                return (1, ic)

            if self.matriz[2][ic] == Tabuleiro.JOGADOR_0 and self.matriz[1][ic] == Tabuleiro.DESCONHECIDO:
                return (1, ic)

            if self.matriz[1][ic] == Tabuleiro.JOGADOR_0 and self.matriz[0][ic] == Tabuleiro.DESCONHECIDO and self.matriz[2][ic] == Tabuleiro.DESCONHECIDO:
                return (0, ic)
                    

        if self.matriz[1][1] == Tabuleiro.JOGADOR_0 and self.matriz[0][0] == Tabuleiro.DESCONHECIDO and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        
        if self.matriz[1][1] == Tabuleiro.JOGADOR_0 and self.matriz[2][0] == Tabuleiro.DESCONHECIDO and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        
        # REGRA 3 - Se o quadrado central estiver livre, marque-o.

        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO and len(lista) > 9:
            return (1, 1)

        # REGRA 4 - Se seu oponente tiver marcado um dos cantos, marque o canto oposto.

        if self.matriz[0][0] == Tabuleiro.JOGADOR_X:
            return (2, 2)
        
        if self.matriz[0][2] == Tabuleiro.JOGADOR_X:
            return (2, 0)
        
        if self.matriz[2][0] == Tabuleiro.JOGADOR_X:
            return (0, 2)
        
        if self.matriz[2][2] == Tabuleiro.JOGADOR_X:
            return (0, 0)

        # REGRA 5 - Se houver um canto vazio, marque-o (Mesma coisa da regra 6)
        # REGRA 6 - Marque arbitrariamente um quadrado vazio.

        if lista:
            p = randint(0, len(lista)-1)
            return lista[p]

        return None