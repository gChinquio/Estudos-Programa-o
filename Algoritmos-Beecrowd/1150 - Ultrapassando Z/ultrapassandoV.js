var input = require("fs").readFileSync("stdin","utf-8");

let valores = input.split("\n");

let z = 0;
//let x = parseInt(valores[0]);
let x = parseInt(valores.shift());

//contador
let i = 1;
while(true){
    if (parseInt(valores[i]) > x){
        z = parseInt(valores[i]);
        break;
    }        
    i++;
}

let passos = 1;
let soma = x;

while(z > soma){
    soma += x;
    passos++;
    x += 1;    
}

console.log(passos);
/*
// a função gets é implementada dentro do sistema para ler as entradas(inputs) dos dados e a função print para imprimir a saída (output) de dados.
// Abaixo segue um exemplo de código que você pode ou não utilizar


let R = parseInt(gets());
let V = 0;

// Complete os espaços em branco com uma possível solução para o problema

while(true){
  V = parseInt(gets())
  if(V > R){
    break
  }
}
let soma = V;
let cont = 1;
//let it = R + 1;
while(true){
  cont++
  soma+= V;                  
  if(soma >= R){
    print(cont)
    break;
  }
}
*/