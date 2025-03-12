<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Músicas que me lembram ti</title>


    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap");

      body {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        background-image: url("https://cdn.wallpapersafari.com/27/32/jt4AoG.jpg");
        font-family: "Roboto", sans-serif;
      }

      div {
        background-color: #ecc1d3;
        width: 420px;
        margin: 10px;
        padding: 8px 18px;
        border-radius: 30px;
        box-shadow: 2px 20px #fcf8f8;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }

      div:hover {
        box-shadow: 4px 4px rgb(253, 12, 133);
        cursor: pointer;
      }

      img {
        width: 40px;
        height: 40px;
      }
    </style>
  </head>
  
   
  <body>

    <h1>Hello</h1>

    <I2>Pois é, eu continuo😳</I2>
    
    <footer>
        <p>Juntando o util ao agradável, juntei várias músicas que sou fã, pra falar que sou sua fã e pra te mostrar meu bom gosto musical. Eu acho triste e estranho, mas eu sigo na paz!! </p>
    </footer>


    <div onclick="changeColor(this)">
      <p>
        Quem de nós dois vai dizer que é impossível o amor acontecer... ♪
      </p>  <a href="https://www.youtube.com/watch?v=z4j9BhlmSSU">Clique
        aqui</a></p>
      <img 
        src="https://i.pinimg.com/originals/e0/73/cc/e073ccc627f9f23776ca0721f68a371f.jpg"
      />
    </div>
    <div onclick="(this)">
      <p>Nunca acreditei na ilusão de ter você pra mim...♫ </p>
      <a href="https://www.youtube.com/watch?v=97hee9msbEs">Clique
        aqui</a></p>
      <img 
        src="https://i.scdn.co/image/ab67616d0000b2732b4da5abb231f0dfc297ff09"
      />
    </div>
    <div onclick="(this)">
      <p>Ela não é a minha namorada, não é minha amante, minha amiga de infância, minha amiga do colégio, eu nunca dividi um lanche com ela antes... ♩</p>
      <a href="https://www.youtube.com/watch?v=ABoCxcG0ulU&list=RDMUifGCXuLNY&index=24">Clique
        aqui</a></p>
      <img
        src="https://i.ytimg.com/vi/ABoCxcG0ulU/maxresdefault.jpg"
      />
    </div>
    <div onclick="(this)">
      <p>
        Seu sorriso é o que eu preciso, enquanto eu resto, eu juro, TANTO FAZ!...♬
      </p>
      <a href="https://www.youtube.com/watch?v=yuXnbJjdSSA&list=RDMUifGCXuLNY&index=8">Clique
        aqui</a></p>
      <img
        src="https://i.ytimg.com/vi/8YBBSHscuhY/mqdefault.jpg"
      />
    </div>
    <div onclick="(this)">
      <p>
        Nunca pensei que pudesse gostar de uma garota que só sabe me esnobar... Sim, é restart ♥
      </p>
      <a href="https://www.youtube.com/watch?v=yuXnbJjdSSA&list=RDMUifGCXuLNY&index=8">Clique
        aqui</a></p>
      <img
        src="https://c-fa.cdn.smule.com/rs-s37/arr/2d/ca/653f0c22-7f04-4da8-a9cb-53305cb38732.jpg"
      />
    </div>
    <div onclick="(this)">
      <p>Pra te ver sorrir, eu posso colorir o céu de outra cor...♭</p>
      <a href="https://www.youtube.com/watch?v=kszkoFI84JU">Clique
        aqui</a>
      <img
        src="https://s1.static.brasilescola.uol.com.br/be/conteudo/images/5c9ea060ec9faa2122a84f079d983bd4.jpg"
      />
    </div>
  </div>
  <div onclick="(this)">
    <p>If you're cold and needed shelter. I'd hold you, but not sweat ya...😉</p>
    <a href="https://www.youtube.com/watch?v=YynKelHGhNc">Clique
      aqui</a>
    <img
      src="https://i.ytimg.com/vi/qI-TPUthY4I/maxresdefault.jpg"
    />
  </div>
</div>
<div onclick="(this)">
  <p>Tropecei no sorriso dela...♮ Um hino, esse hino</p>
  <a href="https://www.youtube.com/watch?v=IyT5ZUpHg6w">Clique
    aqui</a>
  <img
    src="https://cdns-images.dzcdn.net/images/cover/d7629f028a478d44d267849c4e1d24dc/500x500.jpg"
  />
</div>
</div>
<div onclick="(this)">
  <p>E nesse tanto de curva, eu me arrisco até na contramão..♯</p>
  <a href="https://www.youtube.com/watch?v=1qKz_QohN7gc">Clique
    aqui</a>
  <img
    src="https://akamai.sscdn.co/uploadfile/letras/albuns/4/f/e/8/765991565961663.jpg"
  />
</div>

<div onclick="(this)">
  <p> Não é que eu esteja apaixonada. Eu tô falando sério. Eu não quero ninguém. Mas se você quiser, eu quero..♫</p>
  <a href="https://www.youtube.com/watch?v=BRw8e5OGnrI">Clique
    aqui</a>
  <img
    src="https://akamai.sscdn.co/uploadfile/letras/albuns/7/3/5/8/1219081640092138.jpg"
  />
</div>


     <script>
      for (var i = 0; i <= 6; i++) {
        function mandaZap(elemento) {
          let texto = elemento.firstElementChild.innerText;
          let numero = prompt("Número do destinatário?(c/ddd xx)");
          let zaplink = `https://api.whatsapp.com/send?phone=55${numero}&text=${texto}`;

          window.open(zaplink);
        }
      } pra colocar zap zap
    </script>
  </body>
</html>
