let input = localStorage.getItem("inputC")
let radio = localStorage.getItem("radioC")
let select = localStorage.getItem("selectC")

let sitio = document.getElementById('contenido')
let parrafo = document.createTextNode("Texto Input: "+input+"\nSeleccion radio: "+radio+"\nSeleccion select: "+select)
sitio.appendChild(parrafo)