(function () {
    var _a;
    const $ = (query) => document.querySelector(query);
    (_a = $("#cadastrar")) === null || _a === void 0 ? void 0 : _a.addEventListener('click', () => {
        var _a, _b;
        const nome = (_a = $('#nome')) === null || _a === void 0 ? void 0 : _a.value;
        const placa = (_b = $('#placa')) === null || _b === void 0 ? void 0 : _b.value;
        function patio() {
            function calcTempo(mil) {
                const minutos = Math.floor(mil / 60000);
                const sec = Math.floor(mil % 60000) / 1000;
                return `${minutos} e ${sec}s`;
            }
            function ler() {
                return localStorage.patio ? JSON.parse(localStorage.patio) : [];
            }
            function salvar(veiculos) {
                localStorage.setItem("patio", JSON.stringify(veiculos));
            }
            function adicionar(veiculo, salvo) {
                var _a, _b;
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
                (_a = row.querySelector(".delete")) === null || _a === void 0 ? void 0 : _a.addEventListener("click", function () {
                    remover(this.dataset.placa);
                });
                (_b = $("#patio")) === null || _b === void 0 ? void 0 : _b.appendChild(row);
                if (salvo)
                    salvar([...ler(), veiculo]);
            }
            function remover(placa) {
                const { entradaDate, nome } = ler().find((veiculo) => veiculo.placa === placa);
                const tempo = calcTempo((new Date().getTime() - new Date(entradaDate).getTime()));
                if (!confirm(`o veiculo ${nome}permaneceu por ${tempo}, Deseja encerrar`))
                    return;
                salvar(ler().filter((veiculo) => veiculo.placa !== placa));
                renderizar();
            }
            function renderizar() {
                $("#patio").innerHTML = "";
                const patio = ler();
                if (patio.length) {
                    patio.forEach((veiculo) => adicionar(veiculo));
                }
            }
            return { ler, adicionar, remover, renderizar, salvar };
        }
        patio().renderizar();
        if (!nome || !placa) {
            alert("Os campos nome e placa são obrigatorios");
            return;
        }
        patio().adicionar({ nome, placa, entradaDate: new Date().toISOString() }, true);
    });
})();
