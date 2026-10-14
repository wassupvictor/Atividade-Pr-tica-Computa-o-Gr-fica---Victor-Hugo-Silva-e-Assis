# Aula de Texturas: Python e OpenGL
Professor Rodrigo Fernandes dos Santos. Ciência da Computação.
## Ambiente
Python 3.11 a 3.14, PyOpenGL 3.1.10, NumPy 1.26 ou 2.x. Usa Pygame 2.6.1 até Python 3.13 e pygame-ce 2.5.8 no Python 3.14.
A placa e o driver devem oferecer contexto OpenGL 3.2 core e GLSL 150.
A instalação das dependências requer internet uma vez. A aula usa texturas locais e funciona sem downloads depois da instalação.
## Windows (PowerShell)
Abra o terminal na pasta alunos.
```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe exemplo_retangulo.py
.venv\Scripts\python.exe exemplo_retangulo.py --repetir 2
.venv\Scripts\python.exe exemplo_cubo.py
```
## macOS (Terminal)
Abra o terminal na pasta alunos.
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python exemplo_retangulo.py
.venv/bin/python exemplo_retangulo.py --repetir 2
.venv/bin/python exemplo_cubo.py
```
`--repetir 2` aplica repeatUV = [2,2] ao retângulo (slide 19).

ESC fecha a janela. S salva a captura em capturas/resultado.png, relativa à pasta de onde o programa foi iniciado.
## Organização
core: Base, Matrix, Object3D, Scene, Camera, Attribute, Uniform, Texture, Mesh, Renderer.
geometry: Geometry, RectangleGeometry, BoxGeometry.
material: Material, TextureMaterial.
shaders: código GLSL. images: grade_uv.png e mosaico.png.
## Relação com o livro
Arquitetura e nomes das classes seguem Stemkoski e Pascale, capítulos 3 a 5.
Este é um subconjunto didático independente, reimplementado para a aula, e não o repositório oficial completo. Pode ser executado sem substituir o projeto anterior dos alunos.
As classes incluem getWorldMatrix, rotateX/Y/Z, Texture.loadImage/uploadData e vertexUV.
Adaptações: argumentos opcionais evitam dicionários mutáveis compartilhados; setPosition usa indexação compatível com NumPy 2; matrizes usam GL_FALSE e armazenamento por colunas; caminhos derivam de __file__; Base solicita explicitamente OpenGL 3.2 core.
O livro usa texture2D e uniform texture. Em GLSL 150 core a função é texture. O uniform chama-se textureSampler para evitar colisão de nomes. Os slides e arquivos usam essa versão.
TextureMaterial mantém repeatUV, offsetUV e baseColor. O uniform sampler2D guarda [textureRef, 1]. O valor enviado ao shader é 1, o número da unidade, e não textureRef ou GL_TEXTURE1.
Transparência: o código combina blending e descarte de alpha menor que 0.10 como no capítulo. As imagens desta aula são opacas. Transparência parcial exige cuidados adicionais de ordenação e não integra o exercício.
## Problemas comuns
Imagem não encontrada: confira images e o nome do arquivo.
Janela não abre: confira suporte a OpenGL 3.2 core e driver atualizado. Sessões remotas podem oferecer outro contexto.
Imagem invertida: mantenha a inversão vertical na conversão RGBA.
Textura branca/preta: confira sampler, unidade e UV.
Rotação irregular: use velocidade em radianos por segundo multiplicada por deltaTime.
## Referência
STEMKOSKI, Lee; PASCALE, Michael. Developing graphics frameworks with Python and OpenGL. Boca Raton: CRC Press, 2022. DOI: 10.1201/9781003181378. Seções 5.1 a 5.4.
Documentação: https://www.pygame.org/docs/ref/display.html e https://pyopengl.sourceforge.net/documentation/manual-3.0/glUniform.html
As texturas foram criadas para este material e podem ser usadas na atividade.

## Entrega da atividade
- **Disciplina:** Computação Gráfica
- **Atividade:** Cubo com satélite texturizado (Texturas)
- **Integrante:** Victor Hugo Silva e Assis
- **Descrição:** Apliquei `mosaico.png` ao cubo principal e criei um cubo satélite filho, com `grade_uv.png` repetida 2x2, afastado do centro e em escala reduzida. O cubo principal tem rotação controlada pelas setas, e o satélite também gira em torno do próprio eixo X.
- **Resposta da questão:** As coordenadas UV associam os vértices da geometria a posições correspondentes na imagem da textura. Com `repeatUV = [2,2]`, as coordenadas são duplicadas nos eixos U e V, repetindo a textura duas vezes em cada direção (quatro repetições por face).

## Verificação realizada
Os dois exemplos e a solução do professor renderizaram com OpenGL 4.5 core (Mesa) em Linux e Python 3.12.14, e também no macOS com Python 3.13.2 (Pygame 2.6.1, PyOpenGL 3.1.10, NumPy 2.5.2). Shaders compilaram e o ciclo de desenho terminou sem erro OpenGL. A orientação da grade foi conferida nas capturas. O Windows tem instruções e contexto 3.2 core preparado, mas não foi testado diretamente. No macOS, Material cria um VAO temporário antes de compilar os shaders, pois o perfil core exige um VAO vinculado na validação do programa.
