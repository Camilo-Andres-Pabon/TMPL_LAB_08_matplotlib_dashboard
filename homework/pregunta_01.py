# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files/input/shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`
    * `Mode_of_Shipment`
    * `Customer_rating`
    * `Weight_in_gms`
    """
    import os

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import pandas as pd

    # -------------------------------------------------------
    # El test verifica:  os.path.exists("../docs/archivo.png")
    # Eso es relativo al CWD de pytest (raíz del proyecto).
    # Por lo tanto docs debe quedar en:  CWD/../docs/
    # -------------------------------------------------------
    docs_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "docs"))
    os.makedirs(docs_dir, exist_ok=True)

    # -------------------------------------------------------
    # CSV también relativo al CWD (raíz del proyecto)
    # -------------------------------------------------------
    csv_path = os.path.join(os.getcwd(), "files", "input", "shipping-data.csv")
    df = pd.read_csv(csv_path)

    # -------------------------------------------------------
    # Gráfica 1 – shipping_per_warehouse.png
    # -------------------------------------------------------
    fig, ax = plt.subplots(figsize=(6, 4))
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    ax.bar(warehouse_counts.index, warehouse_counts.values, color="steelblue")
    ax.set_title("Shipping per Warehouse Block")
    ax.set_xlabel("Warehouse Block")
    ax.set_ylabel("Number of Shipments")
    plt.tight_layout()
    fig.savefig(os.path.join(docs_dir, "shipping_per_warehouse.png"))
    plt.close(fig)

    # -------------------------------------------------------
    # Gráfica 2 – mode_of_shipment.png
    # -------------------------------------------------------
    fig, ax = plt.subplots(figsize=(6, 4))
    shipment_counts = df["Mode_of_Shipment"].value_counts()
    ax.pie(
        shipment_counts.values,
        labels=shipment_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#4C72B0", "#DD8452", "#55A868"],
    )
    ax.set_title("Mode of Shipment")
    plt.tight_layout()
    fig.savefig(os.path.join(docs_dir, "mode_of_shipment.png"))
    plt.close(fig)

    # -------------------------------------------------------
    # Gráfica 3 – average_customer_rating.png
    # -------------------------------------------------------
    fig, ax = plt.subplots(figsize=(6, 4))
    avg_rating = df.groupby("Warehouse_block")["Customer_rating"].mean().sort_index()
    ax.bar(avg_rating.index, avg_rating.values, color="coral")
    ax.set_title("Average Customer Rating by Warehouse")
    ax.set_xlabel("Warehouse Block")
    ax.set_ylabel("Average Rating")
    ax.set_ylim(0, 5)
    plt.tight_layout()
    fig.savefig(os.path.join(docs_dir, "average_customer_rating.png"))
    plt.close(fig)

    # -------------------------------------------------------
    # Gráfica 4 – weight_distribution.png
    # -------------------------------------------------------
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df["Weight_in_gms"], bins=20, color="mediumseagreen", edgecolor="white")
    ax.set_title("Weight Distribution (gms)")
    ax.set_xlabel("Weight (gms)")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    fig.savefig(os.path.join(docs_dir, "weight_distribution.png"))
    plt.close(fig)

    # -------------------------------------------------------
    # index.html referenciando los 4 PNGs
    # -------------------------------------------------------
    html_content = """\
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Shipping Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #333; margin-bottom: 30px; }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      max-width: 1100px;
      margin: 0 auto;
    }
    .card {
      background: white;
      border-radius: 8px;
      padding: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      text-align: center;
    }
    .card img { width: 100%; height: auto; }
  </style>
</head>
<body>
  <h1>Shipping Dashboard</h1>
  <div class="grid">
    <div class="card"><img src="shipping_per_warehouse.png" alt="Shipping per Warehouse" /></div>
    <div class="card"><img src="mode_of_shipment.png" alt="Mode of Shipment" /></div>
    <div class="card"><img src="average_customer_rating.png" alt="Average Customer Rating" /></div>
    <div class="card"><img src="weight_distribution.png" alt="Weight Distribution" /></div>
  </div>
</body>
</html>
"""
    with open(os.path.join(docs_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)