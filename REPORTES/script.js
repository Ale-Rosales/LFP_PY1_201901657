function TomarDatos(){
    /*let input = document.getElementById('inputF')*/
    let input = ValorInput('inputF')
    let radio = findSelection('opciones')
    /*let select = document.getElementById('seleccion')*/
    let select = ValorSelect('seleccion')

    //alert("Nombre: "+nombre.value+"\nSexo: "+sexo+"\nPais: "+pais.value)
    if(input == null){
        localStorage.setItem("inputC","")
        localStorage.setItem("radioC",radio)
        localStorage.setItem("selectC",select)
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe)
    }else if(radio == null){
        localStorage.setItem("radioC","")
        localStorage.setItem("inputC",input)
        localStorage.setItem("selectC",select)
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe)        
    }else if(select == null){
        localStorage.setItem("radioC",radio)
        localStorage.setItem("inputC",input)
        localStorage.setItem("selectC","")
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe)
    }else if(radio == null && select == null){
        localStorage.setItem("radioC","")
        localStorage.setItem("inputC",input)
        localStorage.setItem("selectC","")
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe) 
    }else if(input == null && select == null){
        localStorage.setItem("radioC",radio)
        localStorage.setItem("inputC","")
        localStorage.setItem("selectC","")
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe) 
    }else if(input == null && radio == null){
        localStorage.setItem("radioC","")
        localStorage.setItem("inputC","")
        localStorage.setItem("selectC",select)
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe) 
    }else if(select == null){
        localStorage.setItem("radioC",radio)
        localStorage.setItem("inputC",input)
        localStorage.setItem("selectC","")
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe)
    }else if(input == null && select == null && radio == null){
        localStorage.setItem("radioC","")
        localStorage.setItem("inputC","")
        localStorage.setItem("selectC","")
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe) 
    }else{
        localStorage.setItem("radioC",radio)
        localStorage.setItem("inputC",input)
        localStorage.setItem("selectC",select)
        let sitio = document.getElementById('frame')
        let iframe = document.createElement('iframe')
        iframe.setAttribute('src',"Frame2.html")
        iframe.setAttribute('height',"200")
        iframe.setAttribute('width',"400")
        sitio.appendChild(iframe)
    }
    /*if (radio != 'undefined' && radio != null){
        localStorage.setItem("radioC",radio)
    }
    if (select != 'undefined' && select != null){
        localStorage.setItem("selectC",select.value)
    }*/
        
    /*let sitio = document.getElementById('frame')
    let iframe = document.createElement('iframe')
    iframe.setAttribute('src',"Frame2.html")
    iframe.setAttribute('height',"200")
    iframe.setAttribute('width',"400")
    sitio.appendChild(iframe)*/
}

function Entrada(){
    let sitio = document.getElementById('frame')
    let iframe = document.createElement('iframe')
    iframe.setAttribute('src',"Frame1.html")
    iframe.setAttribute('height',"200")
    iframe.setAttribute('width',"400")
    sitio.appendChild(iframe)
}

function ValorInput(field){
    var test = document.getElementById(field);
    return test.value
}

function ValorSelect(field){
    var test = document.getElementById(field);
    return test.value
}
     

function findSelection(field) {
    var test = document.getElementsByName(field);
    var sizes = test.length;
    if(sizes == 0){
        return ""
    }else{

    for (i=0; i < sizes; i++) {
            if (test[i].checked==true) {
            return test[i].value;
        }
    }

    }
   
}

function unselect(){
    document.querySelectorAll('[name=opciones]').forEach((x) => x.checked=false);
}