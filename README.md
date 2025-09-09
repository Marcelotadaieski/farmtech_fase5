
---

## 🚜 Entrega 1 — Machine Learning

### Objetivo
- Analisar a base `crop_yield.csv` (condições de solo, temperatura, umidade, precipitação).  
- Explorar tendências de rendimento com **clusterização (KMeans)**.  
- Criar **5 modelos preditivos de regressão** para estimar o rendimento.  

### Passos Realizados
1. **EDA (Exploratory Data Analysis)**  
   - `df.info()`, `df.describe()` e verificação de nulos.  
   - Histogramas, boxplots e scatterplots (ex.: temperatura × rendimento).  
   - Identificação de outliers.  

2. **Clusterização (Unsupervised)**  
   - Algoritmo **KMeans** (3 a 5 clusters).  
   - Dispersão colorida pelos clusters.  
   - Identificação de possíveis clusters de outliers.  

3. **Modelagem Preditiva (Supervised)**  
   - Modelos testados:  
     - Regressão Linear  
     - Decision Tree  
     - Random Forest  
     - Ridge / Lasso  
     - Gradient Boosting / XGBoost  
   - Avaliação com **R², RMSE, MAE**.  
   - Comparação final em tabela.  

4. **Conclusões**  
   - Insights do EDA.  
   - Clusters que representam cenários discrepantes.  
   - Modelo com melhor desempenho.  
   - Limitações (dataset pequeno, variáveis limitadas, ausência de tuning).  

📓 Notebook disponível em [`/notebooks/MarceloTadaieski_rmXXXXX_pbl_fase5.ipynb`](./notebooks/MarceloTadaieski_rmXXXXX_pbl_fase5.ipynb)  

🎥 **Vídeo da Entrega 1**: [link do YouTube aqui]  

---

## ☁️ Entrega 2 — Cloud AWS

### Objetivo
Estimar custos de hospedar a ML em uma **instância EC2** (On-Demand) com:  
- 2 vCPUs  
- 1 GiB RAM  
- 50 GB armazenamento  
- Rede até 5 Gbps  

### Comparação de Custos
| Região        | vCPUs | RAM  | Armazenamento | Rede    | Custo Mensal |
|---------------|-------|------|---------------|---------|--------------|
| São Paulo     | 2     | 1GiB | 50 GB EBS     | ≤5Gbps  | R$ xxx / US$ xxx |
| N. Virginia   | 2     | 1GiB | 50 GB EBS     | ≤5Gbps  | US$ xxx       |

📸 Prints:  
- ![AWS São Paulo](./figures/aws_calc_sp.png)  
- ![AWS N. Virginia](./figures/aws_calc_use1.png)  

### Justificativa
- **N. Virginia** costuma ser mais barata devido à escala global da AWS.  
- Contudo, por requisitos de **residência de dados no Brasil**, **latência menor** e **compliance regulatório**, a melhor escolha para este projeto é **São Paulo (sa-east-1)**.  

🎥 **Vídeo da Entrega 2**: [link do YouTube aqui]  

---

## 🏆 Desafios “Ir Além” (opcionais)
O grupo poderá explorar:  
- **Opção 1:** ESP32 + Wi-Fi + Sensores → envio de dados para BD/MQTT/HTML.  
- **Opção 2:** ESP32 + Machine Learning → classificar saúde da plantação em Saudável / Não saudável.  

Documentação parcial em [`/ir-alem/`](./ir-alem).  

---

## 🔧 Como Executar
```bash
# Criar e ativar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
# ou
pip install jupyter pandas numpy matplotlib seaborn scikit-learn xgboost

# Abrir o notebook
jupyter notebook
