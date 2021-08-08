var magicEndpoint = "https://574i3vnyuk.execute-api.sa-east-1.amazonaws.com/default/testFunction"
var baseAddr = "https://pt.wikipedia.org/wiki/"

function findPath() {
    let inicialVal = document.getElementById("Pagina Inicial").value;
    let endVal = document.getElementById("Pagina Final").value;
    if((inicialVal) && (endVal)){
        let holder = document.getElementById("res")
        holder.innerHTML = "<p class='alert alert-info'>Traçando Trajetória</p><img src='imgs/loading2.gif'/>"
        let names = {};
        names['startName'] = inicialVal;
        names['endName'] = endVal;
        let pathReq = new XMLHttpRequest();
        pathReq.onload = function(){
            if (pathReq.status != 200) {
                console.log("failure");
                console.log(pathReq.response);
                console.log(pathReq.responseText);
                holder.innerHTML = "<p class = 'alert alert-danger'>Não foi possivel achar um caminho</p>";
                return;
            }
            else{
                let results = JSON.parse(pathReq.responseText);
                console.log("Result from API:");
                console.log(results);

                if (results == 'ERROR name not in dabatase'){
                    holder.innerHTML = "<p class = 'alert alert-danger'>Uma das paginas não existe</p>"
                }
                else{
                    holder.innerHTML = "";
                    results.forEach(function(item, index) {
                        holder.innerHTML += '<div class="linkEnclosure"><a target="_blank" href="' + baseAddr + item + '"> ' + item + '</a></div>'; 
                    })
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
        label.disabled = true;
    }
    else{
        label.disabled = false;
        label.innerHTML = source.value;
        label.onclick = function(){
            window.open(baseAddr+source.value, "_blank").focus();
        }
    }
}

window.onload = function(){
    updatePage(document.getElementById("Pagina Inicial"), document.getElementById("buttonInicial"))
    updatePage(document.getElementById("Pagina Final"), document.getElementById("buttonFinal"))
}