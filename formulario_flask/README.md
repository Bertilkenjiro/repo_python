\# 🧾 Projeto Flask – Formulário de Respostas



\## 🎯 Objetivo

Desenvolver uma aplicação web simples com \*\*Flask\*\* para coletar respostas via formulário e armazená-las localmente em um arquivo \*\*CSV\*\*.  

O objetivo principal é demonstrar o uso de \*\*rotas, templates e manipulação de dados\*\* em Python, servindo como base para projetos mais complexos de back-end e ETL web.



---



\## 🧠 Inteligência Aplicada

\- Estruturação de \*\*rotas Flask\*\* (`@app.route`) para exibir e processar formulários;

\- Utilização de \*\*templates HTML\*\* com \*\*Jinja2\*\*;

\- Gravação de dados em arquivo \*\*CSV\*\* com `csv.writer`;

\- Organização modular do código e tratamento de exceções simples.



---



\## 🧩 Estrutura do Projeto

formulario\_flask/

│

├── app.py → Arquivo principal da aplicação Flask

├── respostas.csv → Armazena as respostas enviadas via formulário

├── templates/

│ └── index.html → Interface HTML do formulário

└── .gitignore → Exclusões de arquivos locais





**---**



💡 Funcionamento



O usuário acessa a página principal e preenche o formulário;



Ao enviar, as informações são registradas no arquivo respostas.csv;



O sistema retorna uma mensagem de sucesso no navegador.





🧩 Exemplo de Saída (respostas.csv)

nome,email,mensagem

Beto,beto@exemplo.com,Excelente projeto!

Maria,maria@teste.com,Adorei a simplicidade.





**## 🧑‍💻 Sobre o Autor**

**Desenvolvido por \*\*Bertil Kenjiro (Beto)\*\* — Analista de Dados apaixonado por tecnologia, visualização e automação.**  

**💼 \[LinkedIn](https://www.linkedin.com/in/betokenjiro) | 📊 \[Portfólio Power BI](https://github.com/Bertilkenjiro)**



**---**



**> ⭐ Se este repositório te inspirou, não esqueça de deixar uma estrela!**



