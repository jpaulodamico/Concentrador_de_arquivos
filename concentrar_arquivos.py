import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime
import logging
import sys

def configurar_logging(log_path):
    """
    Configura o sistema de logging para registrar as operações em um arquivo de log.
    
    :param log_path: Caminho completo para o arquivo de log.
    """
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'  # Anexa ao arquivo de log existente
    )

def gerar_nome_unico(destino, nome_arquivo):
    """
    Gera um nome único para o arquivo adicionando um timestamp se já existir no destino.
    
    :param destino: Diretório de destino onde o arquivo será salvo.
    :param nome_arquivo: Nome original do arquivo.
    :return: Nome único do arquivo.
    """
    destino_arquivo = destino / nome_arquivo
    if not destino_arquivo.exists():
        return destino_arquivo

    nome, ext = os.path.splitext(nome_arquivo)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    novo_nome = f"{nome}_{timestamp}{ext}"
    return destino / novo_nome

def concentrar_arquivos(origem, destino, mover=False, tipos=None, excluir_pastas=None, log_path=None):
    """
    Concentra todos os arquivos de subpastas da origem para a pasta destino com melhorias.
    
    :param origem: Diretório de origem para procurar os arquivos.
    :param destino: Diretório de destino onde os arquivos serão concentrados.
    :param mover: Se True, move os arquivos ao invés de copiá-los.
    :param tipos: Lista de extensões de arquivos a serem processados (ex: ['.jpg', '.pdf']).
    :param excluir_pastas: Conjunto de nomes de pastas a serem excluídas.
    :param log_path: Caminho para o arquivo de log.
    """
    origem = Path(origem)
    destino = Path(destino)

    # Configurar logging
    if log_path:
        configurar_logging(log_path)
    else:
        # Logging padrão para console
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            stream=sys.stdout
        )

    if not origem.exists():
        logging.error(f"O diretório de origem '{origem}' não existe.")
        return

    # Cria o diretório de destino se não existir
    destino.mkdir(parents=True, exist_ok=True)
    logging.info(f"Iniciando o processo de {'movimento' if mover else 'cópia'} dos arquivos.")
    logging.info(f"Origem: {origem}")
    logging.info(f"Destino: {destino}")

    # Percorre todos os arquivos nas subpastas
    for root, dirs, files in os.walk(origem):
        # Excluir pastas especificadas
        if excluir_pastas:
            dirs[:] = [d for d in dirs if d not in excluir_pastas]

        for file in files:
            caminho_arquivo = Path(root) / file

            # Filtrar tipos de arquivos se especificado
            if tipos:
                if caminho_arquivo.suffix.lower() not in tipos:
                    continue  # Pula arquivos que não correspondem aos tipos permitidos

            destino_arquivo = gerar_nome_unico(destino, file)

            try:
                if mover:
                    shutil.move(str(caminho_arquivo), str(destino_arquivo))
                    logging.info(f"Movido: {caminho_arquivo} -> {destino_arquivo}")
                else:
                    shutil.copy2(str(caminho_arquivo), str(destino_arquivo))
                    logging.info(f"Copiado: {caminho_arquivo} -> {destino_arquivo}")
            except Exception as e:
                logging.error(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")

    logging.info("Processo concluído.")

def main():
    parser = argparse.ArgumentParser(
        description="Concentra arquivos de várias pastas em uma única pasta com melhorias avançadas."
    )
    parser.add_argument('origem', help="Diretório de origem para procurar os arquivos.")
    parser.add_argument('destino', help="Diretório de destino onde os arquivos serão concentrados.")
    parser.add_argument('-m', '--mover', action='store_true', help="Mover os arquivos ao invés de copiá-los.")
    parser.add_argument('-t', '--tipos', nargs='*', help="Extensões de arquivos a serem processados (ex: .jpg .pdf).")
    parser.add_argument('-e', '--excluir', nargs='*', help="Nomes de pastas a serem excluídas do processamento.")
    parser.add_argument('-l', '--log', help="Caminho para o arquivo de log. Se não for especificado, o log será exibido no console.")
    args = parser.parse_args()

    # Normalizar extensões de arquivos para minúsculas e garantir o ponto
    tipos = [ext.lower() if ext.startswith('.') else f".{ext.lower()}" for ext in args.tipos] if args.tipos else None

    excluir_pastas = set(args.excluir) if args.excluir else None

    concentrar_arquivos(
        origem=args.origem,
        destino=args.destino,
        mover=args.mover,
        tipos=tipos,
        excluir_pastas=excluir_pastas,
        log_path=args.log
    )

if __name__ == "__main__":
    main()
