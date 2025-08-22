import yfinance as yf
import pandas as pd
from typing import List, Optional, Dict, Any


class Stock:
    """Represents a stock with methods to fetch financial metrics."""

    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        self.data = yf.Ticker(self.ticker)
        self.info: Dict[str, Any] = self.data.info or {}

    def get_pe_ratio(self) -> Optional[float]:
        """Return the trailing P/E ratio if available."""
        return self.info.get("trailingPE")

    def get_dividend_yield(self) -> float:
        """Return dividend yield in percentage, defaults to 0 if missing."""
        return (self.info.get("dividendYield", 0) or 0) * 100

    def get_eps_growth_proxy(self) -> float:
        """
        Proxy for 5Y EPS growth using quarterly earnings growth.
        Replace with CAGR when available.
        """
        return self.info.get("earningsQuarterlyGrowth", 0.0)

    def is_candidate(
        self, min_yield: float = 3.0, max_pe: float = 15.0, min_growth: float = 0.05
    ) -> bool:
        """Check if stock meets screening criteria."""
        dy = self.get_dividend_yield()
        pe = self.get_pe_ratio()
        growth = self.get_eps_growth_proxy()

        return (
            dy >= min_yield
            and pe is not None
            and pe <= max_pe
            and growth >= min_growth
        )

    def summary(self) -> Dict[str, Any]:
        """Return a summary of key stock metrics."""
        return {
            "Ticker": self.ticker,
            "P/E Ratio": self.get_pe_ratio(),
            "Dividend Yield (%)": round(self.get_dividend_yield(), 2),
            "EPS Growth Proxy": self.get_eps_growth_proxy(),
        }


class StockScreener:
    """Screens multiple stocks based on fundamental criteria."""

    def __init__(self, tickers: List[str]):
        self.tickers = tickers
        self.results: List[Dict[str, Any]] = []

    def screen(
        self, min_yield: float = 3.0, max_pe: float = 15.0, min_growth: float = 0.05
    ) -> pd.DataFrame:
        """
        Run screening for all tickers and return a DataFrame of candidates.
        """
        for ticker in self.tickers:
            try:
                stock = Stock(ticker)
                if stock.is_candidate(min_yield, max_pe, min_growth):
                    self.results.append(stock.summary())
            except Exception as e:
                print(f"⚠️ Error with {ticker}: {e}")
        return pd.DataFrame(self.results)


if __name__ == "__main__":
    # Example usage: Large-cap US dividend stocks
    tickers = ["KO", "JNJ", "T", "XOM", "PG", "MO", "IBM", "CVX", "VZ", "MMM"]
    screener = StockScreener(tickers)
    filtered_stocks = screener.screen()
    print(filtered_stocks)

