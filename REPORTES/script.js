function TomarDatos(){
    let input = document.getElementById('inputF')
    let radio = findSelection('genero')
    let select = document.getElementById('paises')

    //alert("Nombre: "+nombre.value+"\nSexo: "+sexo+"\nPais: "+pais.value)

    localStorage.setItem("inputC",input.value)
    localStorage.setItem("radioC",radio)
    localStorage.setItem("selectC",select.value)

    let sitio = document.getElementById('frame')
    let iframe = document.createElement('iframe')
    iframe.setAttribute('src',"Frame2.html")
    iframe.setAttribute('height',"200")
    iframe.setAttribute('width',"400")
    sitio.appendChild(iframe)
}

function Entrada(){
    let sitio = document.getElementById('frame')
    let iframe = document.createElement('iframe')
    iframe.setAttribute('src',"Frame1.html")
    iframe.setAttribute('height',"200")
    iframe.setAttribute('width',"400")
    sitio.appendChild(iframe)
}

function findSelection(field) {
    var test = document.getElementsByName(field);
    var sizes = test.length;
    for (i=0; i < sizes; i++) {
            if (test[i].checked==true) {
            return test[i].value;
        }
    }
}

function unselect(){
    document.querySelectorAll('[name=genero]').forEach((x) => x.checked=false);
}