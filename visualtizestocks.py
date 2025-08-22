import matplotlib.pyplot as plt
import pandas as pd
from filterstocks import StockScreener


def plot_dividend_yield(df: pd.DataFrame, save: bool = True, show: bool = False):
    """Plot and save dividend yield of screened stocks."""
    plt.figure(figsize=(8, 5))
    plt.bar(df["Ticker"], df["Dividend Yield (%)"])
    plt.title("Dividend Yield (%) by Stock")
    plt.ylabel("Dividend Yield (%)")
    plt.xlabel("Ticker")
    plt.tight_layout()
    if save:
        plt.savefig("dividend_yield.png")
    if show:
        plt.show()
    plt.close()


def plot_pe_ratios(df: pd.DataFrame, save: bool = True, show: bool = False):
    """Plot and save P/E ratios of screened stocks."""
    plt.figure(figsize=(8, 5))
    plt.bar(df["Ticker"], df["P/E Ratio"], color="orange")
    plt.title("P/E Ratio by Stock")
    plt.ylabel("P/E Ratio")
    plt.xlabel("Ticker")
    plt.tight_layout()
    if save:
        plt.savefig("pe_ratios.png")
    if show:
        plt.show()
    plt.close()


def plot_eps_growth(df: pd.DataFrame, save: bool = True, show: bool = False):
    """Plot and save EPS Growth Proxy of screened stocks."""
    plt.figure(figsize=(8, 5))
    plt.bar(df["Ticker"], df["EPS Growth Proxy"], color="green")
    plt.title("EPS Growth Proxy by Stock")
    plt.ylabel("Growth (fraction)")
    plt.xlabel("Ticker")
    plt.tight_layout()
    if save:
        plt.savefig("eps_growth.png")
    if show:
        plt.show()
    plt.close()


if __name__ == "__main__":
    # Example usage
    tickers = ["KO", "JNJ", "T", "XOM", "PG", "MO", "IBM", "CVX", "VZ", "MMM"]
    screener = StockScreener(tickers)
    filtered_stocks = screener.screen()

    if filtered_stocks.empty:
        print("No stocks passed the filter.")
    else:
        print(filtered_stocks)

        # Generate and save visualizations
        plot_dividend_yield(filtered_stocks)
        plot_pe_ratios(filtered_stocks)
        plot_eps_growth(filtered_stocks)

        print("✅ Plots saved as dividend_yield.png, pe_ratios.png, eps_growth.png")
