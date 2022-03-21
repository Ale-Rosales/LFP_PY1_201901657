/*let input = localStorage.getItem("inputC")
let radio = localStorage.getItem("radioC")
let select = localStorage.getItem("selectC")*/

let sitio = document.getElementById('contenido')
let parrafo = document.createTextNode(localStorage.getItem("inputC")+"\n"+"\n"
+localStorage.getItem("radioC")+"\n"+"\n"
+localStorage.getItem("selectC"))
sitio.appendChild(parrafo)