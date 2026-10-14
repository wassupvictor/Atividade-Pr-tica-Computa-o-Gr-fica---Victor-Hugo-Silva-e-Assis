# ATIVIDADE: mini sistema solar com composição de matrizes.
# Leia ATIVIDADE.md. Altere apenas os trechos marcados com TODO.
# ESC fecha. P salva capturas/resultado.png para a entrega.
import argparse

from OpenGL.GL import *

from core.base import Base
from core.utils import Utils
from core.uniform import Uniform
from core.matrix import Matrix
from formas import quadrado
from objeto import Objeto
from shaders import VERTEX_SHADER, FRAGMENT_SHADER

RAIO_ORBITA_PLANETA = 0.6
RAIO_ORBITA_LUA = 0.2


class SistemaSolar(Base):

    def initialize(self):
        self.programRef = Utils.initialize_program(VERTEX_SHADER, FRAGMENT_SHADER)
        glClearColor(0.04, 0.05, 0.10, 1.0)

        # quadrados de lado 2, centrados na origem (coordenadas locais)
        self.sol = Objeto(self.programRef, *quadrado([1.0, 0.75, 0.1], [1.0, 0.5, 0.0]))
        self.planeta = Objeto(self.programRef, *quadrado([0.2, 0.5, 1.0], [0.1, 0.3, 0.7]))
        self.lua = Objeto(self.programRef, *quadrado([0.85, 0.85, 0.85], [0.5, 0.5, 0.5]))

        self.modelMatrix = Uniform("mat4", Matrix.make_identity())
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")
        self.projectionMatrix = Uniform("mat4", Matrix.make_orthographic())
        self.projectionMatrix.locateVariable(self.programRef, "projectionMatrix")

        # velocidades em radianos por segundo
        self.velocidadeSol = 0.3
        self.velocidadeOrbita = 0.8
        self.velocidadeRotacaoPlaneta = 3.0
        self.velocidadeOrbitaLua = 2.5

        # ângulos acumulados: somar velocidade * deltaTime evita "saltos"
        # quando a velocidade muda durante a execução
        self.anguloSol = 0.0
        self.anguloOrbita = 0.0
        self.anguloRotacaoPlaneta = 0.0
        self.anguloOrbitaLua = 0.0

    def update(self):
        # TODO 5: setas para cima/baixo ("up"/"down") alteram self.velocidadeOrbita
        #         (use isKeyPressed e não deixe a velocidade ficar negativa)
        ajusteVelocidade = self.deltaTime
        if self.input.isKeyPressed("up"):
            self.velocidadeOrbita += ajusteVelocidade
        if self.input.isKeyPressed("down"):
            self.velocidadeOrbita = max(0.0, self.velocidadeOrbita - ajusteVelocidade)

        self.anguloSol += self.velocidadeSol * self.deltaTime
        self.anguloOrbita += self.velocidadeOrbita * self.deltaTime
        self.anguloRotacaoPlaneta += self.velocidadeRotacaoPlaneta * self.deltaTime
        self.anguloOrbitaLua += self.velocidadeOrbitaLua * self.deltaTime

        # TODO 1: o sol deve girar em torno do próprio centro (use self.anguloSol)
        matrizSol = Matrix.make_rotation_z(self.anguloSol) @ Matrix.make_scale(0.25)

        # TODO 2: o planeta deve ORBITAR o sol (use self.anguloOrbita)
        # TODO 3: o planeta deve GIRAR em torno do próprio eixo (use self.anguloRotacaoPlaneta)
        matrizOrbitaPlaneta = (
            Matrix.make_rotation_z(self.anguloOrbita)
            @ Matrix.make_translation(RAIO_ORBITA_PLANETA, 0, 0)
        )
        matrizPlaneta = (
            matrizOrbitaPlaneta
            @ Matrix.make_rotation_z(self.anguloRotacaoPlaneta)
            @ Matrix.make_scale(0.1)
        )

        # TODO 4: a lua deve orbitar o PLANETA, acompanhando-o (use self.anguloOrbitaLua)
        matrizLua = (
            matrizOrbitaPlaneta
            @ Matrix.make_rotation_z(self.anguloOrbitaLua)
            @ Matrix.make_translation(RAIO_ORBITA_LUA, 0, 0)
            @ Matrix.make_scale(0.05)
        )

        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.projectionMatrix.uploadData()
        for objeto, matriz in [(self.sol, matrizSol),
                               (self.planeta, matrizPlaneta),
                               (self.lua, matrizLua)]:
            self.modelMatrix.data = matriz
            self.modelMatrix.uploadData()
            objeto.desenhar()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frames", type=int)
    parser.add_argument("--screenshot")
    args = parser.parse_args()
    SistemaSolar(title="Atividade: sistema solar").run(args.frames, args.screenshot)
