import matplotlib.pyplot as plt
import seaborn as sns

def plot_nulls(df):
    """Muestra un heatmap de valores nulos."""
    plt.figure(figsize=(8,5))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Mapa de valores nulos")
    plt.show()

def plot_histograms(df):
    """Histogramas para todas las columnas numéricas."""
    df.hist(figsize=(12,8), bins=20, color="skyblue", edgecolor="black")
    plt.suptitle("Distribución de variables numéricas")
    plt.show()

def plot_correlations(df):
    """Muestra un mapa de calor de correlaciones."""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Matriz de correlación")
    plt.show()

def scatter_length_weight(df):
    """Ejemplo: grafica la relación entre longitud y peso."""
    if "Length" in df.columns and "Weight" in df.columns:
        plt.figure(figsize=(8,6))
        sns.scatterplot(x=df["Length"], y=df["Weight"], alpha=0.7)
        plt.title("Relación entre longitud y peso de los cocodrilos")
        plt.show()
