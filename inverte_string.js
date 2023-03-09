const entrada = "Target Sistemas"
const saida = [];
const tam = (entrada.length) -1;
console.log(tam);
for(let i=0; i<=tam; i++){
    saida[i]=entrada[tam-i]
}
console.log(saida.join(''));