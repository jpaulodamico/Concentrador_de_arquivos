# Concentrador de Arquivos Avançado

**ConcentraArquivos Avançado** é um script Python robusto projetado para consolidar arquivos de múltiplas pastas em uma única pasta de destino. Com funcionalidades avançadas, como tratamento de nomes duplicados, filtragem por tipos de arquivos, exclusão de pastas específicas e registro de operações, este script facilita a organização eficiente de grandes volumes de arquivos espalhados em diversas localizações.

## 🛠️ Características

- **Concentração de Arquivos:** Copia ou move todos os arquivos de subpastas de um diretório de origem para um único diretório de destino.
- **Tratamento de Nomes Duplicados:** Gera nomes únicos adicionando um timestamp (`YYYYMMDDHHMMSS`) para evitar sobrescritas.
- **Registro de Operações (Logging):** Registra todas as operações realizadas (cópias, movimentos, erros) em um arquivo de log ou no console.
- **Filtragem de Tipos de Arquivos:** Permite processar apenas tipos específicos de arquivos (por exemplo, `.jpg`, `.pdf`).
- **Exclusão de Pastas Específicas:** Ignora pastas determinadas durante a busca de arquivos.
- **Interface de Linha de Comando Amigável:** Utiliza `argparse` para facilitar a configuração e execução do script.

## 📋 Requisitos

- **Python 3.6+** instalado no sistema.
- Permissões adequadas para ler as pastas de origem e escrever na pasta de destino.
- Conhecimento básico de utilização da linha de comando (Terminal no macOS/Linux ou Prompt de Comando no Windows).

## 💾 Instalação

1. **Verifique a Instalação do Python:**

   Abra o terminal (macOS/Linux) ou o Prompt de Comando (Windows) e execute:

   ```bash
   python --version
   ```

   ou

   ```bash
   python3 --version
   ```

   Se Python não estiver instalado, baixe e instale a partir do [site oficial do Python](https://www.python.org/downloads/).

2. **Baixe o Script:**

   - Crie uma pasta para armazenar o script, por exemplo:

     ```
     C:\Users\SeuUsuario\ScriptsPython\
     ```

     ou

     ```
     /home/seuusuario/ScriptsPython/
     ```

   - Baixe o arquivo `concentrar_arquivos_avancado.py` e salve na pasta criada.

3. **Instale Dependências (Opcional):**

   O script utiliza apenas bibliotecas padrão do Python, portanto, não há dependências externas a serem instaladas.

## 🚀 Uso

### 📝 Sintaxe Básica

```bash
python concentrar_arquivos_avancado.py origem destino [opções]
```

ou, se `python3` for necessário no seu sistema:

```bash
python3 concentrar_arquivos_avancado.py origem destino [opções]
```

### 📂 Parâmetros

- **`origem`** (obrigatório): Caminho para o diretório de origem onde os arquivos estão localizados.
- **`destino`** (obrigatório): Caminho para o diretório de destino onde os arquivos serão concentrados.

### 🛠️ Opções de Linha de Comando

- **`-m`, `--mover`**: Move os arquivos ao invés de copiá-los.
- **`-t`, `--tipos`**: Lista de extensões de arquivos a serem processados (ex: `.jpg`, `.pdf`).
- **`-e`, `--excluir`**: Lista de nomes de pastas a serem excluídas do processamento.
- **`-l`, `--log`**: Caminho para o arquivo de log. Se não for especificado, o log será exibido no console.

### 📝 Exemplos de Comando

1. **Copiar Todos os Arquivos de Todas as Subpastas:**

   ```bash
   python concentrar_arquivos_avancado.py "/caminho/para/origem" "/caminho/para/destino"
   ```

2. **Mover Todos os Arquivos de Todas as Subpastas:**

   ```bash
   python concentrar_arquivos_avancado.py "/caminho/para/origem" "/caminho/para/destino" --mover
   ```

3. **Copiar Apenas Arquivos `.jpg` e `.pdf`:**

   ```bash
   python concentrar_arquivos_avancado.py "/caminho/para/origem" "/caminho/para/destino" --tipos .jpg .pdf
   ```

4. **Copiar Todos os Arquivos, Excluindo Pastas Específicas (`temp`, `backup`):**

   ```bash
   python concentrar_arquivos_avancado.py "/caminho/para/origem" "/caminho/para/destino" --excluir temp backup
   ```

5. **Mover Arquivos e Registrar as Operações em um Arquivo de Log:**

   ```bash
   python concentrar_arquivos_avancado.py "/caminho/para/origem" "/caminho/para/destino" --mover --log "/caminho/para/logs/transferencia.log"
   ```

**Nota:** Em sistemas Windows, utilize aspas (`" "`) para caminhos que contêm espaços.

### 📂 Exemplo Completo

**Cenário:**

- **Diretório de Origem:** `C:\Users\SeuUsuario\Documentos`
- **Diretório de Destino:** `C:\Users\SeuUsuario\ArquivosConcentrados`
- **Tipos de Arquivos a Processar:** `.jpg`, `.pdf`
- **Pastas a Excluir:** `temp`, `backup`
- **Arquivo de Log:** `C:\Users\SeuUsuario\Logs\transferencia.log`

**Comando:**

```bash
python concentrar_arquivos_avancado.py "C:\Users\SeuUsuario\Documentos" "C:\Users\SeuUsuario\ArquivosConcentrados" --tipos .jpg .pdf --excluir temp backup --log "C:\Users\SeuUsuario\Logs\transferencia.log"
```

**Resultado:**

- Todos os arquivos `.jpg` e `.pdf` das subpastas de `Documentos`, exceto das pastas `temp` e `backup`, serão **copiados** para `ArquivosConcentrados`.
- Arquivos com nomes duplicados serão renomeados com um timestamp.
- Todas as operações serão registradas no arquivo `transferencia.log`.

## ⚙️ Personalizações e Melhorias

O script é altamente flexível e pode ser personalizado conforme suas necessidades. Aqui estão algumas sugestões:

1. **Filtragem Avançada de Arquivos:**
   - Adicione condições adicionais para filtrar arquivos com base em tamanho, data de modificação, etc.

2. **Interface Gráfica (GUI):**
   - Utilize bibliotecas como `Tkinter` ou `PyQt` para criar uma interface amigável para usuários que preferem não usar a linha de comando.

3. **Verificação de Conteúdo Duplicado:**
   - Implemente uma verificação baseada em hashes para evitar copiar arquivos que são idênticos em conteúdo, mesmo que tenham nomes diferentes.

4. **Opções Avançadas de Logging:**
   - Adicione níveis de logging diferentes (DEBUG, INFO, WARNING, ERROR).
   - Rotacione os arquivos de log para evitar que cresçam indefinidamente.

5. **Exibição de Progresso:**
   - Implemente uma barra de progresso usando bibliotecas como `tqdm` para fornecer feedback visual durante a execução.

## 🛠️ Resolução de Problemas

1. **Erro: `PermissionError`**

   - **Causa:** Falta de permissões adequadas para ler os arquivos nas pastas de origem ou escrever na pasta de destino.
   - **Solução:** Execute o terminal ou Prompt de Comando com privilégios de administrador ou ajuste as permissões das pastas.

2. **Erro: `ModuleNotFoundError` ou `ImportError`**

   - **Causa:** Falta de bibliotecas necessárias.
   - **Solução:** As bibliotecas utilizadas são padrão do Python. Certifique-se de estar utilizando uma versão compatível do Python (3.6+).

3. **Os Arquivos Não São Copiados ou Movidos Corretamente**

   - **Causa:** Caminhos de origem ou destino incorretos, ou erros de sintaxe no comando.
   - **Solução:** Verifique se os caminhos estão corretos e que estão entre aspas se contiverem espaços. Revise a sintaxe do comando.

4. **Arquivos com o Mesmo Nome Não São Renomeados Corretamente**

   - **Causa:** Problema na lógica de geração de nomes únicos.
   - **Solução:** Verifique se a função `gerar_nome_unico` está sendo executada corretamente. Adicione logs de depuração se necessário.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você encontrou um bug ou tem uma sugestão de melhoria, sinta-se à vontade para abrir uma [issue](#) ou enviar um [pull request](#).

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📬 Contato

Para dúvidas, sugestões ou contribuições, entre em contato:

- **Nome:** João Paulo
- **Email:**jpaulodamico@hotmail.com
---

**Nota:** Sempre faça backup de seus dados antes de executar operações em massa para evitar perda acidental de informações.
