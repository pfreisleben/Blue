const cardPersonagens = document.querySelectorAll('.card-personagem');
const cardArmas = document.querySelectorAll('.card-arma');
const vidaPorPersonagem = {
  globin: 8,
  orc: 12,
  feiticeira: 18,
};
const danoPorArma = {
  soco: 2,
  arco: 5,
  espada: 10,
};

function seleciona() {
  if (!this.classList.contains('selecionado')) {
    if (this.classList.contains('card-personagem')) {
      for (let personagem of cardPersonagens) {
        personagem.classList.remove('selecionado');
      }
      this.classList.add('selecionado');
    } else {
      for (let arma of cardArmas) {
        arma.classList.remove('selecionado');
      }
      this.classList.add('selecionado');
    }
  }
}

function calcularDano() {
  let personagemSelecionado = document
    .getElementsByClassName('card-personagem selecionado')[0]
    .getAttribute('data-nome');
  let armaSelecionada = document
    .getElementsByClassName('card-arma selecionado')[0]
    .getAttribute('data-nome');
}

for (let personagem of cardPersonagens) {
  personagem.addEventListener('click', seleciona);
}
for (let arma of cardArmas) {
  arma.addEventListener('click', seleciona);
}

document.getElementById('calcular').addEventListener('click', calcularDano);
