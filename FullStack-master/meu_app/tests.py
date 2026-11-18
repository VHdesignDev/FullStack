from django.test import SimpleTestCase
import random


class SorteioApresentacoesTest(SimpleTestCase):

    def test_sortear_grupos(self):

        # Grupos da Tarefa 5
        grupos = {
            1: [
                "Emilly de Almeida Cruz",
                "Carolina Tissot",
                "Vitor Hugo Fogaça Fagundes",
                "Lucas Both da Rosa"
            ],

            2: [
                "Keenan Yuri Gottschalk Benetti",
                "Gregory Bernardes da Silva",
                "Rodrigo Ruan Farias",
                "João Henrique Kohlrausch Ribeiro"
            ],

            3: [
                "Gabriela Martins Klipel",
                "Laiane Liczinski Alves",
                "Joselaine Corrêa de Oliveira",
                "Tamires Franciéli da Silva Jesus"
            ],

            4: [
                "Flamarion Fagundes Pinto",
                "Gerson Alexandre Maus",
                "Matheus Griza Estrazulas",
                "Crystopher Kochler Corbari"
            ],

            5: [
                "Gustavo Alex de Souza",
                "Gabriela Rodrigues",
                "Nereu Aquiles Rebechi Júnior",
                "Murilo Rheinheimer"
            ],

            6: [
                "Arthur Henrique Pinheiro",
                "João Augusto dos Reis Both",
                "João Matheus Gewehr",
                "Cássio Felipe Cambruzzi"
            ],

            7: [
                "Felipe da Rocha",
                "Gabriel Vinicius da Silva",
                "Juliano Rehling de Lima",
                "Renan Gustavo Chaves",
                "Leonardo Kotcheski Filipiaki"
            ],

            8: [
                "Gabriel Eberhardt Fleck",
                "Lucas Pacheco dos Santos",
                "Patrick Bueno Ayres",
                "Vitor de Souza Pinto",
                "Bruno Henrique Kessler"
            ]
        }

        # Sorteia a ordem dos grupos
        numeros = list(grupos.keys())
        random.shuffle(numeros)

        # Divide em dois dias
        dia1 = numeros[:4]
        dia2 = numeros[4:]

        print("\n" + "=" * 55)
        print("       SORTEIO DAS APRESENTAÇÕES - TAREFA 5")
        print("=" * 55)

        for dia, sorteados in [
            ("DIA 1", dia1),
            ("DIA 2", dia2)
        ]:

            print(f"\n{'=' * 18} {dia} {'=' * 18}")

            for ordem, numero_grupo in enumerate(sorteados, start=1):

                print(f"\n{ordem}ª APRESENTAÇÃO - GRUPO {numero_grupo}")

                for aluno in grupos[numero_grupo]:
                    print(f"   - {aluno}")

        # Verificações automáticas
        self.assertEqual(len(dia1), 4)
        self.assertEqual(len(dia2), 4)

        # Confere se nenhum grupo foi repetido
        self.assertEqual(len(set(dia1 + dia2)), 8)

        # Confere se todos os grupos participaram
        self.assertEqual(
            set(dia1 + dia2),
            set(grupos.keys())
        )

        print("\n" + "=" * 55)
        print("          SORTEIO REALIZADO COM SUCESSO!")
        print("=" * 55)
        print("Dia 1: 4 grupos")
        print("Dia 2: 4 grupos")
        print("Nenhum grupo repetido!")
        print("=" * 55 + "\n")
