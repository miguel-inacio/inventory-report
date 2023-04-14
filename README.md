# Projeto Inventory Report 💻 

Projeto desenvolvido no curso de desenvolvimento web da Trybe, no módulo de Ciência da Computação.

### Tecnologias utilizadas:
- Python

### Rodando localmente

Clone o repositório

```bash
  git clone git@github.com:miguel-inacio/inventory-report.git
```

Entre no diretório do projeto

```bash
  cd inventory-report
```

Crie e entre em um ambiente virtual

```bash
    python3 -m venv .venv && source .venv/bin/activate
```

Instale as dependências

```bash
 python3 -m pip install -r dev-requirements.txt
```

<details>
  <summary> Observações </summary>
  
  ### Os seguintes módulos e seus conteúdos foram desenvolvidos por mim:
  Em inventory_report:
    - main.py
    <hr>
    /importer:
        - csv_importer.py
        - importer.py
        - json_importer.py
        - xml_importer.py
    <hr>
    /inventory:
        - inventory_iterator.py
        - inventory_refactor.py
        - inventory.py
        - product.py
    /reports:
        - complete_report.py
        - simple_report.py
  Em tests:
    /product:
        - test_product.py
    /product_report:
        - test_product_report.py
    /report_decorator:
        - test_report_decorator.py
  
</details>
