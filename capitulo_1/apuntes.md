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

## Instalación de Kali

En este apartado, lo cierto es que tomé las mismas indicaciones del libro salvo por el link recomendado para ver las máquinas disponibles desde la página de Windows, a mí. Por lo que para completar este paso lo que hice fue visitar el link de VirtualBox que dejé más arriba e hice la instalación tal cual indica el wizard.

Luego de instalado el hipervisor, lo que hice fue descargar el archivo formato vbox referente a Kali Linux para luego montarlo en el VirtualBox. Para ello, se abre el programa y le das al símbolo "+" que está en verde. Se abrirá un modal que te invitará a buscar el archivo .vbox dentro de tus carpetas; yo la había descargado en 'descargas' por lo que la monté desde allí.

Fuera del ámbito de este curso está la explicación de la distribución de carpetas de Linux, simplemente usaremos la abstracción para hacer uso de la herramienta. Prometo en otro repo hacer centro en este tema porque es realmente importante.

## Actualización de Python

En este apartado, lo que se busca es actualizar la versión de Python que trae por defecto Kali Linux. Para ello, lo que hice fue abrir la terminal y escribir el siguiente comando:

```
- sudo apt update
- apt list --upgradable
- sudo apt upgrade
- sudo apt dist-upgrade
- sudo apt autoremove
```

Iremos con un poco más de detalle sobre cada comando:

- `sudo apt update`: Este comando se encarga de actualizar la lista de paquetes disponibles en los repositorios configurados en el sistema. Es importante ejecutarlo antes de intentar instalar o actualizar cualquier paquete, ya que garantiza que el sistema tenga la información más reciente sobre las versiones disponibles.

El símil que encontré para entender este comando es el de un supermercado. Imagina que quieres comprar algo en un supermercado, pero antes de ir, quieres saber qué productos tienen disponibles y a qué precio. Para eso, revisas el catálogo del supermercado, que es como la lista de paquetes en los repositorios. El comando `sudo apt update` es como revisar ese catálogo para asegurarte de que tienes la información más actualizada sobre los productos disponibles antes de hacer tu compra.

- `apt list --upgradable`: Este comando muestra una lista de los paquetes que tienen actualizaciones disponibles. Es útil para verificar qué paquetes pueden ser actualizados antes de proceder con la actualización.

Ahora, para comprender este comando, volvamos al símil del supermercado. Después de revisar el catálogo (con `sudo apt update`), quieres saber qué productos que ya tienes en tu carrito de compras tienen una versión más nueva disponible. El comando `apt list --upgradable` es como revisar tu carrito para ver qué productos pueden ser reemplazados por versiones más recientes antes de finalizar tu compra.

- `sudo apt upgrade`: Este comando actualiza todos los paquetes instalados en el sistema a sus versiones más recientes disponibles en los repositorios. Sin embargo, no instala ni elimina ningún paquete, por lo que si una actualización requiere la instalación de un nuevo paquete o la eliminación de uno existente, este comando no lo hará. Siguiendo con la referencia del supermercado, `sudo apt upgrade` es como ir al supermercado con tu carrito de compras y actualizar los productos que ya tienes, pero sin agregar nuevos productos ni eliminar los que ya están en tu carrito. Si un producto que quieres actualizar requiere un nuevo producto para funcionar, este comando no lo instalará automáticamente.

- `sudo apt dist-upgrade`: Este comando es similar a `sudo apt upgrade`, pero también maneja las dependencias de los paquetes. Si una actualización requiere la instalación de un nuevo paquete o la eliminación de uno existente, `dist-upgrade` lo hará automáticamente. Es útil para asegurarse de que todas las actualizaciones se apliquen correctamente, incluso si requieren cambios en las dependencias. Una vez más, recurrimos a nuestro ejemplo del supermercado: `sudo apt dist-upgrade` es como ir al supermercado con tu carrito de compras y actualizar los productos que ya tienes, pero también estar dispuesto a agregar nuevos productos o eliminar algunos de tu carrito si es necesario para completar la actualización. Si un producto que quieres actualizar requiere un nuevo producto para funcionar, este comando lo instalará automáticamente, y si un producto ya no es necesario, lo eliminará de tu carrito.

- `sudo apt autoremove`: Este comando se utiliza para eliminar paquetes que fueron instalados como dependencias de otros paquetes y que ya no son necesarios. Después de actualizar o eliminar paquetes, es posible que queden dependencias huérfanas que ocupan espacio en el sistema. `autoremove` ayuda a limpiar esos paquetes innecesarios.

Otra vez, nuestro símil superestrella del super: `sudo apt autoremove` es como revisar tu carrito de compras después de hacer tus actualizaciones y eliminar cualquier producto que ya no necesitas o que fue agregado como parte de una actualización pero que ahora es innecesario. Es una forma de mantener tu carrito (y tu sistema) limpio y organizado, eliminando cualquier producto (paquete) que ya no es necesario.

_nota:_ La palabra `sudo` al inicio del comando indica que se requiere privilegios de superusuario para ejecutarlo, lo que es necesario para realizar cambios en el sistema. Al ejecutar este comando, el sistema se conectará a los repositorios y descargará la información sobre los paquetes disponibles, incluyendo sus versiones y dependencias. Esto es fundamental para asegurarse de que las actualizaciones se realicen correctamente y que se instalen las versiones más recientes de los paquetes.

### ¿Cómo saber qué versión de Python tengo instalada?

Para saber qué versión de Python tienes instalada, puedes usar el siguiente comando en la terminal:

```
python --version
```

De esta manera, el sistema te mostrará la versión de Python que está actualmente instalada en tu sistema. Es importante tener una versión actualizada de Python para asegurarte de que puedes aprovechar las últimas características y mejoras de seguridad que se han implementado en el lenguaje.

## Instalación de venv y creación de un entorno virtual

En este apartado, lo que se busca es instalar la librería encargada de permitirnos crear entornos virtuales, venv, y crear un entorno virtual. Para ello, lo que hice fue abrir la terminal y escribir el siguiente comando:

```
sudo apt install python3-venv
```

Este comando instala el paquete `python3-venv`, que es necesario para crear entornos virtuales en Python.

### ¿Qué es un entorno virtual?

Un entorno virtual es una herramienta que permite crear un espacio aislado para tus proyectos de Python, lo que significa que puedes tener diferentes versiones de paquetes y dependencias para cada proyecto sin que interfieran entre sí.

Esto es especialmente útil cuando trabajas en múltiples proyectos que pueden requerir diferentes versiones de las mismas bibliotecas. Al usar un entorno virtual, puedes asegurarte de que cada proyecto tenga su propio conjunto de dependencias, lo que facilita la gestión y evita conflictos entre paquetes.

### ¿Cómo crear un entorno virtual?

Hay varias maneras de crear el entorno virtual dependiendo del sistema operativo en el que te encuentres trabajando. En sistemas basados en Unix (como Linux y macOS), el comando que mencioné anteriormente es el adecuado. Sin embargo, en Windows, el comando para crear un entorno virtual es ligeramente diferente:

```
python -m venv nombre_del_entorno
```

En este comando, `nombre_del_entorno` es el nombre que deseas darle a tu entorno virtual. Al ejecutar este comando, se creará una carpeta con ese nombre que contendrá todos los archivos necesarios para el entorno virtual.

En Windows, después de crear el entorno virtual, debes activarlo usando el siguiente comando:

```
.\nombre_del_entorno\Scripts\activate
```

En la terminal verás que se muestra el nombre del entorno virtual entre paréntesis, lo que indica que el entorno virtual está activo. A partir de este momento, cualquier paquete que instales usando `pip` se instalará dentro de este entorno virtual, sin afectar a otros proyectos o al sistema global de Python.

### Desactivación del entorno virtual

Para desactivar el entorno virtual y volver al entorno global de Python, simplemente puedes usar el siguiente comando:

```
deactivate
```

Al ejecutar este comando, el nombre del entorno virtual desaparecerá de la terminal, indicando que has vuelto al entorno global de Python. Es importante recordar desactivar el entorno virtual cuando hayas terminado de trabajar en tu proyecto para evitar confusiones y asegurarte de que estás utilizando el entorno correcto para cada proyecto.

### Instalación de paquetes dentro del entorno virtual

Una vez que tienes tu entorno virtual activo, puedes instalar paquetes usando `pip`, que es el gestor de paquetes de Python. Por ejemplo, si quieres instalar la biblioteca `requests`, puedes usar el siguiente comando:

```
pip install requests
```

Esto instalará la biblioteca `requests` dentro de tu entorno virtual, lo que significa que solo estará disponible para ese proyecto específico y no afectará a otros proyectos o al sistema global de Python. Es una forma eficiente de gestionar las dependencias de tus proyectos y mantener tu entorno de desarrollo organizado.

### BONUS - Gestión de paquetes en el entorno virtual

#### ¿Cómo saber qué paquetes tengo instalados en el entorno virtual?

Para saber qué paquetes tienes instalados en tu entorno virtual, puedes usar el siguiente comando:

```
pip list
```

Este comando te mostrará una lista de todos los paquetes que están instalados en tu entorno virtual, junto con sus versiones. Es una forma útil de verificar qué dependencias tienes para tu proyecto y asegurarte de que estás utilizando las versiones correctas de cada paquete.

#### ¿Cómo generar un archivo de requisitos para tu proyecto?

Para generar un archivo de requisitos que liste todas las dependencias de tu proyecto, puedes usar el siguiente comando:

```
pip freeze > requirements.txt
```

Este comando crea un archivo llamado `requirements.txt` que contiene una lista de todos los paquetes instalados en tu entorno virtual, junto con sus versiones. Este archivo es útil para compartir tu proyecto con otros desarrolladores o para desplegar tu aplicación en un entorno de producción, ya que permite instalar todas las dependencias necesarias con un solo comando:

```
pip install -r requirements.txt
```

Este comando lee el archivo `requirements.txt` e instala todas las dependencias listadas en él, asegurando que tu proyecto tenga todas las bibliotecas necesarias para funcionar correctamente en cualquier entorno donde se despliegue. El flag `-r` indica que `pip` debe leer las dependencias desde el archivo especificado.

## Higiene del código en Python

En este apartado, lo que se busca es entender qué es la "higiene del código" en Python. La higiene del código se refiere a las prácticas y principios que ayudan a mantener el código limpio, legible y fácil de mantener. Esto incluye aspectos como la organización del código, el uso de nombres descriptivos para variables y funciones, la eliminación de código innecesario, y la adherencia a las convenciones de estilo de Python (PEP 8).

Un par de ejemplos de buenas prácticas para mantener una buena higiene del código en Python incluyen:

- Usar nombres descriptivos para variables y funciones: Esto ayuda a que el código sea más legible y fácil de entender. Por ejemplo, en lugar de usar `x` como nombre de una variable, podrías usar `user_age` si la variable representa la edad de un usuario.
- Eliminar código innecesario: Si tienes código que ya no se utiliza o que es redundante, es importante eliminarlo para mantener el código limpio y evitar confusiones. Esto incluye comentarios obsoletos, funciones que ya no se llaman, o variables que no se utilizan.
- La importación de paquetes debe hacerse al inicio del archivo: Esto es una convención en Python que ayuda a mantener el código organizado y facilita la identificación de las dependencias del proyecto. Al colocar todas las importaciones al inicio del archivo, es más fácil para otros desarrolladores ver qué bibliotecas se están utilizando y evitar problemas de importación circular. Y deben hacerse en orden alfabético: Esto hace más fácil encontrar una importación específica y mantener un estilo consistente en todo el proyecto.
