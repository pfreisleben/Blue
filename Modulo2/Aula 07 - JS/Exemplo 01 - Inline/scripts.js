function altera() {
  const elemento1 = document.getElementById('botao');
  if (elemento1.innerText == 'Texto mudou') {
    elemento1.innerText = 'Texto voltou';
    document.bgColor = 'black';
  } else {
    elemento1.innerText = 'Texto mudou';
    document.bgColor = 'red';
  }
}
