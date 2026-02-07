# Apuntes 1

En este primer capítulo que se busca es tener el entorno adecuado para empezar a practicar.
En inicio, necesitaremos lo siguiente:

- Un hipervisor alojado: En mi caso, me decanté por Virtualbox ya que lo he usado anteriormente.
- Una imagen de Kali Linux: Es el OS que vamos a usar en gran parte del libro por lo que descargué una imagen de su página web.

Ahora, ¿qué es un hipervisor? en términos simples es una capa de software que permite separar lo que es el hardware del software, permitiendo crear máquinas virtuales. En nuestro caso se le llama "hipervisor alojado" ya que necesita de otro OS y un programa para poder operar. Los hay "bare metal" pero eso es otro tema en el cual no vamos ahondar porque va más allá del objetivo del capítulo.

Para instalar VirtualBox me fui a la página de Oracle, [https://www.virtualbox.org/](https://www.virtualbox.org/), y descargué la última versión de host de Windows ya que es el OS que tengo en la laptop.

Por otro lado, me fui a la web de Kali Linux y descargué la imagen más reciente de su OS desde la siguiente página [https://www.kali.org/get-kali/#kali-virtual-machines](https://www.kali.org/get-kali/#kali-virtual-machines).

Una vez, teniendo todo puesto a punto, o al menos "casi", seguí las indicaciones del libro para alcanzar los siguientes objetivos:

1. Actualizar la versión de Python que trae por defecto Kali Linux.
2. Instalar la librería encargada de permitirnos crear entornos virtuales, venv, y crear un entorno virtual. 
3. Entender que es la "higiene del código" en Python.
