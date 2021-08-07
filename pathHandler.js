var magicEndpoint = "https://574i3vnyuk.execute-api.sa-east-1.amazonaws.com/default/testFunction"
var baseAddr = "https://pt.wikipedia.org/wiki/"

function findPath() {
    let inicialVal = document.getElementById("Pagina Inicial").value;
    let endVal = document.getElementById("Pagina Final").value;
    if((inicialVal) && (endVal)){
        let holder = document.getElementById("res")
        holder.innerHTML = "<a>Traçando Trajetória</a>"
        let names = {};
        names['startName'] = inicialVal;
        names['endName'] = endVal;
        let pathReq = new XMLHttpRequest();
        pathReq.onload = function(){
            if (pathReq.status != 200) {
                console.log("failure");
                console.log(pathReq.response);
                console.log(pathReq.responseText);
                holder.innerHTML = "<a>Não foi possivel achar um caminho</a>";
                return;
            }
            else{
                let results = JSON.parse(pathReq.responseText);
                console.log("Result from API:");
                console.log(results);

                if (results == 'ERROR name not in dabatase'){
                    holder.innerHTML = "<a>Uma das paginas não existe</a>"
                }
                else{
                    holder.innerHTML = "->";
                    results.forEach(function(item, index) {
                        holder.innerHTML += '<a target="_blank" href="' + baseAddr + item + '"> ' + item + '</a>'; 
                    })
                    holder.innerHTML += "<-";
                }
    
            }
        }
        pathReq.open("POST", magicEndpoint, true);
        
        console.log("Sending data to endpoint");
        console.log(JSON.stringify(names))
        pathReq.send(JSON.stringify(names));
    }
}

function updatePage(source, label) {
    if(source.value == "") {
        label.innerHTML = source.id;
    }
    else{
        label.innerHTML = source.value;
    }
    label.onclick = function(){
        window.open(baseAddr+source.value, "_blank").focus();
    }
}

window.onload = function(){
    updatePage(document.getElementById("Pagina Inicial"), document.getElementById("buttonInicial"))
    updatePage(document.getElementById("Pagina Final"), document.getElementById("buttonFinal"))
}