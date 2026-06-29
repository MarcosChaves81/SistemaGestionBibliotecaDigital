# SistemaGestionBibliotecaDigital

## Universidad nacional Guillermo Brown
### Trabajo práctico final | Programación Avanzada
### Comisión 3
### Profesor: Diego Ezequiel Luparello 
### Grupo:
  1) ### Santiago Calina
  2) ### Marcos Chaves
  3) ### Brian Fernandez

## Consigna 
Este proyecto consiste en el desarrollo de un Sistema de Gestión de Biblioteca Digital implementado en Python, diseñado bajo el paradigma de Programación Orientada a Objetos (POO) y la aplicación de patrones de diseño avanzados. La aplicación permite administrar de manera integral el ciclo de vida de libros (alta, modificación, baja y listado de títulos con datos como ISBN y cantidad de páginas) y usuarios (gestión de perfiles mediante nombre, DNI y correo electrónico), además de controlar un  subsistema de préstamos y devoluciones que valida en tiempo real la disponibilidad de los ejemplares y registra de forma estricta las fechas de cada operación.

En su apartado técnico, el sistema destaca por la implementación rigurosa de conceptos de programacion, tales como estructuras de herencia y comportamiento polimórfico, relaciones explícitas de agregación y composición para el modelado de datos, la creación de decoradores personalizados e incluso lógica avanzada mediante metaclases de Python. Asimismo, la arquitectura incorpora un patrón de diseño debidamente justificado para optimizar la creación o el comportamiento de los componentes, todo respaldado y documentado visualmente a través de un diagrama de clases UML completo.

## Explicacion de la resolucion 
Se escogió dividir el sistema en modelos, gestores y utilidades, con el fin de mantener una arquitectura organizada y facilitar el mantenimiento del código.

Las entidades principales (Libro, Usuario y Prestamo) representan la información de la problemática.

Los gestores son los encargados de ejecutar las operaciones de alta, baja, modificación y búsqueda de datos.

Con el objetivo de reforzar los conocimientos adquiridos en la materia, se realizaron:

- Una clase abstracta.
- Polimorfismo usando el método mostrar_info().
- El patrón Singleton para asegurar una única instancia del sistema.
- Una metaclase para obligar a implementar el método mostrar_info.
- Un decorador personalizado que registre las acciones realizadas por los administradores.
También se han agregado validaciones para verificar la integridad de los datos y se ha utilizado persistencia en archivos de texto para almacenar la información del sistema.

El proyecto está organizado utilizando gestores especializados para cada entidad.

- GestionLibros
- GestionUsuarios
- GestionPrestamos

La clase *SistemaBiblioteca* centraliza la creación y coordinación de los gestores.

El diagrama UML se encuentra dentro de la carpeta:


diagramas/


## Proyecto desarrollado con fines exclusivamente académicos.

