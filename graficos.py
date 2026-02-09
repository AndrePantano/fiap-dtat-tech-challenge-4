class Graficos:
    def __init__(self, pd, plt):
        self.tabela = None
        self.ordem = None
        self.titulo = None
        self.plt = plt
        self.pd = pd
        self.axes = None

    def gerar_graficos(self):
        
        self.tabela = self.tabela.loc[self.ordem]

        fig, axes = self.plt.subplots(1, 2, figsize=(15,5), sharey=True)

        self.ax1 = axes[0]
        self.ax2 = axes[1]

        self.grafico1()
        self.grafico2()

        self.plt.tight_layout()
        self.plt.show()

    def grafico1(self):

        # Barras empilhadas
        self.tabela.plot(
            kind="bar",
            stacked=True,
            ax=self.ax1
        )

        self.ax1.set_title(f"Distribuição percentual dos graus de obesidade\n por {self.titulo}")
        self.ax1.set_xlabel(self.titulo)
        self.ax1.set_ylabel("Percentual (%)")
        self.ax1.set_ylim(0, 100)

        for container in self.ax1.containers:
            labels = [
                f"{v:.1f}%" if v >= 5 else ""
                for v in container.datavalues
            ]
            self.ax1.bar_label(
                container,
                labels=labels,
                label_type="center",
                fontsize=8,
                clip_on=False
            )

        self.ax1.legend(
            title="Grau de obesidade",
            loc="upper center",
            bbox_to_anchor=(0.5, -0.35),
            ncol=4,
            frameon=False
        )

        self.ax1.tick_params(axis="x", labelrotation=0)

    def grafico2(self):

        grupos = {
            "Baixo / Normal": ["Abaixo do peso", "Peso normal"],
            "Sobrepeso": ["Sobrepeso nível I", "Sobrepeso nível II"],
            "Obesidade": ["Obesidade tipo I", "Obesidade tipo II", "Obesidade tipo III"]
        }

        tabela_agrupada = self.pd.DataFrame({
            grupo: self.tabela[cols].sum(axis=1)
            for grupo, cols in grupos.items()
        })

        # Barras agrupadas
        tabela_agrupada.plot(
            kind="bar",
            ax=self.ax2,
            width=0.8
        )

        self.ax2.set_title(f"Agrupamento dos graus de obesidade\n por {self.titulo}")
        self.ax2.set_xlabel(self.titulo)
        self.ax2.set_ylabel("Percentual (%)")
        self.ax2.set_ylim(0, 100)

        for container in self.ax2.containers:
            labels = [
                f"{v:.1f}%" for v in container.datavalues
            ]
            self.ax2.bar_label(container, labels=labels, fontsize=8)

        self.ax2.legend(
            title="Grau de obesidade",
            loc="upper center",
            bbox_to_anchor=(0.5, -0.35),
            ncol=4,
            frameon=False
        )

        self.ax2.tick_params(axis="x", labelrotation=0)
