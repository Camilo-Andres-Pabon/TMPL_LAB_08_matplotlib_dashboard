# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import base64
    from io import BytesIO

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import pandas as pd

    # -------------------------------------------------------
    # 1. Crear carpeta docs si no existe
    # -------------------------------------------------------
    os.makedirs("docs", exist_ok=True)

    # -------------------------------------------------------
    # 2. Cargar datos
    # -------------------------------------------------------
    df = pd.read_csv("data/shipping-data.csv")

    # -------------------------------------------------------
    # 3. Función auxiliar: figura → cadena base64 PNG
    # -------------------------------------------------------
    def fig_to_base64(fig):
        buf = BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        encoded = base64.b64encode(buf.read()).decode("utf-8")
        plt.close(fig)
        return encoded

    # -------------------------------------------------------
    # 4. Gráfica 1 – Warehouse_block (barras)
    # -------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    ax1.bar(warehouse_counts.index, warehouse_counts.values, color="steelblue")
    ax1.set_title("Envíos por Warehouse Block")
    ax1.set_xlabel("Warehouse Block")
    ax1.set_ylabel("Cantidad")
    img1 = fig_to_base64(fig1)

    # -------------------------------------------------------
    # 5. Gráfica 2 – Mode_of_Shipment (pastel)
    # -------------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    shipment_counts = df["Mode_of_Shipment"].value_counts()
    ax2.pie(
        shipment_counts.values,
        labels=shipment_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#4C72B0", "#DD8452", "#55A868"],
    )
    ax2.set_title("Modo de Envío")
    img2 = fig_to_base64(fig2)

    # -------------------------------------------------------
    # 6. Gráfica 3 – Customer_rating (barras)
    # -------------------------------------------------------
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    rating_counts = df["Customer_rating"].value_counts().sort_index()
    ax3.bar(rating_counts.index, rating_counts.values, color="coral")
    ax3.set_title("Calificación del Cliente")
    ax3.set_xlabel("Rating (1-5)")
    ax3.set_ylabel("Cantidad")
    ax3.set_xticks(rating_counts.index)
    img3 = fig_to_base64(fig3)

    # -------------------------------------------------------
    # 7. Gráfica 4 – Weight_in_gms (histograma)
    # -------------------------------------------------------
    fig4, ax4 = plt.subplots(figsize=(5, 4))
    ax4.hist(df["Weight_in_gms"], bins=20, color="mediumseagreen", edgecolor="white")
    ax4.set_title("Distribución de Peso (gms)")
    ax4.set_xlabel("Peso (gms)")
    ax4.set_ylabel("Frecuencia")
    img4 = fig_to_base64(fig4)

    # -------------------------------------------------------
    # 8. Crear HTML con las 4 gráficas embebidas
    # -------------------------------------------------------
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Shipping Dashboard</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 20px;
    }}
    h1 {{
      text-align: center;
      color: #333;
      margin-bottom: 30px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      max-width: 1100px;
      margin: 0 auto;
    }}
    .card {{
      background: white;
      border-radius: 8px;
      padding: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      text-align: center;
    }}
    .card img {{
      width: 100%;
      height: auto;
    }}
  </style>
</head>
<body>
  <h1>Shipping Dashboard</h1>
  <div class="grid">
    <div class="card">
      <img src="data:image/png;base64,{img1}" alt="Warehouse Block" />
    </div>
    <div class="card">
      <img src="data:image/png;base64,{img2}" alt="Mode of Shipment" />
    </div>
    <div class="card">
      <img src="data:image/png;base64,{img3}" alt="Customer Rating" />
    </div>
    <div class="card">
      <img src="data:image/png;base64,{img4}" alt="Weight in gms" />
    </div>
  </div>
</body>
</html>
"""

    # -------------------------------------------------------
    # 9. Guardar el HTML en docs/
    # -------------------------------------------------------
    output_path = os.path.join("docs", "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content) 