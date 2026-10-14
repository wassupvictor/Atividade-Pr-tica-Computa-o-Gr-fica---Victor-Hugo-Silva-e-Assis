# Aula de Grafo de Cena: Python e OpenGL
Prof. Rodrigo Fernandes dos Santos. Computação Gráfica, Unipac Barbacena.

## Ambiente
Python 3.11 a 3.14, PyOpenGL 3.1.10 e NumPy 1.26 ou 2.x. Usa Pygame 2.6.1 até Python 3.13 e pygame-ce 2.5.8 no Python 3.14.
A placa de vídeo precisa oferecer OpenGL 3.2 core.

## Windows (PowerShell)
Abra o terminal na pasta `alunos`.
```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe demo1_cena.py
.venv\Scripts\python.exe demo2_hierarquia.py
.venv\Scripts\python.exe demo3_camera.py
```

## macOS (Terminal)
Abra o terminal na pasta `alunos`.
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python demo1_cena.py
.venv/bin/python demo2_hierarquia.py
.venv/bin/python demo3_camera.py
```

No PyCharm, abra a pasta `alunos` como projeto e execute cada arquivo com **Run**.

ESC fecha a janela. P salva a captura em `capturas/resultado.png`.

## Demonstrações
| Arquivo | O que mostra | Teclas |
|---|---|---|
| `demo1_cena.py` | A receita: Renderer, Scene, Camera e Mesh (Geometry + Material) | — |
| `demo2_hierarquia.py` | Sistema solar com pivôs (`Object3D` vazio) | ESPAÇO pausa |
| `demo3_camera.py` | A câmera como Object3D, presa a um "rig" | WASD, QE, RF, setas |

## Organização
- `core/`: `Base`, `Matrix`, `Attribute`, `Uniform`, `Object3D`, `Scene`, `Camera`, `Mesh` e `Renderer`.
- `geometry/`: `Geometry` e `BoxGeometry` (posições e uma cor por face).
- `material/`: `Material` e `BasicMaterial` (shaders com `baseColor` e cores por vértice).
- `formas.py`: `caixa(largura, altura, profundidade, cor)` cria uma Mesh em forma de caixa.
- `atividade_braco.py`: arquivo inicial da atividade (veja `ATIVIDADE.md`).

## Convenções
- `getWorldMatrix() = pai.getWorldMatrix() @ transform`.
- `translate`, `rotateX/Y/Z` e `scale` são **locais** por padrão (`localCoord=True`, multiplica à direita).
- `setPosition` troca só a translação da matriz local, sem mexer na rotação.
- Velocidades em unidades ou radianos **por segundo**, multiplicadas por `self.deltaTime`.
- `self.isKeyPressed('w')` é contínuo; `self.isKeyDown('space')` vale só no quadro em que a tecla foi apertada.

## Problemas comuns
- O objeto não aparece: ele não foi adicionado à cena (nem a um pai que está na cena).
- Gira em torno do centro em vez da ponta: falta um pivô (`Object3D`) na articulação.
- Filho gira junto com o "irmão": confira qual objeto é o pai em `add`.
- `ModuleNotFoundError: core`: execute a partir da pasta `alunos`.

## Referência
STEMKOSKI, Lee; PASCALE, Michael. *Developing graphics frameworks with Python and OpenGL*. Boca Raton: CRC Press, 2022. Capítulo 4 (A Scene Graph Framework).

## Entrega da atividade
- **Disciplina:** Computação Gráfica
- **Atividade:** Braço robótico (Grafo de cena)
- **Integrante:** Victor Hugo Silva e Assis
- **Descrição:** Montei o braço como uma hierarquia de objetos: a base contém o pivô do ombro, que controla o braço e o pivô do cotovelo; o cotovelo controla o antebraço e a garra. As teclas A/D, W/S e I/K controlam a base, o ombro e o cotovelo.
- **Resposta da questão:** Os pivôs `Object3D` definem os centros das articulações. As caixas são centradas na origem local e, sozinhas, girariam em torno do próprio centro; ligando-as aos pivôs como filhos e posicionando-as em relação a eles, cada segmento gira pela ponta e leva consigo os objetos descendentes.
