interface IVeiculo{
    nome: string;
    placa: string;
    entradaDate: Date | string;    
}

(function() {
    const  $ = (query: string): HTMLInputElement | null => document.querySelector(query);

    $("#cadastrar")?.addEventListener('click', () => {
        const nome = $('#nome')?.value;
        const placa = $('#placa')?.value;

        function patio(){

            function calcTempo(mil: number){
                const minutos  = Math.floor(mil/60000);
                const sec = Math.floor(mil % 60000)/1000;

                return `${minutos} e ${sec}s`;
            }

            function ler(): IVeiculo[]{
                return localStorage.patio ? JSON.parse(localStorage.patio) : []

            }
            function salvar(veiculos: IVeiculo[]){
                localStorage.setItem("patio", JSON.stringify(veiculos));
            }

            function adicionar(veiculo: IVeiculo, salvo?: boolean){
                
                let row = document.createElement("tr");
                console.log(row);
                row.innerHTML = 
                `<td>${veiculo.nome}</td>
                <td>${veiculo.placa}</td>
                <td>${veiculo.entradaDate}</td>
                <td>
                    <button class="delete" data-placa="${veiculo.placa}"> X </button>
                </td>
                `;

                row.querySelector(".delete")?.addEventListener("click", function(){
                    remover(this.dataset.placa as string)
                }
                );

                $("#patio")?.appendChild(row);
                if(salvo) salvar([...ler(), veiculo]);
            }
            function remover(placa: string){
                const { entradaDate, nome} = ler().find(
                    (veiculo) => veiculo.placa === placa);
                
                const tempo = calcTempo((new Date().getTime() - new Date(entradaDate).getTime()));

                if(
                    !confirm(`o veiculo: ${nome} permaneceu por ${tempo}s, Deseja encerrar?`)
                )
                return;

                    salvar(ler().filter((veiculo) => veiculo.placa !== placa));
                
                renderizar();
            }
            function renderizar(){
                $("#patio")!.innerHTML = "";
                const patio = ler();

                if(patio.length){
                    patio.forEach((veiculo) => adicionar(veiculo));                                            
                }

                
            }
            return {ler, adicionar, remover, renderizar, salvar};
        }
        patio().renderizar();

        if(!nome || !placa){        
            alert("Os campos nome e placa são obrigatorios");
            return;         
        }   

        patio().adicionar({nome, placa, entradaDate: new Date().toISOString()}, true);
    });
 })();