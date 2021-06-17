// Definir dados iniciais
const pessoa = {
  nome: 'Betão',
  sobrenome: 'Einstein',
  idade: 42,
  doido: true,
  imagem_doido: 'https://www.hypeness.com.br/1/2017/08/EinsteinL3.jpg',
  imagem_seria:
    'https://upload.wikimedia.org/wikipedia/commons/5/50/Albert_Einstein_%28Nobel%29.png',
};

const nome = document.getElementById('nome');
const sobrenome = document.getElementById('sobrenome');
const idade = document.getElementById('idade');
const elementoBotao = document.getElementById('alteraHumor');

nome.innerHTML = pessoa.nome;
sobrenome.innerHTML = pessoa.sobrenome;
idade.innerHTML = pessoa.idade;

function atualizaHumor() {
  pessoa.doido = !pessoa.doido;
  const elementoImagem = document.getElementById('imagem');
  const elementoHumor = document.getElementById('bloco_humor');
  if (pessoa.doido) {
    elementoImagem.src = pessoa.imagem_doido;
    elementoHumor.innerHTML = `${pessoa.nome} tá <b>DOIDO</b>!`;
  } else {
    elementoImagem.src = pessoa.imagem_seria;
    elementoHumor.innerHTML = `${pessoa.nome} tá <b>SÉRIO!</b>`;
  }
}
atualizaHumor();

elementoBotao.addEventListener('click', atualizaHumor);
