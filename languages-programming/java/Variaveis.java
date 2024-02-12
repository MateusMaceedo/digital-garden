public class Variaveis {

  public static void main(String[] args) {
    String nome = "Mateus";
    int idade;
    idade = 26;

    String mensagem = String.format("Olá, meu nome é %s e tenho %d anos.", nome, idade);

    // %s: String
    // %d: Número inteiro
    // %f: Número de ponto flutuante
    // %b: Valor booleano
    // %c: Caractere
    System.out.println("Exemplo, primeiro declara e ao longo do programa é feito a atribuição do valor");
    System.out.println(mensagem);

    int idadeEsposa = 26;

    String mensagemEsposa = String.format("Olá, meu nome é %s e minha esponsa tem %d anos.", nome, idadeEsposa);

    System.out.println("Exemplo, declarando e atribuindo a valor para a variavel");
    System.out.println(mensagemEsposa);
  }
}
